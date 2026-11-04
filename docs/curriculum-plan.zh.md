# 课程规划与设计日志

本仓库结构的工作笔记：为什么各节是这样排的、调研过什么、已经定下（和否掉）哪些决定、
还有什么悬而未决。留在这里，是为了即便对话上下文丢了，推理过程也还在。

最后更新：2026-10-07。

## 这个仓库是什么

可运行的 Colab notebook，讲 **FDE / AI Engineer** 的应用层 LLM 技术栈，不用框架，
跑在**免费的 Groq API** 上。是一份 FDE / AI 工程师转型学习计划的动手配套项目。共享的
`aien` 包（仓库根目录）负责 setup；同一份共享 RFC 语料贯穿
RAG + evals，这样 evals 度量的就是你真正搭出来的那套检索。

## 当前结构（13 节）

```
00 Setup            environment、key、成本管控、花费护栏
01 Model APIs       prompt 基础、结构化输出、工具调用、streaming、上下文/缓存+batch
02 Evals I          新增 — 在第 01 节的提取任务上「先度量，再调优」（不依赖 RAG）
03 RAG              what-is-rag → embedding → 混合/rerank → chunking → why-rag-fails
04 Evals II         黄金集、LLM-as-judge、把回归当作 CI（与 RAG 耦合）
05 Agents           从零实现循环、工具设计、护栏/预算、MCP、skills、harness 工程
06 Adaptation       fine-tune、RAG、prompt 三者对比；LoRA/QLoRA；可选的 GPU LoRA 附录
07 Security         prompt 注入（直接+间接）、OWASP LLM Top 10、信任边界
08 Operations       可观测性/LLMOps；可靠性/降级；实验追踪与模型注册表（MLflow）
09 Serving & perf   新增 — serving 框架（vLLM/TGI/Triton/TensorRT-LLM）；推理性能；概念 + GPU 附录
10 ML system design 新增 — 设计一个推理服务（QPS/显存/延迟/成本、扩缩容、SLA）；概念，无代码
11 Customer craft   需求界定/探索、范围界定文档模板、demo 纪律（原 09）
12 Capstone         已部署项目任务书（不是 notebook）（原 10）
```

RAG 内部顺序是刻意的（**检索先于 chunking**）：在看到检索在某套 chunking 策略上
成功/失败之前，你没法评判它；而且一份 RFC（约 40k token）没法整篇 embedding（模型
窗口约 256 token），所以 chunking 的*必要性*放在 03/embeddings 展示，它的*手艺*
留到 03/chunking。

## AI 系统方向新增（2026-08-25）：第 09、10 节，08/03

起因是目标的转移：要打包出一段能写进简历的 **AI 分布式系统 / 应用**实习经历：现代
技术栈（RAG+LLM、LangChain、vLLM/Triton/TensorRT、MLflow、LoRA），*用框架*而不是
从零实现，并把 **ML 系统设计 + 性能**加了进来；学生不走算法方向，所以不追求建模深度。

冲突通过**叠加而非推翻**「不用框架」这条规则来化解（该规则仍管着教学用的 00–08 节，
而它本身就是最强的面试答案：「先手写一遍循环去理解它，*然后*在知道它能买到什么之后
再伸手去拿框架」）：

- **08/03 实验追踪与模型注册表（MLflow）** —— 可运行；记录第 04 节 eval harness 的
  run/参数/指标，注册一个模型并做阶段推进。把「我跑过一次 eval」变成可追踪的工作流。
  [候选 4]
- **09 Serving 与推理性能** —— 新增一节。09/01 *服务化框架*（vLLM/TGI/Triton/
  TensorRT-LLM：各自优化什么、怎样映射到 OpenAI 兼容的那道接缝、什么时候选哪个）；
  09/02 *推理性能*（连续批处理、KV cache、量化、吞吐 vs 延迟、规模估算）。概念优先 +
  **可选的、圈起来的 Colab-T4 vLLM 附录**（与 06 的 LoRA 附录同一套圈法；Groq 只做
  推理，不能自托管）。[候选 1]
- **10 ML 系统设计与性能** —— 新增一节。10/01 *设计一个推理服务*，把 ML 系统设计面试
  从头到尾做一遍（QPS/显存/延迟/成本估算、副本扩缩、排队、缓存、SLA）。概念，无可运行
  代码（像 05/04 MCP 一样圈起来）。[候选 2]
- **框架桥接概念单元**（候选 3）—— 已完成。在 **03/04**（LangChain 与 LlamaIndex：
  RAG 是一种模式而不是一个库；03 里每一种失败模式在框架内部同样会发生）和 **05/06**
  （LangChain 与 LangGraph：AgentExecutor/状态图*就是*你手写的那套循环；LangGraph =
  把 harness 持久化）的练习题之前，各追加一格「框架在哪里登场」的 markdown。延续仓库
  既有的「框架加了多少东西」模式（04/03、05/01）；给出简历关键词，又不推翻不用框架的
  原则。不加新 notebook。
- 候选 5–7（Agile/Scrum 角色扮演文档、针对框架栈的结业项目重写、面试录取评分表）被用户
  推迟。**5 和 7 已砍，6（结业项目重写）仍然想要**，但不在这一批里。

**AI 系统方向构建：完成**（2026-08-25）。已交付：08/03（MLflow，在 3.1.4 上跑绿）、
09/01 + 09/02（serving + 性能，概念 + GPU 附录）、10/01（系统设计，概念）、03/04 +
05/06 的框架桥接格，以及**结业项目（12）重写** —— 加了一张「使用现代技术栈」的表
（LangChain/LlamaIndex/LangGraph、vLLM/TGI、LoRA、MLflow）并映射到各教学节，一节系统
思维（09–10 的规模/性能数字），可靠性/成本，以及一节**团队/Agile-Scrum 与角色**
（PM/EM/AIML/Platform/SRE/QA 角色表、导师角色扮演、简历里的过程+影响 bullet、面试
准备清单）。这交付了候选 6 和原目标里的角色叙事诉求。候选 5 和 7 仍然砍掉。**这条线
没有未完成的活儿。**

方向落地后的全仓库检查（2026-08-25）：全部 30 个 notebook 可解析 + 每个代码单元可
编译；徽章 URL 与路径一致；所有内部交叉链接 + README 链接可解析；没有残留的
09-customer-craft/10-capstone 引用。重新编号已验证干净。

09/01 vLLM 附录加固（2026-08-26）：真实跑过一次 Colab-T4 之后暴露出三个真实的 serving
栈故障，现在都在 notebook 里处理了：(1) vLLM 升级 torch → Colab 里过期的 `torchaudio`
CUDA 版本不匹配，在 import 时把服务打崩（transformers 会无条件 import 它）；修法 =
卸载 torchaudio。(2) 一次失败尝试残留的 EngineCore 占着整块 GPU → 「Free memory …
less than desired GPU memory utilization」；修法 = 杀掉残留进程 / 重启 runtime +
`--gpu-memory-utilization 0.85`。(3) 服务启动时日志写进 DEVNULL → 盲等超时；修法 =
日志写文件 + 退出时打印尾部、`--enforce-eager`。另加一格显式的清理单元（`server`
terminate + pkill + nvidia-smi）。端到端确认过：TinyLlama 在 T4 上服务起来，同一个
OpenAI 客户端拿到了 completion。这些坑被写成第 09 节的教训（自托管 = 依赖管理 + 资源
管理），不藏起来。

重新编号：客户手艺 09→**11**，结业项目 10→**12**（只更新了 3 处引用：README ×2 +
被移动的那个 notebook 自己的徽章；没有其他交叉链接指向它们）。新节插在 Operations
之后，因为 serving/性能/设计属于「把它做成真的」这类关切，跟把 security/ops 放后面的
理由一样。

构建状态（2026-08-25）：骨架 + **09/01 已构建并验证**（14 格，可编译，除指向 10/01 的
前向引用外链接都可解析）。待构建：09/02、10/01、08/03、框架桥接单元、结业项目重写。

## 调研过的资料

- **OWASP LLM Top 10（2025）** —— prompt 注入排第 1；直接催生了第 07 节。
- **MCP**（modelcontextprotocol.io）—— 现在已是标准（Claude/OpenAI/VS Code/Cursor）；
  作为纯概念折进 agents（仓库避免用框架）。
- **PEFT / LoRA / QLoRA**（HuggingFace）—— 主流做法，能在免费 Colab T4 上跑。
- **RAG 经典** —— Lewis et al. 2020、AWS、Pinecone、Prompting Guide。确立了
  RAG ≠ embedding（retrieval 可以是向量/BM25/混合/SQL/API）。
- **Groq** —— 只做推理（没有训练，也没有 caching/batch API）；支持多模态（`qwen`）
  和 LoRA 的 *serving*。
- **两位独立的课程评审者**（market-lens + pedagogy-lens），各自被要求从第一性原理设计
  理想方案。他们得出了相同结论（见下）。

## 已锁定的决定（附理由）

1. **Evals 是主线，早早引入。** 两位评审者的头号修正：RAG→Evals 是反的（没有指标就
   没法调 RAG）。拆成 02（基础，放在提取任务上）+ 04（丰富版，放在 RAG 上）。保留
   共享语料的设计，靠*拆分*而不是把丰富的 eval notebook 从 RAG 上改指向别处。
2. **加入 FDE 客户手艺（09）。** 两位都称它的缺席是「FDE」仓库最大的单一缺口；它是一个
   有名字的面试环节。
3. **多模态与多 agent：只做概念 / 移出主线。** 两位评审者各自都反对把它们放进动手模块
   （多 agent 动手「奖励的恰恰是课程应当压制的那个直觉」）。多模态唯一有力的论据是
   Groq 的可行性，而这不属于规划优先级。→ 不作为模块加入。
   **2026-10-23 修订：** 多模态可以出现在*案例研究*里（12/04，深度伪造图像检测），因为
   在那里它是把 evals 主线串起来，而不是教一种新模态。仍然没有多模态*模块*。
4. **优先级规则（用户）：**「计划是否想要它」>「它是否还能跑在 Groq 上」。Groq 只是
   交付细节；计划点名要讲而 Groq 跑不了的主题，就把真实 provider 的 API 形态当作参考
   代码展示，而不是把它稀释掉。
5. **fine-tuning 保持在后面，以做判断的方式讲**，附一个可选的、圈起来的 GPU LoRA
   附录，既贴合计划（「仅概念层面」），又不忽视 LoRA 的崛起。
6. **security 放在 agents 之后；ops 放在 security 之后** —— 这些横切的「把它做成真的」
   关切，需要一个真实系统才有意义。两位评审者都认可。

## 明确否掉的

- 多模态 / 多 agent 作为动手核心模块（见第 3 条）。
- 独立的 prompt engineering *英雄模块*（两位评审者都警告它会养出盲从套路的把戏）。但
  一次审计（2026-08-20）发现，原本设想的「织进各节」其实从未发生：prompting 到处被
  *使用*，却哪里都没被*教*。修法是加入 `01-model-apis/00-prompting-basics`（把基础
  当作通往结构化输出的入口：清晰指令、few-shot、格式规范、CoT，绑定 eval 习惯，反盲从
  套路）。不是英雄模块；是放在节首的一小段折入，正是计划一直以来的本意。
- fine-tuning 内部原理 / RLHF / 经典 ML / agent 框架深挖（计划说跳过）。
- 数据管道 / 部署基础设施类 notebook（那是结业项目的活）。

## 阶段 2：完成（2026-08-17）

四位评审者建议的打磨项全部交付：

1. **Eval 主线交叉链接** —— 00 setup 的「冲击」为它做了铺垫；03/RAG 引言回指第 02 节的
   习惯；agents 之后（05/guardrails）加了一个 **trajectory-eval** 触点，让 evals 可见地
   *回来*。
2. 00 Setup 里的**非确定性「冲击」格**（同一个 prompt ×5 结果不同；严格的输出契约会
   间歇性地崩）。
3. 05/agent-loop 开头的**先 workflow 后自主**告诫（「最后才伸手拿循环；步骤已知就用
   pipeline」）。
4. **跨 provider 参考代码**（不可运行的 markdown 片段，对照当前 provider 文档核实过）：
   01/context-caching 里 Anthropic 的 `cache_control` + OpenAI Batch 的 submit/poll；
   06/adaptation 里 OpenAI 的 `fine_tuning.jobs` + Bedrock 备注。保持为圈起来的
   markdown，这样它们不会弄坏一次 Groq 运行。

没有遗留的结构性工作。以后的工作要么是内容打磨，要么是那趟仍然待办的端到端 Colab
执行（见注意事项）。

## 最佳实践与反模式（2026-08-18 加入）

- **`docs/best-practices-and-anti-patterns.md`** —— 面向整个技术栈的 ✅ 该做 / ❌ 别做
  汇总，一节一节来，末尾是「最重要的五条」。兼作面试前复习表和结业项目前清单；从结业
  项目 README 链接过去（「上线之前」）。
- **每个 notebook 的收尾单元** —— 在 6 个原本没有的 notebook 的练习题之前，加一张
  统一的 `## Practices & anti-patterns` 表（02-tool-calling、03-hybrid、03-chunking、
  04-regression、05-mcp、08-observability）。其余 notebook 已带有等价内容（阶梯、清单、
  「什么时候 pipeline 胜过 agent」、诊断卡），原样保留以免重复。

## Harness 工程 notebook 加入（2026-08-25）

- 新增 **05/06-harness-engineering**（可运行；在第 01 节的 FS/工具/循环基础上，跑在
  Groq 上）。它与 prompt engineering（消息）和 model adaptation（权重）并列，点名了
  第三条轴：**harness 工程 = 这次调用外围的脚手架**。定位成一个*综合*收尾：先用一张
  明确的表格把 01–05 重述为 harness 组件（循环 / 工具输入 / 边界 / 外部工具 / 打包好的
  经验），再教这一节一直隐含未讲的三根杠杆：**(1) 上下文组装与压缩**（窗口 = 每轮重建
  的预算；保留任务+近期+承诺，中间内容做摘要），**(2) 工具结果整形**（nb-02 的*返回*
  侧：把大块内容头尾截断、让错误可行动，通过加进紧凑循环里的 `shape_result` 接缝接上），
  **(3) 验证循环**（harness 用代码算出 ground truth，失败就循环；nb-03 的
  trajectory-eval 指的正是输出）。收尾是一张 ASCII harness 示意图（「模型是固定的；
  其余一切都是你拥有的代码」）和一条规则：*在伸手去要更大的模型 / 做 fine-tune 之前，
  先修 harness（§06）*。它并**不**重开决定 #3：讲的是单 agent 的上下文/脚手架工程，
  不是编排。README + best-practices 的 05 表 + 本日志都已更新；所有内部链接核实过。
  按既有注意事项为纯静态（这里没跑过，也没有 key）；新增的验证循环格会真的发起模型
  调用，所以在 Colab 执行那一趟里要标出来。

## Skills notebook 加入（2026-08-23）

- 新增 **05/05-skills-and-progressive-disclosure**（纯概念，无可运行代码，跟 MCP 一样的
  圈法：Skills 住在 agent 宿主里，不是裸的 Groq `chat.completions` 调用）。补上一个真实
  的缺口：仓库教了工具、agent 循环、MCP，却没教怎么*把可复用的经验打包*起来供 agent
  按需加载。按**模式优先**来定位（渐进式披露 /「上下文是一份预算」），以 Anthropic 的
  `SKILL.md` 作为具体实例。这是刻意的，因为这个格式如今已是**开放标准**
  （agentskills.io），被多家厂商采纳（OpenAI Codex、Gemini CLI、各家编辑器），所以它是
  一条耐久的模式，而不是某家厂商的功能。主线是三件套 **Tools *行动* / MCP *连接* /
  Skills *打包***。从 04-mcp 交叉链接过来；README + 本文档已更新。细节对照
  Anthropic/agentskills 的线上文档核实于 2026-08-23：6 字段的可移植 frontmatter
  （`name`、`description` 必填；没有 `version`），3 层渐进式披露（约 100 tok 元数据 →
  <5k 正文 → 随包附带的文件/脚本，脚本经 bash 运行，所以只有输出进入上下文）。这
  **不**推翻决定 #3（多 agent/多模态仍在主线之外）：Skills 是单 agent 的上下文管理
  概念，不是编排。

## 适配：FFT 与 LoRA 的第二条轴（2026-08-23 加入）

- 给 06 加了一格 **「全量 fine-tuning 与 LoRA」**（在「LoRA 是什么」之后、provider 路线
  之前）：总的框定（fine-tuning = 类别；FFT + LoRA = 两种方法），一张对比表（可训练
  参数量、显存、产物大小、灾难性遗忘），以及 **LoRA 为什么占主导** —— 多租户 serving
  （一个冻结底座 + 热插拔适配器）与可及性（单卡）。两条 AWS 引证对照线上文章核实于
  2026-08-23：SageMaker/Bedrock 上的 multi-LoRA vLLM serving（证实按请求换适配器；
  量化说法「5×10%-GPU → 1 GPU」），以及 Bedrock Custom Model Import GA（证实只接受
  全量/合并后的 Safetensors，所以 LoRA 必须先合并进去，与既有的第 9 格 Bedrock 备注
  一致）。两道新练习题（FFT-vs-LoRA 的判断；设计多适配器的 serving 故事）。刻意保持为
  「做判断」，不做内部原理深挖：没有优化器/梯度数学。进一步坐实了[下文的重定位]里的
  分类精度；best-practices 的 06 表已更新。

## 适配 notebook 重定位（2026-08-22 加入）

- **06/fine-tune-vs-rag-vs-prompt** 围绕一条*模型修改程度*的光谱重新定位
  （prompt → RAG │ LoRA → 全量 fine-tune；改输入还是改权重），而不是按流行度；另加一格
  「钟摆」（fine-tuning 曾是早期默认 → 领域摆向 prompt/RAG → fine-tuning 收敛到大规模
  风格化 + 小模型蒸馏）。补上分类精度：LoRA 是 fine-tuning 的*一种*，不是与它平级。
  托管参考代码扩展成核实过的三层划分：**抽象封装**（OpenAI、Bedrock：没有 LoRA 旋钮）
  vs **显式 LoRA**（Together、Fireworks：`lora=True`/`--lora-rank`）vs 自训（`peft`）。
  所有片段仅供参考。provider API 对照线上文档核实于 2026-08-22；更正了此前一个错误
  说法——Bedrock 会给出「LoRA endpoint」（Bedrock 没有 LoRA 界面；AWS 上的显式 LoRA
  是 SageMaker）。

## Callout 主题化（2026-08-18 加入）

站点品牌的提示框，约束在于 Colab/GitHub 的 notebook 渲染器会剥掉 CSS，也不支持
`[!NOTE]` alert 扩展（已核实：两边都显示为字面文字）。约定写在 `docs/theming.md`：

- **emoji 标注的引用块** —— `> **⭐ Key takeaway —** …`。角色经 emoji 映射到站点的
  `--role-*` 颜色：⭐ 核心要点、💡 原因、🔵 面试信号、⚠️ 生产现实、🚩 常见错误。干净，
  在 Colab + GitHub 里一模一样。
- 每个 notebook 只用在**最强的那一条要点/错误**上，**1–2 个**，且只在洞见被埋在行文
  里时。已经带有 practices 表或清单的 notebook（tool-calling、llm-judge）不动。
- 真正的彩色框需要内联 HTML 的 `<div style=…>`（为保持源码干净，选择不用），或者那条
  推迟的 HTML 托管路线（拿到 walkthrough 青色强调色的唯一路径）。

## 案例研究待办（2026-08-26 规划，尚未构建）

加入端到端的**案例研究** —— 演练过的真实世界叙事（概念优先，像 10/01），按两条轴组织，
好让它们覆盖不同的*应用类型*，而不是 RAG-QA 的三个变体：
- **轴 1 —— 用例**（客户支持、文档处理、安全/eval，……）
- **轴 2 —— 应用类型 / 技术**（RAG+agent 构建、pipeline 判断、对抗性基准 harness、
  分类器、语义推荐，……）

归处已定（2026-08-26）：第 **12 节改名「案例研究与结业项目」**（目录
`12-case-studies-and-capstone/`）。案例和结业项目任务书现在住在一起：案例是演练过的
范例，结业项目是「现在换你自己搭」。按案例的性质分：**叙事很重的全栈案例可以做成文档，
但按用户要求 A 是可运行的 notebook**；自包含的案例（C、D）同样也是可运行的 notebook。
结业项目任务书保持为文档（`CAPSTONE.md`）：一个 notebook 项目会传达出「周末黑客」的
气质；案例研究可以是 notebook，因为是演练过的范例，而学生的结业项目必须是一个真正部署
的仓库。

**状态：** A 已构建 + 可运行（2026-08-26），为
`12-case-studies-and-capstone/01-customer-support-assistant.ipynb`（28 格，需要 Groq
key）。叙事从原草稿保留，另按阶段配最小可运行代码，跑在 6 篇文章的语料 + 5 题黄金集上。
第 8 阶段的回归是**真的**：语料迁移后 `index_corpus()` 接缝留着没动 → eval 分数下降 →
重建索引 → 恢复。第 12 节的 `README.md`（先案例后结业项目）+ `CAPSTONE.md`（由旧的
结业项目 README 改名而来）。旧的 `docs/case-studies/` 已删除；草稿已删。所有链接核实
过。此处为纯静态（没有 key）；在 Colab 里跑一遍确认，像 06/09 那样。

**C 和 D 已构建 + 可运行（2026-08-26）**，为 `02-...pipeline-vs-agent.ipynb` 和
`03-red-team-robustness-benchmark.ipynb`。注意：案例的*字母*按文件顺序重编：A（客户
支持），**B = 合同提取 pipeline-vs-agent**（原为「C」），**C = 红队基准**（原为「D」）。
B 把同一个提取任务分别做成 agent 和 pipeline，并用准确率 + token 数证明：步骤已知时
pipeline 胜出（05/03 的论点，被度量了）。C 是一种全新的系统类型：attacker→target→judge
的 PAIR 循环，报告 ASR（从用户的简历越狱项目泛化而来）；以**防御性**方式框在一个无害
的代理任务上（「绝不泄露某个密语」），不含任何真正有害内容或可迁移的越狱手法。三个案例
现在都列在第 12 节的 README + 主 README 里；全部可编译 + 链接 + 徽章核实过。案例研究
待办完成（E/F 仍推迟）。全部为纯静态（需要 Groq key）；在 Colab 里跑一遍确认。

**锁定进待办（用户选了 A+C+D）：**
- **A —— 客服助手，从范围界定到部署**（旗舰，已完成）。构建角度；RAG + agent。串起
  11 范围界定 → 03 RAG → 02/04 evals → 05 agent（订单查询）→ 07 注入防御（工单是一个
  攻击面）→ 09 serving → 08 可观测性 → 11 demo。**结尾是「两周后，答案质量崩了，来
  诊断它」这一幕**（旧的「凌晨 3 点事故」想法折进 A 的终场，用 08 的追踪 + 04 的回归
  eval）：一条弧线覆盖 build→debug。结业项目的活的范本。
- **C —— 合同提取：pipeline vs agent**（判断角度，较轻）。那个面试判断题：步骤已知时，
  诱人的 agent 与正确的 pipeline 之争；用 eval + 成本数字把它辩清楚。把 05 的
  「pipeline 胜过 agent」论点补成一个完整的演练案例。
- **D —— 红队鲁棒性基准**（对抗性 harness / 基准；仓库的一种新应用类型：搭一个 harness
  去*评测/攻击*模型，而不是服务一个模型）。从用户真实的简历项目泛化而来（一个 PAIR
  循环越狱器：攻击模型 → 目标 → Llama-Guard judge，约 68% ASR）。组合了 05 的循环 +
  04 的 LLM-as-judge + 07 的安全 + 02 的 evals（ASR 指标）。能在 Groq 上跑（攻击/目标/
  judge 都有 Groq 模型，含 Llama Guard）。

**考虑过、推迟（E/F）：** E，AI 生成文本 / 标题党检测（LLM 分类器 + eval）。它的*图像*
版最初被认为偏离主题（多模态）；后来被当作**案例 D**（见下）捡了回来，定位为分类器/
eval 案例而不是多模态模块。F，语义推荐 + 解释（embedding 检索 + LLM rerank；只有框成
LLM/embedding 推荐系统而非经典 CF 才算切题）。

**D —— 面向 EU AI Act 第 50(4) 条的深度伪造检测（2026-10-23 构建；2026-11-02 简化，
见下方最后一条注）**，为 `12-case-studies-and-capstone/04-deepfake-image-detection.ipynb`
（47 格）。取代了同日的骨架。框在 **第 50(4) 条**（部署方必须披露深度伪造）上，而不是
50(3)（那是情绪识别）；一次违规 = 生成 AND 描画了真实主体/事件（不是显然的虚构）AND
发布时未披露。数据：**OpenFake** 的 `core`（HF `ComplexDataLab/OpenFake`，CC BY-NC
4.0，每行带生成器 + 发布日期 + prompt）；在 `HOLDOUT_AFTER` 当天或之后发布的生成器被
留作「未见」。测试集被赋予受控的披露方式（无 / 可见标签 / IPTC trainedAlgorithmicMedia
XMP）和两种变体（原始 / 洗涤过的 JPEG，会剥掉元数据）。条件 2 用的是文本模型读 prompt
得出的**银标签**（在练习题 1 里审计）。比较 A（CLIP ViT-B/32 线性探针，CPU，阈值按
5% FPR 校准）、B（VLM `qwen/qwen3.8-27b` 端到端）、D（来源字节校验），以及系统层面的
A only / A+D / B / C 混合，在检测（AUC、已见与未见的召回、FPR）与合规（精确率/召回率）
上。VLM + 银标签结果缓存进 `case_d_cache.json`（只有分数，从不存图）。**GPU 附录：**
在 6k 张图上跑 ViT-L/14 探针 + LoRA fine-tune（peft，q/v 投影），有和没有 JPEG 增强
各一份，注册进同一批报告。刻意用 `transformers` + `scikit-learn` 做那个经典 ML 检测器
（notebook 里已声明）。**验证：** 主路径在本地用打桩的 dataset/Groq/CLIP 端到端跑过
（表格能渲染，缓存避免重复调用）；尚未对真实的 OpenFake / Groq 跑过，GPU 附录未测。
**Colab OOM 修复（2026-10-24）：** 第一次 Colab 运行在采样格里崩了（RAM 全被吃光）：
流式 `.shuffle(buffer_size=5_000)` 把 5k 行连整尺寸图片一起攥在手里。对着真实 OpenFake
测还暴露出 (a) 行是按来源分组存储的，所以小的 shuffle 缓冲混不开；(b) 流式会把每张被
跳过的图也下载下来（每张约 0.7 MB；30 张的样本跑了几个小时）；(c) `release_date` 混着
`YYYY-MM-DD`、`YYYY-MM`、`unknown`、`None`，字符串比较把 `unknown`（更早、无日期的
生成器）算进了「未见」。`sample()` 现在直接读 parquet 文件（`HfFileSystem` + `pyarrow`）：
第一趟只从随机行组里读 label/model/release_date，行在各生成器间轮转挑选，第二趟只下载
含有被选中行的行组。日期被归一化；无日期 = 已见。**对真实 OpenFake 验证过：** 测试
（120）与验证（200）各约 3 分钟采完，0.8 GB RAM。一个发现，现在是 notebook 里的一条
提示框 + 打印输出：各 split 不是独立同分布（验证集里的真实图 = LAION/Pexels，测试集里
的真实图 = ImageNet/DOCCI；生成器也更旧、不同），所以校准出的 FPR 未必可迁移。仍未跑：
全尺寸的训练采样、Groq 调用、GPU 附录。
**Hub 超时（2026-10-26）：** 在 Colab 里，训练采样在 parquet 读取上撞到
`The read operation timed out`（行组约 100 MB）。光靠重试不够，因为一个 split 失败就
丢掉已下载的一切，所以 `sample()` 现在**可续跑**：`HF_HUB_DOWNLOAD_TIMEOUT=60`（默认
10s），每次读取重试 4 次带退避，计划（哪些行）加上每个完成的行组都做检查点（pickle，
原子写），放在 `SAMPLE_DIR` 下。若某个行组仍然失败，该格会带着「重跑这一格」的消息抛出；
重跑只下载缺的部分（`allow_partial=True` 允许缺着继续）。一个不提供服务的 pass-1 文件
会被跳过。检查点里存的是缩小后的 OpenFake 图像（CC BY-NC），所以 notebook 现在提示要把
`SAMPLE_DIR` 保持私有并在之后删除；挂载 Drive 能让它跨 runtime 重启保留。离线测过：
注入超时、一个永不提供服务的文件、总是失败的行组（第 1 次运行停下，第 2 次只下载那两个，
第 3 次什么都不下并返回相同的 id）。尚未在 Colab 里重跑。

**Groq 每日上限（2026-10-26）：** 一次 Colab 运行中途因速率限制失败（输出丢了，所以是
推断，不是观察到的）。Groq 的速率限制文档列出视觉模型为 30 RPM、8K TPM、**200K TPD**
（标注为 Developer 计划的基础限制；以组织的限制页为准）。按每图约 2.2K token，旧默认值
（120 图 × 2 变体 = 240 次调用 ≈ 530K token）需要约 3 天，而每日上限是重试不掉的。改动：
`N_TEST` 30/30/30（180 次调用 ≈ 2 天）；`VLM_TOKENS_PER_DAY` + `vlm_budget()` 打印
剩余调用数与所需天数（单次调用 token 一旦有缓存就从中量出）；`run_all()` 捕获
`groq.RateLimitError`（aien 建的是 `groq.Groq` 客户端，不是 openai）并暂停而不是崩溃；
`collect()` 只保留有 VLM 结果的行，好让所有方案都在同一批图上比较，打印覆盖率，并提示
在重置后重跑。原始图先跑，所以第 1 天就能拿到 `original` 那几张表。Setup 格展示了怎样
把 `CACHE_PATH` 和 `SAMPLE_DIR` 放到 Drive 上，让一次运行能跨天。用打桩的 TPD 429
（第 100 次调用后）离线测过：第 1 天在洗涤变体 11/90 处暂停并报告渲染结果；第 2 天只发
那 80 次缺的调用。

**为廉价首跑而重构（2026-10-29）：** (1) 采样改用 HF dataset viewer 的 `/rows` API，
不再用 parquet：每次请求从任意偏移拿 100 行元数据，每行都带指向自己那张图的链接，所以
只有被选中的图会被下载（每张约 100-200 KB，8 线程）。计划（`plan.json`）和每张图都在
`SAMPLE_DIR` 里做检查点；过期的签名链接通过重读那一行来刷新。对真实 OpenFake 用默认值
验证过：测试 15 / 验证 100 / 训练 200 张图，总共 2.7 分钟，0.1 GB RAM，43 MB 磁盘，
11 / 39 / 37 个不同的生成器。notebook 里的注意事项：viewer 把图片重新编码为 JPEG 后
提供。如果 viewer API 哪天不能用了，parquet 采样器在 commit 9c19528。(2) 所有尺寸旋钮
集中在一处，默认值极小：`N_TRAIN_PER_CLASS=100`、`N_CAL_PER_CLASS=50`、
`N_TEST_PER_GROUP=5`、`VARIANTS=["original"]`（洗涤变体是选做项）。默认一次运行 =
15 次测试 VLM 调用 + 2 次 walkthrough 调用。(3) 批量运行之前新增「一张图，一步步来」
一节：一张假图（优先用点真实主体的 prompt）分别以无披露和可见标签发布，展示检测器分数
与阈值、VLM 的 JSON + token、来源、gold，以及每个系统的标记；`SYSTEMS`/`flag()` 移到
这里。离线测过（rows-API 打桩）：干净、抖动（343 次重试）、每日上限（在 9/15 处暂停，
第 2 天发那 7 次缺的调用）、洗涤变体开启。**未决问题：** OpenFake 的随机 prompt 很少
点名真实主体（真实测试样本：公鸡、穿山甲、猫娘……），所以小测试集可能一条 gold 违规
都没有，导致合规表全是 0%。

**首次 Colab 运行 + 筛选过的测试组（2026-10-30）：** 极小的默认值在 Colab 里端到端
跑通了：15/15 个 VLM 结果，0 个解析失败，每图约 1,500-1,750 token（不是 2,300），每图
约 18.6 秒，大部分在等 TPM。一个探针 AUC 1.00 但在校准阈值下召回只有 40-60%（校准集的
真实图是 LAION/Pexels，测试集的真实图是 ImageNet/DOCCI：阈值不可迁移）；VLM AUC 0.78。
正如预料，0 条 gold 违规，所以合规表全是 0%，walkthrough 退回到一张显然是虚构的图。
206 条测试 split 的假图 prompt 里只有约 5 条点名了真实主体。修法：加第四个测试组
`fake_real_entity`（`SCREENED`），在 `plan()` 期间从任意生成器的假图里填充：一条首字母
大写的正则留下约 28% 的 prompt（找到了的全部真实主体都留下），再由文本模型每次 20 条
筛选。随机组不变；检测 AUC 不含筛选组；披露方式按组轮转，所以筛选组拿到的是
无/无/可见/元数据；采样格会打印筛选出的 prompt 以便审计；walkthrough 优先选一张筛选图。
默认一次运行现在是 20 次测试 + 最多 2 次 walkthrough VLM 调用。离线测试：干净、抖动、
每日上限都通过。尚未对真实文本模型跑过，所以真实的筛选命中率和文本调用数还没量过。
仍然未决：「已见」是按发布日期定义的，而在那次 Colab 运行里 0/5 个 `fake_seen` 生成器
其实在 TRAIN 里。

**简化为一场 walkthrough（2026-11-02）：** Hugging Face 的限流（约 320 张图的采样期间
`/rows` 报 HTTP 错误）让完整评测在 Colab 里很痛苦，所以用户选了一条简单流程：加载模型、
判几张手挑的 OpenFake 案例、做比较、再判任意图片 URL。现在是 31 格。**A** 是现成的，
阈值 0.5，不用训练或校准数据：`bendavidsteel/openfake-swinv2-base`（OpenFake 作者们的
demo 检测器，SwinV2-base，logits / 2.0）作为 `A_openfake`，再加
`umm-maybe/AI-image-detector`（流行于 2022 的检测器）作为 `A_generic` 做对照。
**示例：** 按行号取 7 行 `core/test`（各 2 次请求，缓存在 `SAMPLE_DIR`，遵守 429 的
`Retry-After`）：6831 皇马新闻发布会和 29127 Daily Show 片场（点名真实主体的假图，
flux.2-klein-9b）、3251 一个穿「Bernie for President」T 恤的匿名男子（刻意的边缘案例，
标注为不是深度伪造）、6814 动漫，以及真实图 6811 / 6851 / 6804。人工标签取代银标签。
9 个发布出来的案例（那两张深度伪造还各以可见标签和带 XMP 元数据的形式发一遍），2 条
gold 违规，总共约 10 次 VLM 调用。砍掉：rows-API 采样器、筛选组、CLIP 探针、洗涤变体、
GPU 附录（现在是练习题 4，「训练你自己的检测器」）；完整版在 commit a16787b。挑示例时
发现：某个测试页上 86/100 行的 `prompt_kind = qwen_caption`（caption 很少点名人物），
这也是为什么点名真实主体的 prompt 看起来很稀少；`published_prompt` 的行则保留名字。
本地对真实 HF 数据和两个真实检测器验证过（VLM 打桩）：`A_openfake` 在每张假图上
0.99-1.00、在每张真实图上 ≤0.01；`A_generic` 在匿名男子假图上 0.10、在动漫上 0.00、
在皇马假图上 0.41；缓存重跑时 0 次 VLM 调用；表跑到一半遇到每日上限会干净地暂停。尚未
在 Colab 里用真实 VLM 跑过。

**重构成六步（2026-11-02，同一天）：** 首次 Colab 运行后用户要求一个更清楚的顺序：
1 需求，2 数据（先展示那 7 张图连同 OpenFake 自己的标签与生成器，再展示带 gold 的
9 个案例），3 方法（工具表 A / B / D，D 的解释，四系统表），4 每个工具即刻加载并跑在
那 9 个案例上，5 四个系统做比较，6 你自己的图片，给出一个直白的**判定**（C 混合方案的
决定，加上第一个让它过或标记的条件，以及哪些系统意见不一致）。逐步的单案例没了；24 格。
然后发布模拟也被砍掉（用户：就当没有披露）：那 7 张图就是那 7 个案例，gold = 假图且
点名真实主体且非虚构（2 条违规），D 会跑但在 OpenFake 文件上什么都找不到、只在第 6 步
里重要，「A + D」没了（没披露任何东西时与 A 完全相同），所以变三个系统；带披露的副本
变成练习题 7。22 格，约 8 次 VLM 调用。
`A_generic`（umm-maybe，本身也是个 Swin）随后被换成 `A_cnn`：CNNDetection
（Wang et al. CVPR 2020，「Blur+JPEG (0.5)」），一个在 ProGAN 上训练的 torchvision
ResNet-50，权重来自作者的 Dropbox（282 MB，用 `weights_only=True` 加载），按最长边
1024 px 打分。不存在训练于 OpenFake 的知名 CNN（Hub 上所有用 OpenFake 训练的模型都是
Swin/ViT/CLIP）。本地它对全部 7 个示例都打出 0.01 以下，含假图（logits 从 -10 到 -44，
全分辨率下也一样）：这就是训练数据的教训。

## 长期注意事项

- **已在 Colab 里端到端执行（截至 2026-10）。** 所有 notebook 都从头到尾跑过，除少数
  牵连较广的尚未重跑。GPU 附录（06 LoRA、09/01 + 09/02 vLLM）在 2026-08-26 于 Colab
  T4 上核实：所用修法见 [[colab-gpu-vllm-gotchas]] 备忘。08/03 MLflow 在本地跑绿。
- **输出是刻意剥掉的。** notebook 提交时不带输出和执行计数，以保持 diff 干净。结果只有
  跑起来才看得到；这是政策，不是验证缺失。
- **模型：** 仓库用 `openai/gpt-oss-120b` / `-20b`（Groq 当前的 production）。若调用报
  404，对照 Groq 的模型列表重新核实。
- **Colab 里没有仓库 checkout** → notebook 通过
  `pip install "git+https://github.com/shangbingo888/AI-EDF-NOTEBOOKS-CN.git@main"`
  安装 `aien`。**注意：** 这里跟的是 `main` 分支，不是 tag——改 `aien` 会立刻影响
  所有已发布的 notebook，所以改之前先在 Colab 里跑一遍受影响的 notebook。如果之后
  想要「发布版不会被 `main` 上的改动弄坏」，就升版本、打 tag，再把每个 notebook 里的
  安装行改成 `@vX.Y.Z`。
