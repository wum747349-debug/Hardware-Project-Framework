# Hardware Project Structure Standard

> 文档状态：Framework v1 Contract
> Project Structure Version：1
> 适用对象：Framework Repository 与 Standalone Project Repository
> 权威职责：Project 结构、绑定 schema、文件职责、事实源、版本与迁移契约

## 1. Contract 层级

Framework 的单向实现关系为：

```text
PROJECT_RULES.md
        ↓
Project_Structure_Standard.md + 08_Project_Workflow.md + AI_Context_Guide.md
        ↓
Template / Skill / Checklist
        ↓
Validator
        ↓
Reference Project / Test Fixture
```

本文是 Project 结构与绑定的权威源。Template 是实现，不得反向定义 Contract；Validator 检查本文要求，不得另造结构；Skill 说明执行方法，Checklist 只列逐项检查。

## 2. Framework / Project Repository Model

Framework Repository 保存通用运行规则、结构标准、八阶段 Workflow、AI Context Routing、Bootstrap、Gate 1.5、Template、Skill、Checklist、Validator、Changelog、Migration Guide 和轻量 Reference Project。

Standalone Project Repository 保存本项目身份、当前阶段、需求、设计事实、器件决策、项目资料、EDA 权威源、BOM、Review、Manufacturing、Bring-up、Test、Revision，以及独立 Git history、issue 和 release。

正式规则：

> Framework 定义方法和契约，不作为真实 Project 的活动事实源。

> 一个正式 Project 只能有一个活动权威仓库。

Standalone Project 的 `Repository Model` 固定为 `Standalone Project`。Legacy Monorepo 中的真实项目只能按第 13 节执行显式迁移与 Authority Cutover。

## 3. Framework Binding

### 3.1 `FRAMEWORK.md` 唯一 schema

Project 根 `FRAMEWORK.md` 必须包含且只维护以下绑定字段：

```text
Framework Repository: <FRAMEWORK_REPOSITORY>
Framework Release: <FRAMEWORK_RELEASE>
Framework Commit: <FRAMEWORK_COMMIT>
Project Structure Version: <PROJECT_STRUCTURE_VERSION>
Repository Model: Standalone Project
Initialization Framework Release: <INITIALIZATION_FRAMEWORK_RELEASE>
Initialization Status: <INITIALIZATION_STATUS>
```

字段语义：

| 字段 | 含义 |
| --- | --- |
| Framework Repository | 提供该绑定快照的 Git repository 身份，不是本地绝对路径 |
| Framework Release | 人类可读的固定 Framework release/tag，例如 `hardware-project-framework-v1.0.0` |
| Framework Commit | 与该 Release 对应、不可歧义的 40 位 immutable Git SHA |
| Project Structure Version | Project Repository 使用的结构契约版本；当前为 `1` |
| Repository Model | 固定为 `Standalone Project` |
| Initialization Framework Release | 首次 Bootstrap 使用的 Framework Release，用于来源追溯 |
| Initialization Status | `Bootstrap Draft`、`Gate 1.5 Pending` 或 `Initialized`；开发自测可使用 `Development Bootstrap` |

Project 必须锁定 Release + Commit，不默认跟随 Framework `main`。`Framework Release`、`Framework Commit` 和 `Initialization Framework Release` 不能用 branch 名代替。

### 3.2 正式与 Development Binding

正式 Project Bootstrap 必须从已发布的固定 Framework Release 获取 Template，`Framework Commit` 必须解析到该 Release 的实际 commit。

在 Framework 尚未发布 RC/Final 时，只允许 Framework 自测或明确预发布评估使用：

```text
Framework Release: development-v0.9
Framework Commit: <本次测试实际使用的完整 immutable commit>
Initialization Framework Release: development-v0.9
Initialization Status: Development Bootstrap
```

Development Binding 不是正式 Release，不得写成已发布的 `hardware-project-framework-v1.0.0-rc1` 或 Final。

## 4. Project `AGENTS.md` Contract

Standalone Project 必须具有轻量 `AGENTS.md`，其唯一职责是启动上下文路由：

1. 先读取 `FRAMEWORK.md`；
2. 再读取本项目 `PROJECT_RULES.md`；
3. 从 `FRAMEWORK.md` 得到绑定 Framework Release + Commit；
4. 从该绑定 Framework 快照读取 `docs/AI_Context_Guide.md`；
5. 只读取当前任务所需 Project Facts + Stage Method + Evidence；
6. 不默认读取 Framework `main`；
7. 不默认读取其他 Project。

Project `AGENTS.md` 不复制完整 Workflow、Skill 或 Checklist，也不得依赖 monorepo `projects/...` 路径或本机绝对路径。

## 5. Project `PROJECT_RULES.md` Contract

Standalone Project 的精简 `PROJECT_RULES.md` 只保存所有阶段始终成立的 Runtime Rules：

1. 当前项目事实只能来自本项目；
2. Framework 版本以 `FRAMEWORK.md` 为准；
3. 不自动采用或读取 Framework `main`；
4. Framework 升级必须显式迁移；
5. 关键硬件参数必须回到官方 datasheet、reference manual 或 application note 核对；
6. `.SchDoc` / `.PcbDoc` 是 EDA 权威实现源；
7. AI 不得伪造 EDA、ERC、DRC、Manufacturing 或 Test 结果；
8. 当前项目阶段只在根 `README.md` 维护；
9. 其他 Project 不能作为当前 Project 事实源；
10. 当前任务只读取必要 Stage Skill。

不得把 Framework 的完整 Workflow、Skill、Checklist 或仓库迁移规则复制到 Project Runtime Rules。

## 6. 四层上下文模型

Standalone Project 使用以下四层模型：

| Layer | 权威内容 | 回答的问题 |
| --- | --- | --- |
| Layer 0 — Framework Binding | `FRAMEWORK.md` | 当前 Project 使用哪个 Framework Release / Commit？ |
| Layer 1 — Runtime Rules | Project `PROJECT_RULES.md` | 所有阶段始终成立的运行规则是什么？ |
| Layer 2 — Project Facts | `README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md`、`references.md`、当前模块/Review/Evidence | 当前 Project 实际是什么？ |
| Layer 3 — Stage Method | 从绑定 Framework 快照按任务读取的 Skill、Checklist、Workflow fragment、专项 Guide | 当前任务应该如何执行？ |

实现证据属于 Layer 2 的事实输入。绑定快照内的 Framework 文档只定义方法，不能反向覆盖 Project Facts。

## 7. Required / Conditional / Stage-enabled

### 7.1 Required — Bootstrap 必须存在

```text
AGENTS.md
FRAMEWORK.md
PROJECT_RULES.md
README.md
requirements.md
block_diagram.md
design_notes.md
references.md
docs/README.md
hardware/README.md
references/README.md
scripts/validate_project_repository.py
```

这些有职责的文件使 `docs/`、`hardware/`、`references/` 和 `scripts/` 在 Git 中可追踪。Required 文件可以处于 Draft、TBD 或待确认状态，但不得用虚构值清除未知事实。

### 7.2 Conditional — 项目实际需要时存在

- `firmware/`：项目确有固件时；
- `docs/user/`：需要用户文档时；
- 专项模块目录、合规资料、测试图片目录；
- `hardware/outputs/*`、`hardware/images/*` 和 `references/datasheets/*`：实际产生相应内容时；
- 其他由项目范围触发且职责明确的目录。

`firmware/` 不再是所有项目 Required。无固件的电源板等项目必须能通过 Project Validator。

### 7.3 Stage-enabled — 进入相关阶段时创建

| 路径 | 最早启用时机 |
| --- | --- |
| `docs/component_selection_plan.md` | Stage 2 开始关键器件候选与决策时 |
| `docs/module_design/*.md` | Stage 3 某模块进入详细设计时 |
| `docs/schematic_review.md` | Stage 4 正式原理图审查时 |
| `docs/pcb_design_rules.md` | Stage 5 Layout Preflight 前 |
| `docs/pcb_review.md` | Stage 5 记录 Layout Preflight 时，Stage 6/7 继续维护同一文件 |
| `docs/bringup_log.md` | Stage 8 准备焊接或首次上电时 |
| `docs/test_report.md` | Stage 8 开始正式测试时 |
| `docs/revision_history.md` | 确立首个硬件版本或发生重要设计变更时 |

Stage-enabled 文件不得为目录整齐而在 Bootstrap 全部预建。文件存在不证明阶段完成，文件不存在也不能反向推断当前阶段；当前阶段只取自根 `README.md`。

### 7.4 禁止无意义占位

禁止为了结构整齐创建没有职责的空目录、低信息量 README、空阶段报告或假输出。Git 无法跟踪真正空目录时，应通过有真实职责的父目录文件保留 Required 目录；Conditional 与 Stage-enabled 目录等实际启用时再创建。

## 8. Standalone Project 最小结构

```text
<project-repository>/
├─ AGENTS.md
├─ FRAMEWORK.md
├─ PROJECT_RULES.md
├─ README.md
├─ requirements.md
├─ block_diagram.md
├─ design_notes.md
├─ references.md
├─ docs/
│  └─ README.md
├─ hardware/
│  └─ README.md
├─ references/
│  └─ README.md
└─ scripts/
   └─ validate_project_repository.py
```

Conditional 与 Stage-enabled 内容不在该树中预建。正式 EDA 源通常在启用时放入 `hardware/altium_project/`；输出、图片与 datasheet 子目录按实际内容创建。

## 9. 文件唯一职责与事实源

| 文件或目录 | 唯一职责 |
| --- | --- |
| `FRAMEWORK.md` | Layer 0 binding 与初始化来源 |
| `PROJECT_RULES.md` | Layer 1 项目 Runtime Rules |
| `README.md` | 项目身份、范围摘要、唯一当前阶段、硬件版本、导航和下一步 |
| `requirements.md` | 第一版目标、不做内容、功能/电源/接口/安全/制造边界、验收标准与待确认问题 |
| `block_diagram.md` | 模块、能量流、信号流与模块边界 |
| `design_notes.md` | 整板设计意图、当前方案、Pin Map、接口与跨模块约定 |
| `references.md` | 项目资料索引、来源、用途、阅读状态与待核对项 |
| `docs/README.md` | Stage-enabled / Conditional 文档职责与导航，不维护当前阶段 |
| `hardware/README.md` | EDA 源、输出、图片及证据边界，不声称内容已产生 |
| `references/README.md` | 本地资料目录职责与来源规则 |
| `scripts/validate_project_repository.py` | Framework 唯一开发源的发布快照，用于独立验证本 Project |

同一事实只在一个主事实源维护。Checklist 不保存项目状态，Skill 不保存项目事实，Validator 不判断硬件设计正确性。

## 10. README 当前阶段字段

项目根 `README.md` 是当前阶段唯一事实源，使用一个明确字段：

```text
Current Project Stage: Bootstrap
```

或：

```text
Current Project Stage: Stage 1 — Requirements Definition
```

合法主阶段是 Stage 1～Stage 8；`Bootstrap` 是八阶段之前的容器状态，不是 Stage 0。Validator 根据该字段判断哪些 Stage-enabled 文件此时必须存在，不根据目录或文件存在反推阶段。

硬件版本独立维护为 `Hardware Revision`，不得与 Framework Release 或 Project Structure Version 混用。

## 11. Placeholder 与未知事实

- `<PROJECT_NAME>`、`<FRAMEWORK_RELEASE>`、`<FRAMEWORK_COMMIT>` 等尖括号标记是 Template placeholder，Bootstrap 必须替换，Validator 必须报告。
- `TBD`、`待确认`、`Draft` 是允许的真实未决状态，不得机械判错。
- 不得为消除 placeholder 或通过 Validator 而虚构器件、参数、EDA、ERC、DRC、Manufacturing 或 Test 结果。

## 12. Project Structure Version

`Project Structure Version: 1` 描述 Standalone Project Repository 的结构契约版本。它不是 Project 硬件版本、Framework Release、PCB Rev 或 Git tag。

只有 Required/Conditional/Stage-enabled 分类、绑定 schema、目录职责或其他结构性 Contract 发生不兼容改动时，才评估提升 Structure Version。文案修正或兼容性新增通常不提升。

## 13. Release、迁移与 Authority Cutover

Framework 发布顺序为：

```text
framework-pre-v1-migration
        ↓
hardware-project-framework-v1.0.0-rc1, rc2, ...
        ↓
hardware-project-framework-v1.0.0
```

正式 Bootstrap 从固定 Release 获取 Template，而不是复制当前 `main`。RC 后若 Required files、绑定 schema、Project `AGENTS.md`、Gate 1.5、Runtime Rules、目录职责、Structure Version 或 Validator required structure 实质变化，必须发布新 RC。

Project 继续使用其绑定版本，直到显式 migration：审查目标 release 与当前绑定差异，迁移 Project 结构/Runtime Rules/Stage Method，运行相应 Validator，记录结果，然后更新 Release + Commit；仅在结构契约变化时更新 Project Structure Version。

Authority Cutover：

```text
迁移前：Legacy Monorepo Project Directory = Current Authority
Cutover 后：Standalone Project Repository = Only Active Project Authority
          Legacy directory = Frozen Migration Source
```

Frozen Migration Source 不继续开发、不修改项目事实、只用于核对；新仓库确认完整前不删除。禁止长期双写。

## 14. Repository Architecture Migration 阶段语义

- Phase 3：Project 2 Pilot + Initial Authority Cutover。
- Phase 4：Project 3 Clean Bootstrap + Initial Authority Cutover。
- Phase 6：Formal Migration Closeout，包括 Project 2 final migration verification、Project 3 final migration verification 和 Project 1 formal standalone migration。

Phase 6 是迁移收尾，不得第二次创建或拆分 Project 2 / Project 3。

## 15. 相关权威文档

- [Framework 通用规则](../PROJECT_RULES.md)
- [Bootstrap、Gate 1.5 与八阶段 Workflow](08_Project_Workflow.md)
- [AI 上下文读取指南](AI_Context_Guide.md)
- [Template 使用指南](Project_Template_Guide.md)
- [Framework Migration Guide](Framework_Migration_Guide.md)
- [Framework Changelog](../CHANGELOG.md)
