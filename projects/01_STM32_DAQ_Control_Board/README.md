# STM32F103C8T6 数据采集/控制开发板

## 项目简介

本项目设计一块基于 `STM32F103C8T6` 的 2 层 PCB 开发板，用于训练 STM32 最小系统、电源输入与保护、USB 转 UART 通信、ADC 输入采集、MOSFET 低边控制输出、常用通信接口扩展、PCB Layout、上电调试和测试验证能力。

第一版目标是做出一块可实现、可焊接、可调试、器件常见易采购、文档和制造输出完整的练习板。不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

## 当前阶段

当前项目已完成需求整理、模块方案拆分、关键器件第一轮选型、关键 datasheet 初步核对、模块原理图设计说明和设计文档整理。

下一步应进入：原理图系统审查 / PCB Layout 前检查。

注意：当前不代表原理图已经审查通过，也不代表可以直接打样。后续需要基于实际 Altium 原理图、PDF 原理图输出、datasheet 和模块设计文档逐项审查。

## 第一版功能

- STM32F103C8T6 最小系统，8MHz HSE，SWD 下载调试。
- USB-C 5V 输入供电，不支持 USB-PD 高压输入。
- AP2112K-3.3TRG1 生成板级 3.3V。
- CH340C 实现 USB 转 UART，电脑端作为 COM 串口。
- 2 路板级 `0-5V` ADC 输入，经分压、限流、滤波和 BAT54S 钳位后进入 MCU。
- 2 路 AO3400A N-MOSFET 低边输出，面向 `5V-12V` 小电流负载。
- UART / I2C / SPI 排针扩展接口，第一版均为 `3.3V` 逻辑。
- 电源指示 LED、用户 LED、复位按键、用户按键和关键测试点。

## 第一版边界

- 不使用 STM32 原生 USB，PA11 / PA12 第一版不接 USB-C D+ / D-。
- USB-C 仅作为 5V 输入和 CH340C 的 USB2.0 数据接口，不支持 9V/12V PD 输入。
- UART / I2C / SPI 扩展接口不直接兼容 5V 逻辑信号。
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
| [design_notes.md](design_notes.md) | 设计总览、主选器件摘要、关键网络和风险入口 |
| [docs/module_design/](docs/module_design/) | 分模块详细设计说明 |
| [references.md](references.md) | datasheet、资料路径和阅读状态索引 |
| [docs/component_selection_plan.md](docs/component_selection_plan.md) | 第一轮关键器件选型计划和历史依据 |
| [docs/schematic_review.md](docs/schematic_review.md) | 原理图系统审查记录模板 |
| [docs/user/project_overview.md](docs/user/project_overview.md) | 面向展示/复盘的项目简介 |
| [docs/user/learning_record.md](docs/user/learning_record.md) | 学习记录和复盘入口 |

## 模块设计文档

- [MCU 最小系统](docs/module_design/01_mcu_minimum_system.md)
- [USB-C 供电与 AP2112K 电源](docs/module_design/02_usb_c_power_ap2112.md)
- [USB 转 UART / CH340C](docs/module_design/03_usb_uart_ch340c.md)
- [ADC 输入保护](docs/module_design/04_adc_input_protection.md)
- [MOSFET 低边输出](docs/module_design/05_mosfet_low_side_output.md)
- [接口、测试点与丝印](docs/module_design/06_interfaces_testpoints.md)

## 下一步

1. 导出或整理实际 Altium 原理图和 PDF 原理图输出。
2. 按 [docs/schematic_review.md](docs/schematic_review.md) 分模块审查。
3. 对照 [design_notes.md](design_notes.md)、[docs/module_design/](docs/module_design/) 和 [references.md](references.md) 核对关键器件、连接、封装和风险项。
4. 原理图审查通过并记录修改后，再进入 PCB Layout。
