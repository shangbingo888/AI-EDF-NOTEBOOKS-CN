# 共享语料

一份刻意弄得乱糟糟的语料，供 RAG（03）和 evals（04）两节共用，好让 eval notebook
度量的就是你真正搭出来的那套检索。

每个 RAG/evals notebook 都包含同一个语料下载 cell（自包含），所以你先跑哪一个，它就
会把内容填进这个目录。按章节顺序，那是 `03-rag/01-embeddings-retrieval.ipynb`。在
Colab 里下载并缓存到这里；本地运行时则直接提交小的源文件。
