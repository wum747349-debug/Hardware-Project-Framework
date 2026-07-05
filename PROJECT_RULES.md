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

## 5. 开源项目参考规则

- 开源项目只能用于参考功能结构、模块划分、接口组织、PCB 布局思路、文档组织和制造输出组织方式。
- 禁止直接复制开源项目的原理图、PCB、BOM、Gerber、生产文件或文字说明作为本项目成果。
- 引用开源项目时必须记录来源仓库地址、参考用途和学习点。
- 所有关键参数必须回到 datasheet / reference manual / application note 核对。
- 对锂电池、电源、MOSFET、ADC 输入、运放、参考电压等风险模块，必须经过对应 checklist 检查。
- 如果未来确实需要复用开源项目中的某个具体电路片段，必须先检查 license，并在文档中记录来源、修改点和验证结果。

## 6. 文件管理规则

- 每个项目必须包含 `README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md` 和 `references.md`。
- Altium 工程文件统一放在 `hardware/altium_project/`。
- Gerber、BOM、PDF、贴片坐标等输出文件统一放在 `hardware/outputs/`。
- `hardware/outputs/gerber/*.zip` 和 `hardware/outputs/fabrication_package/*.zip` 可以作为制造阶段成果提交。
- Altium 生成的 DRC/ERC 报告、BOM、iBOM、HTML/PDF 报告如属于阶段成果，可以保留。
- 固件工程统一放在 `firmware/`。
- 调试记录统一放在 `docs/bringup_log.md`。
- 测试报告统一放在 `docs/test_report.md`。
- 改版记录统一放在 `docs/revision_history.md`。
- 项目截图统一放在 `hardware/images/`。

## 7. AI 协作规则

AI 在协助本仓库时，应优先阅读：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/00_Project_Roadmap.md`
4. `docs/08_Project_Workflow.md`
5. `references/open_source_hardware_projects.md`
6. 当前项目的 `requirements.md`
7. 当前项目的 `design_notes.md`
8. 当前项目的 `references.md`
9. 当前项目的 `schematic_review.md` / `pcb_review.md` / `bringup_log.md`

AI 不应直接给出未经依据的硬件结论。涉及芯片连接、电源参数、充电电流、ADC 输入范围、MOSFET 驱动能力、运放供电范围、ADC 参考电压等内容时，必须提示需要核对 datasheet。

## 8. 安全规则

- 锂电池项目必须使用限流电源首次上电。
- 不允许无人看管充电测试。
- 不使用鼓包、破损或来历不明的锂电池。
- 不随意提高充电电流。
- 电源类项目必须记录输入电压、电流、芯片温度和输出电压。
- MOSFET 驱动感性负载时必须考虑续流路径和保护。
- 模拟输入接口必须考虑输入电压范围、限流和保护。
