# Repository Architecture Migration Master Plan

> Document Status: Active Migration Roadmap
> Audience: Human-facing Repository Architecture Migration Roadmap
> Runtime Contract: No
> Lifecycle: Becomes a Historical Engineering Record after Framework v1 closeout

## 1. Purpose and boundary

本计划用于把 Legacy Monorepo 收敛为一个 Framework Repository 与多个 Standalone Project Repository。核心不是移动目录，而是分离方法与项目事实，让每个真实 Project 只有一个活动权威源，并以可恢复、可核对的方式完成发布和 Cutover。

本计划是给用户阅读的 migration / release plan，主要维护当前 Phase、真实状态、路线理由、下一项主任务、真正风险边界与 Human Approval，以及 Framework Release、Project Binding 和 Final v1 的总体策略。AI/Codex 的 read-only assessment、transaction steps、validation sequence、STOP conditions 与 execution report 由 AI Runbook 维护，不在本计划重复展开。

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

Framework development state 与 Project bound Framework state 是两个独立状态：

```text
Framework main continues evolving
        !=
Project 1 / 2 / 3 remain pinned to an immutable release
```

这种 version pinning 是正常状态，不是 migration failure，也不会自动形成技术债。发布新的 Framework release 不会自动更新任何既有 Project binding；Project 不默认跟随 Framework `main` 或最新 Release。

## 3. Starting Point — Historical Completed Work

- Baseline Freeze：`framework-pre-v1-migration` 永久恢复点，指向 `3e9d4801bdd5768f8edc0e14e8f01bf278721e54`；
- Framework v0.9 Executable Candidate：Contract、Template、初始化方法、Validator 与 CI 已可执行，但不是 RC 或 Final；
- Project 2 的 Standalone Bootstrap、Stage 1 与 Gate 1.5 Pilot 已为 Phase 1 提供迁移反馈；其后续 migration / cutover 结果见下方最小 orientation。

这些里程碑不再沿用旧 Phase 0～8 作为未来主线。Git HEAD、Project binding 与 Hardware Stage 继续由 Git、Project `FRAMEWORK.md` 和根 `README.md` 维护。

### Current Migration Status

- Phase 1 — Pilot Stabilization：`CLOSED — Human Review Approved`；
- Phase 2 — Clean Bootstrap & RC Readiness：`CLOSED — RC1 Published / Human Review Approved`；
- Project 2：Bootstrap / Stage 1 / Gate 1.5 Pilot、Framework binding migration 与 Authority Cutover 均已完成；Standalone Repository 是 Only Active Project Authority；
- RC1：`hardware-project-framework-v1.0.0-rc1` @ `b36d9d399651e5c1a2b07dbc70d6e1487df57fd5`；
- Phase 3 — Formal Project Migration & Authority Cutover：`ACTIVE`；
- Project 2 migration：`COMPLETE / CLOSED`；
- Project 3 RC1 Compatible Framework Sync：`COMPLETE`；
- Project 3 Authority Cutover：`COMPLETE`；
- Project 3 migration：`COMPLETE / CLOSED`；
- Project 3 Current Stage：`Stage 1 — Requirements Definition`；
- Project 3 Stage 2：`NOT AUTHORIZED`；
- Next migration subject：`Project 1`；
- Repository Rename：`NOT AUTHORIZED / NOT EXECUTED`。

以上只保留 roadmap orientation，不作为动态 Project 状态数据库。执行任何迁移时，必须从真实 GitHub 默认分支、Project 根 `README.md`、`FRAMEWORK.md` 与适用 authority marker 重新核对 HEAD、Stage、initialization、binding 和 authority；不得依赖本节保存易变的 Project HEAD 或详细 lifecycle wording。Framework `main` 的后续变化不构成任何 Project binding change。

Migration 的 routine validation、CI、diff inspection、technical review 与 evidence collection 默认自动执行并合并报告。真正风险边界是 Framework Contract Migration、Authority Cutover、Stage / Gate 状态变化、release publication、repository identity transition 与 destructive change；每项只保留其必要的一次 Human Approval，不把自动核验改写为人工 Gate。当前任务已授权范围内的普通 commit 与 push 不另设 Human Gate。

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

成熟执行模型统一为：

```text
Formal Migration Assessment — READ ONLY
        ↓
READY / READY WITH MINOR NOTES
        ↓
ONE required Human Approval
        ↓
Atomic Migration Transaction
        ↓
Automatic Closeout Verification
```

Assessment 必须覆盖当前状态、固定 binding、事实完整性、authority readiness、exact bounded transaction 与 recovery expectations。`BLOCKED` 停止；一次批准只授权已评估的 transaction；通过自动 closeout verification 后关闭，不另设 Readiness 或 Closeout Approval。详细执行和报告要求由 AI Runbook 维护。

该模型按真正独立的风险边界应用。Framework Contract Migration 与 Authority Cutover 若同时适用于同一 Project，仍是两项 transaction 和两次各自批准；已完成并验证的 Compatible Framework Sync 不在后续 Cutover 中重复执行或重复批准。

若 Project 2 已在 Phase 1 完成获批的 Pilot Authority Cutover，本 Phase 对 Project 2 只执行 final migration verification、binding verification 与 closeout review，不执行第二次 Cutover。

Outputs / Done：三个 Project 分别完成权威收敛；Standalone 成为各自 Only Active Project Authority，Legacy 冻结；没有双写、事实改变或伪造阶段推进。

Project 2 不需要为了 RC 进入 Stage 2。但若未来要在 Standalone Repository 真正开展 Stage 2，应先明确 Authority Cutover，避免形成两个活动事实源。

Project 1 Formal Migration 不等待 Framework Final v1。Project 1 可继续基于已验证 RC1 完成 `Formal Migration → Authority Cutover → Automatic Closeout`；完成后关闭 Phase 3，再进入 Phase 4 Framework Closeout。Template cleanup、documentation cleanup、Repository Rename 与 Final v1 都不是 Project 1 migration 的前置依赖。

### Phase 4 — Framework Closeout & v1 Final

Goal：完成 Transition Repository 到正式 Framework Repository 的收尾。

Actions 可包含：Documentation Inventory / Rationalization、Template human-facing language usability cleanup、轻量 Reference Project、README / CHANGELOG / Guide closeout、Repository identity / Rename，以及 final Template / Fixture / Validator / CI consistency 与 Final Release readiness。确认三个 Project 权威收敛后，current tree 不再保留真实 Project 活动副本，但 Git history 保持可追溯。每项动作仍按自身 scope 与风险边界授权，不因进入 Phase 4 自动获批。

Phase 4 release strategy：

```text
No Contract-affecting change:
RC1 → compatible main cleanup → Final validation → v1.0.0

Contract-affecting change requiring renewed candidate validation:
RC1 → RC2 → Final validation → v1.0.0
```

因此 RC2 是 optional、impact-triggered，不是 sequence-mandatory，也不建立单独 RC2 Gate。

Future backlog candidate：`scripts/validate_project_migration.py` 可作为 assessment helper，未来辅助检查 binding、target binding、validator snapshot identity、structure completeness、stage、initialization、legacy artifact inventory、authority markers 与明显 stale lifecycle wording。它不是 migration authority、不是新的 Human Gate、也不是 Runtime Contract；Phase 4 是否实现需另行评估，本轮不实现。

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

Usability review 还应确认 human-facing documentation 提供足够中文解释，同时保留 canonical English terms、fields、schema key、identifier、path、command 与 validator-sensitive heading；不要求对历史文件机械全文翻译。为避免 Project 1 migration 或后续 Bootstrap 继续产生同类可读性问题，future generation-rule correction 可以在 Project 1 migration 前完成；既有 Project 3 readability debt 不在此处重开 migration，可留待 Phase 4 rationalization 或后续 targeted cleanup 处理。

Phase 4 前可以进行 inventory、read-only classification 和 planning。Project 2、Project 3 与 Project 1 migration 期间，不得仅为仓库整洁而提前执行旧文档 destructive cleanup。实际 `move`、`merge`、`archive`、`retire` 或 `delete` 只在三个真实 Project 全部完成 Authority Cutover 后的 Phase 4 中，依照审查结论与所需 Human Approval 执行。

Outputs / Done：Repository identity、current tree、文档、Template、Fixture、Validator 与 CI 一致，用户批准并实际发布 `hardware-project-framework-v1.0.0`。Rename 只在此阶段且真实 GitHub 操作获批后执行，不能由文档提前假定。

Repository Rename 是 Framework Repository identity transition，不只是 GitHub UI 或 README 改名。Phase 4 负责新仓库身份、内部与文档链接及 release identity 的一致性；真实 Project 不得仅因仓库改名而静默重写 `FRAMEWORK.md`。Project 必须在适用的 binding update 中显式选择 Framework release + immutable commit，并一并采用 Rename 后的 Framework Repository identity。`Repository Rename ≠ automatic Project Framework migration`。

发布 `hardware-project-framework-v1.0.0` 不触发 bulk Project rebinding。Existing Project 仅在新 capability 确有需要、当前 binding 存在已知 Contract / Validator 问题、新 Stage 明确依赖新 Framework，或用户明确授权升级时，才执行 explicit Framework Contract Migration；否则继续使用原 immutable binding。

## 5. Framework change management after the pilot

Project 2 pilot 已将长期 Framework change management 收敛为 `Compatible Framework Sync` 与 `Framework Contract Migration`。分类边界、执行流程与 Human Approval Policy 由 [Framework Migration Guide](Framework_Migration_Guide.md) 维护；本一次性 Master Plan 不重复定义或覆盖该长期治理。

Repository Architecture Transition 自身的 Authority Cutover、Repository Rename、Legacy deletion 与 RC / Final publication 仍按各自 Human Gate 执行。Transition closeout 后，本 Master Plan 成为 Historical Engineering Record，AI Runbook retire / archive；长期 Framework change management 不继承本计划的 Phase、Pilot 或 Closeout bureaucracy。Framework `main` 变化始终不等于 Project 自动变化。

## 6. RC strategy

RC publication 统一采用：

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

Candidate Validation 不需要独立 Human Approval。只有 immutable candidate SHA 通过 required validation 并判定 `READY` 后，才请求一次 Human Publish Approval。批准后执行一个 bounded atomic publication transaction；post-publish verification 通过即自动 `CLOSED`，失败则 STOP 并报告异常，不宣告关闭。不存在独立 RC Readiness、Technical、Publication 或 Closeout Approval。

RC2 / RC3 均为 optional、impact-triggered。Framework `main` 出现新 commit 不等于必须发布新 RC；documentation / Guide / migration process / authoring、usability、language guidance，以及不改变 Contract 的兼容 human-facing Template wording cleanup，通常不要求 RC2。

只有变化实质影响 Runtime Contract、Structural Contract、Project Structure、binding schema、validator contract / behavior、release-sensitive compatibility，或重大修复需要重新进行 release-candidate validation 时，才评估新 RC。RC 后发生这类 Contract-affecting change 时不得继续宣称旧 RC 已验证。

## 7. Final Done Criteria

Final publication 采用与 RC 相同的简化模型：

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

Final candidate 必须锁定 immutable candidate SHA 并完成 required validation；automatic verification 失败时 STOP，不宣告 Final CLOSED，也不增加第二个 closeout approval。

迁移完成意味着：三个 Project 各自只有一个活动权威仓库；Legacy current tree 不再承载活动副本但历史可追溯；Framework 只保留方法、Contract、Template、工具与 Reference/Test Fixture；正式 Project 使用固定 Release + SHA；Rename 已真实完成且引用已修复；v1 Final 的验证、CI、tag 与 release 均经一次 Human Publish Approval 并实际完成。
