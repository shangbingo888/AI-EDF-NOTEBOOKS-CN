# utils

共享 setup 现在放在仓库根目录的 `aien` 包里（由每个 notebook 的第一格安装）：
`from aien import setup`。它只做一件事：加载 API key，然后交回一个现成的 Groq
client。

刻意保持到最小。一旦共享代码在 notebook 所教的概念之上长出抽象层，它就失败了。忍住
别去搭框架。这个文件夹留作未来某个只服务 notebook 的辅助工具（比如美化打印）的落脚
处——那种还不值得打包的东西。
