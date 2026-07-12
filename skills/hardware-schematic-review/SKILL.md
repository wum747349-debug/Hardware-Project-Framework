# Hardware Schematic Review Skill

## 适用场景

当需要审查原理图、PDF 原理图、Altium 截图、模块连接关系、接口定义或设计思路时，使用本 Skill。

本 Skill 用于在进入 PCB Layout 前发现电源、接口、保护、最小系统、模拟前端和调试可达性问题。

## 适用项目范围

本 Skill 默认服务当前仓库已有的三个硬件项目：

1. STM32 数据采集/控制开发板
2. 单节锂电池充电与保护电源板
3. STM32 + 运放 + ADC 模拟信号采集板

同时也适用于后续新增的低压嵌入式硬件、传感器采集、电源管理、模拟前端、MCU 控制类项目。

如果新增项目涉及高压、射频、高速数字、隔离电源、汽车电子、医疗电子或安规认证，需要在本 Skill 基础上增加专项检查项。

## 最小读取上下文

进行原理图审查前，AI 默认读取：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/AI_Context_Guide.md`
4. `skills/hardware-schematic-review/SKILL.md`
5. 当前项目的 `requirements.md`
6. 当前项目的 `design_notes.md`
7. 当前项目的 `references.md`
8. 当前可解析的实现证据，如原理图 PDF、网表、ERC 报告、BOM、元件报告、引脚或封装映射报告、必要截图

按需读取：

- `skills/hardware-datasheet-reading/SKILL.md`，仅在需要核对关键器件参数时读取
- `skills/hardware-component-selection/SKILL.md`，仅在需要追溯选型依据时读取
- 当前项目已有的 `docs/schematic_review.md`，仅在继续审查或追踪历史问题时读取
- 相关 checklist

如果当前项目没有 `docs/schematic_review.md`，应在审查完成后创建。

## 审查输入能力边界

- `.SchDoc` 是 Altium 原理图的权威设计源文件，用于人工编辑、版本追踪和工程归档。
- 在没有可靠 Altium 解析器、脚本或自动化接口时，AI 不得声称已经读取、解析或核对 `.SchDoc` 内部电路。
- 原理图 PDF 主要用于图形连线、网络名和页面结构审查；只有 PDF 时属于有限审查，不能替代 ERC、网表和封装映射核对。
- 网表适合核对网络连接，ERC 报告适合核对 EDA 规则问题，BOM / 元件报告适合核对器件、封装和位号，截图适合补充局部证据。
- `requirements.md`、`design_notes.md` 和 `docs/module_design/*.md` 是需求和设计意图，不能单独证明 EDA 实现已经同步。

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

| 分类 | 主要用途 | 推荐 checklist |
|---|---|---|
| 总体结构 | 模块边界、电源路径、信号流向、网络命名、跨页连接 | `checklists/schematic_checklist.md` |
| 电源 | 输入保护、稳压、去耦、热耗散、电源测试点 | `checklists/schematic_checklist.md` |
| MCU 最小系统 | 供电、复位、BOOT、时钟、SWD、未用脚 | `checklists/stm32_board_checklist.md` |
| 通信接口 | UART / I2C / SPI / USB 方向、电平、保护、丝印 | `checklists/stm32_board_checklist.md`、`checklists/schematic_checklist.md` |
| ADC / 模拟输入 | 输入范围、限流、滤波、钳位、参考电压 | `checklists/schematic_checklist.md`、`checklists/analog_frontend_checklist.md` |
| MOSFET / 功率输出 | 栅极驱动、默认状态、续流路径、负载接口、散热 | `checklists/schematic_checklist.md` |
| 电池 | 充电、保护、接口极性、限流上电和测试安全 | `checklists/power_board_safety_checklist.md` |
| 运放 / 外置 ADC | 供电范围、共模范围、输出摆幅、带宽、参考电压 | `checklists/analog_frontend_checklist.md` |
| 封装、测试点和可制造性 | 封装映射、极性、测试可达性、丝印和手焊风险 | `checklists/schematic_checklist.md` |

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

只有在实现证据足够、修改已由用户在 EDA 中完成并通过 PDF、网表、ERC、BOM、报告或截图复核后，才能关闭对应问题；证据不足时标记为“待 EDA 核对”。

## 禁止事项

- 不要只说“看起来没问题”。
- 不要跳过电源、电池、ADC、MOSFET、运放、参考电压等高风险模块。
- 不要在没有 datasheet 依据时确认关键连接完全正确。
- 不要把开源项目原理图当作最终依据。
- 不要忽略测试点、调试接口和首次上电安全检查。
- 不要建议用户直接进入 PCB Layout，除非所有高风险问题已经关闭；证据不足、待验证或待 EDA 核对的高风险问题均视为未关闭。
