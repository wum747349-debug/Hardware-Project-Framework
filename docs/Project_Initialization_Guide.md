# Project Initialization Guide

> 适用范围：从固定 Framework Release 创建 Standalone Project，完成 Bootstrap、Stage 1 和 Gate 1.5

本指南只给出操作顺序。结构、schema 与分类以 [Project Structure Standard](Project_Structure_Standard.md) 为准；Lifecycle 与 Gate 以 [Workflow](08_Project_Workflow.md) 为准；AI 读取范围以 [AI Context Guide](AI_Context_Guide.md) 为准。

## 准备：Toolchain 与实验条件

Project Bootstrap 前先确认完成当前工作所需的工具角色；Framework 不把特定品牌或单一工具链写成所有 Project 的固定要求。

- EDA：用于原理图、PCB、封装、BOM 与制造输出；当前 Framework 的证据边界以 Altium Designer 工作流为主。
- Firmware（仅实际需要时）：选择与目标 MCU / SoC 匹配的配置、编译、下载和调试工具，例如厂商配置工具、IDE、编译器与硬件调试器。
- Version control 与 documentation：使用 Git、托管平台、Markdown、表格和截图工具维护可追溯版本与说明。
- Bring-up / Test（仅进入实际活动时）：按项目风险准备万用表、可限流电源、适用调试器；示波器、逻辑分析仪、USB 转串口、焊接与返修工具按真实需求启用。

在 Project Facts 或 Evidence 中按需记录关键工具、版本、配置与测量条件。工具可用不等于 EDA、ERC、DRC、制造、焊接或测试已经完成；实际结果仍由用户执行并提供证据。

## 1. 从固定 Release 获取 Template

1. 选择已发布的 Framework Release；预发布评估可选择已发布的 RC，例如 `hardware-project-framework-v1.0.0-rc1`，Final 发布后可选择对应 Final Release。
2. 确认该 Release 的 immutable 40 位 commit SHA。
3. 从该 Release 快照取得 `templates/hardware_project_template/`，不要复制 Framework `main` 的漂移工作树。
4. 将 Template 内容复制到一个新的空白 Project repository root。

`development-vX.Y.Z` 只用于 Framework 自测或明确的 Pinned Framework Evaluation，并绑定 evaluation 实际使用的 immutable full commit；`development-v0.9` 继续用于历史 Bootstrap / provenance compatibility。正常 Standalone Project Bootstrap 应选择实际已发布的固定 Release。Development identity 不是 published Release；不得把 Framework `main` 当作 Release。

## 2. 填写 Project Identity 与 Binding

1. 在根 `README.md` 替换 `<PROJECT_NAME>` 与 `<HARDWARE_REVISION>`，写入真实 Project Identity。
2. 按 Structure Standard 的唯一 schema 填写 `FRAMEWORK.md`。
3. 正式绑定填写固定 Release + 对应 Commit；开发自测或明确 prerelease evaluation 填写 `development-vX.Y.Z` + 实际 immutable full commit。
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
2. 确认没有未标注的其他 Project facts、非法 monorepo runtime dependency、无意义目录或提前产生的后续阶段结论；显式标注的合法 migration provenance 可以保留。
3. 确认当前状态真实为 `Current Project Stage: Stage 1 — Requirements Definition` 与 `Initialization Status: Gate 1.5 Pending`，运行 Gate 模式验证：

```bash
python scripts/validate_project_repository.py --gate-1-5
```

4. 如失败，保持 `Gate 1.5 Pending`，修正阻断项并重新执行。
5. Checklist 与 Validator 均无阻断项只表示 Gate 1.5 达到 technical readiness；它们不会自动授权 Gate 1.5 Human PASS。未获得 Human Approval 时必须保持 `Gate 1.5 Pending`。
6. Technical readiness 确认后，取得 Gate 1.5 PASS 的明确 Human Approval。
7. 只有获得该 Human Approval 后，才记录 Gate 1.5 PASS，并将 `Initialization Status` 更新为 `Initialized`。
8. 更新状态后运行普通 Validator，确认最终 Project 状态仍合法：

```bash
python scripts/validate_project_repository.py
```

9. 普通 Validator 通过后才允许进入 Stage 2。

```text
Checklist + Validator PASS
        ↓
technical readiness
        ↓
Human Approval for Gate 1.5 PASS
        ↓
record Gate 1.5 PASS
        ↓
Initialization Status = Initialized
```

Validator 只检查可自动判定的结构、binding、placeholder、链接、阶段文件和明显残留；它不能判断真实硬件需求是否充分，也不能证明 EDA、ERC、DRC、Manufacturing 或 Test。

## 6. Framework Validator 与 Template 维护

Framework 维护者运行：

```bash
python scripts/validate_framework_repository.py
python scripts/validate_project_repository.py templates/hardware_project_template --template
```

Template 中的 Project Validator 是 Framework 唯一开发源 `scripts/validate_project_repository.py` 的发布快照；不得人工分叉维护。
