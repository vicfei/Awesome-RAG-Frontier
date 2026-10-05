<div align="center">

# Awesome RAG Frontier

**追踪检索增强生成（RAG）的前沿——真正在交付的论文、项目与技术。机器保证每周刷新，人工负责筛选。**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![refreshed](https://img.shields.io/badge/refreshed-2026--10--05-2ea44f)](.github/workflows/refresh.yml)
[![tracked](https://img.shields.io/badge/projects--tracked-45-blue)](data/projects.json)

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

---

## 为什么再做一个 RAG 清单？

市面上多数 "Awesome RAG" 清单是会慢慢过期的论文目录——一个 3 万 star 的 RAG 平台周二刚发大版本，一年后仍然不在任何一份清单里。本仓库押注三件它们没做的事：

1. **工程与研究并重。** 产品、框架、解析、评测、GraphRAG 与论文享有同等地位——因为前沿现在以仓库的形式交付，而不只是 PDF。
2. **新鲜度由机器保证。** star 数、活跃日期、每周 arXiv 摘要由 [GitHub Action](.github/workflows/refresh.yml) 每周一自动重生成。表格过期是 bug，不是常态。
3. **同时覆盖两个生态。** 中英文 RAG 社区互相借鉴却很少互读。每个条目都带双语一句话点评。

收录靠规则，不靠感觉：见 **[criteria.md](criteria.md)**。

## 目录

[为什么再做一个 RAG 清单？](#为什么再做一个-rag-清单) · [本月 RAG 动态](#news) · [项目](#项目) · [雷达](#radar) · [论文](#论文人工精选) · [基准](#值得了解的基准) · [企业落地实践](#practices) · [参与贡献](#参与贡献) · [许可证](#许可证)

<a id="news"></a>

## 🔥 本月 RAG 动态

短小、带日期、带出处的更新日志——从 [news/2026-09.md](news/2026-09.md) 开始。

## 项目

<!-- frontier:projects:start -->

### 知识库平台与产品

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [ragflow](https://github.com/infiniflow/ragflow) | 深度文档理解 RAG 引擎，解析能力同类最强，引用可解释。 | 91,687 | 2026-10-04 |
| [onyx](https://github.com/onyx-dot-app/onyx) | 企业搜索助手（原 Danswer）：40+ 数据源连接器 + 之上的 RAG 问答。 | 32,323 | 2026-10-05 |
| [WeKnora](https://github.com/Tencent/WeKnora) | 腾讯开源的大模型知识库平台：混合检索+重排、父子分块、GraphRAG、沙箱内 Agent 技能、自维护 Wiki。Go 实现，MIT 协议。 | 32,095 | 2026-10-01 |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | 简洁的文档问答 Web UI，支持 RAG/GraphRAG 工作流，适合演示与内部工具。 | 25,797 | 2026-07-14 |
| [rags](https://github.com/run-llama/rags) ⚠️ | 用自然语言定义『你的数据上的 ChatGPT』，基于 LlamaIndex。 | 6,550 | 2024-04-05 |
| [code-graph-rag](https://github.com/vitali87/code-graph-rag) | 面向 monorepo 的代码图 RAG：查询、理解、编辑多语言代码库。 | 5,231 | 2026-10-05 |
| [ragapp](https://github.com/ragapp/ragapp) ⚠️ | 面向企业的 Agentic RAG 应用，Docker 一键部署。 | 4,445 | 2025-01-22 |

### 框架与引擎

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [langchain](https://github.com/langchain-ai/langchain) | LangChain：通用 LLM 工具链，集成生态最大，RAG 链齐备。 | 147,457 | 2026-10-05 |
| [llama_index](https://github.com/run-llama/llama_index) | LlamaIndex：LLM 应用数据框架，多数 RAG 技术栈的摄取/索引/检索基座。 | 52,411 | 2026-10-01 |
| [haystack](https://github.com/deepset-ai/haystack) | Haystack：类型严格、组件显式的生产级 RAG 管线，检索血统纯正。 | 26,653 | 2026-10-05 |
| [R2R](https://github.com/SciPhi-AI/R2R) ⚠️ | R2R：生产级 RAG 引擎，自带 API、看板与 Agentic 检索。 | 8,011 | 2025-11-07 |
| [UltraRAG](https://github.com/OpenBMB/UltraRAG) | UltraRAG：低代码、基于 MCP 组合复杂 RAG 管线的框架。 | 5,711 | 2026-10-05 |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | AutoRAG：用你自己的评测数据自动搜索最优 RAG 模块与参数。 | 5,111 | 2026-10-05 |

### GraphRAG 与知识图谱

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [LightRAG](https://github.com/HKUDS/LightRAG) | LightRAG（EMNLP 2025）：简单快速的 GraphRAG，图+向量双层检索。 | 39,981 | 2026-10-03 |
| [graphrag](https://github.com/microsoft/graphrag) | Microsoft GraphRAG：命名词汇的原始实现，LLM 构建知识图谱回答语料级问题。 | 36,225 | 2026-10-05 |
| [graphiti](https://github.com/getzep/graphiti) | Graphiti（Zep）：面向 Agent 记忆的时序知识图谱，边带双时间轴有效性。 | 31,444 | 2026-10-04 |
| [cognee](https://github.com/topoteretes/cognee) | Cognee：把数据变成知识图谱、服务检索增强 Agent 的记忆引擎。 | 31,371 | 2026-10-05 |
| [nano-graphrag](https://github.com/gusye1234/nano-graphrag) ⚠️ | nano-graphrag：极简可改的 GraphRAG 参考实现，读懂模式看它。 | 3,992 | 2026-01-27 |

### 文档解析与多模态摄取

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [markitdown](https://github.com/microsoft/markitdown) | 微软的多面手转换器：Office / PDF / 音频 / 图片 → Markdown，无数 LLM 摄取脚本的默认胶水。 | 188,534 | 2026-10-04 |
| [MinerU](https://github.com/opendatalab/MinerU) | MinerU：把 PDF/扫描件转成 Markdown/JSON，再丑的版式也能啃，很多 RAG 栈的解析层默认选择。 | 81,101 | 2026-09-30 |
| [docling](https://github.com/DS4SD/docling) | Docling（IBM）：文档解析库，结构/表格/版面理解能力强。 | 68,397 | 2026-10-05 |
| [anydoc](https://github.com/firecrawl/anydoc) | Firecrawl 的高保真文档转换引擎（Word / PPT / Excel / EPUB / PDF → 干净输出），也是 WeKnora 内置的解析器。 | 22,512 | 2026-08-28 |
| [unstructured](https://github.com/Unstructured-IO/unstructured) | Unstructured：摄取层事实标准，任意文档格式 → 干净的类型化元素。 | 15,527 | 2026-10-05 |
| [PixelRAG](https://github.com/StarTrail-org/PixelRAG) | PixelRAG（arXiv:2606.28344）：像素级 RAG，直接在渲染像素上检索，跳过文本解析。 | 10,187 | 2026-10-01 |

### 评测与可观测性

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [langfuse](https://github.com/langfuse/langfuse) | Langfuse：开源 LLM 可观测性，端到端追踪 RAG 管线并对轨迹做评测。 | 35,391 | 2026-10-05 |
| [deepeval](https://github.com/confident-ai/deepeval) | DeepEval：LLM 评测框架，含 RAG 指标，pytest 风格，自带 LLM 裁判。 | 18,635 | 2026-10-05 |
| [ragas](https://github.com/vibrantlabsai/ragas) ⚠️ | Ragas：事实标准的 RAG 评测库：忠实度、答案相关性、上下文精确率/召回率。 | 15,931 | 2026-02-24 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Phoenix：LLM/Agent 应用的追踪与评测，含检索 span 分析。 | 11,709 | 2026-10-04 |

### 研究沙盒与课程

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 以 notebook 为主的教程库（LLM / RAG / Agent），RAG 是头牌主线之一而非点缀。 | 38,216 | 2026-09-10 |
| [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 60+ 种 RAG 技术的可运行 notebook 合集，技术食谱书。 | 29,669 | 2026-09-21 |
| [llm-universe](https://github.com/datawhalechina/llm-universe) | Datawhale 面向小白的中文大模型应用开发教程，压轴项目是完整的 RAG 知识库助手。 | 14,075 | 2026-08-27 |
| [all-in-rag](https://github.com/datawhalechina/all-in-rag) | Datawhale 出品的 RAG 全栈教程书（中文，在线可读）。 | 11,689 | 2026-09-30 |
| [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | 实战课程：能在生产环境活下来的 Agentic RAG 模式。 | 9,590 | 2026-06-05 |
| [rag-from-scratch](https://github.com/langchain-ai/rag-from-scratch) ⚠️ | LangChain 官方『RAG 从零实现』系列代码。 | 9,445 | 2025-06-26 |
| [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 免费实战课程，向量检索、RAG 与 RAG 评测构成核心模块。 | 7,418 | 2026-09-15 |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | FlashRAG（人大）：模块化 RAG 研究工具箱，40+ 方法，可复现基准。 | 3,585 | 2026-10-01 |

### 值得信任的同侪清单

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 100+ 可运行的 AI Agent 与 RAG 应用模板，该领域最大的 awesome 仓库。 | 140,741 | 2026-09-30 |
| [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) | 双语 LLM 全栈资源库，RAG 是其中一个高质量章节。 | 8,998 | 2026-09-21 |
| [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | 上下文工程综述清单，RAG 正在走向的邻近前沿。 | 3,316 | 2026-05-28 |
| [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 有综述论文背书的 GraphRAG 论文清单，该方向维护最认真的学术追踪。 | 2,663 | 2026-06-02 |
| [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | 长上下文建模清单：『长上下文 vs RAG』之争的另一半。 | 2,175 | 2026-08-17 |
| [RAG-Survey](https://github.com/hymie122/RAG-Survey) ⚠️ | RAG 论文分类清单（基础/增强/任务），配套综述论文。 | 1,790 | 2024-08-20 |
| [Awesome-LLM-RAG-Application](https://github.com/lizhe2004/Awesome-LLM-RAG-Application) ⚠️ | 中文 RAG 清单，业界案例（QCon/AICon 分享）部分最扎实。 | 1,659 | 2026-03-10 |
| [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) | 工程视角的 RAG 资源地图：模式、工具、生产注意事项。 | 1,387 | 2026-09-23 |
| [Awesome-LLM-RAG](https://github.com/jxzhangjhu/Awesome-LLM-RAG) | 按研究主题组织的 RAG 论文清单。 | 1,366 | 2026-10-03 |

_每周自动刷新，最近一次：2026-10-05。⚠️ = 已归档或沉寂超过 6 个月。原始数据见 [data/stats.json](data/stats.json)。_

<!-- frontier:projects:end -->

<a id="radar"></a>

## 📡 雷达 — 未达门槛观察线

有前景但尚未达到收录门槛的条目——通常是搭乘可见浪潮的早期或单人项目（当前：**RAG × Agent Skills**，见[动态](news/2026-09.md)）。与其他部分一样自动刷新。

<!-- frontier:radar:start -->

| 项目 | 为何值得关注 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [rag-skill](https://github.com/ConardLi/rag-skill) | RAG-as-skill 浪潮的起点：层级索引文件 + grep + 渐进披露做本地知识检索，无向量无嵌入。已归档，后继为 garden-skills。 | 714 | 2026-04-25 |
| [rag-to-skill](https://github.com/Jia-Hong-Peng/rag-to-skill) | 把 JSONL RAG 语料转成可安装、可审计的 Claude Code skill——用带来源锚点的精选知识包替代运行时检索。 | 68 | 2026-05-10 |
| [enowx-rag](https://github.com/enowdev/enowx-rag) | Go 实现的 MCP 服务器，为编码 Agent 提供按项目持久化的 RAG 记忆：Qdrant/pgvector/Chroma、混合检索、重排、内嵌看板。 | 40 | 2026-07-16 |
| [RAG-Data-Curator-Agent-Skill](https://github.com/leichu0612-byte/RAG-Data-Curator-Agent-Skill) | 结构感知分块（节 → 标题 → 段落 → 句子）打包成 Agent skill + CLI，带溯源元数据和质量报告。 | 86 | 2026-09-11 |
| [Skill-First-Hybrid-RAG](https://github.com/lyxhnu/Skill-First-Hybrid-RAG) ⚠️ | Skill 优先的 Agent 工作台，skill 证据不足时回退到向量 + BM25 混合检索，自带 Ragas 评测与可编辑的 Markdown 记忆，研究级。 | 95 | 2026-03-24 |

_未达门槛观察线 — 自动刷新于 2026-10-05。达到完整收录标准后自动毕业进入主表（见 criteria.md）。_

<!-- frontier:radar:end -->

## 论文（人工精选）

由人工维护，每周 arXiv 候选草稿（[`news/_drafts/`](news/_drafts)）供稿，是否收录由人决定。

### 综述与奠基

| 论文 | 年份 | 一句话点评 |
| --- | --- | --- |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 2020 | 给这个模式命名的原初论文。 |
| [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) | 2023 | 至今最清晰的 RAG 分类学地图。 |
| [Agentic Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2501.09136) | 2025 | 把 RAG 重新表述为一系列 Agent 决策。 |
| [A Survey of Graph RAG](https://arxiv.org/abs/2501.13958) | 2025 | 图原生分支的综述，分类学齐全。 |

### 范式论文（人们仍在用的词汇）

| 论文 | 年份 | 核心思想 |
| --- | --- | --- |
| [HyDE](https://arxiv.org/abs/2212.10496) | 2022 | 用假设性答案的向量代替查询向量。 |
| [FLARE](https://arxiv.org/abs/2305.06983) | 2023 | 生成中途按低置信度 token 主动触发检索。 |
| [Self-RAG](https://arxiv.org/abs/2310.11511) | 2023 | 模型自我评判检索质量与引用。 |
| [CRAG](https://arxiv.org/abs/2401.15884) | 2024 | 生成前先纠正糟糕的检索结果。 |
| [RAPTOR](https://arxiv.org/abs/2401.18059) | 2024 | 递归树状摘要作为索引结构。 |
| [HippoRAG](https://arxiv.org/abs/2405.14831) | 2024 | 知识图谱 + 个性化 PageRank，仿海马体记忆。 |
| [LightRAG](https://arxiv.org/abs/2410.05779) | 2024 | 图+向量双层检索，EMNLP 2025。 |

### 2026 前沿

| 论文 | 为什么值得关注 |
| --- | --- |
| [PixelRAG](https://arxiv.org/abs/2606.28344) | 在渲染像素上检索——『解析可选』的 RAG。仓库已破 1 万 star。 |
| [The Fellowship of the Query: Learning Retrieval Actions](https://arxiv.org/abs/2609.28653) | 用轨迹微调让小模型充当 RAG 的下一步动作控制器——分解、检索、改写、验证、停止。把 agentic RAG 命题端到端学出来。 |
| [Return or Revise? Learning When Revision Helps QA](https://arxiv.org/abs/2609.30087) | 学习检索证据是否值得触发一次修订——返回还是修订的决策由训练习得，而非拍脑袋规则。 |
| [VeriSpeak](https://arxiv.org/abs/2609.30227) | 面向语音事实核查的探针基准——RAG 的多模态前沿正走出纯文本。 |

## 值得了解的基准

| 基准 | 测什么 |
| --- | --- |
| BEIR | 异构语料上的零样本检索。 |
| HotpotQA / 2WikiMultiHopQA / MuSiQue | 多跳问答——RAG 推理标准三件套。 |
| MultiHop-RAG | 网页文档+图片上的多跳推理。 |
| GraphRAG-Bench | 面向 GraphRAG 系统的图推理问答。 |

<a id="practices"></a>

## 🏭 企业落地实践（人工精选）

RAG 在企业里究竟怎么运营——一手工程博客与可验证的案例，不是厂商宣讲稿。本节门槛：一手或可验证、带日期、技术含量大于营销。

| 实践 | 来源 | 年份 | 一句话教训 |
| --- | --- | :--: | --- |
| [Enhanced Agentic-RAG](https://www.uber.com/en-PK/blog/enhanced-agentic-rag/) | Uber 工程博客 | 2025 | 文档深度加工 + agentic 检索，把值班助手 Genie 的回答精度拉到接近人类。 |
| [What We Learned from a Year of Building with LLMs（I & II）](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) | O'Reilly | 2023 | 生产级 LLM 应用的经典总结：评测先行、架构从简、成本是设计轴。至今仍然对。 |
| [Milvus 在携程酒店搜索中的应用](https://zilliz.com.cn/blog/usercase-milvus-trip) | Zilliz / 携程 | 2024 | 旅游行业规模的向量检索：真实排序约束下的召回工程。 |
| [得物：RAG 在开放平台智能答疑的探索](https://mp.weixin.qq.com/s/6yhYLKfNrumSMs7ELvktjg) | 得物技术 | — | 中文电商实践：从朴素知识库问答走向结构化、评测驱动的答疑。 |

日期以来源发布为准；欢迎 PR 修正或补充——本节一次只长一条经过验证的条目。

## 参与贡献

欢迎——见 **[CONTRIBUTING.md](CONTRIBUTING.md)**。项目收录改 `data/projects.json`；论文收录改上面章节；动态线索提 issue。

**利益披露：** 发起维护者是 [Tencent/WeKnora](https://github.com/Tencent/WeKnora) 的历史前 20 贡献者。WeKnora 按『知识库平台与产品』分类收录，与其他条目适用同一套公开标准——同样的门槛、同样的自动刷新、同样的除名规则。披露身份，而非隐瞒。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=vicfei/Awesome-RAG-Frontier&type=Date)](https://star-history.com/#vicfei/Awesome-RAG-Frontier&Date)

## 许可证

[MIT](LICENSE)。精选内容本质是数据而非代码——随便复用，愿意的话回链一下。
