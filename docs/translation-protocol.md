# 翻译执行协议

本文件是批量翻译的执行说明。任何执行者（人或 agent）在翻译本仓库任何一个文件前，先读这份协议和 `docs/translation-glossary-zh.md`。

## 硬性规则

1. **不改英文原文件**。翻译只产出新文件，英文版始终保持可运行、可对照。
2. **不改 `scripts/` 下的脚本**。脚本已通过全仓库身份往返测试（36 个文件、1070 个单元全部通过）。
3. **不改代码语义**。变量名、函数名、类名、字符串字面量、`print` 输出、`raise` 错误消息、命令、路径、URL、模型名一律不动。
4. **不跳过校验**。`nb_verify.py` 必须报 PASS 才算这一篇做完。
5. **不使用机器翻译的直译语气**。按 `docs/translation-glossary-zh.md` 的文体约定，读起来要像中文技术书，而不是英文句子的逐词替换。

## 命名约定

| 原文件 | 译文 |
|---|---|
| `03-rag/01-embeddings-retrieval.ipynb` | `03-rag/01-embeddings-retrieval.zh.ipynb` |
| `docs/theming.md` | `docs/theming.zh.md` |

## Notebook 翻译流程

对每一个 `.ipynb`，按顺序执行四步。

**第 1 步：抽出待译文本**

```bash
python3 scripts/nb_extract.py <源文件> .translation/<名字>.jsonl
```

输出里每行是一个待译单元，含 `id`、`kind`（`markdown` / `comment` / `docstring`）、`cell`、`src`。

**第 2 步：写译文**

新建 `.translation/<名字>.zh.json`，格式是 `{"<id>": "<中文>"}`。要求：

- 覆盖 `.jsonl` 里出现的**每一个** id，一个都不能少。
- `markdown` 单元：整格翻译，保留原有的标题层级、列表、表格、加粗、`code` 反引号、链接位置。
- `comment` 单元：翻译注释文字，**保留行首的 `#` 符号和原有缩进**。注释常被拆成多行，翻译时让整段读通顺，每行仍以 `#` 开头。
- `docstring` 单元：只写纯文本，**不要写三引号**，脚本会自动加上并折行。保留其中的 `code` 反引号和英文标识符。
- 纯链接或纯 HTML 的 markdown 单元（例如 Colab 徽章那一格）：直接照抄原文本作为译文。

**第 3 步：回填并生成**

```bash
python3 scripts/nb_fill.py .translation/<名字>.jsonl .translation/<名字>.zh.json
python3 scripts/nb_apply.py <源文件> .translation/<名字>.jsonl <译文路径>
```

**第 4 步：校验，必须通过**

```bash
python3 scripts/nb_verify.py <源文件> <译文路径> --work .translation/<名字>.jsonl
```

看到 `PASS <文件名>` 才算完成。若报 `FAIL`，按提示修正译文后重跑第 3、4 步。

## Markdown 文档翻译流程

文档没有代码单元格，直接写整份 `*.zh.md` 文件，然后处理内部链接：

```bash
python3 scripts/md_fixlinks.py <译文路径>
```

该脚本把指向中英对照文件的相对链接（如 `](03-rag/01-embeddings-retrieval.ipynb)`）改成指向中文版。绝对 URL 不动。

## 术语

以 `docs/translation-glossary-zh.md` 为准。遇到词表未覆盖的新术语：先按「保留英文 + 首次出现括号加中文解释」处理，并把该术语补进词表。

## 完成后的汇报格式

每个文件报一行：`<译文路径> — PASS`。最后汇总：本批产出的文件清单、单元总数、校验结果。若某个文件无法通过校验，明确指出文件、失败原因、以及你打算怎么修。
