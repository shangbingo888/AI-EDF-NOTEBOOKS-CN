"""AI-EDF-NOTEBOOKS-CN 的共享初始化代码。

只做一件事：加载 Groq API key（Colab Secrets 或环境变量），并交回一个
可直接使用的 client 加上默认模型。这段代码原本内联在每个 notebook 里——
现在集中到一处，改动只需落在一个地方。

刻意保持极小。notebook 教的是原始 API 的用法；这里只去掉复制粘贴的凭据
样板代码，不隐藏任何值得学习的概念。未抽象前的版本见
00-setup/00-environment.ipynb。
"""

DEFAULT_MODEL = "openai/gpt-oss-120b"

__all__ = ["setup", "load_key", "DEFAULT_MODEL"]


def load_key():
    """确保 GROQ_API_KEY 已写入环境变量。

    在 Colab 里，从 Secrets 读取（左侧边栏的钥匙图标）。在本地运行，则
    期望它以环境变量的形式存在。缺失时抛出清晰、可操作错误，而不是等到
    后面在 client 内部才失败。
    """
    import os

    try:
        from google.colab import userdata  # 只能在 Colab 内导入
    except ImportError:
        # 不在 Colab 里——期望 key 存在于环境变量中。
        if not os.environ.get("GROQ_API_KEY"):
            raise RuntimeError(
                "GROQ_API_KEY is not set. Run `export GROQ_API_KEY=...` in your "
                "shell before launching Jupyter, or set it in os.environ."
            )
        return

    # 在 Colab 里：从 Secrets 取值，出错时给出的信息会指明确切的修法。
    try:
        os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
    except Exception as e:
        raise RuntimeError(
            "Couldn't read GROQ_API_KEY from Colab Secrets. Click the key icon "
            "in the left sidebar, add a secret named exactly GROQ_API_KEY, and "
            "flip 'Notebook access' on for this notebook, then re-run this cell."
        ) from e


def setup(model=DEFAULT_MODEL, quiet=False, max_retries=8):
    """加载 key，并返回可直接使用的 (client, model) 组合。

    notebook 里的用法：

        from aien import setup
        client, MODEL = setup()

    传入 `model=` 可以覆盖默认模型（例如批量任务换用一个更小的模型）。
    如果后续调用报 404，列出可用模型看看——见 00-setup/00-environment.ipynb。

    `max_retries`（默认 8，SDK 默认是 2）：Groq 免费档的每分钟 token 上限
    很低，所以一个连续发起多次调用的 notebook 可能撞上 HTTP 429。SDK 会对
    429 自动退避重试，并遵循服务端的 `retry-after` 提示；把上限调高，只是
    让这些短暂的等待透明地过去，而不是变成报错。没超限时不产生任何成本。
    """
    load_key()
    from groq import Groq  # 延迟导入，这样没有装 groq 时 `import aien` 依然可用

    client = Groq(max_retries=max_retries)
    if not quiet:
        print(f"Groq client ready. MODEL = {model}")
    return client, model
