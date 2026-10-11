# 企业知识库实践手册（v0.1）：从选型路由到知识形态

> **English abstract** — Enterprises are confused about knowledge bases not because products lack capability but because selection logic is missing: material and queries differ per department. This playbook gives (1) a routing table — material type × query type → architecture; (2) a knowledge-forms view — what shape organized knowledge should take (RAG / FAQ / Wiki / Graph / Tree / PageIndex / MindMap / Timeline / Skills / PageCard); (3) five practice principles; (4) vendor evidence that the market is already voting for this thesis. All sources cited at the end. Living document — corrections via PR.

## 一、问题：部门异质性

知识库产品的功能清单越来越长——多模态、图谱、GraphRAG、Agentic RAG、工作流、skill、MCP、sandbox——但企业反而更迷茫。迷茫的根源不是能力缺口，是**选择缺口**：

- **素材异质**：财务堆 Excel（表格、可计算、带 schema），战略/HR 堆 Word 与 PPT（叙事性、政策性），法务/工程堆 PDF（版式复杂、引用敏感），还有大量知识躺在核心系统的 SQL 表里（活数据，不是文档）。
- **查询异质**：有人查制度条文（文字），有人要算合计环比（计算），有人对"最新"极其敏感（时效）。

这一点已有多家厂商从不同角度独立印证：袋鼠云主张"按数据形态路由访问方式"[[1]](#ref1)；达观数据直接以"知识库不能一刀切、按部门定制问答策略"为产品论点[[2]](#ref2)；腾讯云 ADP 用"主 Agent 按部门分发子 Agent"的架构落地同一判断[[3]](#ref3)。市场已经用产品投票。

## 二、选型路由：素材 × 查询 → 架构

| 素材 | 真实性质 | 典型查询 | 正确形态 |
| --- | --- | --- | --- |
| 财务/运营的电子表格 | 表格、带 schema、可计算 | "Q3 华东区合计多少？" | text-to-SQL 或语义层 + 代码执行——向量检索会摧毁数字语义 |
| 战略/HR 的 Word 与 PPT | 叙事性、政策性 | "差旅报销上限是多少？" | 经典 RAG；PPT 的瓶颈在解析 |
| 法务/工程的 PDF | 版式复杂、引用敏感 | "这条结论出自哪个条款？" | 高保真解析（MinerU / docling / PixelRAG）+ 强制引用 |
| 核心系统的 SQL 表 | 活数据，不是文档 | "当前库存多少？" | 原地查询 + 同步——永远不要"导入知识库" |
| 以上任何一种 | 时间敏感 | "截至现在？" | 带新鲜度 SLA 的增量同步，不是批量重嵌入 |

最容易翻车的一格：把 Excel 当文档切块做向量检索。数字一旦被切块嵌入，"合计""环比"这类问题再也算不准——这不是调参能救的，是工具选错了。

## 三、知识形态：组织成什么

路由决定管线；形态决定知识的产物长什么样。以下十种形态的完整论证见《从 RAG 到知识编译》[[0]](#ref0)，此处为速查表：

| 形态 | 组织单元 | 适合 |
| --- | --- | --- |
| RAG | 检索证据 | 从大量资料中找到并综合信息 |
| FAQ | 问题 + 标准答案 | 稳定回答高频问题 |
| Wiki | 页面 + 内部链接 | 长期沉淀领域知识 |
| Graph | 实体 + 关系 | 探索对象之间的关联 |
| Tree | 父子主题 | 按主题逐级理解 |
| PageIndex | 长文档章节索引节点 | 定位复杂长文档中的信息 |
| MindMap | 中心主题 + 分支 | 快速把握知识整体结构 |
| Timeline | 时间 + 事件 | 理解演化与历史 |
| Skills | 任务说明 + 操作资源 | 支撑 Agent 复用操作知识 |
| PageCard | 页面摘要 + 链接 | 快速发现与筛选，不替代内容本身 |

按素材/任务的推荐默认值[[0]](#ref0)：产品帮助文档 → FAQ·RAG·Wiki；架构文档 → Graph·Wiki·MindMap；长研究报告 → PageIndex·RAG·PageCard；行业知识 → Tree·Wiki·MindMap；项目过程记录 → Timeline·Wiki·PageCard；SOP 与操作手册 → Skills·Wiki·FAQ。

多形态共存时应建立**共享知识底座**（Document / Content / Topic / Entity / Relation / Fact / Event / Page / Procedure 统一对象模型），而不是每种形态各自维护解析、溯源与更新管线[[0]](#ref0)。

## 四、五条实践原则

1. **从一个部门最高频的一类问题起步**，不要煮海[[6]](#ref6)。
2. **先给知识资产分类再选技术**：叙事文档 / 表格 / 活数据三分法先行[[1]](#ref1)。
3. **按查询类型路由**：文字 → 检索；计算 → SQL 或代码执行；新鲜度 → 同步架构。现代栈里"检索只是 agent 的一个工具"。
4. **分部门定制评测**：文档问答看召回与引用忠实度，计算类看结果正确率——一把尺子量不了两者。
5. **治理决定成败**：素材所有权、更新责任、权限边界（角色-部门-用户三维[[2]](#ref2)；血缘与脱敏继承[[1]](#ref1)；动态权限的形式化验证[[4]](#ref4)）。

## 五、厂商与工程证据

| 证据 | 来源与日期 | 可借鉴点 |
| --- | --- | --- |
| 按 data-form 路由 + 资产目录前提 | 袋鼠云 DTStack，2026-08[[1]](#ref1) | 文档/结构化/关系三分访问方式 |
| RRF 混合检索 + MD5 指纹增量索引 + 全链路降级 | 腾讯云社区（OODER），2026-07[[5]](#ref5) | 800/100 分块、检索融合、容错设计 |
| 按部门问答策略引擎 | 达观数据，2025-10[[2]](#ref2) | 三维权限、场景规则、政策时效适配（厂商自述数据未验证） |
| 主 Agent + 部门子 Agent 分域问答 | 腾讯云 ADP，2026-01[[3]](#ref3) | 标签分域检索、显式兜底（平台教程） |
| Agentic RAG 提升值班助手精度 | Uber Engineering，2025-05[[7]](#ref7) | 文档深度加工 + agentic 检索的 生产效果 |
| 一年 LLM 应用的生产总结 | O'Reilly，2023[[6]](#ref6) | 评测先行、架构从简、成本是设计轴 |

## 六、开放问题（v0.1 明确未解决）

- 跨部门评测尚无标准工具与数据集：每家都在自建尺子。
- 新鲜度 SLA 的量化口径（"分钟级/小时级/日级"对应什么架构成本）缺乏公开数据。
- 知识形态的自动推荐（素材特征 → 形态组合）目前只有规则版，无学习方法。
- 本手册引用的厂商收益数字（如"效率提升 X%"）均为自述，未独立复现。

## 引用出处

<a id="ref0"></a>[0] 《从 RAG 到知识编译：FAQ / LLMWiki / Graph / PageIndex / Skill 数10种知识库形态对比》，微信公众号，2026。[链接](https://mp.weixin.qq.com/s/G5_XI7ZgCoyrfZGx6cEcow)

<a id="ref1"></a>[1] 《从 RAG 到数据资产：面向落地的企业级 Agent 知识库建设》，袋鼠云 DTStack 技术博客，2026-08。[链接](https://www.dtstack.com/zh-cn/blogs/812-from-rag-to-data-assets-how-to-build-a-landing-oriented-enterprise-level-agent-knowledge-base)

<a id="ref2"></a>[2] 《知识库一刀切？达观专属问答策略引擎按部门》，达观数据，2025-10。[链接](https://www.datagrand.com/blog/%e7%9f%a5%e8%af%86%e5%ba%93-%e4%b8%80%e5%88%80%e5%88%87%ef%bc%9f%e8%be%be%e8%a7%82%e4%b8%93%e5%b1%9e%e9%97%ae%e7%ad%94%e7%ad%96%e7%95%a5%e5%bc%95%e6%93%8e%e6%8c%89%e9%83%a8%e9%97%a8.html)

<a id="ref3"></a>[3] 《企业知识库问答 Multi-Agent 实战》，腾讯云 ADP，2026-01。[链接](https://adp.tencentcloud.com/zh/blog/enterprise-knowledge-qa-multiagent)

<a id="ref4"></a>[4] 《全域知识编织》（正文未完整验证，仅引用其权限治理概念），腾讯云开发者社区，2026-07。[链接](https://cloud.tencent.cn/developer/article/2712327)

<a id="ref5"></a>[5] 《OODER 文档知识库六层知识飞轮》，腾讯云开发者社区（OneCode），2026-07。[链接](https://cloud.tencent.com.cn/developer/article/2718117)

<a id="ref6"></a>[6] 《What We Learned from a Year of Building with LLMs (I & II)》，O'Reilly，2023。[链接](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)

<a id="ref7"></a>[7] 《Enhanced Agentic-RAG》，Uber Engineering，2025-05。[链接](https://www.uber.com/en-PK/blog/enhanced-agentic-rag/)

---

*本文档随仓库演进；修正与补充请提 PR，引用出处必须可访问。*
