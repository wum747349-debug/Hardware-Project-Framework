# Hardware Schematic Review Skill

## 适用场景

本 Skill 提供 schematic review 方法，主要用于 Stage 4 Formal Schematic Review，也可在其他 Stage 对明确的 scoped review / risk-review 任务按需使用。Stage 3 日常模块设计、连接核对、参数计算和轻量 verification 默认由 `hardware-schematic-design` Skill 处理；读取或按需使用本 Skill 不自动改变 Project Stage，不自动构成 Stage 4 Formal Review，也不等同于 Stage 4 PASS 或 PCB Layout approval。

本 Skill 用于在进入 PCB Layout 前发现电源、接口、保护、最小系统、模拟前端和调试可达性问题。

## 适用项目范围

本 Skill 适用于常见低压嵌入式、电源管理、传感器采集、模拟前端和 MCU 控制类项目。高压、射频、高速数字、隔离、汽车、医疗或安规场景需增加专项检查方法。

## 最小读取上下文

进行原理图审查前，AI 默认读取：

1. Layer 0/1：Project `FRAMEWORK.md`、`PROJECT_RULES.md` 与绑定 Framework 的 `docs/AI_Context_Guide.md`
2. 本 Skill
3. 当前 Project 的 `requirements.md`、`design_notes.md`、`references.md`
4. Stage 4 Formal Schematic Review 所需的当前完整原理图 PDF 与当前 BOM

按需读取：

- 当前 Project 已有的 `docs/schematic_review.md`
- `skills/hardware-datasheet-reading/SKILL.md` 或 `skills/hardware-component-selection/SKILL.md`
- 相关 checklist
- 当前问题需要的 netlist、ERC、component / pin / footprint mapping 或 screenshot evidence

## 审查输入能力边界

- `.SchDoc` 是 Altium 原理图的权威设计源文件，用于人工编辑、版本追踪和工程归档。
- 在没有可靠 Altium 解析器、脚本或自动化接口时，AI 不得声称已经读取、解析或核对 `.SchDoc` 内部电路。
- 原理图 PDF 主要用于图形连线、网络名和页面结构审查；BOM 用于核对位号、数量、参数或型号和 PCB 封装。完整原理图 PDF 和当前版本 BOM 可以支持常规原理图系统审查；无法由二者确认的实际网络、引脚映射、封装映射或其他 EDA 实现事项，应说明结论限制或标记为“待 EDA 核对”。
- BOM 最低字段不要求所有行都有具体制造商料号；关键器件缺少明确型号或封装时应记录具体缺失项，通用件可用参数、额定值、精度和封装描述。
- ERC 输出不是默认必需审查输入。AI 只有在用户提供 ERC 报告、Messages 导出或相关截图时，才分析 ERC 问题；未提供 ERC 输出时，不声称已经核对 ERC，不记录 ERC 执行或结果状态，也不把“未提供 ERC 输出”本身作为审查未完成或不能进入 PCB Layout 的理由。
- 网表、元件报告、引脚或封装映射报告和局部截图均为条件触发证据。局部截图只能补充局部证据，不能代替完整原理图 PDF。
- `requirements.md`、`design_notes.md` 和 `docs/module_design/*.md` 是需求和设计意图，不能单独证明 EDA 实现已经同步。
- Stage 4 可复用可追溯且足以覆盖当前目标的既有 review evidence；无需 schematic、PDF 或 BOM byte- / SHA-identical。对 unchanged coverage 不机械重审，只复核 changed、previously uncovered 或 evidence-insufficient areas。Reuse 不等于跳过 Stage 4，也不得把未验证的 ERC、EDA mapping 或 footprint mapping 升级为 PASS；ERC 未验证不因此自动成为 Stage 4 blocker。

## 审查目标

原理图审查不是只判断“能不能连通”，而是要检查：

- 电源是否安全可靠
- MCU 最小系统是否完整
- 复位、BOOT、时钟、SWD 是否正确
- UART / I2C / SPI 接口方向和电平是否合理
- ADC 输入范围、滤波、限流和保护是否可靠
- MOSFET 驱动和负载保护是否完整
- 锂电池充电与保护是否安全
- 运放供电、输入输出范围和滤波是否合理
- 外置 ADC 和参考电压是否匹配
- 测试点是否足够
- 封装、BOM、丝印、接口定义是否一致

## 审查顺序

按以下模块分类审查，并根据项目类型读取对应 checklist：

| 分类            | 主要用途                               | 推荐 checklist                                                                  |
| ------------- | ---------------------------------- | ----------------------------------------------------------------------------- |
| 总体结构          | 模块边界、电源路径、信号流向、网络命名、跨页连接           | `checklists/schematic_checklist.md`                                           |
| 电源            | 输入保护、稳压、去耦、热耗散、电源测试点               | `checklists/schematic_checklist.md`                                           |
| MCU 最小系统      | 供电、复位、BOOT、时钟、SWD、未用脚              | `checklists/stm32_board_checklist.md`                                         |
| 通信接口          | UART / I2C / SPI / USB 方向、电平、保护、丝印 | `checklists/stm32_board_checklist.md`、`checklists/schematic_checklist.md`     |
| ADC / 模拟输入    | 输入范围、限流、滤波、钳位、参考电压                 | `checklists/schematic_checklist.md`、`checklists/analog_frontend_checklist.md` |
| MOSFET / 功率输出 | 栅极驱动、默认状态、续流路径、负载接口、散热             | `checklists/schematic_checklist.md`                                           |
| 电池            | 充电、保护、接口极性、限流上电和测试安全               | `checklists/power_board_safety_checklist.md`                                  |
| 运放 / 外置 ADC   | 供电范围、共模范围、输出摆幅、带宽、参考电压             | `checklists/analog_frontend_checklist.md`                                     |
| 封装、测试点和可制造性   | 封装映射、极性、测试可达性、丝印和手焊风险              | `checklists/schematic_checklist.md`                                           |

Skill 只规定审查方法和输出结构；逐项检查句应维护在 `checklists/` 中。

## 输出格式

每次审查必须按以下格式输出：

### 当前结论

从以下三种中选择：

- 可以进入 PCB Layout：所有高风险问题已关闭；未关闭的中、低风险问题已有明确处置方案，且不影响板级安全、封装选择、接口定义和 PCB 关键布局。
- 修改后再进入 PCB Layout：仍存在会影响功能、封装、接口或布局的中风险问题。
- 存在高风险，暂不建议进入 PCB Layout：存在任何未关闭的高风险问题。

### 问题清单

| 编号 | 模块 | 问题描述 | 风险等级 | 建议修改 | 状态 | 证据或关联文件 |
|---|---|---|---|---|---|---|

状态建议统一使用：待决策、待修改、待核对、待 EDA 核对、已修改 / 待复核、已关闭。只有具备与问题类型相匹配的实现证据时，才能标记“已关闭”。

### 需要核对 datasheet 的项目

| 器件 | 需要核对的参数 | 核对原因 |
|---|---|---|

### 建议增加的测试点

| 网络 | 测试目的 | 是否必须 |
|---|---|---|

### 下一步操作

说明：

- 哪些地方必须修改
- 哪些地方建议优化
- 哪些资料需要补充
- 是否需要重新审查
- 是否可以进入 PCB Layout

## 风险等级

- 高风险：可能损坏芯片、电池、电源，可能导致无法上电，或存在明显安全风险。
- 中风险：可能影响功能、稳定性、精度、温升、寿命或调试难度。
- 低风险：主要影响文档一致性、可读性、可维护性、丝印、测试便利性或后续整理。

## 结果记录

审查完成后，应提醒用户将结论写入或更新：

- 当前项目的 `docs/schematic_review.md`
- 必要时更新当前项目的 `design_notes.md`、BOM 草稿、`requirements.md` 或 `docs/revision_history.md`

如果当前项目没有 `docs/schematic_review.md`，应在审查完成后创建。

只有在实现证据足够、修改已由用户在 EDA 中完成并通过默认必需证据或与问题类型匹配的条件触发证据复核后，才能关闭对应问题；证据不足时标记为“待 EDA 核对”。高风险问题如果依赖 ERC、网表或封装映射才能关闭，则必须补充对应证据。

## 禁止事项

- 不要只说“看起来没问题”。
- 不要跳过电源、电池、ADC、MOSFET、运放、参考电压等高风险模块。
- 不要在没有 datasheet 依据时确认关键连接完全正确。
- 不要把开源项目原理图当作最终依据。
- 不要忽略测试点、调试接口和首次上电安全检查。
- 不要建议用户直接进入 PCB Layout，除非所有高风险问题已经关闭；证据不足、待验证或待 EDA 核对的高风险问题均视为未关闭。
