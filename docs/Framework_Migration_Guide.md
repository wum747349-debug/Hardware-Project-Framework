# Framework Migration Guide

> 适用范围：Standalone Project 从一个固定 Framework Release 显式升级到另一个固定 Release，以及 Legacy Project 的 Authority Cutover 准备

本指南只说明迁移操作。Binding、Structure Version 与 Authority Contract 以 [Project Structure Standard](Project_Structure_Standard.md) 为准；迁移前后 Stage 与回退影响以 [Workflow](08_Project_Workflow.md) 为准。

## 1. 不自动升级

Project 继续使用 `FRAMEWORK.md` 绑定的 Release + Commit。Framework `main`、新 RC 或新 Final 的出现不会自动改变 Project Runtime Rules、Structure 或 Stage Method。

禁止仅修改版本字段而不迁移实际差异，也禁止让 Project 同时依赖两个 Framework 版本。

## 2. Framework Release Upgrade

1. 记录当前 `Framework Repository`、`Framework Release`、`Framework Commit` 与 `Project Structure Version`。
2. 选择目标固定 Release，核对其 immutable commit、Changelog 与 Migration Guide。
3. 比较当前绑定与目标 Release 的 Required files、`FRAMEWORK.md` schema、Project `AGENTS.md`、Runtime Rules、Gate、目录职责、Stage Method 和 Validator。
4. 先在独立 migration branch 或可恢复工作区迁移 Project 文件；保留 Project facts、EDA 源、Evidence 与 Git history。
5. 只应用目标 Release 要求的结构与 Runtime 变化，不把 Template placeholder、Reference Project facts 或其他 Project facts复制进来。
6. 从目标 Release 同步 `scripts/validate_project_repository.py` 发布快照。
7. 运行目标 Release 要求的 Project Validator 和受影响 Gate/checklist；根据实际影响回退并重验相应 Stage。
8. 所有阻断项关闭后，更新 `Framework Release` 与 `Framework Commit`；只有结构契约版本变化时才更新 `Project Structure Version`。
9. 提交迁移 diff、验证结果与明确升级说明。未通过时保持原 binding，不部分切换。

## 3. Structure Version Change

Structure Version 变化必须建立旧路径到新职责的映射，确认 Required/Conditional/Stage-enabled 分类、事实源和相对链接。Hardware Revision 不因 Framework Structure 变化自动提升；只有硬件设计实际改变时才按 Project 规则处理。

## 4. Legacy Project Authority Cutover

迁移前，Legacy Monorepo Project Directory 是 Current Authority。准备 Cutover 时：

1. 建立 Legacy 文件到 Standalone Project 职责的映射；
2. 保留 EDA 权威源、项目事实、Evidence 与历史追溯；
3. 在 Standalone Repository 运行迁移验证与当前 Stage 所需 Gate；
4. 由用户明确批准 Authority Cutover；
5. Cutover 后，Standalone Project Repository 成为 Only Active Project Authority；Legacy 目录成为 Frozen Migration Source。

Frozen Migration Source 不继续开发、不修改项目事实、只用于核对；新仓库确认完整前不删除。禁止长期双写。

Phase 3/4 分别执行 Project 2/3 initial cutover；Phase 6 只做 Project 2/3 final migration verification 与 Project 1 formal standalone migration，不第二次拆分 Project 2/3。

## 5. 禁止事项

- 不从 Framework `main` 直接覆盖 Project；
- 不用假 Release、branch 名或短 SHA 替代 binding；
- 不重写 Framework Legacy history，不移动 `framework-pre-v1-migration`；
- 不为结构外观改写或伪造 EDA、ERC、DRC、Manufacturing 或 Test；
- 不在用户批准前执行真实 Project Authority Cutover。
