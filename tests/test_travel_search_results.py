"""Offline regressions for the chapter 5 travel search example.

Install camel-ai==0.2.75 flask==3.0.3 python-dotenv==1.0.1 'mcp<2', then:
    python -m unittest discover -s tests -p test_travel_search_results.py -v
"""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import unittest
from unittest.mock import patch

import httpx
from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
MODULE = (
    ROOT / "code" / "第五章" / "examples" / "NavigatorAI" / "backend"
    / "module" / "travel_information_integration.py"
)
ITEMS = [{
    "result_id": 1,
    "title": "成都旅行",
    "description": "参观博物馆，然后品尝当地美食。",
    "url": "https://example.com/travel",
}]


class TravelSearchResultsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = patch.dict(os.environ, {
            "GOOGLE_API_KEY": "offline-test",
            "SEARCH_ENGINE_ID": "offline-test",
            "FIRECRAWL_API_KEY": "offline-test",
            "QWEN_API_KEY": "offline-test",
            "MODELSCOPE_SDK_TOKEN": "offline-test",
        })
        cls.env.start()
        cls.addClassCleanup(cls.env.stop)
        spec = importlib.util.spec_from_file_location("travel_search_example", MODULE)
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def setUp(self):
        self.planner = self.module.TravelPlanner.__new__(self.module.TravelPlanner)
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_plain_json_results_are_preserved(self):
        for value in (ITEMS, {"related_results": ITEMS}):
            with self.subTest(value=value):
                response = json.dumps(value, ensure_ascii=False)
                self.assertEqual(self.planner.extract_json_from_response(response), ITEMS)

    def test_fenced_json_results_are_preserved(self):
        for value in (ITEMS, {"related_results": ITEMS}):
            response = json.dumps(value, ensure_ascii=False)
            for newline in ("\n", "\r\n"):
                with self.subTest(value=value, newline=newline):
                    fenced = f"筛选结果：{newline}```json{newline}{response}{newline}```"
                    self.assertEqual(self.planner.extract_json_from_response(fenced), ITEMS)

    def test_json_content_is_not_rewritten(self):
        items = [{**ITEMS[0], "description": "保留 ```json 与 ```，以及换行\n和空格  "}]
        response = json.dumps(items, ensure_ascii=False)
        self.assertEqual(self.planner.extract_json_from_response(response), items)

    def test_tutorial_code_preserves_plain_and_fenced_results(self):
        text = (ROOT / "docs" / "chapter5" / "5-Comprehensive-Case.md").read_text(encoding="utf-8")
        blocks = re.findall(r"^````python\n(.*?)^````", text, re.MULTILINE | re.DOTALL)
        code = next(block for block in blocks if "class TravelPlanner:" in block)
        namespace = {"__name__": "travel_search_tutorial"}
        exec(compile(code, "chapter5_travel_search", "exec"), namespace)
        planner = namespace["TravelPlanner"].__new__(namespace["TravelPlanner"])
        response = json.dumps(ITEMS, ensure_ascii=False)
        for content in (response, f"```json\n{response}\n```", f"```json\r\n{response}\r\n```"):
            with self.subTest(content=content):
                self.assertEqual(planner.extract_json_from_response(content), ITEMS)

    def test_invalid_or_unsupported_responses_remain_empty(self):
        for response in (
            "not json", "[] trailing garbage", '[{"result_id": 1}',
            '```json\n[{"result_id": 1}\n```',
            '```json\n[{"result_id": 1}]',
            '{"unrelated": []}', '"string"', 'null',
        ):
            with self.subTest(response=response):
                self.assertEqual(self.planner.extract_json_from_response(response), [])

    def test_search_pipeline_preserves_all_four_categories(self):
        requests = []
        responses = iter([
            json.dumps(ITEMS, ensure_ascii=False),
            json.dumps({"related_results": ITEMS}, ensure_ascii=False),
            "```json\n" + json.dumps(ITEMS, ensure_ascii=False) + "\n```",
            "```json\r\n" + json.dumps(ITEMS, ensure_ascii=False) + "\r\n```",
        ])

        def respond(request):
            requests.append(json.loads(request.content))
            return httpx.Response(200, json={
                "id": "offline-completion", "object": "chat.completion", "created": 0,
                "model": "Qwen/Qwen2.5-72B-Instruct",
                "choices": [{"index": 0, "message": {
                    "role": "assistant", "content": next(responses),
                }, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
            })

        # Keep the real CAMEL agent, model backend and OpenAI client. Only the
        # external search call and model HTTP transport use deterministic data.
        with httpx.Client(transport=httpx.MockTransport(respond)) as http_client:
            with OpenAI(api_key="offline-test", http_client=http_client) as client:
                planner = self.module.TravelPlanner("成都", 3)
                planner.model._client = client
                with patch.object(planner.search_toolkit, "search_google", return_value=ITEMS) as search:
                    result = planner.search_and_rerank()

        self.assertEqual(search.call_count, 4)
        self.assertEqual(len(requests), 4)
        self.assertEqual(result["city"], "成都")
        self.assertEqual(result["days"], 3)
        for category in ("guides", "attractions", "must_eat", "local_food"):
            with self.subTest(category=category):
                self.assertEqual(result["travel_info"][category], [{
                    "result_id": 1, "title": ITEMS[0]["title"],
                    "description": ITEMS[0]["description"], "long_description": None,
                }])
        for request in requests:
            self.assertIn(ITEMS[0]["description"], request["messages"][-1]["content"])


if __name__ == "__main__":
    unittest.main()
