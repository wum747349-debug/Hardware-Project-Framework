# PROJECT_RULES

## 1. 仓库定位

本仓库是硬件设计实战项目工作区，用于训练和沉淀硬件设计能力，包括原理图设计、PCB Layout、器件选型、样板调试、测试验证和简历项目整理。

## 2. 当前项目

本仓库包含三个核心项目：

1. STM32 数据采集/控制开发板
2. 单节锂电池充电与保护电源板
3. 基于 STM32 + 运放 + ADC 的模拟信号采集板

## 3. 工具链

- EDA 软件：Altium Designer
- STM32 配置工具：STM32CubeMX
- 固件开发：Keil MDK
- 文档格式：Markdown
- 版本管理：Git / GitHub

## 4. 设计原则

- 官方 datasheet、reference manual 和 application note 优先于教程和开源项目。
- 开源项目只能作为参考设计，不允许直接照抄。
- 每个模块必须说明设计依据。
- 第一版优先保证可实现、可焊接、可调试，不追求过度复杂。
- 优先使用常见、易采购、易焊接、资料完整的器件。
- 每个关键电源、复位、调试、通信、ADC 信号必须预留测试点。
- 所有项目必须保留原理图审查、PCB 审查、上电调试和测试记录。
- 任何设计修改都要记录原因和结果。
- 不允许只保留 Altium 源文件，必须同时输出 PDF、图片、BOM、Gerber 和说明文档。

## 5. 文件管理规则

- 每个项目必须包含 `README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md` 和 `references.md`。
- Altium 工程文件统一放在 `hardware/altium_project/`。
- Gerber、BOM、PDF、贴片坐标等输出文件统一放在 `hardware/outputs/`。
- 固件工程统一放在 `firmware/`。
- 调试记录统一放在 `docs/bringup_log.md`。
- 测试报告统一放在 `docs/test_report.md`。
- 改版记录统一放在 `docs/revision_history.md`。
- 项目截图统一放在 `hardware/images/`。

## 6. AI 协作规则

AI 在协助本仓库时，应优先阅读：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/00_Project_Roadmap.md`
4. 当前项目的 `requirements.md`
5. 当前项目的 `design_notes.md`
6. 当前项目的 `references.md`
7. 当前项目的 `schematic_review.md` / `pcb_review.md` / `bringup_log.md`

AI 不应直接给出未经依据的硬件结论。涉及芯片连接、电源参数、充电电流、ADC 输入范围、MOSFET 驱动能力、运放供电范围、ADC 参考电压等内容时，必须提示需要核对 datasheet。

## 7. 安全规则

- 锂电池项目必须使用限流电源首次上电。
- 不允许无人看管充电测试。
- 不使用鼓包、破损或来历不明的锂电池。
- 不随意提高充电电流。
- 电源类项目必须记录输入电压、电流、芯片温度和输出电压。
- MOSFET 驱动感性负载时必须考虑续流路径和保护。
- 模拟输入接口必须考虑输入电压范围、限流和保护。
