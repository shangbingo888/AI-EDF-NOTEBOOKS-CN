# 翻译验收报告

本报告由 `scripts/nb_verify.py` 与一次全局代码等价性扫描生成。

## 总览

| 项 | 数量 |
|---|---|
| 翻译的 notebook | 34 个 |
| 翻译的文档 | 11 个 |
| 翻译单元（markdown 单元格） | 422 |
| 翻译单元（代码注释） | 508 |
| 翻译单元（docstring） | 62 |
| **合计** | **992** |

## Notebook 校验结果

对每一对「英文源文件 / 中文译文」执行四类硬校验：nbformat 合法性、代码单元格可解析、抹除注释与 docstring 后代码逐字节一致、译文确实落入输出。

| 中文译文 | 校验 |
|---|---|
| `00-setup/00-environment.zh.ipynb` | PASS |
| `01-model-apis/00-prompting-basics.zh.ipynb` | PASS |
| `01-model-apis/01-structured-output.zh.ipynb` | PASS |
| `01-model-apis/02-tool-calling.zh.ipynb` | PASS |
| `01-model-apis/03-streaming.zh.ipynb` | PASS |
| `01-model-apis/04-context-and-caching.zh.ipynb` | PASS |
| `02-evals-basics/01-measuring-outputs.zh.ipynb` | PASS |
| `03-rag/00-what-is-rag.zh.ipynb` | PASS |
| `03-rag/01-embeddings-retrieval.zh.ipynb` | PASS |
| `03-rag/02-hybrid-and-reranking.zh.ipynb` | PASS |
| `03-rag/03-chunking.zh.ipynb` | PASS |
| `03-rag/04-why-rag-fails.zh.ipynb` | PASS |
| `04-evals/01-golden-sets.zh.ipynb` | PASS |
| `04-evals/02-llm-as-judge.zh.ipynb` | PASS |
| `04-evals/03-regression-evals.zh.ipynb` | PASS |
| `05-agents/01-agent-loop-from-scratch.zh.ipynb` | PASS |
| `05-agents/02-tool-design.zh.ipynb` | PASS |
| `05-agents/03-guardrails-and-budgets.zh.ipynb` | PASS |
| `05-agents/04-mcp-and-the-tool-ecosystem.zh.ipynb` | PASS |
| `05-agents/05-skills-and-progressive-disclosure.zh.ipynb` | PASS |
| `05-agents/06-harness-engineering.zh.ipynb` | PASS |
| `06-adaptation/01-fine-tune-vs-rag-vs-prompt.zh.ipynb` | PASS |
| `07-security/01-prompt-injection-and-trust.zh.ipynb` | PASS |
| `08-operations/01-observability-and-llmops.zh.ipynb` | PASS |
| `08-operations/02-reliability-and-fallbacks.zh.ipynb` | PASS |
| `08-operations/03-experiment-tracking-and-registry.zh.ipynb` | PASS |
| `09-serving-inference/01-serving-frameworks.zh.ipynb` | PASS |
| `09-serving-inference/02-inference-performance.zh.ipynb` | PASS |
| `10-ml-system-design/01-designing-an-inference-service.zh.ipynb` | PASS |
| `11-customer-craft/01-scoping-and-discovery.zh.ipynb` | PASS |
| `12-case-studies-and-capstone/01-customer-support-assistant.zh.ipynb` | PASS |
| `12-case-studies-and-capstone/02-contract-extraction-pipeline-vs-agent.zh.ipynb` | PASS |
| `12-case-studies-and-capstone/03-red-team-robustness-benchmark.zh.ipynb` | PASS |
| `12-case-studies-and-capstone/04-deepfake-image-detection.zh.ipynb` | PASS |

## 代码等价性

- 比对的代码单元格：235 个
- 代码被改动的单元格：0 个
- 结论：全部代码逻辑与原文件逐字节一致，变量名、函数名、字符串字面量、print 输出、错误消息均未改动

## 文档清单

- `.github/ISSUE_TEMPLATE/bug-or-api-drift.zh.md`
- `.github/ISSUE_TEMPLATE/notebook-request.zh.md`
- `12-case-studies-and-capstone/CAPSTONE.zh.md`
- `12-case-studies-and-capstone/README.zh.md`
- `CONTRIBUTING.zh.md`
- `README.zh.md`
- `data/README.zh.md`
- `docs/best-practices-and-anti-patterns.zh.md`
- `docs/curriculum-plan.zh.md`
- `docs/theming.zh.md`
- `utils/README.zh.md`

## 未翻译的文件（刻意保留）

- `LICENSE`——法律文本
- `.github/ISSUE_TEMPLATE/config.yml`——配置文件
- `docs/assets/social-preview.png`——图片
- 所有英文原文件（`*.ipynb`、`*.md`）——保持可运行、可对照

## 质量门禁

- 无翻译单元残留英文超标（阈值：markdown 单元格 10%）
- 所有中文文档的相对内部链接均解析到真实文件
- `aien/__init__.py` 原地翻译后通过 `py_compile` 与 `import` 校验

## 工具链

| 脚本 | 作用 |
|---|---|
| `scripts/nbcommon.py` | 共享逻辑：定位 markdown、注释、docstring 的可译区间 |
| `scripts/nb_extract.py` | 从 notebook 抽出待译文本为 work 清单 |
| `scripts/nb_apply.py` | 按 id 回填译文，生成中文 notebook |
| `scripts/nb_verify.py` | 硬校验，含代码等价性与译文覆盖检查 |
| `scripts/nb_fill.py` | 用 JSON 译文表回填 work 清单 |
| `scripts/md_fixlinks.py` | 把中文文档的相对链接改指中文版 |
| `scripts/md_checklinks.py` | 检查中文文档链接是否解析 |
