from typing import List, Dict, Any

from camel.toolkits import SearchToolkit, FunctionTool
from camel.utils import dependencies_required


# 重写SearchToolkit().search_duckduckgo
class MySearchToolkit(SearchToolkit):
    @dependencies_required("ddgs")
    def search_duckduckgo(
        self,
        query: str,
        source: str = "text",
        number_of_result_pages: int = 10,
    ) -> List[Dict[str, Any]]:
        r"""Use DuckDuckGo search engine to search information for
        the given query.

        This function queries the DuckDuckGo API for related topics to
        the given search term. The results are formatted into a list of
        dictionaries, each representing a search result.

        Args:
            query (str): The query to be searched.
            source (str): The type of information to query (e.g., "text",
                "images", "videos"). Defaults to "text".
            number_of_result_pages (int): The number of result pages to
                retrieve. Adjust this based on your task - use fewer results
                for focused searches and more for comprehensive searches.
                (default: :obj:`10`)

        Returns:
            List[Dict[str, Any]]: A list of dictionaries where each dictionary
                represents a search result.
        """
        from ddgs import DDGS
        from requests.exceptions import RequestException

        ddgs = DDGS()
        responses: List[Dict[str, Any]] = []

        if source == "text":
            try:
                results = ddgs.text(
                    query=query, max_results=number_of_result_pages
                )
            except RequestException as e:
                # Handle specific exceptions or general request exceptions
                responses.append({"error": f"duckduckgo search failed.{e}"})
                return responses

            # Iterate over results found
            for i, result in enumerate(results, start=1):
                # Creating a response object with a similar structure
                response = {
                    "result_id": i,
                    "title": result["title"],
                    "description": result["body"],
                    "url": result["href"],
                }
                responses.append(response)

        elif source == "images":
            try:
                results = ddgs.images(
                    query=query, max_results=number_of_result_pages
                )
            except RequestException as e:
                # Handle specific exceptions or general request exceptions
                responses.append({"error": f"duckduckgo search failed.{e}"})
                return responses

            # Iterate over results found
            for i, result in enumerate(results, start=1):
                # Creating a response object with a similar structure
                response = {
                    "result_id": i,
                    "title": result["title"],
                    "image": result["image"],
                    "url": result["url"],
                    "source": result["source"],
                }
                responses.append(response)

        elif source == "videos":
            try:
                results = ddgs.videos(
                    query=query, max_results=number_of_result_pages
                )
            except RequestException as e:
                # Handle specific exceptions or general request exceptions
                responses.append({"error": f"duckduckgo search failed.{e}"})
                return responses

            # Iterate over results found
            for i, result in enumerate(results, start=1):
                # Creating a response object with a similar structure
                response = {
                    "result_id": i,
                    "title": result["title"],
                    "description": result["description"],
                    "embed_url": result["embed_url"],
                    "publisher": result["publisher"],
                    "duration": result["duration"],
                    "published": result["published"],
                }
                responses.append(response)

        # If no answer found, return an empty list
        return responses


    def get_tools(self) -> List[FunctionTool]:
        original_tools = super().get_tools()
        custom_tools = []
        for tool in original_tools:
            if hasattr(tool, '__name__') and tool.__name__ == "search_duckduckgo":
                custom_tool = FunctionTool(self.search_duckduckgo)
                custom_tools.append(custom_tool)
            else:
                if isinstance(tool, FunctionTool):
                    custom_tools.append(tool)
                else:
                    custom_tools.append(tool)
        return custom_tools