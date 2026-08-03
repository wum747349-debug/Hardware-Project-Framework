# Framework Changelog

本文件记录 Framework 方法、结构、Template、Skill、Checklist 与 Validator 的发布级变化。真实 Project 的硬件 revision 和项目 release 由各 Standalone Project Repository 自己维护。

## Unreleased — Framework v0.9 Executable Candidate

Status: development implementation for human review; not an RC or Final release.

### Contract

- Defined Framework / Project authority boundaries and the Legacy Monorepo → Framework Era transition.
- Defined the unique `FRAMEWORK.md` schema, Release + Commit binding, Project Structure Version 1, and explicit migration policy.
- Defined the four-layer context model, Bootstrap, Stage 1, and Gate 1.5 without changing the eight hardware stages.
- Classified project content as Required, Conditional, or Stage-enabled; `firmware/` is Conditional.
- Clarified Authority Cutover and Phase 6 migration-closeout semantics.

### Executable Implementation

- Added the Standalone Project initialization Guide, Skill, and Gate 1.5 checklist.
- Rebuilt the Template as a minimal Standalone Repository without real Project facts or pre-created Stage files.
- Added the standalone Project Validator and synchronized Template snapshot.
- Added the Framework Validator and lightweight CI checks.
- Added clean-bootstrap smoke coverage using an explicit `development-v0.9` binding.

No Framework RC/Final tag or Reference Project is included in v0.9.
