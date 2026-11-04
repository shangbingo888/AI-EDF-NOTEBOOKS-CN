---
name: Bug / API drift
about: 某个单元格报错、模型返回 404，或者某个库的 API 变了
title: "[Bug] "
labels: bug
---

**哪个 notebook 的哪一格？**
<!-- 例如：06-adaptation/01-fine-tune-vs-rag-vs-prompt.ipynb 里的 LoRA 附录 -->

**发生了什么？**
<!-- 把报错粘上来。如果是依赖/API 漂移（peft、trl、vllm、transformers、
     Groq 的模型 id 等），请附上报错的库版本。这些 notebook 跑在真实的 API 和库上，
     所以版本漂移是预期之内的——把版本号写清楚，是你最该提供的信息。 -->

**环境**
- 在哪里运行：<!-- Colab（CPU / T4 GPU）/ 本地 -->
- 相关的 Groq 模型：<!-- 例如 openai/gpt-oss-120b -->

**预期行为**
<!-- 本来应该发生什么。 -->
