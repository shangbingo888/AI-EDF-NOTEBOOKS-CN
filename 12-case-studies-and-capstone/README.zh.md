# 案例研究与结业项目

教学 notebook（00–11）各自只讲一项技能。这最后一节是它们汇成**项目**的地方：先看一个
做好的实例，再亲手搭一个自己的。

## 案例研究：看别人从头到尾做一遍

一个**案例研究**把某个贴近现实的场景一路走完：一句含糊的客户需求，经过范围界定、度量、
搭建、上线，然后**在生产中 debug**。凡是「讲一遍不如跑一遍」的地方，它们都可运行——你
能亲眼看着一个索引过期时质量分往下掉，重新建索引后又恢复。

| 案例 | 用例 | 应用类型 | 它教的角度 |
|---|---|---|---|
| [01 — Customer-support assistant](01-customer-support-assistant.zh.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/01-customer-support-assistant.zh.ipynb) | 客户支持 | RAG + agent，**搭建 → debug** | 把一句含糊的需求界定成一个已部署、已评测的系统，再在它上线后质量崩塌时诊断它 |
| [02 — Contract extraction: pipeline vs agent](02-contract-extraction-pipeline-vs-agent.zh.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/02-contract-extraction-pipeline-vs-agent.zh.ipynb) | 文档处理 | **Pipeline vs agent** | 那道判断题：在同一个任务上把两者都搭出来，用 eval + token 成本证明：步骤已知时 pipeline 胜出 |
| [03 — Red-team robustness benchmark](03-red-team-robustness-benchmark.zh.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/03-red-team-robustness-benchmark.zh.ipynb) | 安全 / 评测 | **对抗性 harness** | 另一种*类型*的系统：attacker→target→judge 的 PAIR 循环，度量的是模型的鲁棒性（ASR），而不是你对外提供的某个服务 |
| [04 — Deepfake detection for EU AI Act Art. 50(4)](04-deepfake-image-detection.zh.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/04-deepfake-image-detection.zh.ipynb) | 信任与安全 / 合规 | **分类器 + VLM + 来源校验，横向对比** | 检测不等于合规：开箱检测器、一个 VLM、一个来源校验和一个混合方案，先在精挑的 OpenFake 案例上过一遍（真实人物深度伪造、匿名伪造、动漫、真实照片），再对你给的任意图片 URL 跑 |

> **⭐ 核心要点 —** 面试和真实工作从不会把「实现一条 RAG pipeline」递到你手上。它们递过来
> 的是「我们客服团队快撑不住了，帮帮忙。」这两句话之间的差距，就是这份工作。案例研究
> 就活在那道缝里。

## 结业项目：现在搭你自己的

案例研究展示的是*某个*项目。**[结业项目（capstone）](CAPSTONE.zh.md)** 是*你自己的*，
那个会写进简历的已部署仓库。它刻意**不是** notebook：在一个筛生产判断力的面试环节里，
notebook 项目会传达出「周末玩家」的信号。案例研究可以是 notebook，因为它是一个做好的
范例；你的结业项目必须是一个真实、已部署的仓库。

**→ [读结业项目任务书](CAPSTONE.zh.md)**，里面有不可妥协的要求、该伸手去够的现代技术栈、
该展示的系统思维数字、Agile/Scrum 的角色故事，以及面试就绪清单。
