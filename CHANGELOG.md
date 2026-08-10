# Framework Changelog

本文件记录 Framework 方法、结构、Template、Skill、Checklist 与 Validator 的发布级变化。真实 Project 的硬件 revision 和项目 release 由各 Standalone Project Repository 自己维护。

## Unreleased

Status: RC1 之后的 documentation-only maintenance；不属于 RC1 snapshot。

### Documentation Maintenance

- 修正 release 状态、Gate 1.5 Human Approval 操作顺序与当前 migration orientation。
- 完成 Project 1 Formal Migration、RC1 binding 与 Authority Cutover；Standalone 成为 Only Active Project Authority，Legacy Project 1 冻结为 Frozen Migration Source，Phase 3 关闭。
- 未修改 Runtime / Structural Contract，也未发布 RC2。

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
