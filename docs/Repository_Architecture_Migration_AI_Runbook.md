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

Phase 3 — Formal Project Migration & Authority Cutover：`ACTIVE`。

Project 2 migration：`COMPLETE / CLOSED`。

Project 3 migration：`COMPLETE / CLOSED`。

Project 3 Authority Cutover：`COMPLETE`。

Next migration subject：`Project 1`。

本节只提供最小 migration orientation。Runbook 是 `AI decision router + transaction executor`，不是第二份动态 Migration Status database。执行任务前必须从真实 GitHub 默认分支、目标 Project 根 `README.md`、`FRAMEWORK.md` 与适用 authority marker 重新核对 HEAD、Stage、initialization、binding 和 authority；Project 3 的实时值不在本 Runbook 重复维护。

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

Framework binding update 必须按 [Framework Migration Guide](Framework_Migration_Guide.md) 分类为 `Compatible Framework Sync` 或 `Framework Contract Migration`，不能据此自动升级真实 Project。Compatible Sync 需要固定 snapshot、impact check 与验证，但用户已明确要求执行时不另设 Human Gate；Contract Migration 需要完整差异审查、Project adaptation、受影响 Gate / Stage reassessment 与一次 Human Approval。Validator 只能实现 Contract 的可自动验证部分，不能反向创造 Contract，也不能要求用虚构事实换取 PASS。

## Execution Route

1. Re-check live repository state：核对工作树、远端默认分支、HEAD、tag、CI、目标 Project binding / authority 与适用权威文件，不把文档中的易变状态当成实时事实。
2. Determine migration classification：区分 Compatible Framework Sync、Framework Contract Migration、Authority Cutover 或其他独立高风险动作，并锁定允许与禁止范围。
3. Run ONE Formal Migration Assessment：一次覆盖 Current Project state、当前与目标 binding、classification、Standalone completeness、Legacy inventory 与事实 reconciliation、pre-cutover fixes、validator / runtime compatibility、authority readiness、exact intended transaction 和 rollback / recovery expectations；结果为 `READY`、`READY WITH MINOR NOTES` 或 `BLOCKED`。
4. If `BLOCKED`：报告 blocker 并停止，不实施部分迁移。
5. If ready and the classified next action requires Human Approval：报告 assessment，并且只停止一次。
6. After approval：执行 assessment 中 exact bounded migration transaction，保护用户修改，限制文件范围，按计划排序 commit / push，并在失败时执行 recovery handling。
7. Run automatic verification：运行适用 Validator、CI、diff / status、binding、authority marker 与 post-push remote verification；人工事实和 EDA / ERC / DRC / 制造 / 测试证据仍不能由 Validator 替代。
8. Report `COMPLETE` / `FAILED`：合并报告 Current Reality、执行内容、验证、限制和恢复状态；automatic closeout verification 不设置新的 Human Approval。

未来迁移取消重复形式化节点：不再设置独立 `Readiness STOP`、`Compatible Sync STOP`、`Cutover Assessment STOP` 或 `Closeout STOP`。这只删除 Pilot-style bureaucracy，不取消真正的高风险 Human Approval。

## Human Approval Policy

长期 Human Approval Policy 以 [Framework Migration Guide](Framework_Migration_Guide.md) 为准；本 transition-only Runbook 只应用该政策，不另造 Runtime Contract。Migration execution 不为 Validator、review、CI check、diff inspection、clean-room validation、evidence collection、commit / push 或 report 分别设置 Human Gate。

- Compatible Framework Sync：`Assessment → explicit execution authorization → Transaction → Verification`；明确授权后不另设 Human Gate。
- Framework Contract Migration：`Assessment → ONE Human Approval → Contract Migration Transaction → Verification`。
- Authority Cutover：`Formal Migration Assessment → ONE Human Approval → Authority Cutover Transaction → Automatic Closeout Verification`。
- Project Hardware Stage advancement、Gate 1.5 Human PASS、RC / Final publication、Repository Rename、Legacy deletion / destructive operation：各自保留所需 Human Approval。
- 当前任务已授权范围内的普通 documentation / code commit 与 push：不另设 Human Gate，但不能隐式执行上述 transition。

Bootstrap Authorization 不是 Hardware Gate，也不是 Stage 0。用户若明确要求创建新的 Standalone Hardware Project，并指定 Project / Repository identity 与固定 Framework Release + immutable Commit，该请求本身就是 Bootstrap execution authorization；适用时仍应先确认 repository visibility 等不可推断输入。正常流程为 `User request → Bootstrap → Validator → Bootstrap Result Report → STOP before Hardware Stage advancement`，无需制造第二个 Bootstrap Human Gate。进入 Stage 1 仍按 Project Stage advancement policy 处理。

Cutover 准备完成不等于 Cutover 已执行。只有用户一次批准且每个 Project 的迁移完整性、Facts、真实 Hardware Stage、EDA/Evidence/References/History、固定 binding、Validator 与人工核对均满足时，才能将 Standalone 标记为 Only Active Project Authority；随后 Legacy 只能是 Frozen Migration Source，禁止双写。

Framework v1 closeout 后，本 Runbook 应 retire / archive；Master Plan 成为 Historical Engineering Record。长期正常 Framework change management 只使用 Compatible Framework Sync 或 Framework Contract Migration，不继承本次 Repository Transition 的 Phase bureaucracy。

Stop condition：若权威 Project Facts、Framework binding、Migration Phase 意图或 Human Gate 状态与 Runbook 假设冲突，或 classification 不明确，停止相应变更并报告差异，不自行推进 Stage、Cutover、Rename 或 Release。
