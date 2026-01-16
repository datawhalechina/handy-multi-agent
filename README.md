# Handy Multi-Agent 教程

<div align="center">
  <img src="https://s2.loli.net/2025/04/05/XagKqdzWe67fDt8.jpg" alt="Handy Multi-Agent Logo">
  <br>
  <p>基于CAMEL框架从零开始构建多智能体系统的实用指南</p>
  <p>
    <a href="https://github.com/datawhalechina/handy-multi-agent/stargazers">
      <img alt="GitHub stars" src="https://img.shields.io/github/stars/datawhalechina/handy-multi-agent">
    </a>
    <a href="https://github.com/datawhalechina/handy-multi-agent/network">
      <img alt="GitHub forks" src="https://img.shields.io/github/forks/datawhalechina/handy-multi-agent">
    </a>
    <a href="https://github.com/datawhalechina/handy-multi-agent/issues">
      <img alt="GitHub issues" src="https://img.shields.io/github/issues/datawhalechina/handy-multi-agent">
    </a>
    <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
      <img alt="GitHub license" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey">
    </a>
  </p>
</div>



> 🎉 **项目已正式发布第一版！** 完整教程文档已更新至docs目录，配套可执行代码位于code目录，可一键运行。如有任何疑问或功能建议，欢迎在GitHub提issue反馈~

## 📖 项目简介

**Handy-Multi-Agent** 是一套专为希望深入了解并实践多智能体系统的开发者设计的实用指南。本教程基于国内领先的多智能体框架 [CAMEL-AI（NeruIPS'2023）](https://arxiv.org/pdf/2303.17760.pdf)，从最基本的单个Agent开发，逐步引导读者构建复杂的Multi Agent应用。

### 🎯 面向人群

本项目侧重于实践和动手构建Agent应用，同时结合必要的理论知识，适合：
- 对多智能体系统、大模型应用或人工智能领域有研究兴趣的学习者
- 希望通过实践了解并探索LLM在多智能体系统中应用的开发者

### 🚀 学习目标

通过本项目，我们希望帮助开发者：
1. **理解基础**：掌握CAMEL框架的使用方法，理解Agent的基本概念
2. **提升技能**：通过实践项目，涉及RAG、Memory、Multi Agent等技术，提高构建和管理智能体的能力
3. **应用实践**：将所学知识应用于解决实际问题，培养实践能力和创新思维

### 👨‍💻 适合人群

- **技术基础**：具备Python编程基础，能够阅读和理解项目源代码和相关理论
- **兴趣与动机**：对AI智能体领域充满热情，希望从代码层面对智能体进行个性化能力开发

## 📚 项目结构

```
handy-multi-agent/
├── docs/                # 教程文档
│   ├── chapter0/        # 第零章：序言
│   ├── chapter1/        # 第一章：环境配置
│   ├── chapter2/        # 第二章：Agent的构成组件
│   ├── chapter3/        # 第三章：CAMEL框架简介及实践
│   ├── chapter4/        # 第四章：CAMEL框架下的RAG应用
│   ├── chapter5/        # 第五章：综合案例
│   ├── chapter6/        # 第六章：结语
│   ├── appendix/        # 附录
│   ├── images/          # 文档图片资源
│   └── files/           # 文档相关文件
│
├── code/                # 配套代码
│   ├── 第一章.ipynb      # 第一章实践代码
│   ├── 第二章.ipynb      # 第二章实践代码
│   ├── 第三章.ipynb      # 第三章实践代码
│   ├── 第四章/           # 第四章实践代码
│   └── 第五章/           # 第五章实践代码
│
└── README.md            # 项目说明文档
```

## 📝 内容目录

### 章节概览

* **第零章：序言**
  * 0.1 加入我们
  * 0.2 如何贡献？
  
* **第一章：环境配置**
  * 1.1 获取CAMEL
  * 1.2 API设置
  * 1.3 Hello CAMEL!
  * 1.4 第一章课程作业
  
* **第二章：Agent 的构成组件**
  * 2.1 智能体概述
  * 2.2 Agent设计原则与方法
  * 2.3 Models
  * 2.4 Messages
  * 2.5 Prompt Engineering
  * 2.6 Memory
  * 2.7 Tools
  * 2.8 第二章课程作业
  
* **第三章：CAMEL框架简介及实践**
  * 3.1 CAMEL框架简介
  * 3.2 创建你的第一个Agent Society
  * 3.3 创建你的Workforce
  * 3.4 第三章课程作业
  
* **第四章：CAMEL框架下的RAG应用**
  * 4.1 RAG的组件介绍
  * 4.2 向量数据库介绍
  * 4.3 搭建知识库
  * 4.4 构建RAG应用
  * 4.5 RAG应用的评估
  * 4.6 Graph RAG应用实战
  * 4.7 第四章课程作业
  
* **第五章：综合案例**
  * 5.1 应用概览
  * 5.2 用户意图识别模块
  * 5.3 旅游信息检索
  * 5.4 攻略生成模块
  * 5.5 反馈优化模块
  * 5.6 搭配知识集用
  * 5.7 第五章课程作业
  
  
* **附录**
  * 支持的模型
  * Loader补充
  * MCP补充（初稿, 飞书在线文档里）

## 🛠️ 使用指南

### 环境要求
- 推荐 Python 3.10 及以上

### 安装CAMEL
```bash
pip install "camel-ai[all]"
```

### 学习步骤
1. **阅读文档**：访问`docs`目录或在线文档，按章节顺序学习理论知识
2. **运行代码**：在`code`目录中找到对应章节的代码文件，按照说明运行实践练习
3. **完成作业**：每章末尾提供的作业可巩固所学知识
4. **项目实践**：综合应用所学内容，实现自己的多智能体系统

## 🔍 在线阅读

完整教程内容可访问以下链接之一查看：
- **GitHub Pages**: [https://datawhalechina.github.io/handy-multi-agent/](https://datawhalechina.github.io/handy-multi-agent/)
- **飞书文档（中文版）**: [https://fmhw1n4zpn.feishu.cn/docx/AF4XdOZpIo6TOaxzDK8cxInNnCe](https://fmhw1n4zpn.feishu.cn/docx/AF4XdOZpIo6TOaxzDK8cxInNnCe)


## 📅 Roadmap

- [x] 发布第一版内容内测
- [x] 飞书内容迁移仓库
- [x] 更新案例源代码文件
- [x] 发布第一版内容公测
- [x] 重构教程结构，系统整理化agent发展历程，补充更多实例和新特性讲解，更新camel版本到制作时最新

## 🧑‍💻 参与贡献

- 如果你想参与项目，欢迎查看 [Issue](https://github.com/datawhalechina/handy-multi-agent/issues) 了解未分配的任务
- 发现问题请在 [Issue](https://github.com/datawhalechina/handy-multi-agent/issues) 中进行反馈🐛
- 对项目感兴趣想要参与可以通过 [Discussion]() 进行交流💬
- 如有任何想法可以联系DataWhale&CAMEL社区开发者

## 👥 贡献者名单

### 核心贡献者
- [陈思州-项目负责人](https://github.com/jjyaoao) (Datawhale成员-CAMEL-AI成员)
- [孙韬-项目负责人](https://github.com/fengju0213) (Datawhale成员-CAMEL-AI成员)
- [姜舒凡-核心贡献者](https://github.com/Tsumugii24) (Datawhale成员)
- [范文栋-核心贡献者](https://github.com/Wendong-Fan) (CAMEL-AI成员-算法工程师)

### 主要贡献者
- [李川-内容创作者](https://github.com/MrLIChuan) (CAMEL-AI成员-索邦大学/巴黎理工学院 博士/助教)
- [小川-内容创作者](https://github.com/) (CAMEL-AI宣传大使)
- [豆腐酱-内容创作者](https://github.com/Tofu0142) (CAMEL-AI宣传大使)
- [王小为-内容创作者](https://github.com/cswangxiaowei) (小米NLP算法工程师)
- [任信行-内容创作者](https://github.com/renxinxing123) (CAMEL-AI宣传大使)
- [陆崇喜-内容创作者](https://github.com/Lucas-CX) (软件工程师)
- [邢硕-内容创作者](https://github.com/Susan2048) (Datawhale意向成员)
- [康婧淇-内容创作者](jkan0031@student.monash.edu) (Datawhale成员)
- [金子涵-内容创作者](https://github.com/dongyu23) (Datawhale意向成员)
- [朱忠懿-内容创作者](https://github.com/aut-rain) (Datawhale鲸英助教)


特别感谢[@Sm1les](https://github.com/Sm1les)对项目的帮助和支持~

## 📱 关注我们

<div align="center">
<table>
  <tr>
    <td align="center">
      <p>扫描下方二维码关注公众号：Datawhale</p>
      <img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width="180" height="180">
    </td>
    <td align="center">
      <p>扫描下方二维码关注公众号：CAMEL-AI</p>
      <img src="https://s2.loli.net/2025/03/06/ED5GPU1dRNqBk9j.png" width="180" height="180">
    </td>
  </tr>
</table>
</div>

## 📄 LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

*注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议*
