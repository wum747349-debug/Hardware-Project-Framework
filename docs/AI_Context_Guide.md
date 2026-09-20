# AI Context Guide

> 文档状态：Framework v1 Contract
> 适用对象：Framework 维护、Standalone Project 与显式迁移任务
> 权威职责：默认、按需与禁止读取范围，以及不改变 Project Runtime / Structural Contract 的会话连续性与纠错复核指导

## 1. 核心规则

AI/Codex 只读取“当前身份与绑定 + 当前 Runtime Rules + 当前 Project Facts + 当前 Stage Method + 当前任务 Evidence”。不为保险加载全部 Project、Skill、checklist、datasheet、模板或历史记录。

Framework Repository 与 Standalone Project 的启动路径不同，不能混用。

当前状态冲突时遵循以下抽象优先级：

```text
当前目标 Repository 的有效 Authority / Current State
> Session Handoff
> Conversation history / AI memory
```

Framework maintenance 的 Authority / Current State 由 Framework 当前权威文件与 Git state 决定；Standalone Project 的 Authority / Current State 由该 Project 自己的权威文件、Evidence 与 `FRAMEWORK.md` 绑定的 immutable Framework snapshot 决定。Session Handoff、Session Starter、Conversation history 与 AI memory 可以帮助恢复 working set 或发现来源，但不能覆盖当前权威状态。

本指南中的 Session Management、Session Handoff、Session Starter、User-Reported Error Review 与 Affected Conclusions 属于 collaboration / context-use guidance；它们不新增 Project Runtime Rule、Project Structure Version、`FRAMEWORK.md` 字段、Stage / Gate、Required / Conditional / Stage-enabled 分类，也不改变 Project `AGENTS.md` 的七步启动路由。

## 2. 文档语言与可读性

本节是 Documentation Language / Readability 的 single source of truth，属于 authoring / usability guidance，不是 Project Runtime Contract 或 Structural Contract，也不改变 Standalone Project `AGENTS.md` context-routing contract。

本指导适用于 Framework human-facing documentation、由 Framework 指导的 Standalone Project creation / migration / maintenance、Project `README.md`、Project Facts、后续 Stage human-facing documentation，以及 AI/Codex 最终面向用户的说明：

1. Human-facing 内容默认以中文为主要解释语言，使普通用户无需依赖完整英文阅读能力也能理解当前流程、状态、职责、风险、推理依据与下一步；明确面向外部英文读者的内容可按其 Audience 使用英文。
2. 必要英文技术术语、正式 Framework 术语与工程缩写可以保留。不常见术语首次出现时可采用“中文解释 + 英文正式术语”；普通技术术语含义明确后，不反复堆叠英文括注。
3. 文件名、路径、schema key、identifier、命令、代码、器件型号、网络名、参数符号、protocol / interface abbreviation、fixed lifecycle field 及其值、validator-sensitive wording 保持正式原文，不进行机械翻译。
4. 同一文档中的术语、模块名称和状态字段保持一致。
5. 中文化不得改变 engineering requirement、Project fact、lifecycle state、Stage / Gate meaning、numerical constraint、Evidence meaning 或 authority relationship。
6. Skill、Template 或 Guide 只引用本节作为执行提示，不复制整套规则，也不成为第二权威源。

## 3. Standalone Project 四层上下文

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

## 4. Framework Repository 维护路由

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

## 5. Bootstrap、Stage 1 与 Gate 1.5

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

## 6. 八阶段最小读取范围

| Stage / Task | 默认读取 | 按需读取 | 不应默认读取 |
| --- | --- | --- | --- |
| Stage 1 — Requirements | Layer 0/1 + 当前项目五个根事实入口 + 初始化 Skill | Workflow Stage 1、专项安全方法 | 其他 Project、全部 datasheet、后续 Skill |
| Stage 2 — Component Selection | Layer 0/1 + 选型 Skill + Requirements/Design/References | 当前候选官方资料、datasheet Skill、专项 checklist | 原理图/PCB Review Skill、无关资料 |
| Stage 3 — Schematic Design | Layer 0/1 + schematic-design Skill + 当前需求、设计说明、资料索引、当前模块文档 | 选型/datasheet Skill、BOM 草稿、封装资料、当前模块所需 Manufacturer official documentation | 其他 Project、全部 Skill、全部 datasheet、全部历史记录 |
| Stage 4 — Formal Schematic Review | Layer 0/1 + Review Skill + Requirements/Design/References + post-convergence 完整 PDF + 当前 BOM + Review 记录 | 当前模块文档；网表/ERC/报告/截图按具体问题触发 | 其他 Project、Template、全部 Skill |
| Stage 5 — Layout Preflight | Layer 0/1 + PCB Skill + README/Requirements/Design/References + Schematic Review + PCB Rules + 关键 Layout 资料 | PDF/BOM/机械/板厂官方能力 | Batch DRC、制造输出、其他 Project |
| Stage 5–6 — PCB Layout / Routing Guidance & Review | Layer 0/1 + `hardware-pcb-layout-review` Skill + README/Requirements/Design/PCB Rules + 当前 PCB Evidence | 模块资料、关键 datasheet、已有 PCB 问题 | 全部资料、Release checklist、制造输出 |
| Stage 7 — PCB Release Review | Layer 0/1 + README + PCB Rules + PCB Review + `hardware-pcb-release-review` Skill + 当前 release candidate evidence + Final Full Batch DRC evidence + actual manufacturing interpretation + PCB Release Checklist | schematic、BOM、模块文档、Stage 5–6 PCB Skill、PCBA data、special fabrication data；只按 unresolved finding / design delta / 实际制造路径触发 | 其他 Project 历史、与当前放行结论无关的全部上游资料 |
| Stage 8 — Bring-up/Test | Layer 0/1 + README + Bring-up/Test 记录 + 原理图与接口说明 | PCB Review、关键 datasheet、安全 checklist、Revision | 其他 Project、Template |
| Firmware task（任何 Stage，按 Task Intent） | 完成 Project 根启动路由后，读取适用的 `firmware/AGENTS.md`（若存在）+ 绑定快照中的 `hardware-firmware-development` Skill + 当前任务所需 Firmware source / build configuration | Relevant Project hardware facts、official device / toolchain documentation、当前 validation evidence | Framework `main`、其他 Project Firmware、无关 Stage Skill、全部 datasheet |

Stage controls lifecycle；task intent selects method。Stage Method 应按实际 task intent 选择，不机械服从用户提供的 Stage label，也不按 `review`、`pin`、`BOM` 等单个关键词路由。Skill 的 primary / default Stage 不表示该 Skill 只能在该 Stage 使用；当前任务明确需要 supporting method 时可以按需读取对应 Skill。这种 supporting use 不自动改变 Project 当前 Stage，不自动满足该 Skill primary Stage 的进入或退出条件，也不自动要求产生该 Stage 的 artifact 或 PASS。

Firmware 采用同一原则：Stage 1 确认是否需要 Firmware、functional boundary、hardware interface requirements 与相关 acceptance criteria，但不要求建立工程；实际开始持续性开发前确认 Project local rules，工程初始化由 compile / prototype / development need 触发。Project `firmware/AGENTS.md` 只补充目录局部规则，不取代 Layer 0/1 或 Project 根 `AGENTS.md`；Firmware task 的顺序是 `Project root rules → firmware/AGENTS.md → bound Framework Firmware Skill → relevant Project hardware facts → implementation / evidence`。Firmware prototype、Build 或后续开发不自动改变当前硬件 Stage，Build PASS 也不替代 Flash、Runtime 或 Hardware Validation。

Stage 3 的日常模块设计、连接核对、参数计算、当前模块或局部设计的 lightweight verification，以及轻量 Cross-Module Integration 默认使用 `hardware-schematic-design`。明确限定范围的 schematic review / risk review 可按需使用 `hardware-schematic-review` 作为 supporting method，同时保持当前 lifecycle Stage。只有针对 completed whole-design evidence（完整 schematic / BOM）的正式整板审查和 PCB Layout-entry decision 才属于 Stage 4 Formal Schematic Review。

Stage 3 中只有当 exact component identity 是验证当前 electrical behavior、safety、thermal 或 package / Layout-sensitive assumption 的必要条件时，才按需使用 `hardware-component-selection` 作为 supporting method。Stage 4 的 component / footprint convergence task 也可按需使用该选型方法；完成 convergence 并更新 authoritative schematic、完整 PDF 与当前 BOM 后，Formal Schematic Review 使用 `hardware-schematic-review`。Stage controls lifecycle；task intent selects method，不因处于 Stage 4 就把 convergence 与 Formal Review 混成同一方法。

执行 Stage transition 时，在构造 bounded transaction scope 前读取 Workflow 的 transition semantics 与 Structure Standard 的 Stage-enabled activation rules，只纳入 target-stage 合法 post-state 立即需要的 artifacts。不要因 transition 默认加载或执行 target Stage 的完整 engineering method；仅在实际 target-stage activity 同时属于当前授权任务时，才按 task intent 加载相应方法与 evidence。

## 7. 工程结论继承与有边界任务执行

已有工程结论在依据可追溯、适用范围明确且对当前版本与目标仍然有效时，后续任务默认继承。更换 Conversation、Codex 或其他执行工具，普通 documentation convergence，Compatible Framework Sync，Stage 准备或已获授权的 Stage transition，重复读取同一资料，或 AI 在没有新依据时再次产生相同疑问，本身都不构成重新评估的充分理由。继承只覆盖已有依据实际支持的结论：`Electrical design selected` 不得升级为 `Hardware validation PASS`，Scoped Review 也不得升级为 Formal Review PASS。

只有出现以下实际触发时，才重新评估相应范围：

1. 相关设计、需求、假设或适用条件发生实质变化；
2. 出现可信矛盾证据，或发现原结论存在实际错误；
3. 现有 evidence 不足以支持当前请求所需的具体结论，包括此前未覆盖的范围；
4. 用户明确要求重新评估相应问题；
5. 当前适用的正式 Stage、validation 或 release requirement 存在尚未满足的必要检查。

重新评估只覆盖实际受影响的内容；局部问题不自动升级为整板审查，无设计变更也不能成为拒绝处理真实新错误证据的理由。正式流程要求 complete coverage 时，可以由仍有效的既有 evidence 与当前必要增量共同满足，不等于重新执行全部历史检查。

Documentation convergence 默认读取已确认事实与依据，更新对应 owning document，检查记录忠实性和必要一致性，然后完成。已有记录需要保留工程推理依据时，优先继承并整理现有依据，不自动重做选型、计算、设计、模块审查或整板审查；发现真实矛盾、实际依据缺失或受影响设计变化时，再按具体问题处理。事实归属继续遵循 Single Authority；implementation fact 的同步继续遵循 Workflow 的 No automatic reverse implementation sync，不在本节另建事实源或反向同步规则。

已有有效关闭依据且没有新的失效触发时，不得因后续任务或 AI 重复提出同一疑问而重新打开问题。仍待验证的问题应继承其真实状态和下一项有效行动，不重复执行不能改变结论的相同静态检查，也不得虚构为已关闭；若它按现有规则阻断当前正式放行，阻断必须保留。不得以用户接受风险、修改文档措辞或收窄任务范围绕过高风险关闭要求。本规则不新增 Issue Lifecycle、Risk Acceptance State 或 Decision Lock。

AI 生成 Codex 或其他下游执行任务时，必须在语义上区分作为输入前提继承的已确定事实、本次授权且必须完成的当前工作，以及只有实际触发条件成立时才执行的检查；不要求固定使用三类标题。任务不得先要求“不重复审查”，又无条件要求重新审查全部模块、重新 qualification 全部已确认器件、重新检查完整 schematic / BOM、重放全部历史 Stage 或再次确认全部已关闭问题，也不得用“为保险起见”“再次全面确认”或“必要时完整复核”等模糊措辞绕过 Minimum Sufficient Context。条件触发任务必须说明实际触发原因和必要范围。

用户给出的 Exact Scope 优先；若合法完成当前任务必须越界，应报告 blocker，不得擅自扩权或交付虚假的部分完成。完成获授权工作及其适用的必要 validation 后即停止，不追加没有实际触发依据的工程活动。本节不削弱 Formal Review、Stage transition、Compatible Framework Sync、Framework Contract Migration、Project Validator、Manufacturing Release 或其他现有安全、evidence 与 validation requirement。

## 8. 条件触发与证据边界

- 目标板厂官方能力：仅在制造基线、规则、裕量或下单核对时读取。
- 关键器件官方资料：仅在当前参数、连接、封装、Layout 或安全判断需要时读取。
- 原理图 PDF / BOM / 报告：仅在相应 Review 或具体追溯问题需要时读取。
- DRC 局部证据：用户摘要不足以判断具体违规、规则或豁免时读取。
- 制造数据与解读：Stage 7 按 actual manufacturing-data / submission path 读取支持当前结论所需的 manufacturing representation，不默认要求 Gerber / Drill 或特定 viewer。
- Pick & Place、Assembly 等 PCBA outputs：仅在项目实际需要 PCB Assembly 时读取。

正式结论或动作前，先判断当前 evidence 是否足以支持该具体结论或动作。证据缺失只阻断依赖该证据的具体结论或动作，不自动阻断无关工作、准备性分析、交互式工程指导、scoped review、可安全限定范围的建议或文档准备；只要仍能形成有价值、边界明确的受限结果，就应继续并明确 limitation，不得将受限结论升级为已经验证的 PASS、confirmed fact 或 release approval。仅当当前请求所需的 minimum evidence 无法从现有 Project authority、适用 authoritative source 或当前可用工具取得，并因此阻断所请求的具体结论或动作时，才向用户索取该 minimum missing evidence，不为保险批量索要无关资料。Evidence 必须与所评估的 PCB / Git / hardware version 兼容且对该结论仍然新鲜；无法识别版本关系时只能给出受限结论。

当前会话中的 PCB / Altium / DRC 截图、用户对当前 EDA 状态的确认、manufacturer CAM / Gerber preview 以及其他 implementation evidence 可以支持当前分析，但不会自动更新 persistent Project authority。当 local/session implementation 新于 committed repository source 时，Interactive Placement、Interactive Routing 和 scoped analysis 不因此自动停止；Formal Review 可对明确识别的最新 evidence 做受限判断，同时说明 persistent repository source 是否同步。Manufacturing Release 前必须无歧义识别 exact release candidate，不得在 repo / local version drift 仍模糊时放行。

B1 / B2 普通交互不要求每轮持久化 evidence。B3 Formal Layout / Routing Review、Stage transition、Final Batch DRC acceptance、Manufacturing Release 和 major waiver 才在现有 owning record `docs/pcb_review.md` 留下最小 durable summary：通常记录 evidence source、对应 PCB / Git / hardware version、date / context、result、limitations 与 decision，不建立严格 metadata schema。Durable summary 不等于所有 raw screenshots / reports 必须提交；raw evidence 默认 optional，仅在项目可追溯需求实际要求时保存。

Stage 5–6 中，精确到具体 net 或 pin-to-pin 的 routing guidance 必须具备足以回答当前限定问题、可靠且属于当前版本的 connectivity evidence；可按任务最小选用可靠可读的 `.PcbDoc` / `.SchDoc`、当前 netlist、当前 schematic PDF、当前模块连接记录或用户提供的局部 pin/net mapping，不要求形成固定来源层级或全部加载。仅有 PCB 图片时，可以进行视觉 routing review 和相对几何指导，但不能据此确定精确连接或 net function。普通视觉 routing review 不自动扩展读取 schematic、BOM 或模块文档；net-specific 问题只加载所需的最小 connectivity evidence。

BOM 只在 MPN、value、footprint、rating 或 population 信息与当前问题相关时按需读取，不能替代 connectivity evidence。

无可靠 `.SchDoc` / `.PcbDoc` 解析能力时，只使用用户提供的 PDF、BOM、图片、报告、规则摘要和输出。图片不能证明网络、间距、线宽、孔径、规则命中、铺铜或 DRC 通过。无法确认的实现事项标记“待 EDA 核对”，不得据此关闭问题或制造放行。

## 9. 会话管理与交接

会话管理只解决“继续当前 Conversation，还是切换并如何把当前 working set 交给下一会话”，不改变四层 Project Context、Stage / Gate 或持久事实源。

继续当前会话的默认条件是：目标、当前 Stage / task、Authority 组成、write target 与 working set 仍连续且清楚。出现以下情况时，应优先形成最小 Session Handoff，并考虑开启新会话：

- 目标或主要任务阶段明显变化；
- 关键决策已经冻结，后续进入不同问题域；
- 大量旧讨论已失效，继续携带会增加 stale-state interference；
- 参与的 Repository / Workspace 组合明显变化；
- Conversation history 已使当前 Authority / Current State 或下一步 scope 开始混淆。

消息数量、token 数量或对话长度本身不是切换理由。不得设置固定 token threshold、Context Score、自动 Session 切换机制，也不新增 Session storage、database、runtime 或 agent。

Session Handoff 只保留下一轮可靠继续所需的最小 working set，通常包括：目标、相关 Repository / branch、适用 Authority、当前 Stage / state、已冻结决策、未解决问题、禁止事项与下一步行动。Domain-specific 项目可以按实际需要增减，不建立统一 schema，也不要求把完整聊天复制进 Repository。

Session Starter 是新会话的轻量入口，用于指出 Repository、branch、适用 Authority、工作原则、执行边界和当前任务；它不是新的 Framework / Project Contract，也不替代 Handoff。新会话必须重新读取目标 Repository 的当前 Authority / Current State，再核对 Handoff；若冲突，以当前 Authority / Current State 为准。

## 10. 用户报错复核与受影响结论

用户明确质疑某个 AI/Codex 结论时：

1. 精确识别被质疑的结论，并暂停继续依赖它；
2. 只读取完成独立复核所需的最小 Authority、Current State、Evidence 与可靠来源；
3. 输出 `Confirmed`、`Corrected` 或 `Unresolved`；
4. `Unresolved` 不恢复为可靠前提；
5. 若为 `Corrected`，检查 Affected Conclusions，包括后续推理、建议、Stage / Gate 判断、文件修改、Validation、Release / Manufacturing decision 与其他依赖结果；
6. 只修复实际失效的最小范围，并重新执行受影响的 validation / review；没有传播时明确说明影响仅限当前结论。

“修复最小失效层”表示先定位目标 Framework / Project 模型中真正出错的 Authority、Context / Retrieval、Evidence、Tool、Workflow、Validation 或 reasoning boundary，再修复该范围；它不要求复制 Workspace Hub 的 Failure Taxonomy，也不假设所有 Project 拥有相同诊断层级。

单次、局部错误在当前任务内解决。只有真实重复、高影响或系统性问题才值得进入 Framework maintenance 评估；不得因为一次错误自动增加 Runtime、Agent、Database、Vector Search、Dashboard、多 Agent、错误日志平台或新的复杂 Context Score。

## 11. 完整 Workflow 读取条件

只在以下情况完整读取 `docs/08_Project_Workflow.md`：

- 判断 Bootstrap、当前 Stage、Gate、回退或阶段权限；
- 执行新 Project 初始化或旧 Project migration；
- 维护 Workflow、Structure、Template 或跨阶段 Contract；
- 用户明确要求完整流程。

普通 datasheet 阅读、单次选型、单次 Review、调试记录或小幅文档维护只读取相关章节和当前任务上下文。
