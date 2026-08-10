# Repository Architecture Migration AI Runbook

> Document Status: Active during Repository Architecture Transition
> Runtime Contract: No
> Lifecycle: Retire or archive after Framework v1 closeout
> 定位：AI Operational Guide for the one-time Repository Architecture Migration

## Scope

Only read this file for Repository Architecture Migration work.

本 Runbook 只服务 Repository Architecture Transition、RC preparation、Project migration、Authority Cutover preparation、Framework Closeout、Repository Rename preparation 与 Final release preparation。普通 Project Requirements、Component Selection、Schematic、PCB、Bring-up 或 Test 任务不得默认读取本文件。本文件不复制到 Project Template 或 Standalone Project，也不是 Project Validator 输入。

职责边界：Master Plan 维护 plan / status / decision model；本 Runbook 维护 execution model，包括 read-only assessment、atomic transaction、RC / Final publication、validation sequence、automatic closeout verification、STOP conditions 与 required final execution report。战略背景和长篇 rationale 不在本文件重复维护。

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

Phase 3 — Formal Project Migration & Authority Cutover：`CLOSED`。

Project 2 migration：`COMPLETE / CLOSED`。

Project 3 migration：`COMPLETE / CLOSED`。

Project 3 Authority Cutover：`COMPLETE`。

Project 1 migration：`COMPLETE / CLOSED`。

Project 1 Standalone：`Only Active Project Authority`。

Legacy Project 1：`Frozen Migration Source`。

Framework Closeout Transaction：`COMPLETE`。

Next risk boundary：`Repository Rename Approval`。

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

所有 Project Migration、RC Publication 与 Final Publication 均使用同一骨架：

```text
Assessment / Validation
        ↓
ONE Human Approval at the real risk boundary
        ↓
Atomic Transaction
        ↓
Automatic Verification
```

执行顺序：

1. Re-check live repository state：核对工作树、远端默认分支、HEAD、tag、release、CI、目标 Project binding / authority 与适用权威文件，不把文档中的易变状态当成实时事实。
2. Classify and bound：确定 Documentation-only issue、Compatible Framework Sync、Framework Contract Migration、Authority Cutover、RC publication、Final publication 或其他独立高风险动作，记录允许范围、禁止范围与 immutable candidate SHA。
3. Assess / validate read-only：完成适用的 assessment 或 candidate validation；验证本身不需要 Human Approval。
4. Decide：结果若为 `BLOCKED` / `NOT READY`，报告 blocker 并 STOP，不实施部分 transaction；ready 时只在真正风险边界请求一次 Human Approval。
5. Execute atomic transaction：只执行 assessment 中 exact bounded transaction，保护用户修改，限制文件范围，按计划排序 commit / push / publication，并保留 recovery handling。
6. Verify automatically：运行适用 Validator、CI、diff / status、binding、authority marker、tag / release identity 与 post-push remote verification。
7. Close and report：verification 全部通过后自动标记 `COMPLETE` / `CLOSED`；失败则标记 `FAILED`、STOP 并报告异常，不增加 closeout approval。

未来迁移取消重复形式化节点：不再设置独立 `Readiness STOP`、`Compatible Sync STOP`、`Cutover Assessment STOP` 或 `Closeout STOP`。这只删除 Pilot-style bureaucracy，不取消真正的高风险 Human Approval。

## Project Migration Transaction

Formal Migration Assessment 必须一次覆盖 Current Project state、当前与目标 immutable binding、classification、Standalone completeness、Legacy inventory 与事实 reconciliation、pre-cutover fixes、validator / runtime compatibility、authority readiness、exact intended transaction 和 rollback / recovery expectations；结果只能是 `READY`、`READY WITH MINOR NOTES` 或 `BLOCKED`。

`READY WITH MINOR NOTES` 仅适用于 notes 不改变 transaction scope、风险边界或 authority 判断的情况。获批后执行一个 bounded logical migration transaction；`Atomic` 不声称跨多个 Git Repository 存在 ACID atomic commit。Automatic closeout verification 必须确认预定 commits / pushes、binding、authority marker、validators、remote state 与无意外 diff；任何失败都停止关闭并进入 recovery report。

## Phase 4 Closeout Execution

Master Plan 的 read-only Assessment 为 `READY WITH MINOR NOTES`；Framework Closeout Transaction execution result 为 `COMPLETE`。Repository Rename 与 Final publication 尚未执行。Phase 4 按以下单一路径继续：

```text
Framework Closeout Transaction
        ↓
Repository Rename Transaction
        ↓
Final Candidate Validation
        ↓
ONE Human Publish Approval
        ↓
Atomic v1.0.0 Publication
        ↓
Automatic Verification
        ↓
Transition CLOSED
```

1. `Framework Closeout Transaction` 将 Master Plan 列出的 documentation、Template usability、Reference Project、Legacy current-tree、README / CHANGELOG / Guide 与 Validator / `--mode final` / CI cleanup 作为一个 bounded logical transaction 规划和验证，不为普通 cleanup 分设 Gate 或 Approval。只有实际 destructive Legacy current-tree removal 必须在执行前获得该风险边界的一次 Human Approval；保留完整 Git history，禁止 `filter-repo`、history rewrite、force push，也不要求另建完整 Legacy archive directory。
2. `Repository Rename Transaction` 在一次 Rename Approval 后执行，并完成 post-Rename identity fixes / verification。Rename 必须早于 Final Candidate SHA lock；不得自动修改 Project 1 / 2 / 3 的 `FRAMEWORK.md` 或执行 bulk Project rebinding，旧 Repository identity + RC1 SHA 继续作为合法历史 binding。Future rebinding 只能通过显式 Framework migration。
3. 完成 Rename verification 后锁定 immutable Final Candidate SHA，再执行 Final Candidate Validation。Assessment、validation 与 automatic verification 不需要 Human Approval。
4. Candidate `READY` 后只请求 `ONE Human Publish Approval`，随后执行 Atomic v1.0.0 Publication 与 Automatic Verification；不存在 Documentation、Template、Reference Project、Final Readiness、Final Technical 或 Final Closeout Approval。

当前策略为 `RC2 required: NO`，支持 `RC1 → compatible Phase 4 cleanup → Final Candidate Validation → v1.0.0`。不得因 `main` 有新 commit 自动要求 RC2。若实际实现会改变 Runtime Contract、Structural Contract、Project Structure Version、`FRAMEWORK.md` schema、Required / Conditional / Stage-enabled model、Project `AGENTS.md` routing、Hardware Stage / Gate semantics、Project facts authority、repository authority model 或 incompatible validator contract，必须 `STOP → reclassify as Contract-affecting change → reassess RC2`。

`examples/reference_project_v1/` 与 Template language cleanup 的内容边界由 Master Plan 维护；执行时必须保持 Reference Project synthetic / lightweight / validator-valid 且不复制真实 Project facts / EDA / authority，并保持中文解释优先、canonical English technical terms 与所有 schema keys、fixed field values、paths、identifiers、commands、validator-sensitive wording 不变。这些是 documentation / regression / usability compatibility work，不自行改变 Runtime / Structural Contract。

## RC Publication Execution

```text
RC Candidate Identified
        ↓
Candidate Validation
        ↓
READY / NOT READY
        ↓
ONE Human Publish Approval
        ↓
Atomic Publication
        ↓
Automatic Post-Publish Verification
        ↓
CLOSED
```

Candidate Validation 固定 candidate SHA，运行 required repository / template validation、diff checks 与适用 CI，并核对版本、tag / release identity 和 release notes scope；此步骤不设 separate Human Approval。`NOT READY` 时 STOP。`READY` 后只请求一次 Human Publish Approval，不再设置 RC Readiness、Technical、Publication 或 Closeout Approval。

Atomic Publication 只发布获批 candidate，按 transaction plan 创建并推送 tag、创建对应 GitHub prerelease，并禁止移动既有 tag 或用另一个 SHA 替换 candidate。Post-publish verification 自动核对远端 tag SHA、GitHub prerelease identity、target commit、release metadata 与 CI；全部通过后 `CLOSED`，任何失败均 STOP 并报告，不自动关闭。

RC2 / RC3 只在 Master Plan 所列 Contract / compatibility impact 触发重新 candidate validation 时评估；不得因 `main` 有新 commit 而自动创建新 RC，也不得创建单独 RC2 Gate。

## Final Publication Execution

```text
Final Candidate Validation
        ↓
ONE Human Publish Approval
        ↓
Atomic Final Publication
        ↓
Automatic Verification
        ↓
Final CLOSED
```

Final Candidate Validation 固定 immutable candidate SHA，执行 final repository / template validation、diff checks、适用 CI、documentation / identity consistency 与 release metadata review，不设独立 readiness approval。若 Phase 4 没有需要重新 candidate validation 的 Contract-affecting change，可直接验证兼容 cleanup 后的 candidate 并从 RC1 进入 Final；否则先按 Master Plan 评估 optional RC2。

Atomic Final Publication 只在一次 Human Publish Approval 后创建并推送 Final tag、创建 GitHub Final release。Automatic Verification 核对远端 tag SHA、release identity、target commit、metadata、CI 与 required closeout state；全部通过后 `Final CLOSED`，失败则 STOP、报告并保持未关闭。

## Validation, STOP and Execution Report

Validation sequence 按 `local scope / diff → required validators → candidate identity → remote branch / tag / release → applicable GitHub Actions → final status` 执行。人工事实和 EDA / ERC / DRC / 制造 / 测试证据不能由 Validator 替代。

除上述 `BLOCKED` / `NOT READY` / verification failure 外，出现 candidate SHA 漂移、未授权 scope、非 fast-forward、意外工作树修改、tag / release 冲突、认证或权限异常、Contract classification 不清、Project Facts / binding / authority 冲突时也必须 STOP；不得自行推进 Stage、Cutover、Rename 或 Release。

Required final execution report 至少包含：initial / final HEAD、candidate SHA、classification、approved transaction、实际 files / repositories / tags / releases、validation 与 Actions 结果、remote verification、Project binding / authority impact、保留的用户修改、异常与 recovery state，以及最终 `COMPLETE / CLOSED` 或 `FAILED / NOT CLOSED`。

## Human Approval Policy

长期 Human Approval Policy 以 [Framework Migration Guide](Framework_Migration_Guide.md) 为准；本 transition-only Runbook 只应用该政策，不另造 Runtime Contract。Migration execution 不为 Validator、review、CI check、diff inspection、clean-room validation、evidence collection、commit / push 或 report 分别设置 Human Gate。

- Compatible Framework Sync：`Assessment → explicit execution authorization → Transaction → Verification`；明确授权后不另设 Human Gate。
- Framework Contract Migration：`Assessment → ONE Human Approval → Contract Migration Transaction → Verification`。
- Authority Cutover：`Formal Migration Assessment → ONE Human Approval → Authority Cutover Transaction → Automatic Closeout Verification`。
- Project Hardware Stage advancement、Gate 1.5 Human PASS、RC / Final publication、Repository Rename、Legacy deletion / destructive operation：各自仅在自己的真正风险边界保留所需 Human Approval；RC / Final publication 各只有一次 Human Publish Approval。
- 当前任务已授权范围内的普通 documentation / code commit 与 push：不另设 Human Gate，但不能隐式执行上述 transition。

Bootstrap Authorization 不是 Hardware Gate，也不是 Stage 0。用户若明确要求创建新的 Standalone Hardware Project，并指定 Project / Repository identity 与固定 Framework Release + immutable Commit，该请求本身就是 Bootstrap execution authorization；适用时仍应先确认 repository visibility 等不可推断输入。正常流程为 `User request → Bootstrap → Validator → Bootstrap Result Report → STOP before Hardware Stage advancement`，无需制造第二个 Bootstrap Human Gate。进入 Stage 1 仍按 Project Stage advancement policy 处理。

Cutover 准备完成不等于 Cutover 已执行。只有用户一次批准且每个 Project 的迁移完整性、Facts、真实 Hardware Stage、EDA/Evidence/References/History、固定 binding、Validator 与人工核对均满足时，才能将 Standalone 标记为 Only Active Project Authority；随后 Legacy 只能是 Frozen Migration Source，禁止双写。

Framework v1 closeout 后，本 Runbook 应 retire / archive；Master Plan 成为 Historical Engineering Record。该 lifecycle disposition 不要求为了物理 archive 再建立 post-Final approval 或 post-Final commit。长期正常 Framework change management 只使用 Compatible Framework Sync 或 Framework Contract Migration，不继承本次 Repository Transition 的 Phase、Pilot 或 Closeout bureaucracy。

Stop condition：若权威 Project Facts、Framework binding、Migration Phase 意图或 Human Gate 状态与 Runbook 假设冲突，或 classification 不明确，停止相应变更并报告差异，不自行推进 Stage、Cutover、Rename 或 Release。
