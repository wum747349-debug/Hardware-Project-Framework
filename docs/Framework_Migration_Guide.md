# Framework Migration Guide

> 职责：Project-side adoption of an immutable Framework Release，以及低频 Authority Cutover exception procedure
>
> 不负责：Framework Repository 自身的 maintenance、Semantic Versioning、RC 或 Release publication

Framework 维护与发布读取 [Framework Maintenance and Release Guide](Framework_Maintenance_and_Release_Guide.md)。若 breaking Framework release 需要由既有 Project 采用，应同时读取两份 Guide：Release Guide 负责“Framework publishes a version”，本 Guide 负责“Project decides whether and how to adopt that version”。

Binding、Structure Version 与 Authority Contract 以 [Project Structure Standard](Project_Structure_Standard.md) 为准；Stage、Gate 与回退影响以 [Workflow](08_Project_Workflow.md) 为准。一次性 Repository Architecture Migration 的 Phase、Pilot、RC、Closeout 历史不属于本指南的长期 Project adoption flow。

## 1. 共同边界：不自动升级

Project 继续使用 `FRAMEWORK.md` 绑定的 Release + Commit。Framework `main`、新 RC 或新 Final 的出现不会自动改变 Project Runtime Rules、Structure、Stage Method 或 binding。任何 Evaluation / Sync / Migration 都必须源于明确用户任务，选择目标固定 identity + immutable full Commit SHA，并在验证通过后才更新 binding。

禁止只修改版本字段而不核对实际差异，也禁止让 Project 同时依赖两个 Framework 版本。`No separate Human Approval gate` 只表示明确的用户执行请求已经构成授权，不允许 AI 主动升级 Project。

Project-side adoption 的共同模型压缩为：

```text
Assess
  → Execute when authorized
  → Verify
```

其中 Pinned Framework Evaluation 与 Compatible Framework Sync 在用户明确请求后不设置 separate Human Approval；Framework Contract Migration 与 Authority Cutover 各自保留 ONE Human Approval。Validation、review、CI 与 diff inspection 只输出 `PASS / FAIL` 或 `READY / NOT READY`，不是 Human Gate。执行仍是有边界、可恢复的 logical transaction，不声称多个 Git Repository 之间存在 ACID atomic commit。

## 2. Pinned Framework Evaluation

Pinned Framework Evaluation 是显式的 prerelease / development evaluation，固定为一个 `development-vX.Y.Z` identity + immutable full Commit SHA：

```text
Assess
  → pin development snapshot
  → use in real Project
  → Verify
```

用户明确要求某 Project 使用指定 development SHA 做 evaluation 时，该请求已经构成执行授权，不再设置 separate Human Approval Gate。Framework 后续修订时，Project 仍停留在旧 evaluation SHA；只有显式请求才能 repin 到新 SHA，禁止自动跟随 moving `main`。

Pinned Framework Evaluation 不是新 Stage、不是新 Gate、不是 RC、不是 Authority Cutover，也不是 Framework Contract Migration。它不新增 `FRAMEWORK.md` 字段、不创建第二 binding source；Project 始终只有一个 active Layer-0 binding。验证失败时保持或恢复原 binding，并输出 `FAIL` 或 `NOT READY`。

Existing Project 进入 Pinned Framework Evaluation 时，只更新 current binding 的 `Framework Release`、`Framework Commit`，必要时更新 `Framework Repository` identity；不得重置 `Initialization Framework Release` 或 `Initialization Status`。`Development Bootstrap` 只适用于真正以 development binding 首次 Bootstrap 的 Project，不适用于 Existing Project 的后续 evaluation。

## 3. Compatible Framework Sync

Compatible Sync 可包括 Validator bug / false-positive fix、文档澄清、Skill / Checklist 澄清、链接修正、CI 改进和兼容工具增强。只有以下语义全部保持不变时才能采用此分类：

- Project Structure Version；
- `FRAMEWORK.md` schema；
- Project `AGENTS.md` context-routing contract；
- Required / Conditional / Stage-enabled 模型；
- Runtime Rules；
- Stage model 与 Gate semantics；
- Project fact authority / responsibility；
- Repository authority model；
- Validator required structure。

执行模型：

```text
Assess
  → Execute when authorized
  → Verify
```

Transaction 包含以下步骤：

1. 选择目标固定 Framework Release + immutable Commit；
2. 执行 compatibility / impact check，并记录为何不改变上述 Contract 语义；
3. 在 working tree 准备并应用 bounded intended changes：目标 `FRAMEWORK.md` current binding、必要的 `scripts/validate_project_repository.py` 发布快照，以及仅有的必要 compatible Project adaptations；
4. 对最终计划提交的 binding + files 组合运行 Project Validator 与受影响检查；
5. 核对 final intended diff 后提交、推送；
6. 验证 remote commit / repository state 并报告结果。

用户已明确要求执行该 Sync 时，不再设置 Readiness Gate、Sync Gate 或 Closeout Gate。若发现 blocker、Contract contradiction 或分类不明确，保持原 binding 并停止报告。

### 3.1 Same-SHA Formalization fast path

当 Project 当前绑定 `development-vX.Y.Z @ SHA-X`，Framework 后续发布 `hardware-project-framework-vX.Y.Z @ SAME SHA-X` 时，只需执行 Same-SHA Formalization：

1. 验证 published release tag 精确指向 `SHA-X`；
2. 验证 Project 已经使用同一 `SHA-X`；
3. 只把 `Framework Release` 更新为正式 release identifier，保持 `Framework Commit` 不变；
4. 对上述 final intended binding + files 组合运行 Project Validator；
5. 核对 diff 后提交、推送；
6. 验证 remote commit / repository state 并报告 `DONE`。

该 fast path 不重做完整 old → new capability review、Project migration、Stage replay、dogfooding replay 或 Authority Cutover。若 Final Release SHA 与 evaluation SHA 不同，则检查 evaluation SHA → final SHA 的实际 diff，只重新验证受影响范围，再按普通 Compatible Framework Sync 更新 binding。

## 4. Framework Contract Migration

发生以下任一实质变化时，必须分类为 Framework Contract Migration：`FRAMEWORK.md` schema、Project Structure Version、Required / Conditional / Stage-enabled 分类、Runtime Rules、Stage / Gate lifecycle、Project 文件职责或事实权威、Project `AGENTS.md` context-routing contract、Validator required structure，或其他不向后兼容的 Runtime / Structural Contract。

执行模型：

```text
Assessment
  → ONE Human Approval
  → Contract Migration Transaction
  → Verification
```

具体步骤：

1. Migration Assessment：建立 old → new Contract diff、impact analysis、受影响 Project 文件、受影响 Stage / Gate、validation 与 rollback plan；
2. 报告 assessment 并取得一次 Human Approval；
3. 在可恢复工作区执行 Migration Transaction，保留 Project facts、EDA 源、Evidence 与 Git history，不复制 Template / Reference / 其他 Project facts；
4. 同步目标 validator snapshot，更新所需 Project 结构、Runtime Rules 与 Stage Method；
5. 更新 binding，并只在结构契约变化时更新 Project Structure Version；
6. 运行 Validator 与受影响 Gate / checklist；失败时按 rollback plan 保持或恢复一致 binding，不留下部分切换；
7. 提交、推送并给出 Final Report。

`One Contract Migration = One Human Approval Gate`。Framework Contract Migration 改变 Runtime / Structural Contract 适配边界；Authority Cutover 改变唯一活动 Project authority，两者是不同风险边界。如果同一 Project 同时需要两者，不得机械合并为一次批准：先按已批准的 Contract Migration transaction 完成并验证，再对 Authority Cutover 的独立 assessment 与 transaction 取得一次批准。Stage advancement、Repository Rename、Legacy deletion 或 Release publication 同样按各自 Human Gate 处理。

## 5. Structure Version Change

Structure Version 变化属于 Framework Contract Migration，必须建立旧路径到新职责的映射，确认 Required / Conditional / Stage-enabled 分类、事实源和相对链接。Hardware Revision 不因 Framework Structure 变化自动提升；只有硬件设计实际改变时才按 Project 规则处理。

## 6. Legacy Project Authority Cutover

Authority Cutover 改变唯一活动事实源，因此采用：

```text
Formal Migration Assessment
  → ONE Human Approval
  → Authority Cutover Transaction
  → Automatic Closeout Verification
```

Formal Migration Assessment 一次完成只读 completeness、integrity、binding、Standalone / Legacy fact reconciliation、validator / runtime compatibility、authority readiness、exact intended transaction 与 rollback / recovery checks，并给出 `READY`、`READY WITH MINOR NOTES` 或 `BLOCKED`。Ready 后取得一次 Human Approval，再执行 Standalone authority marker、Legacy freeze marker、migration docs sync、ordered commit / push；随后自动执行 validation、remote authority verification 与 Closeout Report。

Cutover 前 Legacy Monorepo Project Directory 是 Current Authority；Cutover 后 Standalone Project Repository 是 Only Active Project Authority，Legacy 目录是 Frozen Migration Source。Frozen source 不继续开发、不修改项目事实、只用于核对；新仓库确认完整前不删除。禁止长期双写。Closeout Review 是执行后的 verification / report，不是新的 Human Approval Gate。

## 7. Human Approval Policy

| Action | Human Approval |
| --- | --- |
| Routine docs / validator / tooling fix | No separate gate |
| Pinned Framework Evaluation | No separate gate once explicitly requested |
| Compatible Framework Sync | No separate gate once explicitly requested |
| Framework Contract Migration | One Human Approval |
| Project Stage advancement | Human Approval |
| Gate 1.5 Human PASS | Human Approval |
| Authority Cutover | One Human Approval |
| RC / Final publication | 由 Release Guide 管理，不属于 Project adoption transaction |
| Repository Rename | Human Approval |
| Legacy deletion / destructive operation | Human Approval |
| Ordinary commit / push inside authorized task | No separate gate |
| Migration Closeout Review | No new approval |

Routine validation、review、CI、diff inspection、evidence collection 与 report 不分别设置 Human Gate。明确用户任务授权始终是执行前提；上表取消的是重复的形式化 `STOP / APPROVE / STOP`，不是用户对 Project 状态变化的控制权。

## 8. Project-side impact、status 与 recovery

每次 adoption 必须记录 target Release + immutable Commit、old → new impact、受影响 Project 文件、validator / compatibility evidence 与 rollback / recovery plan。使用现有 Project Contract 管理动态状态，不建立新 schema：

- 根 `README.md` 维护 `Current Project Stage`，并可在有用时提供简洁的当前 lifecycle summary；
- `FRAMEWORK.md` 维护当前 Framework binding、`Initialization Status` 与 initialization provenance；
- `requirements.md`、`block_diagram.md`、`design_notes.md`、`references.md` 只维护 Project Facts / Baseline，避免重复 Gate、Migration 或 Authority 动态状态。

`requirements.md` 如需状态措辞，应偏向稳定 baseline，例如 `Baseline: Stage 1 Requirements Baseline`，而不是长期复制 `Gate 1.5 PASS`、`Initialized`、Authority state 或 Migration state。执行 adoption 或 Authority Cutover 时仍须读取真实 GitHub 与上述权威文件，不能把本 Guide、历史 Master Plan 或 retired Runbook 当作动态状态源。失败时保持或恢复一致 binding；不得留下文件来自新版本但 `FRAMEWORK.md` 仍指向旧版本的部分切换。

## 9. 禁止事项

- 不从 Framework `main` 直接覆盖 Project；
- 不把新 RC、Final Release 或 Framework `main` commit 当作自动 rebinding 授权；
- 不用 Authority Cutover 代替普通 Compatible Framework Sync 或 Framework Contract Migration；
- 不用假 Release、branch 名或短 SHA 替代 binding；
- 不重写 Framework Legacy history，不移动 `framework-pre-v1-migration`；
- 不为结构外观改写或伪造 EDA、ERC、DRC、Manufacturing 或 Test；
- 不在所需 Human Approval 前执行 Contract Migration、Project Stage advancement、Gate 1.5 PASS、Authority Cutover、Release、Rename 或 destructive operation。
