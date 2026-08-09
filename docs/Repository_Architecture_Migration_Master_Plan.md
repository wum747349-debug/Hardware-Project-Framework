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
- Current Active Phase：`Phase 2 — Clean Bootstrap & RC Readiness`；
- Phase 2 Preconditions Review：`PASS`；
- Current Phase 2 Step：Bootstrap Authorization；
- Project 2：Bootstrap / Stage 1 / Gate 1.5 Pilot 已完成；Authority Cutover 尚未执行，Legacy Project 2 仍是 Current Authority；
- Project 3：Clean Bootstrap 尚未执行，也未发生任何 Project 3 Hardware Stage advancement。

Phase 2 必须在 Project 3 初始化前显式选择 immutable Framework snapshot；Proposed Framework Snapshot 不等于 Adopted Project 3 Framework Snapshot，Framework `main` 或当前 HEAD 均不得被自动视为 Project 3 binding。本状态不表示 Project 3 已初始化、Gate 1.5 已通过、RC readiness 已通过或 RC 已发布。

Migration 的 routine validation、CI、diff inspection、technical review 与 evidence collection 默认自动执行并合并报告；只有实质状态、权威、binding、release、repository identity transition，或 destructive change / 明确枚举的 externally visible repository transition 才需要 Human approval。当前任务已授权范围内的普通 commit 与 push 不另设 Human Gate。

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

Outputs / Done：Project 3 Clean Bootstrap / Stage 1 / Gate 1.5 通过，Framework CI 通过并形成 RC Readiness Review 输入。Project 3 不需为 RC 强行进入后续 Hardware Stage。

### Phase 3 — Formal Project Migration & Authority Cutover

Goal：按 Project 2、Project 3、Project 1 顺序，逐个完成正式迁移验证与 Cutover。

Actions：每个 Project 独立核对 Standalone 内容、Project Facts、真实 Hardware Stage、EDA / Evidence / References / History、固定 Framework binding、Project Validator、人工迁移检查，并取得用户明确批准。

若 Project 2 已在 Phase 1 完成获批的 Pilot Authority Cutover，本 Phase 对 Project 2 只执行 final migration verification、binding verification 与 closeout review，不执行第二次 Cutover。

Outputs / Done：三个 Project 分别完成权威收敛；Standalone 成为各自 Only Active Project Authority，Legacy 冻结；没有双写、事实改变或伪造阶段推进。

Project 2 不需要为了 RC 进入 Stage 2。但若未来要在 Standalone Repository 真正开展 Stage 2，应先明确 Authority Cutover，避免形成两个活动事实源。

### Phase 4 — Framework Closeout & v1 Final

Goal：完成 Transition Repository 到正式 Framework Repository 的收尾。

Actions：确认三个 Project 权威收敛；从 current tree 移除真实 Project 活动副本但保留 Git history；建立轻量 `examples/reference_project_v1/`；收尾 README、CHANGELOG 与 Migration Guide；清理 Transition-only 低价值内容；执行获批的 GitHub Rename 并修复身份与链接；验证 Template、Fixture、Validator 与 CI。

Outputs / Done：Repository identity、current tree、文档、Template、Fixture、Validator 与 CI 一致，用户批准并实际发布 `hardware-project-framework-v1.0.0`。Rename 只在此阶段且真实 GitHub 操作获批后执行，不能由文档提前假定。

Repository Rename 是 Framework Repository identity transition，不只是 GitHub UI 或 README 改名。Phase 4 负责新仓库身份、内部与文档链接及 release identity 的一致性；真实 Project 不得仅因仓库改名而静默重写 `FRAMEWORK.md`。Project 必须在适用的 binding update 中显式选择 Framework release + immutable commit，并一并采用 Rename 后的 Framework Repository identity。`Repository Rename ≠ automatic Project Framework migration`。

## 5. Framework change-management candidate

以下仅为 **Pilot Change-Management Policy / Candidate Design — Not yet a standalone Project Runtime Contract**。

| Class | Examples | Required handling |
| --- | --- | --- |
| Framework Sync | Validator bug/误判修复，Skill/Checklist 澄清，文档或链接修正，不改变 Runtime Contract 的兼容工具增强 | 显式执行；指定 snapshot；运行必要验证；不自动跟随 `main`。 |
| Framework Migration | Required/Conditional/Stage-enabled、`FRAMEWORK.md` schema、Runtime Rules、Gate/Stage lifecycle、Structure Version 或文件职责变化 | 完整差异审查、Project adaptation、受影响 Gate/Stage reassessment，并显式更新 binding。 |

Framework `main` 变化绝不等于 Project 自动变化。是否将 Sync 固化为长期 Contract，留待独立审查。

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

RC Entry Criteria：Contract 无已知阻断性矛盾；Project 2 已完成 Bootstrap / Stage 1 / Gate 1.5 Pilot；Project 3 Clean Bootstrap / Stage 1 / Gate 1.5 通过；Template 不依赖 Legacy monorepo；Project 与 Framework Validator 基本实现 Contract；Framework CI 通过；Validator 不迫使 Project 虚构事实；剩余工作不会再改变 RC Project Contract。

RC 后若实质修改 Contract，必须 `rc1 → Contract change → rc2 → revalidation`，不得继续宣称旧 RC 已验证。

## 7. Final Done Criteria

迁移完成意味着：三个 Project 各自只有一个活动权威仓库；Legacy current tree 不再承载活动副本但历史可追溯；Framework 只保留方法、Contract、Template、工具与 Reference/Test Fixture；正式 Project 使用固定 Release + SHA；Rename 已真实完成且引用已修复；v1 Final 的验证、CI、tag 与 release 均获用户批准并实际完成。
