# Project Initialization Guide

> 适用范围：从固定 Framework Release 创建 Standalone Project，完成 Bootstrap、Stage 1 和 Gate 1.5

本指南只给出操作顺序。结构、schema 与分类以 [Project Structure Standard](Project_Structure_Standard.md) 为准；Lifecycle 与 Gate 以 [Workflow](08_Project_Workflow.md) 为准；AI 读取范围以 [AI Context Guide](AI_Context_Guide.md) 为准。

## 1. 从固定 Release 获取 Template

1. 选择已发布的 Framework Release，例如 `hardware-project-framework-v1.0.0`。
2. 确认该 Release 的 immutable 40 位 commit SHA。
3. 从该 Release 快照取得 `templates/hardware_project_template/`，不要复制 Framework `main` 的漂移工作树。
4. 将 Template 内容复制到一个新的空白 Project repository root。

Framework RC/Final 尚未发布时，只可为 Framework 自测或明确预发布评估使用 `development-v0.9`，并绑定测试实际使用的 immutable commit；不得把未发布的 RC 名称写成正式 Release。

## 2. 填写 Project Identity 与 Binding

1. 在根 `README.md` 替换 `<PROJECT_NAME>` 与 `<HARDWARE_REVISION>`，写入真实 Project Identity。
2. 按 Structure Standard 的唯一 schema 填写 `FRAMEWORK.md`。
3. 正式绑定填写固定 Release + 对应 Commit；开发自测填写 `development-v0.9` + 实际 immutable commit。
4. 初始化期间使用 `Bootstrap Draft` 或 `Development Bootstrap`；进入 Stage 1 后可使用 `Gate 1.5 Pending`。
5. 不使用本机绝对路径、branch 名、假 SHA 或其他 Project 的仓库身份。

## 3. 完成 Bootstrap

- 确认全部 Required files 存在；
- 确认 `firmware/` 与所有 Stage-enabled 文件没有被默认预建；
- 建立 README 的事实与导航入口；
- 清除所有尖括号 Template placeholder；
- 未知 Project facts 保留为 `TBD`、`待确认` 或 Draft；
- 运行 Project Validator，但不把结构通过解释为 Requirements、EDA 或验证完成。

Bootstrap validation：

```bash
python scripts/validate_project_repository.py
```

## 4. 执行 Stage 1

将根 README 的唯一阶段字段改为：

```text
Current Project Stage: Stage 1 — Requirements Definition
```

然后用真实已知信息建立第一版 Requirements Baseline：

- Project Goal 与 Out of Scope；
- Functional / Module Boundary；
- Power / Interface Requirements；
- Safety Boundary；
- Manufacturing Baseline；
- Acceptance Criteria；
- Open Questions 及核对计划；
- 第一版 Block Diagram、Design Notes 和 References 入口。

未知项可以明确保持 TBD，不得为通过 Gate 虚构器件、参数、EDA 或验证结果。

## 5. 执行 Gate 1.5

1. 使用 [Project Initialization Checklist](../checklists/project_initialization_checklist.md) 逐项检查人工事实。
2. 确认没有其他 Project 残留、无意义目录或提前产生的后续阶段结论。
3. 将 `Initialization Status` 更新为 `Initialized`，运行 Gate 模式验证：

```bash
python scripts/validate_project_repository.py --gate-1-5
```

4. 如失败，将状态恢复为 `Gate 1.5 Pending`，修正阻断项并重新执行。
5. 只有 checklist 与 Validator 均无阻断项时，Gate 1.5 才可记为 PASS 并允许进入 Stage 2。

Validator 只检查可自动判定的结构、binding、placeholder、链接、阶段文件和明显残留；它不能判断真实硬件需求是否充分，也不能证明 EDA、ERC、DRC、Manufacturing 或 Test。

## 6. Framework Validator 与 Template 维护

Framework 维护者运行：

```bash
python scripts/validate_framework_repository.py
python scripts/validate_project_repository.py templates/hardware_project_template --template
```

Template 中的 Project Validator 是 Framework 唯一开发源 `scripts/validate_project_repository.py` 的发布快照；不得人工分叉维护。
