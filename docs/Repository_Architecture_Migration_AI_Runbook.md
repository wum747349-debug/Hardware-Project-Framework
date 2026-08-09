# Repository Architecture Migration AI Runbook

> Document Status: Active during Repository Architecture Transition
> Runtime Contract: No
> Lifecycle: Retire or archive after Framework v1 closeout
> 定位：AI Operational Guide for the one-time Repository Architecture Migration

## Scope

Only read this file for Repository Architecture Migration work.

本 Runbook 只服务 Repository Architecture Transition、RC preparation、Project migration、Authority Cutover preparation、Framework Closeout、Repository Rename preparation 与 Final release preparation。普通 Project Requirements、Component Selection、Schematic、PCB、Bring-up 或 Test 任务不得默认读取本文件。本文件不复制到 Project Template 或 Standalone Project，也不是 Project Validator 输入。

## Authority / Precedence

```text
Runtime / Structural Contract
        > Migration execution documents

Migration Master Plan
        > Migration AI Runbook
```

`PROJECT_RULES.md`、`Project_Structure_Standard.md`、`08_Project_Workflow.md` 与 `AI_Context_Guide.md` 定义正常 Runtime / Structural Contract；Runbook 不能覆盖它们。Master Plan 定义一次性 migration roadmap，Runbook 只提供执行路由。Runbook 与 Master Plan 的迁移目标冲突时修 Runbook；Migration 文档与正式 Contract 冲突时以 Contract 为准，并将冲突分类报告。

## Migration Orientation

Phase 2：`CLOSED — RC1 Published / Human Review Approved`。

RC1：`hardware-project-framework-v1.0.0-rc1` @ `b36d9d399651e5c1a2b07dbc70d6e1487df57fd5`。

Phase 3 — Formal Project Migration & Authority Cutover：`ACTIVE — Human Authorized`。

Current Project：`Project 2`。

Current Step：`Project 2 Authority Cutover — COMPLETE / STOP`。

- Project 2 Hardware Stage：`Stage 1 — Requirements Definition`；
- Project 2 Stage 2：`NOT AUTHORIZED`；
- Project 2 Framework binding migration：`COMPLETED`；
- Project 2 Authority Cutover：`COMPLETED`；
- Project 2 Active Authority：`wum747349-debug/LiIon-Charger-Protection-Board`；
- Legacy Project 2：`FROZEN MIGRATION SOURCE`；
- Project 3 migration：`NOT STARTED`；
- Repository Rename：`NOT AUTHORIZED / NOT EXECUTED`。

### Project 2 Migration Milestone

- Standalone initialization pilot completed.
- Stage 1 / Gate 1.5 pilot completed.
- Framework binding migration and Authority Cutover are complete.
- The Standalone Repository is the Only Active Project Authority.
- Legacy Project 2 is retained only as a Frozen Migration Source.

本节只提供 migration orientation，不维护 Project Runtime Facts。Project 2 当前 Stage 以其根 `README.md` 为唯一权威源；当前 Framework binding 以其 `FRAMEWORK.md` 为权威源。执行任务前必须重新读取这些权威文件，不得把本 Runbook 当作 `Migration_Status.md`。

### Project 3 Phase 2 Orientation

Project 3 当前里程碑：

- Clean Bootstrap：`COMPLETE`；
- Stage 1：`COMPLETE`；
- Gate 1.5：`PASS`；
- Initialization Status：`Initialized`；
- Phase 2 clean-room objective：`COMPLETE`。

Phase 2 clean-room execution path（completed）：

```text
Bootstrap Authorization
  → Create empty Standalone Repository
  → Bootstrap from fixed immutable Framework snapshot
  → Automatic validation and Bootstrap Result Report
  → STOP for Human approval to enter Stage 1
  → Stage 1
  → Gate 1.5 checklist and validation
  → Human Gate 1.5 PASS
  → Initialization Status = Initialized
  → STOP
  → Framework Generalization / RC Readiness input
```

Phase 2 closeout：`COMPLETE`。RC1 已作为 GitHub prerelease 发布。Project 2 Framework binding migration 与 Authority Cutover 已分别获得 Human Approval 并完成；这不构成 Project 2 Stage 2 授权。Project 3 Stage 2：`NOT AUTHORIZED`；Project 3 migration：`NOT STARTED`。本次执行在 Project 2 Cutover 后停止。

本节只提供当前 migration orientation 与已完成执行路径，不是 Project 3 Runtime Facts 或 Framework binding 的权威源。执行任务前仍须从 Project 3 根 `README.md` 与 `FRAMEWORK.md` 重新核对当前 Stage、初始化状态和 binding。

## Read Routing

Repository Migration Task 的建议顺序：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/AI_Context_Guide.md`
4. 与任务直接相关的 Contract
5. `docs/Repository_Architecture_Migration_AI_Runbook.md`
6. 仅在必要时读取目标 Project 的最小 Facts / Evidence

默认不读取全部 Project、全部 datasheet、全部 EDA，也不默认读取 Master Plan。仅在用户审查整体 Migration Roadmap，Phase / RC / Final / Cutover 意图不清，Runbook 可能偏离当前 Migration Goal，或正在修改 Master Plan 本身时读取 Master Plan。Baseline 文档只在核对永久恢复点时读取。

## Classification

先分类问题，再选择权威层和修改范围：

| Issue Classification | 含义 |
| --- | --- |
| Project bug | 单个 Project 的事实、结构或实现不符合其绑定 Contract |
| Validator bug | Validator 错误实现或误判现有 Contract |
| Contract bug | Contract 内部已有明确矛盾或错误 |
| Contract gap | Contract 缺少完成当前判断所需的规则 |
| Documentation-only issue | 不改变 Contract 语义的表达、导航或链接问题 |

变更再分类为 `Compatible Sync candidate` 或 `Contract Migration`。这是 Pilot policy，不能据此自动升级真实 Project。Sync candidate 仍需显式 snapshot 与验证；Contract Migration 需要完整差异审查、Project adaptation 和受影响 Gate / Stage reassessment。Validator 只能实现 Contract 的可自动验证部分，不能反向创造 Contract，也不能要求用虚构事实换取 PASS。

## Execution Loop

1. 重新核对本地工作树、远端默认分支、HEAD、tag、CI 与目标 Project binding/authority；不把文档中的易变 SHA 当成实时事实。
2. 确定本次只属于一个 Migration Phase 或明确的跨 Phase 审查，并记录允许与禁止动作。
3. 按 Issue / Change Classification 建立最小修改集合；保护用户已有改动和 Legacy Project 内容。
4. 运行与改动相称的 Framework、Template 或 Project 验证；人工事实、EDA、ERC、DRC、制造和测试不能由 Validator 替代。
5. 汇总报告 Current Reality、修改、限制、验证与仍需用户决定的 Human approval。Routine checks 不单独触发停顿；仅在发现 blocker、Contract contradiction，或下一动作需要 Human approval 时停止。

## Human Approval Policy

Migration execution 不为每个 Validator、review、CI check、diff inspection、clean-room validation、evidence collection 或 report 分别设置 Human Gate。Automatic checks should remain automatic，并在未发现 blocker 时合并执行和报告。

只有下一动作造成实质状态、权威、binding、release 或 repository transition，或执行 destructive change / 下列明确枚举的 externally visible repository transition 时，才需要用户明确批准。包括：

- 第一次创建正式 Standalone Project Repository 并写入固定 binding 的 Bootstrap Authorization；
- Project Hardware Stage advancement；
- Gate 1.5 Human PASS 及 `Initialization Status: Gate 1.5 Pending → Initialized`；
- Authority Cutover；
- 真实 Project 的 Framework binding migration；
- RC / Final tag 与 GitHub Release；
- Repository Rename、Legacy Project deletion、history-affecting migration action 或 destructive cleanup。

当前任务已授权范围内的普通 documentation / code commit 与 push 不另设 Human Gate；它们不能被用来隐式执行上述 transition。

Bootstrap Authorization 不是新的 Hardware Gate，也不是 Stage 0。第一次写入新 Standalone Project 前，用户必须确认 fixed Framework Release + immutable Commit、Project Identity、Standalone Repository identity、适用时的 repository visibility，以及创建并 Bootstrap 该仓库的授权。Bootstrap Authorization 不授权进入 Stage 1；Bootstrap 与自动验证完成后必须报告结果并停止，等待 Stage 1 advancement approval。

未经用户明确批准，不得执行：Project Stage advancement、Authority Cutover、Legacy Project deletion、Repository Rename、RC / Final tag 或 release、真实 Project 的 Framework binding migration。也不得把 Framework `main` 变化自动同步到 Project。

Cutover 准备完成不等于 Cutover 已执行。只有用户批准且每个 Project 的迁移完整性、Facts、真实 Hardware Stage、EDA/Evidence/References/History、固定 binding、Validator 与人工核对均满足时，才能将 Standalone 标记为 Only Active Project Authority；随后 Legacy 只能是 Frozen Migration Source，禁止双写。

Stop condition：若权威 Project Facts、Framework binding、Migration Phase 意图或 Human Gate 状态与 Runbook 假设冲突，停止相应变更并报告差异，不自行推进 Stage、Cutover、Rename 或 Release。
