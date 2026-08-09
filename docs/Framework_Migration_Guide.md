# Framework Migration Guide

> 适用范围：Standalone Project 在固定 Framework Release + immutable Commit 之间执行 Compatible Framework Sync 或 Framework Contract Migration，以及 Legacy Project 的 Authority Cutover

本指南维护长期 Framework change-management 操作与 Human Approval Policy。Binding、Structure Version 与 Authority Contract 以 [Project Structure Standard](Project_Structure_Standard.md) 为准；Stage、Gate 与回退影响以 [Workflow](08_Project_Workflow.md) 为准。一次性 Repository Architecture Transition 的 Phase、Pilot、RC、Cutover 排期与 Closeout 不属于本指南定义的 Runtime Contract。

## 1. 共同边界：不自动升级

Project 继续使用 `FRAMEWORK.md` 绑定的 Release + Commit。Framework `main`、新 RC 或新 Final 的出现不会自动改变 Project Runtime Rules、Structure、Stage Method 或 binding。任何 Sync / Migration 都必须源于明确用户任务，选择目标固定 Release + immutable Commit，并在验证通过后才更新 binding。

禁止只修改版本字段而不核对实际差异，也禁止让 Project 同时依赖两个 Framework 版本。`No separate Human Approval gate` 只表示明确的用户执行请求已经构成授权，不允许 AI 主动升级 Project。

## 2. Compatible Framework Sync

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

执行流程：

1. 选择目标固定 Framework Release + immutable Commit；
2. 执行 compatibility / impact check，并记录为何不改变上述 Contract 语义；
3. 应用最小兼容改动，必要时同步 `scripts/validate_project_repository.py` 发布快照；
4. 运行 Project Validator 与受影响检查；
5. 验证通过后更新 `FRAMEWORK.md` binding；
6. 提交、推送并报告结果。

用户已明确要求执行该 Sync 时，不再设置 Readiness、Sync、Closeout 等独立 Human Gate。若发现 blocker、Contract contradiction 或分类不明确，保持原 binding 并停止报告。

## 3. Framework Contract Migration

发生以下任一实质变化时，必须分类为 Framework Contract Migration：`FRAMEWORK.md` schema、Project Structure Version、Required / Conditional / Stage-enabled 分类、Runtime Rules、Stage / Gate lifecycle、Project 文件职责或事实权威、Project `AGENTS.md` context-routing contract、Validator required structure，或其他不向后兼容的 Runtime / Structural Contract。

执行流程：

1. Migration Assessment：建立 old → new Contract diff、impact analysis、受影响 Project 文件、受影响 Stage / Gate、validation 与 rollback plan；
2. 报告 assessment 并取得一次 Human Approval；
3. 在可恢复工作区执行 Migration Transaction，保留 Project facts、EDA 源、Evidence 与 Git history，不复制 Template / Reference / 其他 Project facts；
4. 同步目标 validator snapshot，更新所需 Project 结构、Runtime Rules 与 Stage Method；
5. 更新 binding，并只在结构契约变化时更新 Project Structure Version；
6. 运行 Validator 与受影响 Gate / checklist；失败时按 rollback plan 保持或恢复一致 binding，不留下部分切换；
7. 提交、推送并给出 Final Report。

`One Contract Migration = One Human Approval Gate`。如果同一事务另行触发 Stage advancement、Authority Cutover、Repository Rename、Legacy deletion 或 Release publication，该独立高风险动作仍按自己的 Human Gate 处理。

## 4. Structure Version Change

Structure Version 变化属于 Framework Contract Migration，必须建立旧路径到新职责的映射，确认 Required / Conditional / Stage-enabled 分类、事实源和相对链接。Hardware Revision 不因 Framework Structure 变化自动提升；只有硬件设计实际改变时才按 Project 规则处理。

## 5. Legacy Project Authority Cutover

Authority Cutover 改变唯一活动事实源，因此保留一个 Human Approval Gate：

1. Cutover Assessment；
2. 自动执行只读 completeness、integrity、binding 与 validation checks；
3. 给出 `READY` / `BLOCKED` report；
4. `READY` 后取得一次 Human Approval；
5. 执行 Cutover Transaction：Standalone authority marker、Legacy freeze marker、migration docs sync、validation、commit 与 push；
6. 给出 Closeout Report。

Cutover 前 Legacy Monorepo Project Directory 是 Current Authority；Cutover 后 Standalone Project Repository 是 Only Active Project Authority，Legacy 目录是 Frozen Migration Source。Frozen source 不继续开发、不修改项目事实、只用于核对；新仓库确认完整前不删除。禁止长期双写。Closeout Review 是执行后的 verification / report，不是新的 Human Approval Gate。

## 6. Human Approval Policy

| Action | Human Approval |
| --- | --- |
| Routine docs / validator / tooling fix | No separate gate |
| Compatible Framework Sync | No separate gate once explicitly requested |
| Framework Contract Migration | One Human Approval |
| Project Stage advancement | Human Approval |
| Gate 1.5 Human PASS | Human Approval |
| Authority Cutover | One Human Approval |
| RC / Final publication | Human Approval |
| Repository Rename | Human Approval |
| Legacy deletion / destructive operation | Human Approval |
| Ordinary commit / push inside authorized task | No separate gate |
| Migration Closeout Review | No new approval |

Routine validation、review、CI、diff inspection、evidence collection 与 report 不分别设置 Human Gate。明确用户任务授权始终是执行前提；上表取消的是重复的形式化 `STOP / APPROVE / STOP`，不是用户对 Project 状态变化的控制权。

## 7. 禁止事项

- 不从 Framework `main` 直接覆盖 Project；
- 不用假 Release、branch 名或短 SHA 替代 binding；
- 不重写 Framework Legacy history，不移动 `framework-pre-v1-migration`；
- 不为结构外观改写或伪造 EDA、ERC、DRC、Manufacturing 或 Test；
- 不在所需 Human Approval 前执行 Contract Migration、Project Stage advancement、Gate 1.5 PASS、Authority Cutover、Release、Rename 或 destructive operation。
