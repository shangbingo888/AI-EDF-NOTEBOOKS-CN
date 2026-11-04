# AI-EDF-NOTEBOOKS

**按面试真正会考你的方式来学应用层 LLM 技术栈：不用框架、用免费 API，从 prompt
一路走到 serving、fine-tuning，再到一个红队基准测试。**

面向 **AI Engineer / Forward Deployed Engineer (FDE)** 技能组合的可运行 Colab
notebook。你在 foundation model 之上搭建能跑的系统（模型 API、RAG、evals、agent、
适配、serving），全程使用原生 API，不用框架。

### 它有什么不一样

- **刻意不用框架。** 你先把 agent 循环、RAG、evals 用原生 API 调用亲手写一遍，
  这样在伸手去够 LangChain/LlamaIndex 之前就明白它们到底做了什么（也能判断
  *什么时候不该*用）。模式是长久的，封装层总在换。
- **Evals 是主线。** 「先度量，再调优」早早装进你脑子里，然后在每一节反复出现。
  正是这个习惯，把「真上过系统的工程师」和「只搭过 demo 的人」区分开。
- **端到端免费运行。** 所有内容都跑在**免费的
  [Groq](https://console.groq.com/) API** 上（不需要信用卡）。Groq 托管不了的两个
  主题——LoRA fine-tuning（06）和自托管 serving（09）——采用概念优先的讲法，另附
  可选的、明确圈起来的 Colab-GPU 附录，这些附录都**在真实的 Colab T4 上验证过**。
- **真实案例，不是玩具 demo。** 四个端到端
  [案例研究](12-case-studies-and-capstone/) 展示这些技能在真实约束下怎么组合：一个
  *在生产环境里被 debug 过*的支持助手、一场 pipeline 与 agent 的成本对决、一个
  红队鲁棒性基准，以及一个深度伪造合规测试系统——它对比检测器、VLM 和混合方案。
- **全程 OpenAI 兼容**，所以每个模式都能直接迁移到 OpenAI，稍作改动也能迁移到
  Anthropic。换掉 base URL，这些技能就都带得走。

作为一份 **FDE / AI 工程师转型学习计划** 的动手配套项目而建。那份计划讲该学什么、
为什么学；这些 notebook 是你真正动手跑的地方。

## 这本书写给谁

正在转向 AI Engineer、FDE、Applied AI 或 Solutions Engineer (AI) 岗位的后端或全栈
工程师。职位名称不同，干的活大体相同。你已经能写出上线代码；你想要的是在它之上再加
一层应用模型的能力。

## 学习顺序

从上往下做。每个 notebook 都是自包含的（自己装依赖、从 Colab secrets 读 API key），
结尾都有练习题。

### 00 — Setup

| Notebook | 你会学到什么 |
|---|---|
| [环境与成本管控](00-setup/00-environment.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/00-setup/00-environment.zh.ipynb) | 通过 Colab secrets 管理 API key、花费护栏、模型选择 |

### 01 — Model APIs

| Notebook | 你会学到什么 |
|---|---|
| [Prompt 基础](01-model-apis/00-prompting-basics.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/01-model-apis/00-prompting-basics.zh.ipynb) | 清晰的指令、few-shot、输出格式规范、逐步推理：最便宜的杠杆，每一招都用一个数字展示它的效果 |
| [结构化输出](01-model-apis/01-structured-output.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/01-model-apis/01-structured-output.zh.ipynb) | 从模型里稳定地拿到 JSON，以及它在哪里会崩 |
| [工具调用](01-model-apis/02-tool-calling.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/01-model-apis/02-tool-calling.zh.ipynb) | 端到端的函数/工具调用，包含错误路径 |
| [流式响应](01-model-apis/03-streaming.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/01-model-apis/03-streaming.zh.ipynb) | streaming 响应，以及 UI 需要从它拿到什么 |
| [上下文与缓存](01-model-apis/04-context-and-caching.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/01-model-apis/04-context-and-caching.zh.ipynb) | 上下文窗口预算、prompt 缓存、batch 与实时定价的对比 |

### 02 — Evals I：度量输出

| Notebook | 你会学到什么 |
|---|---|
| [度量输出](02-evals-basics/01-measuring-outputs.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/02-evals-basics/01-measuring-outputs.zh.ipynb) | 针对第 01 节任务建立黄金集和指标；在动手搭任何需要调优的东西*之前*，先装上「先度量，再调优」的习惯。Evals 是主线，从这节之后的每一节它都会回来 |

### 03 — RAG

| Notebook | 你会学到什么 |
|---|---|
| [什么是 RAG](03-rag/00-what-is-rag.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/03-rag/00-what-is-rag.zh.ipynb) | retrieve → augment → generate 循环、为什么 RAG 胜过朴素的 LLM，以及为什么 RAG 不等于 embedding，附带一个 15 行的可运行 demo |
| [Embedding 与检索](03-rag/01-embeddings-retrieval.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/03-rag/01-embeddings-retrieval.zh.ipynb) | embedding 的选择、向量检索、相似度的坑。先把检索跑通 |
| [混合检索与重排序](03-rag/02-hybrid-and-reranking.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/03-rag/02-hybrid-and-reranking.zh.ipynb) | 关键词 + 向量的混合检索、reranker，以及各自在什么时候值回成本 |
| [分块](03-rag/03-chunking.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/03-rag/03-chunking.zh.ipynb) | 在真实的脏语料上实践分块策略，放到最后再回头，用检索效果来评判它们 |
| [RAG 为什么会失败](03-rag/04-why-rag-fails.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/03-rag/04-why-rag-fails.zh.ipynb) | 诊断烂答案：瓶颈通常是检索质量，而不是生成 |

### 04 — Evals II：拉开差距的那一环

| Notebook | 你会学到什么 |
|---|---|
| [黄金集](04-evals/01-golden-sets.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/04-evals/01-golden-sets.zh.ipynb) | 为第 03 节的 RAG 系统构建黄金集 |
| [LLM 作为评判模型](04-evals/02-llm-as-judge.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/04-evals/02-llm-as-judge.zh.ipynb) | judge prompt、与人工判断的一致率，以及 judge 自身的失败模式 |
| [回归评测](04-evals/03-regression-evals.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/04-evals/03-regression-evals.zh.ipynb) | 把 evals 当作 CI：在你改 prompt 或换模型时抓住质量回归 |

### 05 — Agents

| Notebook | 你会学到什么 |
|---|---|
| [从零实现 agent 循环](05-agents/01-agent-loop-from-scratch.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/01-agent-loop-from-scratch.zh.ipynb) | 用原生 API 调用写出一个能跑的 agent 循环，不用任何框架 |
| [工具设计](05-agents/02-tool-design.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/02-tool-design.zh.ipynb) | 设计出模型真正用得好的工具 |
| [护栏与预算](05-agents/03-guardrails-and-budgets.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/03-guardrails-and-budgets.zh.ipynb) | 停止条件、成本/延迟预算，以及 pipeline 什么时候胜过 agent |
| [MCP 与工具生态](05-agents/04-mcp-and-the-tool-ecosystem.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/04-mcp-and-the-tool-ecosystem.zh.ipynb) | 概念：Model Context Protocol 标准化了什么、它怎样映射到原生工具循环，以及什么时候该用它 |
| [Skills 与渐进式披露](05-agents/05-skills-and-progressive-disclosure.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/05-skills-and-progressive-disclosure.zh.ipynb) | 概念：把可复用的经验打包成 agent 按需加载的东西。`SKILL.md` 模式、它对上下文预算的回报，以及把 Tools/MCP/Skills 讲成一个故事 |
| [Harness 工程](05-agents/06-harness-engineering.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/05-agents/06-harness-engineering.zh.ipynb) | 综合：围绕这次调用的那副脚手架——上下文组装与压缩、工具结果的整形、验证循环。为这一节一直零散传授的那门手艺正式命名 |

### 06 — 适配模型

| Notebook | 你会学到什么 |
|---|---|
| [微调、RAG、prompt 三条路线对比](06-adaptation/01-fine-tune-vs-rag-vs-prompt.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/06-adaptation/01-fine-tune-vs-rag-vs-prompt.zh.ipynb) | 什么时候改模型的权重，什么时候改它的输入；LoRA/QLoRA 是什么、成本多少；你在会议室里会打的那场辩论，另附一个在免费 GPU 上真跑 LoRA fine-tune 的可选环节 |

### 07 — Security

| Notebook | 你会学到什么 |
|---|---|
| [prompt 注入与信任边界](07-security/01-prompt-injection-and-trust.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/07-security/01-prompt-injection-and-trust.zh.ipynb) | 直接与间接的 prompt 注入、输出处理、PII、过度授权。OWASP LLM Top 10 风险，先现场攻破再加固 |

### 08 — Operations

| Notebook | 你会学到什么 |
|---|---|
| [可观测性与 LLMOps](08-operations/01-observability-and-llmops.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/08-operations/01-observability-and-llmops.zh.ipynb) | 追踪每一次调用、安全地记录 prompt、成本/延迟/错误指标、漂移检测，以及 observe→eval 的反馈闭环 |
| [可靠性与降级](08-operations/02-reliability-and-fallbacks.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/08-operations/02-reliability-and-fallbacks.zh.ipynb) | 带退避的重试、超时、降级模型、输出校验、熔断器、优雅降级 |
| [实验追踪与模型注册表](08-operations/03-experiment-tracking-and-registry.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/08-operations/03-experiment-tracking-and-registry.zh.ipynb) | 端到端使用 MLflow：从第 04 节的 eval harness 里记录 run/参数/指标，注册并给模型做版本，再按阶段推进：正是这套工具，把「我跑过一次 eval」变成可追踪、可复现的工作流 |

### 09 — Serving 与推理性能

当免费的 Groq API 跑不了某个主题时（这些框架需要 GPU），notebook 就采用
**概念优先**的讲法，并圈出一个可选的 Colab-GPU 附录，跟第 06 节的 LoRA 附录是同一种
模式。

| Notebook | 你会学到什么 |
|---|---|
| [服务化框架](09-serving-inference/01-serving-frameworks.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/09-serving-inference/01-serving-frameworks.zh.ipynb) | AI 工程师真正要在其间做选择的 serving 技术栈（vLLM、TGI、Triton、TensorRT-LLM）：各自优化什么、怎样映射到你一直在调用的原生 API，以及什么时候该用哪个 |
| [推理性能](09-serving-inference/02-inference-performance.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/09-serving-inference/02-inference-performance.zh.ipynb) | 吞吐和延迟背后的那些杠杆：连续批处理、KV cache、量化，以及吞吐与延迟的取舍，另附估算一次部署规模的草稿纸计算 |

### 10 — ML 系统设计与性能

| Notebook | 你会学到什么 |
|---|---|
| [设计一个推理服务](10-ml-system-design/01-designing-an-inference-service.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/10-ml-system-design/01-designing-an-inference-service.zh.ipynb) | 概念：ML 系统设计面试，从头到尾演练一遍：QPS/显存/延迟/成本估算、副本扩缩、排队、缓存，以及各类 SLA 取舍，全都落在一个贴近现实的 LLM serving 题目上 |

### 11 — 客户手艺（FDE 的差异点）

| Notebook | 你会学到什么 |
|---|---|
| [需求界定与探索](11-customer-craft/01-scoping-and-discovery.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/11-customer-craft/01-scoping-and-discovery.zh.ipynb) | 把一句含糊的客户需求变成范围清晰、可评测的系统：探索式提问、一页纸的范围界定文档、demo 的纪律：这正是大多数工程师拿不出证据的客户场景面试环节 |

### 12 — 案例研究与结业项目

技能在这里汇成项目。先看一个**案例研究**（一个贴近现实的场景，端到端跑通、可运行），
再进入**结业项目（capstone）**：那个由你自己搭建、真正部署上线的仓库。
（[本节概览](12-case-studies-and-capstone/README.zh.md)。）

| Notebook | 你会学到什么 |
|---|---|
| [案例研究 A — 客服助手](12-case-studies-and-capstone/01-customer-support-assistant.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/01-customer-support-assistant.zh.ipynb) | 一个场景从范围界定 → 搭建 → 上线 → **在生产中 debug**：一句含糊的需求变成已部署、已评测的 RAG+agent 助手，随后出现一次真实的质量回归（语料迁移后索引过期），由你诊断并修复。一条从搭建到 debug 的弧线，串起第 02–11 节 |
| [案例研究 B — 合同提取：pipeline 与 agent 之争](12-case-studies-and-capstone/02-contract-extraction-pipeline-vs-agent.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/02-contract-extraction-pipeline-vs-agent.zh.ipynb) | 面试官最爱考的那个判断题：把*同一个*提取任务分别用 agent 和 pipeline 实现一遍，然后用准确率 + token 成本证明：当步骤已知时 pipeline 胜出 |
| [案例研究 C — 红队鲁棒性基准](12-case-studies-and-capstone/03-red-team-robustness-benchmark.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/03-red-team-robustness-benchmark.zh.ipynb) | 另一种*类型*的系统，一个评测模型而不是服务模型的 harness：attacker→target→judge（PAIR）循环，用来度量攻击成功率，它把 agent 循环、LLM-judge、安全与 evals 组合在一起 |
| [案例研究 D — 面向 EU AI Act 第 50(4) 条的深度伪造检测](12-case-studies-and-capstone/04-deepfake-image-detection.zh.ipynb)<br>[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shangbingo888/AI-EDF-NOTEBOOKS-CN/blob/main/12-case-studies-and-capstone/04-deepfake-image-detection.zh.ipynb) | 对比三种标记*未披露*深度伪造的方案：一个开箱即用的检测器（在 OpenFake 上训练的 SwinV2，对比经典的 2020 年 CNNDetection ResNet-50）、一个端到端的 VLM，以及一个额外加了来源校验的混合方案。先在精挑的案例上跑，再对任何你给的图片 URL 跑。它展示了为什么「这是不是 AI 生成的」和「它是否违反 Art. 50(4)」需要不同的工具 |

**结业项目：** 那份[任务书](12-case-studies-and-capstone/CAPSTONE.zh.md)，对应那个会写进你
简历的已部署项目——一个带有 serving 组件和 eval 报告的真实仓库。案例研究是为了学习；
结业项目是为了求职。

## 约定

- **原生模型 API，不用框架。** 模式是长久的，封装层总在换。
- **一份共享语料**（`data/`），RAG 和 eval 两节共用，这样 evals 度量的就是你真正搭出来
  的那套检索。
- **自包含的 notebook。** 第一格装依赖，第二格调用
  `from aien import setup; client, MODEL = setup()` 从 Colab secrets（或本地环境变量）
  加载你的 key。notebook 之间没有隐藏状态。`aien` 是本仓库里那个极小的共享 setup 包
  （凭据加载只有一处可改），由第一格自动安装。
- **每个 notebook 都以练习题收尾。** 做完再往下走。

## 环境搭建

1. 在 [console.groq.com](https://console.groq.com/) 领一个免费 API key，不需要信用卡。
2. 在 Colab 里：左侧边栏的钥匙图标 → 把 `GROQ_API_KEY` 加为 secret，并打开该 notebook
   的访问开关。
3. 点任意 notebook 的徽章打开它，从上往下运行。

要在本地跑：`pip install -r requirements.txt && pip install -e .`（第二条命令安装
`aien` setup 辅助包），`export GROQ_API_KEY=...`，然后用 Jupyter 打开。

