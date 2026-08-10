# Repository Architecture Migration Master Plan

> Document Status: Active Migration Roadmap
> Audience: Human-facing Repository Architecture Migration Roadmap
> Runtime Contract: No
> Lifecycle: Becomes a Historical Engineering Record after Framework v1 closeout

## 1. Purpose and boundary

本计划用于把 Legacy Monorepo 收敛为一个 Framework Repository 与多个 Standalone Project Repository。核心不是移动目录，而是分离方法与项目事实，让每个真实 Project 只有一个活动权威源，并以可恢复、可核对的方式完成发布和 Cutover。

一次性 Migration Planning 与正常 Runtime Contract 相互独立：

```text
Runtime Contract                     Migration Engineering
        ↓                                    ↓
PROJECT_RULES.md                     Master Plan
  ↓                                    ↓
Structure + Workflow + AI Context    AI Runbook
  ↓
Template / Skill / Checklist
  ↓
Validator → Fixture
```

本计划不复制 binding schema、八阶段细节、Skill 或 Validator 实现；不进入 Project Template，不定义 Project Hardware Stage，也不成为 Project Facts 的权威源。正式 Contract 仍以 `PROJECT_RULES.md`、`Project_Structure_Standard.md`、`08_Project_Workflow.md` 与 `AI_Context_Guide.md` 为准。

## 2. Current and target architecture

当前 GitHub Repository 仍是 `wum747349-debug/Hardware-Practice-Projects`，处于 Repository Architecture Transition。目标名称是 `Hardware-Project-Framework`，但 GitHub 实际 Rename 前，文档、链接和 binding 必须继续使用真实身份。

```text
Current: Legacy Monorepo
├─ Framework candidate content
└─ projects/ (Legacy Migration Sources)

Target:
Framework Repository
└─ Contract / Template / Skill / Checklist / Validator / Fixture

Standalone Project Repositories
└─ each Project's facts / EDA / evidence / history
```

Framework 只定义方法。正式 Project 锁定固定 Release + immutable 40 位 Commit SHA，不自动跟随 `main`。每个 Project 的 Cutover 独立批准；Cutover 前 Legacy Directory 是 Current Authority，之后 Standalone Repository 是 Only Active Project Authority，Legacy 只作 Frozen Migration Source，禁止长期双写。

## 3. Starting Point — Historical Completed Work

- Baseline Freeze：`framework-pre-v1-migration` 永久恢复点，指向 `3e9d4801bdd5768f8edc0e14e8f01bf278721e54`；
- Framework v0.9 Executable Candidate：Contract、Template、初始化方法、Validator 与 CI 已可执行，但不是 RC 或 Final；
- Project 2 已完成 Standalone Bootstrap、Stage 1 与 Gate 1.5 Pilot；
- Project 2 仍为 Stage 1，Legacy 仍是 Current Authority，尚未 Cutover，也未获 Stage 2 授权。

这些里程碑不再沿用旧 Phase 0～8 作为未来主线。Git HEAD、Project binding 与 Hardware Stage 继续由 Git、Project `FRAMEWORK.md` 和根 `README.md` 维护。

### Current Migration Status

- Phase 1 — Pilot Stabilization：`CLOSED — Human Review Approved`；
- Phase 2 — Clean Bootstrap & RC Readiness：`CLOSED — RC1 Published / Human Review Approved`；
- Phase 2 Preconditions Review：`PASS`；
- Project 2：Bootstrap / Stage 1 / Gate 1.5 Pilot、Framework binding migration 与 Authority Cutover 均已完成；Standalone Repository 是 Only Active Project Authority；
- Project 3：Clean Bootstrap 已完成，Stage 1 Requirements Definition 已完成，Gate 1.5 Human Review 与 Technical Closeout 均已 PASS，`Initialization Status: Initialized`；仍处于 Stage 1，Stage 2 未获授权；
- Phase 2 clean-room objective：`COMPLETE`；
- RC1：`hardware-project-framework-v1.0.0-rc1` @ `b36d9d399651e5c1a2b07dbc70d6e1487df57fd5`；
- Phase 3 — Formal Project Migration & Authority Cutover：`ACTIVE`；
- Project 2 migration：`COMPLETE / CLOSED`；
- Next migration subject：`Project 3`；
- Next allowed activity：`Project 3 Formal Migration Readiness Review — READ ONLY`；
- Project 2 Hardware Stage：`Stage 1 — Requirements Definition`；
- Project 2 Stage 2：`NOT AUTHORIZED`；
- Project 2 Framework binding migration：`COMPLETED`；
- Project 2 Authority Cutover：`COMPLETED`；
- Project 2 Active Authority：`wum747349-debug/LiIon-Charger-Protection-Board`；
- Legacy Project 2：`FROZEN MIGRATION SOURCE`；
- Project 3 migration：`NOT STARTED`；
- Project 3 Framework Binding Migration / Authority Cutover：`NOT AUTHORIZED / NOT EXECUTED`；
- Repository Rename：`NOT AUTHORIZED / NOT EXECUTED`。

Project 3 的 clean-room 结果证明 Framework 能在不依赖 Legacy Project 3、Project 1、Project 2 或本地 Framework 路径的情况下完成 Bootstrap → Stage 1 → Gate 1.5 → Initialized。Project 3 继续绑定其显式选择的 immutable Framework snapshot；Framework `main` 或当前 HEAD 的后续变化不构成 Project 3 binding change。

RC1 tag 与 GitHub prerelease 已发布，Phase 2 已完成 Human Review 并关闭。Phase 3 中 Project 2 Framework binding migration 与 Authority Cutover 已分别获得 Human Approval 并完成，Project 2 migration 已 `COMPLETE / CLOSED`；Project 2 Stage 2 仍未授权。下一个迁移对象是 Project 3，但当前只允许执行 `Project 3 Formal Migration Readiness Review — READ ONLY`；这不构成开始 Project 3 migration、执行 Framework Binding Migration 或 Authority Cutover、推进 Stage 2 的授权。Repository Rename 仍未授权或执行。

Migration 的 routine validation、CI、diff inspection、technical review 与 evidence collection 默认自动执行并合并报告。Compatible Framework Sync 在用户已明确要求后不另设 Human Gate；Framework Contract Migration、Authority Cutover、Stage / Gate 状态变化、release、repository identity transition 与 destructive change 按 [Framework Migration Guide](Framework_Migration_Guide.md) 保留各自的一次或必要 Human Approval。当前任务已授权范围内的普通 commit 与 push 不另设 Human Gate。

## 4. Four active phases

### Phase 1 — Pilot Stabilization

Goal：用 Project 2 的真实 Pilot 反馈收敛 Contract、Template、Skill、Checklist、Validator、AI Context 与 Migration boundary。

Actions：问题先分类为 `Project bug`、`Validator bug`、`Contract bug`、`Contract gap` 或 `Documentation-only issue`，再按权威层级修复；不得因 Validator 当前实现直接修改 Contract。

Outputs / Done：Pilot 问题已归类处置，Framework、Template 与 smoke fixture 通过验证，无已知阻断性架构矛盾，也不要求 Project 虚构事实才能 PASS。本 Phase 不要求 Project 2 进入 Stage 2。

#### Conditional Pilot Cutover

Project 2 不需要进入 Stage 2 才能满足 Framework RC readiness。若 Project 2 在 Framework RC 前确需开始真实 Stage 2 工作，可在 Phase 1 单独审查并执行 Pilot Authority Cutover；该 Cutover 必须满足正常 Authority 完整性检查并获得用户明确批准，且不代表 Framework RC 或 Final 已发布。

因此 `Project 2 Stage 2 ≠ RC Entry Requirement`；但 Standalone Project 2 开始真实 Stage 2 前必须先解决唯一 Authority，不能让 Legacy 保持 Current Authority 的同时在 Standalone 中进行新的硬件设计。

### Phase 2 — Clean Bootstrap & RC Readiness

Goal：用 Project 3 完成 Clean Bootstrap、Stage 1、Gate 1.5，证明 Framework 不依赖 Legacy monorepo、Project 1、Project 2 特例或本地 Framework 路径。

Actions：从明确 snapshot 初始化 Project 3；按 Contract 建立最小事实入口并执行 Gate；Framework 继续用 temporary fixture / smoke test 验证 Template。

Outputs / Done：Project 3 Clean Bootstrap / Stage 1 / Gate 1.5 已通过并完成初始化，Framework Generalization / RC Readiness Review 已通过，`hardware-project-framework-v1.0.0-rc1` 已发布，Phase 2 已关闭。Project 3 不需为 RC 强行进入后续 Hardware Stage。

### Phase 3 — Formal Project Migration & Authority Cutover

Goal：按 Project 2、Project 3、Project 1 顺序，逐个完成正式迁移验证与 Cutover。

Actions：每个 Project 独立核对 Standalone 内容、Project Facts、真实 Hardware Stage、EDA / Evidence / References / History、固定 Framework binding、Project Validator、人工迁移检查，并取得用户明确批准。

若 Project 2 已在 Phase 1 完成获批的 Pilot Authority Cutover，本 Phase 对 Project 2 只执行 final migration verification、binding verification 与 closeout review，不执行第二次 Cutover。

Outputs / Done：三个 Project 分别完成权威收敛；Standalone 成为各自 Only Active Project Authority，Legacy 冻结；没有双写、事实改变或伪造阶段推进。

Project 2 不需要为了 RC 进入 Stage 2。但若未来要在 Standalone Repository 真正开展 Stage 2，应先明确 Authority Cutover，避免形成两个活动事实源。

### Phase 4 — Framework Closeout & v1 Final

Goal：完成 Transition Repository 到正式 Framework Repository 的收尾。

Actions：确认三个 Project 权威收敛；从 current tree 移除真实 Project 活动副本但保留 Git history；建立轻量 `examples/reference_project_v1/`；收尾 README、CHANGELOG 与 Migration Guide；按文档治理分类与获批处置清理 Transition-only 低价值内容；执行获批的 GitHub Rename 并修复身份与链接；验证 Template、Fixture、Validator 与 CI。

#### Documentation Inventory & Rationalization

Framework v1 Final 前对 legacy / transition-era 文档执行：

```text
Inventory → Classification → Disposition → Rationalization
```

每个文档先分类为 `Contract`、`Guide`、`Stage Method / Checklist`、`Transition Historical Record` 或 `Legacy Project / Portfolio Material`，再选择 `keep`、`merge`、`move`、`archive`、`retire` 或 `delete` disposition。分类与决策必须先于删除；不得仅为了让仓库看起来整齐而直接删除文件。

初始审查候选（initial review candidates）为：

- `docs/00_Project_Roadmap.md`；
- `docs/01_Toolchain_Setup.md`；
- `docs/02_Altium_Design_Rules.md`；
- `docs/03_Component_Selection_Rules.md`；
- `docs/04_PCB_Review_Checklist.md`；
- `docs/05_Bringup_Test_Checklist.md`；
- `docs/06_Debug_Record_Template.md`；
- `docs/07_Resume_Project_Notes.md`。

这些文件只是待审查候选，不是预先确定的删除清单。审查应识别重复职责、已被新 Contract / Guide / Skill / Checklist 替代的内容、transition-only wording、Legacy Monorepo assumption、三个具体 Project / portfolio assumption、应进入 Stage Method / Skill / Checklist 的长期工程方法，以及已无长期价值的历史说明。`docs/00_Project_Roadmap.md` 和 `docs/07_Resume_Project_Notes.md` 应作为 `Legacy Project / Portfolio Material` 的重点候选进行审查，但不预判最终 disposition。

Phase 4 前可以进行 inventory、read-only classification 和 planning。Project 2、Project 3 与 Project 1 migration 期间，不得仅为仓库整洁而提前执行旧文档 destructive cleanup。实际 `move`、`merge`、`archive`、`retire` 或 `delete` 只在三个真实 Project 全部完成 Authority Cutover 后的 Phase 4 中，依照审查结论与所需 Human Approval 执行。

Outputs / Done：Repository identity、current tree、文档、Template、Fixture、Validator 与 CI 一致，用户批准并实际发布 `hardware-project-framework-v1.0.0`。Rename 只在此阶段且真实 GitHub 操作获批后执行，不能由文档提前假定。

Repository Rename 是 Framework Repository identity transition，不只是 GitHub UI 或 README 改名。Phase 4 负责新仓库身份、内部与文档链接及 release identity 的一致性；真实 Project 不得仅因仓库改名而静默重写 `FRAMEWORK.md`。Project 必须在适用的 binding update 中显式选择 Framework release + immutable commit，并一并采用 Rename 后的 Framework Repository identity。`Repository Rename ≠ automatic Project Framework migration`。

## 5. Framework change management after the pilot

Project 2 pilot 已将长期 Framework change management 收敛为 `Compatible Framework Sync` 与 `Framework Contract Migration`。分类边界、执行流程与 Human Approval Policy 由 [Framework Migration Guide](Framework_Migration_Guide.md) 维护；本一次性 Master Plan 不重复定义或覆盖该长期治理。

Repository Architecture Transition 自身的 Authority Cutover、Repository Rename、Legacy deletion 与 RC / Final publication 仍按各自 Human Gate 执行。Transition closeout 后，本 Master Plan 成为 Historical Engineering Record，AI Runbook retire / archive；长期 Framework change management 不继承本计划的 Phase、Pilot 或 Closeout bureaucracy。Framework `main` 变化始终不等于 Project 自动变化。

## 6. RC strategy

RC 是 Release Candidate，位置固定为：

```text
development / v0.9
  → Project 2 Pilot Stabilization
  → Project 3 Clean Bootstrap
  → RC Readiness Review
  → hardware-project-framework-v1.0.0-rc1
  → Formal Migration / Authority Cutover
  → Framework Closeout
  → hardware-project-framework-v1.0.0
```

RC Entry Criteria：Contract 无已知阻断性矛盾；Project 2 已完成 Bootstrap / Stage 1 / Gate 1.5 Pilot；Project 3 Clean Bootstrap / Stage 1 / Gate 1.5 通过；Template 不依赖 Legacy monorepo；Project 与 Framework Validator 基本实现 Contract；Framework CI 通过；Validator 不迫使 Project 虚构事实；Clean-room 未暴露 Project-specific hidden dependency；剩余工作不会再改变 RC Project Contract。

RC 后若实质修改 Contract，必须 `rc1 → Contract change → rc2 → revalidation`，不得继续宣称旧 RC 已验证。

## 7. Final Done Criteria

迁移完成意味着：三个 Project 各自只有一个活动权威仓库；Legacy current tree 不再承载活动副本但历史可追溯；Framework 只保留方法、Contract、Template、工具与 Reference/Test Fixture；正式 Project 使用固定 Release + SHA；Rename 已真实完成且引用已修复；v1 Final 的验证、CI、tag 与 release 均获用户批准并实际完成。
