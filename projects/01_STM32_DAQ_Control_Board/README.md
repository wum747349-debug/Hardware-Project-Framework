# STM32F103C8T6 数据采集/控制开发板

> 文档状态：当前有效
> 当前阶段：整板原理图系统审查
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前原理图 PDF、当前 BOM 与已确认设计决定

## 项目简介

本项目设计一块基于 `STM32F103C8T6` 的 2 层 PCB 开发板，用于训练 STM32 最小系统、电源输入与保护、USB 转 UART 通信、ADC 输入采集、MOSFET 低边控制输出、常用通信接口扩展、PCB Layout、上电调试和测试验证能力。

第一版目标是做出一块可实现、可焊接、可调试、器件常见易采购、文档和制造输出完整的练习板。不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

## 当前阶段

当前项目已完成需求整理、模块方案拆分、关键器件第一轮选型、关键 datasheet 初步核对、模块原理图设计说明、原理图主要电气问题修改和当前文档同步。

下一步应进入：关键器件封装、引脚和焊盘映射的 Altium 人工核对，然后再进入 PCB Layout。

注意：当前原理图电气设计基本定稿，但不代表已经具备直接打样条件。AI 未解析 `.SchDoc` 内部电路，ERC、关键封装方向和 pin/pad mapping 仍需用户在 Altium 中人工核对。

## 第一版功能

- STM32F103C8T6 最小系统，8MHz HSE，SWD 下载调试。
- USB-C 5V 输入供电，不支持 USB-PD 高压输入。
- AP2112K-3.3TRG1 生成板级 3.3V。
- CH340C 实现 USB 转 UART，电脑端作为 COM 串口。
- 2 路板级 `0-5V` ADC 输入，经分压、限流、滤波和 BAT54S 钳位后进入 MCU。
- 2 路 AO3400A N-MOSFET 低边输出，面向 `5V-12V` 小电流负载。
- CH340C 占用 USART1，外部 UART 扩展改用 USART2，避免与板载 USB-UART 冲突。
- I2C1、SPI1、USART2 和公用电源 + GPIO 排针扩展接口，第一版均为 `3.3V` 逻辑。
- 电源指示 LED、PB5 用户 LED、复位按键、PB8 用户按键和关键测试点。

## 第一版边界

- 不使用 STM32 原生 USB，PA11 / PA12 第一版不接 USB-C D+ / D-。
- USB-C 仅作为 5V 输入和 CH340C 的 USB2.0 数据接口，不支持 9V/12V PD 输入。
- UART / I2C / SPI 扩展接口不直接兼容 5V 逻辑信号。
- I2C1 已配置板载 `R19/R20 = 4.7kΩ` 上拉到 `3.3V`；若外部模块也自带上拉，多个上拉会并联，连接多个模块前应检查等效上拉阻值和低电平灌电流。
- `+5V_SYS` 已引到公用扩展排针，更适合作为 5V 输出取电点，不建议作为外部反灌供电入口。
- 不允许将 0-5V ADC 外部输入直接接入 STM32 ADC 引脚。
- ADC 不用于高速波形采集，不追求高精度模拟测量。
- MOSFET 输出只做小电流低边开关，推荐使用电流 `<=300mA`，设计目标可按 `<=500mA` 预留。
- MOSFET 外部负载电源 VLOAD 建议 `5V-12V`，最大不超过 `12V`，且必须与板子 GND 共地。
- 3.3V 外供能力限制为 `<=100mA`。

## 文档导航

| 文档 | 用途 |
|---|---|
| [requirements.md](requirements.md) | 项目需求、功能边界和待确认问题 |
| [block_diagram.md](block_diagram.md) | 系统框图、模块连接和关键边界 |
| [design_notes.md](design_notes.md) | 当前整板设计意图与接口约定主文档：主选器件、关键网络、Pin Map、接口定义和风险入口 |
| [docs/README.md](docs/README.md) | docs 目录结构和阶段文档入口 |
| [docs/module_design/](docs/module_design/) | 分模块详细设计说明 |
| [references.md](references.md) | datasheet、资料路径和阅读状态索引 |
| [docs/component_selection_plan.md](docs/component_selection_plan.md) | 第一轮关键器件选型计划和历史依据 |
| [docs/schematic_review.md](docs/schematic_review.md) | 原理图审查记录与问题追踪 |
| [hardware/README.md](hardware/README.md) | Altium 源文件、导出文件和图片目录约定 |
| [docs/user/project_overview.md](docs/user/project_overview.md) | 面向展示/复盘的项目简介 |
| [docs/user/learning_record.md](docs/user/learning_record.md) | 学习记录和复盘入口 |

## 推荐阅读顺序

1. 先读本文，确认项目目标、阶段和边界。
2. 读 [requirements.md](requirements.md)，确认需求、约束和验收边界。
3. 读 [block_diagram.md](block_diagram.md)，建立系统模块和信号流向。
4. 读 [design_notes.md](design_notes.md)，核对当前设计意图、主选器件、Pin Map 和接口定义。
5. 按模块阅读 [docs/module_design/](docs/module_design/)。
6. 使用 [docs/schematic_review.md](docs/schematic_review.md) 记录原理图审查问题和关闭状态。

## 模块设计文档

- [MCU 最小系统](docs/module_design/01_mcu_minimum_system.md)
- [USB-C 供电与 AP2112K 电源](docs/module_design/02_usb_c_power_ap2112.md)
- [USB 转 UART / CH340C](docs/module_design/03_usb_uart_ch340c.md)
- [ADC 输入保护](docs/module_design/04_adc_input_protection.md)
- [MOSFET 低边输出](docs/module_design/05_mosfet_low_side_output.md)
- [接口、测试点与丝印](docs/module_design/06_interfaces_testpoints.md)

## 下一步

1. 以当前原理图 PDF `hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf` 和当前 BOM `hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx` 作为文档同步后的实现证据。
2. 按 [docs/schematic_review.md](docs/schematic_review.md) 完成关键器件封装、引脚、焊盘映射、USB-C 机械方向、接口朝向、丝印和测试点可达性人工核对。
3. 若 Altium ERC、网表或封装映射报告后续导出，再按证据更新审查记录。
4. 完成上述人工核对后，再进入 PCB Layout。
