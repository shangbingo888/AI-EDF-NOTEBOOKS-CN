# 翻译词表（AI-EDF-NOTEBOOKS-CN 中文版）

本文件是全部 notebook 与文档翻译的统一口径。翻译前先读这张表，遇到新术语先补进来再动手。

## 核心原则

1. **术语优先保留英文**。工程师读者对 `embedding`、`agent`、`prompt` 的英文形态更熟悉，硬译反而增加理解成本。首次出现时用括号给中文解释，例如「embedding（向量化表示）」。
2. **代码零改动**。变量名、函数名、类名、字符串字面量、`print` 输出、`raise` 错误消息一律不动。
3. **结构照搬**。原文的标题层级、列表、表格、粗体、`code` 反引号、链接位置全部保留。
4. **不译内容**：命令、路径、URL、模型名（如 `openai/gpt-oss-120b`）、包名、API 参数名。

## 保留英文的术语

按类别列出。这些词在译文中直接写英文。

| 保留 | 说明 |
|---|---|
| prompt | 提示词。首次出现可写「prompt（提示词）」 |
| embedding | 向量化表示 |
| agent | 智能体 |
| RAG | Retrieval-Augmented Generation |
| tool calling | 工具调用 |
| token | 词元 |
| context window | 上下文窗口 |
| chunking | 分块 |
| reranking | 重排序 |
| retrieval | 检索 |
| eval / evaluation | 评测 |
| golden set | 黄金集 |
| judge | 评判模型（LLM-as-judge 保留英文） |
| guardrail | 护栏 |
| fine-tuning | 微调 |
| LoRA | 低秩适配 |
| serving | 服务化 |
| inference | 推理 |
| fallback | 降级 |
| observability | 可观测性 |
| harness | 测试骨架 |
| docstring | 文档字符串 |
| streaming | 流式 |
| batch | 批量 |
| cache / caching | 缓存 |
| latency | 延迟 |
| spend guard | 花费护栏 |
| rate limit | 速率限制 |
| red team | 红队 |
| capstone | 结业项目 |

## 固定译法

这些词组有统一译名，不要自由发挥。

| 英文 | 中文 |
|---|---|
| Forward Deployed Engineer (FDE) | 前向部署工程师（FDE） |
| AI Engineer | AI 工程师 |
| prompt injection | prompt 注入 |
| progressive disclosure | 渐进式披露 |
| regression eval | 回归评测 |
| structured output | 结构化输出 |
| tool design | 工具设计 |
| agent loop | agent 循环 |
| context budgeting | 上下文预算 |
| prompt caching | prompt 缓存 |
| experiment tracking | 实验追踪 |
| model registry | 模型注册表 |
| cost hygiene | 成本管控 |
| rate-limit backoff | 限流退避 |
| hallucination | 幻觉 |
| grounding | 落地事实 |
| anti-pattern | 反模式 |
| best practice | 最佳实践 |

## 文体约定

- 第二人称用「你」，不用「您」。
- 讲解语气保持原文的直白与自信，不要变得客套。原文说 "Don't hardcode a model name and forget it" 就写「不要把模型名写死然后忘了它」。
- 表格、编号步骤、加粗强调的词语位置与原文一一对应。
- 原文的 `**Goal:**`、`**How to pick one:**` 这类加粗小标签译成 `**目标：**`、`**怎么选：**`，保持加粗。
- 标题中的 `&` 译成「与」，如 "Environment & Cost Hygiene" → 「环境与成本管控」。
- 代码注释译成中文，但注释里若本身是命令或参数说明，保留其英文关键字。例如 `# only importable inside Colab` → `# 只能在 Colab 内导入`；而 `# pip install groq` 保持原样。

## 笔记本文档标题对照（供交叉引用时统一）

| 文件 | 中文标题 |
|---|---|
| 00-environment | 环境与成本管控 |
| 00-prompting-basics | Prompt 基础 |
| 01-structured-output | 结构化输出 |
| 02-tool-calling | 工具调用 |
| 03-streaming | 流式响应 |
| 04-context-and-caching | 上下文与缓存 |
| 01-measuring-outputs | 度量输出 |
| 00-what-is-rag | 什么是 RAG |
| 01-embeddings-retrieval | Embedding 与检索 |
| 02-hybrid-and-reranking | 混合检索与重排序 |
| 03-chunking | 分块 |
| 04-why-rag-fails | RAG 为什么会失败 |
| 01-golden-sets | 黄金集 |
| 02-llm-as-judge | LLM 作为评判模型 |
| 03-regression-evals | 回归评测 |
| 01-agent-loop-from-scratch | 从零实现 agent 循环 |
| 02-tool-design | 工具设计 |
| 03-guardrails-and-budgets | 护栏与预算 |
| 04-mcp-and-the-tool-ecosystem | MCP 与工具生态 |
| 05-skills-and-progressive-disclosure | Skills 与渐进式披露 |
| 06-harness-engineering | Harness 工程 |
| 01-fine-tune-vs-rag-vs-prompt | 微调、RAG、prompt 三条路线对比 |
| 01-prompt-injection-and-trust | prompt 注入与信任边界 |
| 01-observability-and-llmops | 可观测性与 LLMOps |
| 02-reliability-and-fallbacks | 可靠性与降级 |
| 03-experiment-tracking-and-registry | 实验追踪与模型注册表 |
| 01-serving-frameworks | 服务化框架 |
| 02-inference-performance | 推理性能 |
| 01-designing-an-inference-service | 设计一个推理服务 |
| 01-scoping-and-discovery | 需求界定与探索 |
| 01-customer-support-assistant | 客服助手 |
| 02-contract-extraction-pipeline-vs-agent | 合同提取：pipeline 与 agent 之争 |
| 03-red-team-robustness-benchmark | 红队鲁棒性基准 |
| 04-deepfake-image-detection | 深度伪造图像检测 |
