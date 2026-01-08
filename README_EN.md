# Handy Multi-Agent Tutorial

<div align="center">
  <img src="https://s2.loli.net/2025/04/05/XagKqdzWe67fDt8.jpg" alt="Handy Multi-Agent Logo">
  <br>
  <p>A Practical Guide to Building Multi-Agent Systems from Scratch with the CAMEL Framework</p>
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

[中文](./README.md) | English

> 🎉 **Version 1.0 officially released!** Complete tutorial documentation has been updated in the docs directory, with executable code available in the code directory. If you have any questions or feature suggestions, please feel free to submit an issue on GitHub~

## 📖 Project Introduction

**Handy-Multi-Agent** is a practical guide designed for developers who want to deeply understand and practice multi-agent systems. This tutorial is based on the leading domestic multi-agent framework [CAMEL-AI (NeurIPS'2023)](https://arxiv.org/pdf/2303.17760.pdf), gradually guiding readers from basic single Agent development to building complex Multi-Agent applications.

### 🎯 Target Audience

This project focuses on practice and hands-on Agent application development, while integrating necessary theoretical knowledge. It is suitable for:
- Learners interested in multi-agent systems, large model applications, or artificial intelligence
- Developers who want to understand and explore LLM applications in multi-agent systems through practice

### 🚀 Learning Objectives

Through this project, we hope to help developers:
1. **Understand Fundamentals**: Master the usage of the CAMEL framework and understand basic Agent concepts
2. **Improve Skills**: Enhance capabilities in building and managing agents through practical projects involving RAG, Memory, Multi-Agent, and other technologies
3. **Apply in Practice**: Apply learned knowledge to solve real-world problems, cultivating practical abilities and innovative thinking

### 👨‍💻 Prerequisites

- **Technical Foundation**: Basic Python programming skills, ability to read and understand project source code and related theories
- **Interest & Motivation**: Passionate about the AI agent field, eager to develop personalized agent capabilities at the code level

## 📚 Project Structure

```
handy-multi-agent/
├── docs/                # Tutorial documentation
│   ├── chapter0/        # Chapter 0: Preface
│   ├── chapter1/        # Chapter 1: Basic Configuration
│   ├── chapter2/        # Chapter 2: Agent Components
│   ├── chapter3/        # Chapter 3: CAMEL Framework Introduction
│   ├── chapter4/        # Chapter 4: RAG Applications with CAMEL
│   ├── chapter5/        # Chapter 5: Comprehensive Case Study
│   ├── chapter6/        # Chapter 6: Conclusion
│   ├── appendix/        # Appendix
│   ├── images/          # Document images
│   └── files/           # Related files
│
├── code/                # Supporting code
│   ├── 第一章.ipynb      # Chapter 1 code
│   ├── 第二章.ipynb      # Chapter 2 code
│   ├── 第三章.ipynb      # Chapter 3 code
│   ├── 第四章/           # Chapter 4 code
│   └── 第五章/           # Chapter 5 code
│
└── README.md            # Project documentation
```

## 📝 Table of Contents

### Chapter Overview

* **Chapter 0: Preface**
  * 0.1 Join Us
  * 0.2 How to Contribute?
  
* **Chapter 1: Basic Configuration**
  * Getting CAMEL, API Setup, Hello CAMEL, Exercises
  
* **Chapter 2: Agent Components**
  * Agent Overview, Design Principles, Models, Messages, Prompt Engineering, Memory, Tools, Exercises
  
* **Chapter 3: CAMEL Framework Introduction and Practice**
  * Framework Introduction, First Agent Society, Creating Workforce, Exercises
  
* **Chapter 4: RAG Applications with CAMEL Framework**
  * RAG Components, Vector Databases, Building Knowledge Base, Building RAG Applications, RAG Evaluation, Graph RAG Practice, Exercises
  
* **Chapter 5: Comprehensive Case Study**
  * Application Overview, Intent Recognition, Travel Information Retrieval, Strategy Generation, Feedback Optimization, Knowledge Integration, Exercises
  
* **Appendix**
  * Supported Models
  * Loader Supplement
  * MCP Supplement (Draft, online in Feishu document)

## 🛠️ Getting Started

### Requirements
- Python 3.10 or higher recommended

### Install CAMEL
```bash
pip install "camel-ai[all]"
```

### Learning Steps
1. **Read Documentation**: Visit the `docs` directory or online documentation, learn theoretical knowledge in chapter order
2. **Run Code**: Find corresponding chapter code files in the `code` directory and run practice exercises as instructed
3. **Complete Assignments**: Consolidate learned knowledge through assignments at the end of each chapter
4. **Project Practice**: Apply comprehensive learned content to implement your own multi-agent system

## 🔍 Online Reading

Complete tutorial content can be accessed through:
- **GitHub Pages**: [https://datawhalechina.github.io/handy-multi-agent/](https://datawhalechina.github.io/handy-multi-agent/)
- **Feishu Document**: [https://fmhw1n4zpn.feishu.cn/docx/AF4XdOZpIo6TOaxzDK8cxInNnCe](https://fmhw1n4zpn.feishu.cn/docx/AF4XdOZpIo6TOaxzDK8cxInNnCe)

## 📅 Roadmap

- [x] Release first version for internal testing
- [x] Migrate Feishu content to repository
- [x] Update case source code files
- [x] Release first version for public testing
- [ ] Restructure tutorial, systematically organize agent development history, add more examples and new features, update CAMEL to latest version

## 🧑‍💻 Contributing

- If you want to participate in the project, check [Issues](https://github.com/datawhalechina/handy-multi-agent/issues) for unassigned tasks
- Report bugs in [Issues](https://github.com/datawhalechina/handy-multi-agent/issues) 🐛
- Interested in participating? Join discussions in [Discussions]() 💬
- Contact Datawhale & CAMEL community developers with any ideas

## 👥 Contributors

### Core Contributors
- [Chen Sizhou - Project Lead](https://github.com/jjaoao) (Datawhale Member - CAMEL-AI Member)
- [Sun Tao - Project Lead](https://github.com/fengju0213) (Datawhale Member - CAMEL-AI Member)
- [Jiang Shufan - Core Contributor](https://github.com/Tsumugii24) (Datawhale Member)
- [Fan Wendong - Core Contributor](https://github.com/Wendong-Fan) (CAMEL-AI Member - Algorithm Engineer)

### Main Contributors
- [Li Chuan - Content Creator](https://github.com/MrLIChuan) (CAMEL-AI Member - Sorbonne/Paris Tech PhD/TA)
- [Xiaochuan - Content Creator](https://github.com/) (CAMEL-AI Ambassador)
- [Tofu Sauce - Content Creator](https://github.com/Tofu0142) (CAMEL-AI Ambassador)
- [Wang Xiaowei - Content Creator](https://github.com/cswangxiaowei) (Xiaomi NLP Algorithm Engineer)
- [Ren Xinxing - Content Creator](https://github.com/renxinxing123) (CAMEL-AI Ambassador)
- [Lu Chongxi - Content Creator](https://github.com/Lucas-CX) (Software Engineer)
- [Xing Shuo - Content Creator](https://github.com/Susan2048) (Datawhale Prospective Member)
- [Kang Jingqi - Content Creator](jkan0031@student.monash.edu) (Datawhale Member)
- [Jin Zihan - Content Creator](https://github.com/dongyu23) (Datawhale Prospective Member)
- [Zhu Zhongyi - Content Creator](https://github.com/aut-rain) (Datawhale Teaching Assistant)

Special thanks to [@Sm1les](https://github.com/Sm1les) for help and support~

## 📱 Follow Us

<div align="center">
<table>
  <tr>
    <td align="center">
      <p>Scan QR code to follow: Datawhale</p>
      <img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width="180" height="180">
    </td>
    <td align="center">
      <p>Scan QR code to follow: CAMEL-AI</p>
      <img src="https://s2.loli.net/2025/03/06/ED5GPU1dRNqBk9j.png" width="180" height="180">
    </td>
  </tr>
</table>
</div>

## 📄 License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

