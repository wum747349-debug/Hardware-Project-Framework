# Hardware Project Initialization Skill

## 适用场景

协助从固定 Framework Release 创建 Standalone Project，完成 Project Bootstrap、Stage 1 Requirements Baseline 和 Gate 1.5 时使用本 Skill。

本 Skill 不定义结构或 Lifecycle；结构以 `docs/Project_Structure_Standard.md` 为准，Gate 以 `docs/08_Project_Workflow.md` 为准，逐项检查使用 `checklists/project_initialization_checklist.md`。

Bootstrap / Stage 1 创建 human-facing Project documentation 时，遵守 Framework `AGENTS.md` 的 Documentation Language / Readability guidance；本 Skill 只传播该执行要求，不另行定义语言规则。

## 最小上下文

1. 先读取当前 Project `FRAMEWORK.md`。
2. 再读取当前 Project `PROJECT_RULES.md`。
3. 从绑定 Framework Release + Commit 快照读取：
   - `docs/AI_Context_Guide.md`；
   - `docs/Project_Structure_Standard.md`；
   - `docs/08_Project_Workflow.md` 的 Bootstrap、Stage 1、Gate 1.5 章节；
   - `docs/Project_Initialization_Guide.md`；
   - 本 Skill 与 Initialization Checklist。
4. 只读取当前 Project 的 Required files 和用户提供的初始化事实。

不默认读取 Framework `main`、其他 Project、全部 Skill、datasheet、EDA、制造文件或历史测试记录。

## Bootstrap 协作

- 确认 Template 来自固定 Release；Framework 自测或明确 prerelease evaluation 使用 `development-vX.Y.Z` + 实际 immutable full commit，`development-v0.9` 仅作为 historical Bootstrap / provenance compatibility 保留。
- 帮助填写 Project Identity 和唯一 `FRAMEWORK.md` schema。
- 建立 Required files、导航和职责目录。
- 保留真实未知项为 `TBD`、`待确认` 或 Draft。
- 不预建 Conditional 或 Stage-enabled 内容。
- 运行 Project Validator 并区分结构结果与硬件事实判断。

## Stage 1 协作

- 整理 Project Goal、Out of Scope、功能与模块边界；
- 整理电源、接口、安全、制造与验收边界；
- 建立第一版 Block Diagram、Design Notes 与 References 入口；
- 对未知项记录影响、来源和核对计划；
- 不提前选择器件，不生成 EDA、Review、DRC、Manufacturing 或 Test 结论。

## Gate 1.5 协作

1. 使用 Initialization Checklist 检查 Identity、Binding、Required、Navigation、placeholder、residue 与 Requirements Baseline。
2. 保持 `Initialization Status: Gate 1.5 Pending`，运行 Project Validator 的 `--gate-1-5` 模式。
3. 将自动检查与人工事实审查分开报告。
4. 任一阻断项存在时输出 `NOT READY`，并保持 `Gate 1.5 Pending`。
5. 全部阻断项关闭时 technical conclusion 为 `READY`。
6. Read-only request 只报告 `READY / NOT READY`，不得记录 Gate PASS、更新 `Initialization Status` 或推进 Stage。
7. Explicit execution request 已明确要求执行 Gate 1.5、完成初始化或条件满足后进入下一阶段时，该请求本身构成 execution authorization；若结论为 `READY`，不再请求第二次 approval，直接记录 Gate 1.5 PASS 并将 `Initialization Status` 更新为 `Initialized`。
8. 更新状态后运行普通 Project Validator；通过后才允许进入 Stage 2。Gate 本身不产生设计结果。

`READY` 不等于自动执行；只有当前用户任务已明确授权状态变化时才执行 Gate PASS。

## 事实与证据禁止事项

- 不虚构 Project facts、器件、参数或制造基线；
- 不虚构 `.SchDoc`、`.PcbDoc`、ERC、DRC、Manufacturing、Bring-up 或 Test；
- 不把其他 Project、Template 或 Reference Project 当作当前 Project 事实；
- 不用假 Release、假 SHA 或 Framework `main` 代替 binding；
- 不为目录整齐创建空目录、空阶段报告或低信息量文件；
- 不把 Validator PASS 写成硬件设计正确、EDA 已同步或验证已完成。

## 输出

- Bootstrap / Stage 1 / Gate 1.5 当前结论；
- 已确认事实与明确未决项；
- Validator command 与结果；
- Gate 阻断项、授权边界、所需动作和下一步。
