# Framework Changelog

本文件记录 Framework 方法、结构、Template、Skill、Checklist 与 Validator 的发布级变化。真实 Project 的硬件 revision 和项目 release 由各 Standalone Project Repository 自己维护。

## v1.1.1

### Changed

- 修正 Gate 1.5 authorization wording drift：统一为 `Checklist + Gate Validator + Fact Review → READY / NOT READY`；read-only review 只报告 readiness，不改变状态；当前用户任务已明确要求执行 Gate 1.5、完成初始化或条件满足后推进时，该请求本身构成 execution authorization，不再追加第二次 approval round-trip。Gate PASS 后仍必须更新 `Initialization Status = Initialized` 并运行 final Project Validator，之后才允许 Stage 2。
- 修正 Framework Publication authorization wording drift：Candidate Validation 仍只输出 `READY / NOT READY`；read-only publication review 在 `READY` 后停止；当前任务已明确要求发布 exact target version / release type 时，该请求构成 Publication Authorization，Candidate Validation 通过后不再重复请求独立 Human Publish Approval。Immutable candidate SHA、drift/conflict STOP、bounded publication transaction、automatic verification 与 recovery boundaries 保持不变。
- 将 Initialization Skill 的 development binding wording 与 Structure Standard / Initialization Guide 对齐为通用 `development-vX.Y.Z`；`development-v0.9` 仅保留 historical Bootstrap / provenance compatibility。
- Framework Validator 本次不新增自然语言 authorization parser；现有 structural / semantic regression coverage 保持不变，避免将用户意图判断绑定到脆弱 exact wording。

### Compatibility

- Runtime Contract: UNCHANGED
- Structural Contract: UNCHANGED
- Project Structure Version: 1 — UNCHANGED
- `FRAMEWORK.md` schema: UNCHANGED
- Required / Conditional / Stage-enabled model: UNCHANGED
- Stage / Gate architecture: UNCHANGED
- Project authority model: UNCHANGED
- Existing Standalone Projects are not automatically rebound by this patch.

## v1.1.0

### Changed

- 强化 Stage 2 Component Selection：新增 procurement-aware、JLCPCB/LCSC-first candidate discovery，以 Manufacturer official documentation 作为 technical qualification authority；默认形成 Primary / Alternate，并在 purchasing、ordering 或 PCBA BOM submission 前轻量复核 point-in-time availability。

- 新增独立 `hardware-schematic-design` Skill，明确 Stage 3 module planning、module-by-module design、parameter calculation、EDA capture guidance 与 Cross-Module Integration Check；同时进一步区分 Stage 3 日常设计与 Stage 4 Formal Schematic Review，并允许 Formal Review 对 unchanged areas 复用充分、可追溯的既有 evidence，只聚焦 relevant delta。

- 强化 Stage 5–6 PCB Layout / Routing 方法：完善 interactive placement 与 interactive routing guidance，明确 routing criticality、dominant constraint、关键 routing corridor、return/reference planning、冲突处理与局部 placement reopen；同时将 PCB rule organization 收敛为能够表达工程意图的最简单 Scope / Net Class 结构，避免不必要的规则复杂化。

- 将 Stage 7 PCB Release Review / Manufacturing Preparation 从 Stage 5–6 Layout / Routing 方法中独立出来，新增 `hardware-pcb-release-review` Skill；正常裸板放行收敛为 exact release candidate → Final Full Batch DRC → actual manufacturing-data path → one faithful and capable manufacturing interpretation → explicit Manufacturing Release Decision，PCBA 与 special fabrication 仅在实际适用时触发。

- 统一 Context / Evidence architecture：按 specific conclusion 判断 evidence sufficiency，只请求 minimum missing evidence；明确 evidence freshness / version compatibility、session evidence 与 persistent Project authority 的边界，以及 Formal Review / Stage transition / Manufacturing Release 所需的 minimum durable summary。Stage 5–6 net-specific routing 只按需读取最小 connectivity evidence，BOM 不再作为固定输入。

- 简化 Framework maintenance、release 与 Project adoption lifecycle：引入长期 Pinned Development Binding、Pinned Framework Evaluation 与 Same-SHA Formalization fast path；普通 adoption 收敛为 `Assess → Execute when authorized → Verify`。Framework publication 收敛为 Release Assessment → Candidate Validation → ONE Human Publish Approval → Publication → Automatic Verification，RC 为 risk-driven optional prerelease。

- 简化并增强 Validator / CI：canonical Framework validation 统一聚合 Framework Contract、Markdown links、Template / snapshot consistency、clean Bootstrap / Gate 1.5、binding / Stage-enabled / migration regression、Reference Project 与 final-state checks，并增加 Runtime Rule semantic-alignment regression guard；Project Validator 兼容 `development-v0.9` 与通用 `development-vX.Y.Z`，继续要求 immutable 40-character SHA 并拒绝 moving branch、`HEAD` 与 short SHA。

### Compatibility

- Runtime Contract: UNCHANGED
- Structural Contract: UNCHANGED
- Project Structure Version: 1 — UNCHANGED
- `FRAMEWORK.md` schema: UNCHANGED
- Required / Conditional / Stage-enabled model: UNCHANGED
- Stage / Gate architecture: UNCHANGED
- Project facts authority and repository authority model: UNCHANGED
- Existing Standalone Projects are not automatically rebound by this release.

## v1.0.0

Status: `hardware-project-framework-v1.0.0` 已作为 GitHub Final Release 发布，tag 指向 `b526ad12680a69737ca4eb36021336bc4dfe307e`。

### Phase 4 Framework Closeout

- 修正 release 状态、Gate 1.5 Human Approval 操作顺序与当前 migration orientation。
- 完成 Project 1 Formal Migration、RC1 binding 与 Authority Cutover；Standalone 成为 Only Active Project Authority，Legacy Project 1 冻结为 Frozen Migration Source，Phase 3 关闭。
- 完成 legacy / transition-era documentation inventory：将通用 Toolchain 知识并入 `Project_Initialization_Guide.md`，将运放与独立 ADC / Reference 选型维度并入 component-selection Skill，将 bring-up 与 debug record 方法收敛为 canonical Checklist，并 retire 8 份旧 source documents。
- 将 Template human-facing documentation 清理为中文解释优先，同时保留 canonical English terms、schema keys、fixed values、paths、identifiers、commands 与 validator-sensitive wording。
- 新增 synthetic、lightweight、validator-valid 的 `examples/reference_project_v1/`，用于 documentation / regression / final validation；不包含真实 Project facts、EDA、Manufacturing output 或 Hardware Evidence。
- 在已完成 Authority Cutover 后，以普通 Git deletion 从 Framework current tree 移除三个 Legacy real-project copies，并保留轻量 history marker 与完整 Git history。
- 将 Framework Validator `--mode final` 与 CI 对齐到 Reference Project validation。
- Runtime Contract：UNCHANGED；Structural Contract：UNCHANGED；RC2 required：NO。
- Repository Rename：COMPLETE；Final v1 publication：PUBLISHED。

## v1.0.0-rc1

Status: `hardware-project-framework-v1.0.0-rc1` 已作为 GitHub prerelease 发布；以下为该 RC1 snapshot 的 release-level summary。

### Contract

- Defined Framework / Project authority boundaries and the Legacy Monorepo → Framework Era transition.
- Defined the unique `FRAMEWORK.md` schema, Release + Commit binding, Project Structure Version 1, and explicit migration policy.
- Defined the four-layer context model, Bootstrap, Stage 1, and Gate 1.5 without changing the eight hardware stages.
- Classified project content as Required, Conditional, or Stage-enabled; `firmware/` is Conditional.
- Clarified the stable Authority Cutover contract without binding Project Runtime Rules to one-time migration phase numbers.

### Documentation Architecture

- Separated the one-time Repository Architecture Migration roadmap from the Project Runtime Contract.
- Added a human-facing Migration Master Plan and a migration-only AI Runbook.
- Removed legacy repository-migration Phase numbering from Runtime Contract enforcement where applicable.

### Executable Implementation

- Added the Standalone Project initialization Guide, Skill, and Gate 1.5 checklist.
- Rebuilt the Template as a minimal Standalone Repository without real Project facts or pre-created Stage files.
- Added the standalone Project Validator and synchronized Template snapshot.
- Added the Framework Validator and lightweight CI checks.
- Added clean-bootstrap smoke coverage using an explicit `development-v0.9` binding.
- Aligned Gate 1.5 validation with the `Gate 1.5 Pending` → PASS → `Initialized` state transition.
- Made Standalone Project validation migration-safe while retaining generic runtime-independence checks.
- Added automated legal-provenance and illegal-runtime-dependency smoke coverage.

RC1 snapshot 不包含 Reference Project。

## v0.9 — Framework v0.9 Executable Candidate

Framework v0.9 是 RC1 之前的 executable candidate 与 development / human-review 阶段。该阶段尚未发布 Framework RC 或 Final tag；其 Contract、Template、Skill、Checklist、Validator 与 CI 工作随后收敛为上方记录的 v1.0.0-rc1。
