# Gate 1.5 — Project Initialization & Requirements Baseline Checklist

## Identity

- [ ] Project Identity 唯一，并与当前 Standalone Repository 一致。
- [ ] 根 README 不含 Template 项目名或其他 Project 身份。

## Framework Binding

- [ ] `FRAMEWORK.md` 包含唯一 schema 的全部字段。
- [ ] Framework Release + 40 位 immutable Commit 已绑定。
- [ ] Project Structure Version 与 Repository Model 正确。
- [ ] Initialization Framework Release 与 Initialization Status 可追溯。
- [ ] 未绑定 Framework `main`，未使用本地绝对路径或假 Release/SHA。

## Required Structure

- [ ] 所有 Required files 与职责目录存在。
- [ ] `scripts/validate_project_repository.py` 可在本 Project 独立运行。
- [ ] 缺少 `firmware/` 或其他 Conditional 内容不会被判错。
- [ ] Stage-enabled 文件没有为了目录整齐在 Bootstrap/Stage 1 全部预建。
- [ ] 没有无职责空目录、低信息量占位文件或假输出。

## README and Navigation

- [ ] 根 README 是当前阶段唯一事实源。
- [ ] 当前阶段真实为 Stage 1，不从文件存在推断。
- [ ] Required facts、Runtime Rules、Binding、docs、hardware、references 与 validator 导航有效。

## Placeholder and Residue

- [ ] 所有尖括号 Template placeholder 已替换。
- [ ] `TBD`、`待确认`、Draft 只表示真实未决事实。
- [ ] 不含 Project 1 / 2 / 3 名称、旧 monorepo 路径或其他 Project facts。

## Stage 1 Requirements Baseline

- [ ] Project Goal 与第一版 Out of Scope 已记录。
- [ ] Functional Boundary 与 Module Boundary 已记录。
- [ ] Power Requirements 与 Interface Requirements 已记录。
- [ ] Safety Boundary 已记录。
- [ ] Manufacturing Baseline 已记录，未知项明确待确认。
- [ ] Acceptance Criteria 已建立。
- [ ] Open Questions 包含影响与核对计划。
- [ ] Block Diagram、Design Notes 与 References 已建立真实入口。

## No Premature Conclusions

- [ ] 尚未开始的选型、EDA、Review、Manufacturing、Bring-up 与 Test 明确保持未开始或未验证。
- [ ] 没有虚构器件、原理图、PCB、ERC、DRC、制造或测试结论。
- [ ] Gate 1.5 没有产生设计结果。

## Validation

- [ ] `python scripts/validate_project_repository.py --gate-1-5` 通过。
- [ ] 人工事实审查无阻断项。
- [ ] Gate 1.5 结论为 PASS，才允许进入 Stage 2。
