# Framework Changelog

本文件记录 Framework 方法、结构、Template、Skill、Checklist 与 Validator 的发布级变化。真实 Project 的硬件 revision 和项目 release 由各 Standalone Project Repository 自己维护。

## Unreleased

Status: Normal Framework Maintenance after published v1.0.0.

### Changed

- 将 Stage 7 PCB Release Review / Manufacturing Preparation 从 Stage 5–6 PCB design / review 方法中分离，引入独立 release Skill，并将正常放行收敛为 Core Bare PCB + conditional PCBA / special fabrication 流程。
- 精简 manufacturing-data verification：Final Full Batch DRC 与最终制造解读互补但不可互换，并按实际 submission path 审查一个忠实且能力足够的表示。
- 明确 specific-conclusion sufficiency、minimum missing evidence、session evidence / persistent authority 与 formal checkpoint 的最小 durable summary；raw evidence 仍为 optional。
- 强化 Stage 3 / Stage 4 的 task-intent routing，并明确 Stage 4 可复用充分、可追溯的既有 schematic-review evidence 覆盖 unchanged areas、聚焦 relevant delta；Stage architecture、Runtime Contract 与 Structural Contract 均未改变。
- 对齐 Project Runtime Rules 的三类 adoption taxonomy，明确 Compatible Sync 必须验证最终计划提交的 binding + files 组合，并澄清 Existing Project 进入 Pinned Framework Evaluation 时不得重置 initialization provenance / status；lifecycle architecture 与 Contract 均未改变。
- 将 development binding 推广为长期 Pinned Development Binding，新增轻量 Pinned Framework Evaluation、Same-SHA Formalization fast path，并把普通 Project adoption 压缩为 `Assess → Execute when authorized → Verify`；保持一个 active Layer-0 binding、既有 Human Approval 风险边界与 Authority Cutover 独立性。
- Project Validator 接受 `development-v0.9` 与通用 `development-vX.Y.Z`，同时继续要求 40 位 immutable Framework Commit，并拒绝 moving branch、`HEAD` 与 short SHA。
- 将 Framework release 高层流程收敛为 Release Assessment、Candidate Validation、ONE Human Publish Approval、Publication 与 Automatic Verification；RC 继续为 risk-driven optional prerelease。
- Component Selection Skill 增加 procurement-aware、JLCPCB/LCSC-first candidate discovery：AI/Codex 在具备公开搜索能力时主动发现 marketplace candidates，并以 Manufacturer datasheet / official documentation 作为 technical qualification authority；默认形成 Primary / Alternate，在 purchasing、ordering 或 PCBA BOM submission 前轻量复核 availability，并将默认输出收敛为 complexity-adaptive Candidate Table、Primary / Alternate Decision 与 Open Issues，其他比较、风险、datasheet 和后置外围输出仅在有助于决策、风险处理或可追溯性时生成。
- 将长期 Framework maintenance / Semantic Versioning / optional RC / Release publication 职责提取到 `docs/Framework_Maintenance_and_Release_Guide.md`。
- 将 `Framework_Migration_Guide.md` 收窄为 Project-side immutable Release adoption，并保留 Authority Cutover 低频 exception procedure。
- 将 Repository Architecture Migration Master Plan 标记为 `CLOSED — Historical Engineering Record`，AI Runbook 标记为 `RETIRED`，并清理 README 与 AI routing 的 transition-era current-state wording。
- Runtime Contract、Structural Contract、Project Structure Version、Project binding 与 Standalone Project：UNCHANGED。

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
