<div align="center">

# Awesome RAG Frontier

**追踪检索增强生成（RAG）的前沿——真正在交付的论文、项目与技术。机器保证每周刷新，人工负责筛选。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![refreshed](https://img.shields.io/badge/refreshed-2026--09--27-2ea44f)](.github/workflows/refresh.yml)
[![tracked](https://img.shields.io/badge/projects--tracked-40-blue)](data/projects.json)

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

---

## 为什么再做一个 RAG 清单？

市面上多数 "Awesome RAG" 清单是会慢慢过期的论文目录——一个 3 万 star 的 RAG 平台周二刚发大版本，一年后仍然不在任何一份清单里。本仓库押注三件它们没做的事：

1. **工程与研究并重。** 产品、框架、解析、评测、GraphRAG 与论文享有同等地位——因为前沿现在以仓库的形式交付，而不只是 PDF。
2. **新鲜度由机器保证。** star 数、活跃日期、每周 arXiv 摘要由 [GitHub Action](.github/workflows/refresh.yml) 每周一自动重生成。表格过期是 bug，不是常态。
3. **同时覆盖两个生态。** 中英文 RAG 社区互相借鉴却很少互读。每个条目都带双语一句话点评。

收录靠规则，不靠感觉：见 **[criteria.md](criteria.md)**。

## 🔥 本月 RAG 动态

短小、带日期、带出处的更新日志——从 [news/2026-09.md](news/2026-09.md) 开始。

## 项目

<!-- frontier:projects:start -->

### 知识库平台与产品

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [ragflow](https://github.com/infiniflow/ragflow) | 深度文档理解 RAG 引擎，解析能力同类最强，引用可解释。 | 91,355 | 2026-09-26 |
| [onyx](https://github.com/onyx-dot-app/onyx) | 企业搜索助手（原 Danswer）：40+ 数据源连接器 + 之上的 RAG 问答。 | 32,259 | 2026-09-27 |
| [WeKnora](https://github.com/Tencent/WeKnora) | 腾讯开源的大模型知识库平台：混合检索+重排、父子分块、GraphRAG、沙箱内 Agent 技能、自维护 Wiki。Go 实现，MIT 协议。 | 30,509 | 2026-09-27 |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | 简洁的文档问答 Web UI，支持 RAG/GraphRAG 工作流，适合演示与内部工具。 | 25,778 | 2026-07-14 |
| [rags](https://github.com/run-llama/rags) ⚠️ | 用自然语言定义『你的数据上的 ChatGPT』，基于 LlamaIndex。 | 6,551 | 2024-04-05 |
| [code-graph-rag](https://github.com/vitali87/code-graph-rag) | 面向 monorepo 的代码图 RAG：查询、理解、编辑多语言代码库。 | 5,182 | 2026-09-27 |
| [ragapp](https://github.com/ragapp/ragapp) ⚠️ | 面向企业的 Agentic RAG 应用，Docker 一键部署。 | 4,442 | 2025-01-22 |

### 框架与引擎

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [langchain](https://github.com/langchain-ai/langchain) | LangChain：通用 LLM 工具链，集成生态最大，RAG 链齐备。 | 147,151 | 2026-09-27 |
| [llama_index](https://github.com/run-llama/llama_index) | LlamaIndex：LLM 应用数据框架，多数 RAG 技术栈的摄取/索引/检索基座。 | 52,330 | 2026-09-27 |
| [haystack](https://github.com/deepset-ai/haystack) | Haystack：类型严格、组件显式的生产级 RAG 管线，检索血统纯正。 | 26,614 | 2026-09-25 |
| [R2R](https://github.com/SciPhi-AI/R2R) ⚠️ | R2R：生产级 RAG 引擎，自带 API、看板与 Agentic 检索。 | 8,009 | 2025-11-07 |
| [UltraRAG](https://github.com/OpenBMB/UltraRAG) | UltraRAG：低代码、基于 MCP 组合复杂 RAG 管线的框架。 | 5,706 | 2026-09-27 |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | AutoRAG：用你自己的评测数据自动搜索最优 RAG 模块与参数。 | 5,112 | 2026-09-27 |

### GraphRAG 与知识图谱

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [LightRAG](https://github.com/HKUDS/LightRAG) | LightRAG（EMNLP 2025）：简单快速的 GraphRAG，图+向量双层检索。 | 39,880 | 2026-09-27 |
| [graphrag](https://github.com/microsoft/graphrag) | Microsoft GraphRAG：命名词汇的原始实现，LLM 构建知识图谱回答语料级问题。 | 36,119 | 2026-09-24 |
| [graphiti](https://github.com/getzep/graphiti) | Graphiti（Zep）：面向 Agent 记忆的时序知识图谱，边带双时间轴有效性。 | 31,200 | 2026-09-27 |
| [cognee](https://github.com/topoteretes/cognee) | Cognee：把数据变成知识图谱、服务检索增强 Agent 的记忆引擎。 | 31,031 | 2026-09-27 |
| [nano-graphrag](https://github.com/gusye1234/nano-graphrag) ⚠️ | nano-graphrag：极简可改的 GraphRAG 参考实现，读懂模式看它。 | 3,989 | 2026-01-27 |

### 文档解析与多模态摄取

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [MinerU](https://github.com/opendatalab/MinerU) | MinerU：把 PDF/扫描件转成 Markdown/JSON，再丑的版式也能啃，很多 RAG 栈的解析层默认选择。 | 80,713 | 2026-09-24 |
| [docling](https://github.com/DS4SD/docling) | Docling（IBM）：文档解析库，结构/表格/版面理解能力强。 | 68,038 | 2026-09-25 |
| [unstructured](https://github.com/Unstructured-IO/unstructured) | Unstructured：摄取层事实标准，任意文档格式 → 干净的类型化元素。 | 15,506 | 2026-09-27 |
| [PixelRAG](https://github.com/StarTrail-org/PixelRAG) | PixelRAG（arXiv:2606.28344）：像素级 RAG，直接在渲染像素上检索，跳过文本解析。 | 10,104 | 2026-09-27 |

### 评测与可观测性

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [langfuse](https://github.com/langfuse/langfuse) | Langfuse：开源 LLM 可观测性，端到端追踪 RAG 管线并对轨迹做评测。 | 35,102 | 2026-09-27 |
| [deepeval](https://github.com/confident-ai/deepeval) | DeepEval：LLM 评测框架，含 RAG 指标，pytest 风格，自带 LLM 裁判。 | 18,464 | 2026-09-25 |
| [ragas](https://github.com/vibrantlabsai/ragas) ⚠️ | Ragas：事实标准的 RAG 评测库：忠实度、答案相关性、上下文精确率/召回率。 | 15,859 | 2026-02-24 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Phoenix：LLM/Agent 应用的追踪与评测，含检索 span 分析。 | 11,631 | 2026-09-27 |

### 研究沙盒与课程

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 60+ 种 RAG 技术的可运行 notebook 合集，技术食谱书。 | 29,606 | 2026-09-21 |
| [all-in-rag](https://github.com/datawhalechina/all-in-rag) | Datawhale 出品的 RAG 全栈教程书（中文，在线可读）。 | 11,443 | 2026-09-04 |
| [rag-from-scratch](https://github.com/langchain-ai/rag-from-scratch) ⚠️ | LangChain 官方『RAG 从零实现』系列代码。 | 9,385 | 2025-06-26 |
| [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | 实战课程：能在生产环境活下来的 Agentic RAG 模式。 | 8,946 | 2026-06-05 |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | FlashRAG（人大）：模块化 RAG 研究工具箱，40+ 方法，可复现基准。 | 3,583 | 2026-09-19 |

### 值得信任的同侪清单

| 项目 | 一句话点评 | Stars | 最近推送 |
| --- | --- | :--: | :--: |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 100+ 可运行的 AI Agent 与 RAG 应用模板，该领域最大的 awesome 仓库。 | 139,956 | 2026-09-26 |
| [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) | 双语 LLM 全栈资源库，RAG 是其中一个高质量章节。 | 8,986 | 2026-09-21 |
| [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | 上下文工程综述清单，RAG 正在走向的邻近前沿。 | 3,312 | 2026-05-28 |
| [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 有综述论文背书的 GraphRAG 论文清单，该方向维护最认真的学术追踪。 | 2,658 | 2026-06-02 |
| [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | 长上下文建模清单：『长上下文 vs RAG』之争的另一半。 | 2,172 | 2026-08-17 |
| [RAG-Survey](https://github.com/hymie122/RAG-Survey) ⚠️ | RAG 论文分类清单（基础/增强/任务），配套综述论文。 | 1,788 | 2024-08-20 |
| [Awesome-LLM-RAG-Application](https://github.com/lizhe2004/Awesome-LLM-RAG-Application) ⚠️ | 中文 RAG 清单，业界案例（QCon/AICon 分享）部分最扎实。 | 1,658 | 2026-03-10 |
| [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) | 工程视角的 RAG 资源地图：模式、工具、生产注意事项。 | 1,380 | 2026-09-23 |
| [Awesome-LLM-RAG](https://github.com/jxzhangjhu/Awesome-LLM-RAG) | 按研究主题组织的 RAG 论文清单。 | 1,364 | 2026-07-22 |

_每周自动刷新，最近一次：2026-09-27。⚠️ = 已归档或沉寂超过 6 个月。原始数据见 [data/stats.json](data/stats.json)。_

<!-- frontier:projects:end -->

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

## 值得了解的基准

| 基准 | 测什么 |
| --- | --- |
| BEIR | 异构语料上的零样本检索。 |
| HotpotQA / 2WikiMultiHopQA / MuSiQue | 多跳问答——RAG 推理标准三件套。 |
| MultiHop-RAG | 网页文档+图片上的多跳推理。 |
| GraphRAG-Bench | 面向 GraphRAG 系统的图推理问答。 |

## 参与贡献

欢迎——见 **[CONTRIBUTING.md](CONTRIBUTING.md)**。项目收录改 `data/projects.json`；论文收录改上面章节；动态线索提 issue。

**利益披露：** 发起维护者是 [Tencent/WeKnora](https://github.com/Tencent/WeKnora) 的历史前 20 贡献者。WeKnora 按『知识库平台与产品』分类收录，与其他条目适用同一套公开标准——同样的门槛、同样的自动刷新、同样的除名规则。披露身份，而非隐瞒。

## 许可证

[MIT](LICENSE)。精选内容本质是数据而非代码——随便复用，愿意的话回链一下。
