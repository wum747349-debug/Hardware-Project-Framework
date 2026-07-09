# 设计说明总览

## 1. 当前设计定位

本项目第一版定位为 `STM32F103C8T6 数据采集/控制开发板`，重点训练低压嵌入式硬件设计的完整流程：需求定义、最小系统、电源输入与保护、通信接口、ADC 输入、MOSFET 输出、PCB Layout、上电调试和测试验证。

第一版优先保证可实现、可焊接、可调试和文档完整，不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

当前文档结构已调整为“设计总览 + 分模块详细设计”。本文件只保留总览、主选器件、关键网络和审查入口；模块细节见 `docs/module_design/`。

## 2. 当前阶段

当前项目已完成：

- 需求整理和模块拆分。
- 第一轮关键器件候选与主选收敛。
- 关键 datasheet 初步阅读和参数提取。
- MCU、电源、USB 转 UART、ADC 输入、MOSFET 输出、接口/测试点的模块原理图设计说明。

下一步应进入：原理图系统审查 / PCB Layout 前检查。

注意：本阶段不表示原理图已经审查通过，不生成最终 BOM，不进入打样结论。

## 3. 系统模块总览

| 模块 | 当前设计摘要 | 详细文档 |
|---|---|---|
| MCU 最小系统 | `STM32F103C8T6`，LQFP48，3.3V 供电，8MHz HSE，NRST，BOOT0，SWD，VDDA/VSSA 处理 | [01_mcu_minimum_system.md](docs/module_design/01_mcu_minimum_system.md) |
| USB-C 供电与 3.3V 电源 | USB-C 5V ONLY，`VBUS_RAW -> F1 -> VBUS_FUSED -> SW2 -> +5V_SYS -> AP2112K -> 3.3V` | [02_usb_c_power_ap2112.md](docs/module_design/02_usb_c_power_ap2112.md) |
| USB 转 UART | `CH340C`，3.3V 供电，USB_DP/USB_DM 接 CH340C，USART1 PA9/PA10 与 MCU 通信 | [03_usb_uart_ch340c.md](docs/module_design/03_usb_uart_ch340c.md) |
| ADC 输入保护 | 2 路 `0-5V` 输入，经 `10kΩ/18kΩ` 分压、`330Ω` 限流、`10nF` 滤波和 `BAT54S` 钳位进入 PA0/PA1 | [04_adc_input_protection.md](docs/module_design/04_adc_input_protection.md) |
| MOSFET 低边输出 | 2 路 `AO3400A` 低边开关，PB0/PB1 控制，`100Ω` 栅极电阻，`100kΩ` 下拉，`SS14` 续流 | [05_mosfet_low_side_output.md](docs/module_design/05_mosfet_low_side_output.md) |
| 接口、测试点与丝印 | UART/I2C/SPI 3.3V 排针、SWD、LED、按键、电源/ADC/MOSFET 测试点和安全丝印 | [06_interfaces_testpoints.md](docs/module_design/06_interfaces_testpoints.md) |

## 4. 当前主选器件摘要

本表是设计依据入口，不是最终 BOM。

| 模块 | 当前主选 / 候选 | 关键边界 |
|---|---|---|
| MCU | `STM32F103C8T6` | LQFP48 方向；需继续核对官方 datasheet / reference manual |
| USB-C 母座 | `TYPE-C 16PIN 2MD(073)` | 只使用 5V VBUS 和 USB2.0 D+/D-；CC1/CC2 各接 5.1kΩ 下拉 |
| 3.3V LDO | `AP2112K-3.3TRG1` | 5V 转 3.3V；外部 3.3V 取电限制 `<=100mA`；注意 SOT25 热耗散 |
| USB 转 UART | `CH340C` | 3.3V 供电；不使用 DTR/RTS 自动下载；TX/RX 与 MCU 交叉连接 |
| USB 数据 ESD | `TPD2EUSB30DRTR-N` | 只保护 USB_DP/USB_DM；靠近 USB-C 接口放置 |
| HSE 晶振 | `XC53G2-8.000-F12NJHP` 候选 | 8MHz；负载电容仍需结合晶振 CL 和 STM32 资料反推 |
| VBUS TVS | `SMF5.0A` | 用于 VBUS 瞬态保护，不替代长期过压保护 |
| 自恢复保险丝 | `C46640983` PPTC | 仅适合当前 5V USB 输入边界；Vmax=6V |
| ADC 钳位 | `BAT54S` | SOT-23，上下轨钳位到 GND / VDDA_3V3；注意反灌风险 |
| MOSFET | `AO3400A` | 3.3V GPIO 直接驱动；仅用于小电流低边开关 |
| 续流二极管 | `SS14` | 色带端/阴极接 VLOAD_EXT，阳极接 MOS_OUT |

## 5. 关键网络摘要

| 网络 | 含义 / 用途 | 主要审查点 |
|---|---|---|
| `VBUS_RAW` | USB-C 母座刚输入的原始 5V | 仅来自 USB-C VBUS；测试点 `TP_VBUS` |
| `VBUS_FUSED` | 经过 F1 自恢复保险丝后的 5V | D1 TVS 并联到 GND；后接电源开关 |
| `+5V_SYS` | 经过 F1 和 SW2 后的系统 5V | 供 AP2112 VIN；测试点 `TP_5V` |
| `3.3V` | AP2112K 输出的板级 3.3V | 供 MCU、CH340C、接口上拉、LED 等 |
| `VDDA_3V3` | MCU 模拟电源网络 | 由 `3.3V` 经 `0Ω` 接入；靠近 VDDA/VSSA 去耦 |
| `USB_DP / USB_DM` | USB2.0 数据线 | 只接 CH340C 和 USB ESD，不接 STM32 PA11/PA12 |
| `MCU_TX / MCU_RX` | MCU 视角 USART1 TX/RX | CH340C TXD -> PA10，CH340C RXD <- PA9 |
| `ADC12_IN0 / ADC12_IN1` | MCU 实际 ADC 输入节点 | 分压、限流、滤波、BAT54S 钳位后进入 PA0/PA1 |
| `MOS_CTRL1 / MOS_CTRL2` | MOSFET 控制 GPIO | PB0/PB1 经 `100Ω` 到 Gate，并由 `100kΩ` 下拉 |
| `MOS_OUT1 / MOS_OUT2` | MOSFET 低边输出节点 | 接 AO3400A Drain、接口 OUT、SS14 阳极 |
| `VLOAD_EXT1 / VLOAD_EXT2` | 外部负载电源正端 | 建议 `5V-12V`，最大不超过 `12V` |

## 6. 主要风险点

- USB-C 只支持 5V 输入，不支持 USB-PD 9V/12V；PCB 丝印建议标注 `USB-C 5V ONLY`。
- AP2112K 不能按 600mA 长期满载设计，3.3V 总电流和外部 3.3V 取电需要保守。
- CH340C 必须按 3.3V UART 电平设计，避免 5V 串口电平直接进入 STM32。
- ADC 外部输入仅限 `0-5V` 正常输入，不支持长期过压；BAT54S 上钳位存在未上电反灌 VDDA 风险。
- MOSFET 输出只用于小电流低边开关；外部 VLOAD 必须与板子 GND 共地。
- SS14 续流二极管极性不能反接，色带端/阴极应接 `VLOAD_EXT`。
- HSE 负载电容仍需根据具体晶振 datasheet、PCB 寄生电容和 STM32 硬件设计资料反推。
- 原理图审查前不能把当前文档当作“已通过审查”的结论。

## 7. 后续审查入口

下一步建议按以下顺序推进：

1. 准备实际 Altium 原理图和 PDF 原理图输出。
2. 使用 [docs/schematic_review.md](docs/schematic_review.md) 按模块填写审查记录。
3. 对照 [docs/module_design/](docs/module_design/) 核查连接、网络名、器件方向、接口定义和测试点。
4. 对照 [references.md](references.md) 核查 datasheet 路径、阅读状态和来源待确认项。
5. 原理图审查记录完成并处理问题后，再进入 PCB Layout。

## 8. 相关文档

- [requirements.md](requirements.md)
- [block_diagram.md](block_diagram.md)
- [references.md](references.md)
- [docs/component_selection_plan.md](docs/component_selection_plan.md)
- [docs/schematic_review.md](docs/schematic_review.md)
- [docs/user/project_overview.md](docs/user/project_overview.md)
