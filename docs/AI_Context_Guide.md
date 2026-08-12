# AI Context Guide

> 文档状态：Framework v1 Contract
> 适用对象：Framework 维护、Standalone Project 与显式迁移任务
> 权威职责：默认、按需与禁止读取范围

## 1. 核心规则

AI/Codex 只读取“当前身份与绑定 + 当前 Runtime Rules + 当前 Project Facts + 当前 Stage Method + 当前任务 Evidence”。不为保险加载全部 Project、Skill、checklist、datasheet、模板或历史记录。

Framework Repository 与 Standalone Project 的启动路径不同，不能混用。

## 2. Standalone Project 四层上下文

| Layer                       | 默认入口                                                         | 内容                                                             |
| --------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------- |
| Layer 0 — Framework Binding | `FRAMEWORK.md`                                               | Framework Repository、Release、Commit、Structure Version、初始化来源与状态 |
| Layer 1 — Runtime Rules     | Project `PROJECT_RULES.md`                                   | 所有阶段始终成立的最小项目规则                                                |
| Layer 2 — Project Facts     | 当前 Project 的 README、需求、框图、设计说明、资料、模块、Review 与 Evidence       | 当前项目实际身份、阶段、设计和结果                                              |
| Layer 3 — Stage Method      | 绑定 Framework 快照中的 Skill、Checklist、Workflow fragment、专项 Guide | 当前任务如何执行                                                       |

Standalone Project `AGENTS.md` 必须按顺序：

1. 读取 Layer 0 `FRAMEWORK.md`；
2. 读取 Layer 1 `PROJECT_RULES.md`；
3. 使用绑定的 Release + Commit 定位 Framework 快照；
4. 从该快照读取本文；
5. 只加载当前任务需要的 Layer 2、Layer 3 和 Evidence。

Project 不默认读取 Framework `main`，不默认读取其他 Project，也不依赖 Framework 与 Project 位于同一父目录。

## 3. Framework Repository 维护路由

仓库接手、架构、导航或 Framework 整体维护先读取：

- `PROJECT_RULES.md`
- `AGENTS.md`
- `docs/AI_Context_Guide.md`
- `README.md`

随后按任务读取：

| 任务 | 按需读取 | 不应默认读取 |
| --- | --- | --- |
| Contract / Structure | `docs/Project_Structure_Standard.md`、`docs/08_Project_Workflow.md`、`docs/Project_Template_Guide.md` | 真实 Project 硬件细节、datasheet、EDA |
| Template / Bootstrap | Structure、Workflow、Template Guide、Template、初始化 Skill/checklist/Validator | 所有真实 Project、全部 Skill |
| Validator | 被检查的权威文档、Template、相关 Skill/checklist、现有 CI | Project 1/2/3 设计事实 |
| 单一 Skill / Checklist | 对应权威文档和被修改文件 | 其他无关 Skill/checklist |
| Normal Framework maintenance / Release | `docs/Framework_Maintenance_and_Release_Guide.md`、受影响 Framework 文件、Validator / CI | 历史 Migration Master Plan / retired Runbook、真实 Project facts |
| Project Framework binding adoption / pinned evaluation | `docs/Framework_Migration_Guide.md`、目标 Project binding、目标 immutable SHA、最小 impact / compatibility evidence | 其他 Project、Framework `main` 的无关变化 |
| Breaking Framework release + Project adoption | 上述两份 Guide，各自保持 publication 与 adoption 风险边界 | 历史 Migration 文档、无关 Project |
| Authority Cutover | `docs/Framework_Migration_Guide.md`、目标 Project 最小事实与 authority evidence | retired Runbook、其他 Project、无关历史输出 |
| Historical Repository Architecture review | Master Plan；只有核对旧 execution model / provenance 时读取 retired Runbook 或 Baseline | 全部 Project、全部资料 |
| README / 通用文档 | 被修改文档及其直接权威引用 | 全部 Project 硬件细节 |

Repository Architecture Migration 已关闭。普通 Framework maintenance 与 Project adoption 不默认读取 Historical Master Plan、retired AI Runbook 或 Baseline；只有显式历史 architecture / provenance review 才按上表最小读取。Legacy Project 只在 Authority Cutover 或迁移核对确有必要时读取最小结构信息；不得把其器件、网络、规则值、板框、板厂参数或阶段结果变成 Framework 默认值。

## 4. Bootstrap、Stage 1 与 Gate 1.5

### Bootstrap

默认读取：Layer 0/1、Structure Standard、Workflow 的 Bootstrap 章节、Project Initialization Guide、初始化 Skill、Template、Project 根 Required files。

按需读取：专项合规方法、目标 Release 的 Migration Guide。

禁止默认读取：其他 Project、全部 Stage Skill、datasheet、EDA、制造和测试历史。

### Stage 1

默认读取：Layer 0/1、项目 `README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md`、`references.md`，以及初始化 Skill 的 Stage 1 章节。

按需读取：Workflow 的 Stage 1 章节、专项安全/合规 checklist。

禁止默认读取：器件选型后的 Stage Skill、其他 Project、全部 datasheet。

### Gate 1.5

默认读取：Layer 0/1、Project Required files、Structure Standard 的 Required/Conditional/Stage-enabled 定义、Workflow Gate 1.5、Initialization Checklist 与 Project Validator 输出。

按需读取：Markdown 链接目标、用户提供的身份或绑定证据。

Gate 1.5 不读取或产生后续阶段设计结果；Validator 结果不能替代对 Requirements Baseline 真实性的人工判断。

## 5. 八阶段最小读取范围

| Stage / Task | 默认读取 | 按需读取 | 不应默认读取 |
| --- | --- | --- | --- |
| Stage 1 — Requirements | Layer 0/1 + 当前项目五个根事实入口 + 初始化 Skill | Workflow Stage 1、专项安全方法 | 其他 Project、全部 datasheet、后续 Skill |
| Stage 2 — Component Selection | Layer 0/1 + 选型 Skill + Requirements/Design/References | 当前候选官方资料、datasheet Skill、专项 checklist | 原理图/PCB Review Skill、无关资料 |
| Stage 3 — Schematic Design | Layer 0/1 + 当前需求、设计说明、资料索引、当前模块文档 | 选型/datasheet Skill、BOM 草稿、封装资料 | 其他 Project、全部历史记录 |
| Stage 4 — Schematic Review | Layer 0/1 + Review Skill + Requirements/Design/References + 完整 PDF + 当前 BOM + Review 记录 | 当前模块文档；网表/ERC/报告/截图按具体问题触发 | 其他 Project、Template、全部 Skill |
| Stage 5 — Layout Preflight | Layer 0/1 + PCB Skill + README/Requirements/Design/References + Schematic Review + PCB Rules + 关键 Layout 资料 | PDF/BOM/机械/板厂官方能力 | Batch DRC、制造输出、其他 Project |
| Stage 5–6 — Layout/Routing Review | Layer 0/1 + PCB Skill + README/Requirements/Design/PCB Rules + 当前 PCB Evidence | 模块资料、关键 datasheet、已有 PCB 问题 | 全部资料、Release checklist、制造输出 |
| Stage 7 — PCB Release Review | Layer 0/1 + PCB Skill + README/Requirements/PCB Rules/PCB Review + 当前 BOM/Evidence + 用户 Batch DRC + 制造输出清单 + Release Checklist | 局部 Gerber、Drill、坐标、截图和报告片段 | 其他 Project 历史 |
| Stage 8 — Bring-up/Test | Layer 0/1 + README + Bring-up/Test 记录 + 原理图与接口说明 | PCB Review、关键 datasheet、安全 checklist、Revision | 其他 Project、Template |

## 6. 条件触发与证据边界

- 目标板厂官方能力：仅在制造基线、规则、裕量或下单核对时读取。
- 关键器件官方资料：仅在当前参数、连接、封装、Layout 或安全判断需要时读取。
- 原理图 PDF / BOM / 报告：仅在相应 Review 或具体追溯问题需要时读取。
- DRC 局部证据：用户摘要不足以判断具体违规、规则或豁免时读取。
- Gerber、Drill、坐标与装配输出：制造放行时读取。

无可靠 `.SchDoc` / `.PcbDoc` 解析能力时，只使用用户提供的 PDF、BOM、图片、报告、规则摘要和输出。图片不能证明网络、间距、线宽、孔径、规则命中、铺铜或 DRC 通过。无法确认的实现事项标记“待 EDA 核对”，不得据此关闭问题或制造放行。

## 7. 完整 Workflow 读取条件

只在以下情况完整读取 `docs/08_Project_Workflow.md`：

- 判断 Bootstrap、当前 Stage、Gate、回退或阶段权限；
- 执行新 Project 初始化或旧 Project migration；
- 维护 Workflow、Structure、Template 或跨阶段 Contract；
- 用户明确要求完整流程。

普通 datasheet 阅读、单次选型、单次 Review、调试记录或小幅文档维护只读取相关章节和当前任务上下文。
