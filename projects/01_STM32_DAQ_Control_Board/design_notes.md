# 设计说明总览

> 文档状态：当前有效，整板设计意图与接口约定主文档
> 当前阶段：阶段 11：PCB 审查问题修正与关闭
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前原理图 PDF、当前 BOM 与已确认设计决定

## 1. 当前设计定位

本项目第一版定位为 `STM32F103C8T6 数据采集/控制开发板`，重点训练低压嵌入式硬件设计的完整流程：需求定义、最小系统、电源输入与保护、通信接口、ADC 输入、MOSFET 输出、PCB Layout、上电调试和测试验证。

第一版优先保证可实现、可焊接、可调试和文档完整，不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

当前文档结构已调整为“设计意图主文档 + 分模块详细依据 + 实际 EDA 实现输入”。本文件集中维护当前已经采用的整板设计方案摘要，包括主选器件、关键网络、MCU 引脚分配、接口定义、有效电平、已确认设计决定、风险和待确认项；详细计算、连接依据和 datasheet 摘要见 `docs/module_design/` 与 `references.md`。

实际电气实现以当前 Altium 原理图、对应审查版 PDF 及必要时导出的网表为准；本文件用于维护设计意图、Pin Map、接口约定、网络命名和已确认设计决定。如果本文档与实际原理图不一致，应在 [docs/schematic_review.md](docs/schematic_review.md) 中记录冲突，不得静默假设两者已经同步。

## 1.1 文档事实源层级

| 文件 / 输入 | 主要职责 |
|---|---|
| [requirements.md](requirements.md) | 功能需求、设计边界和验收标准 |
| [design_notes.md](design_notes.md) | 设计意图、当前主选方案摘要、Pin Map、接口约定、网络命名和已确认设计决定 |
| Altium `.SchDoc`、当前审查版 PDF、必要时的网表 | 确认实际电气实现，包括实际器件位号、接线、网络和元件参数 |
| [docs/module_design/](docs/module_design/) | 模块级连接依据、参数计算、datasheet 依据、风险和 PCB 检查项 |
| [docs/schematic_review.md](docs/schematic_review.md) | 原理图审查状态、问题、风险、证据和关闭情况 |
| [docs/pcb_review.md](docs/pcb_review.md) | 阶段 11 当前问题、关闭依据、风险统计和制造门禁 |

## 2. 当前阶段

当前项目已完成 PCB Layout，并已形成首轮 PCB 辅助审查记录。当前处于阶段 11 的问题修正与关闭阶段，重点是依据用户在 Altium 中的确认、当前规格书、原理图 PDF、BOM 和 PCB 审查输入，逐项关闭可关闭问题并保留制造门禁。

注意：本阶段不表示 PCB、DRC 或制造输出已经通过；不得生成正式制造文件，也不推进到阶段 12。

## 3. 系统模块总览

| 模块 | 当前设计摘要 | 详细文档 |
|---|---|---|
| MCU 最小系统 | `STM32F103C8T6`，LQFP48，3.3V 供电，8MHz HSE，NRST，BOOT0，SWD，VDDA/VSSA 处理 | [01_mcu_minimum_system.md](docs/module_design/01_mcu_minimum_system.md) |
| USB-C 供电与 3.3V 电源 | USB-C 5V ONLY，`VBUS_RAW -> F1 -> VBUS_FUSED -> SW3 -> +5V_SYS -> U8 AP2112K -> 3.3V` | [02_usb_c_power_ap2112.md](docs/module_design/02_usb_c_power_ap2112.md) |
| USB 转 UART | `CH340C`，3.3V 供电，USB_DP/USB_DM 接 CH340C，USART1 PA9/PA10 与 MCU 通信 | [03_usb_uart_ch340c.md](docs/module_design/03_usb_uart_ch340c.md) |
| ADC 输入保护 | 2 路 `0-5V` 输入，经 `12kΩ/18kΩ` 分压、`330Ω` 限流、`10nF` 滤波和 `BAT54S` 钳位进入 PA0/PA1，5V 标称输入映射到约 3.0V | [04_adc_input_protection.md](docs/module_design/04_adc_input_protection.md) |
| MOSFET 低边输出 | 2 路 `AO3400A` 低边开关，PB0/PB1 控制，保留 TIM3_CH3/TIM3_CH4 双路硬件 PWM 能力，`SS14` 续流 | [05_mosfet_low_side_output.md](docs/module_design/05_mosfet_low_side_output.md) |
| 接口、测试点与丝印 | USART2、I2C1、SPI1、公用电源 + GPIO 3.3V 排针、SWD、PB5 低电平点亮用户 LED、PB8 用户按键、电源/ADC/MOSFET 测试点和安全丝印 | [06_interfaces_testpoints.md](docs/module_design/06_interfaces_testpoints.md) |

## 4. 当前主选器件摘要

本表是设计依据入口，不是最终 BOM。

| 模块 | 当前主选 / 候选 | 关键边界 |
|---|---|---|
| MCU | `STM32F103C8T6` | LQFP48 方向；需继续核对官方 datasheet / reference manual |
| USB-C 母座 | `TYPE-C-31-M-12`，立创 `C165948` | Rev A 唯一当前型号；只使用 5V VBUS 和 USB2.0 D+/D-；CC1/CC2 各接 5.1kΩ 下拉 |
| 3.3V LDO | `AP2112K-3.3TRG1` | 5V 转 3.3V；外部 3.3V 取电限制 `<=100mA`；注意 SOT25 热耗散 |
| USB 转 UART | `CH340C` | 3.3V 供电；不使用 DTR/RTS 自动下载；TX/RX 与 MCU 交叉连接 |
| USB 数据 ESD | `TPD2EUSB30DRTR-N` | 只保护 USB_DP/USB_DM；靠近 USB-C 接口放置 |
| HSE 晶振 | `XC53G2-8.000-F12NJHP` | 8MHz 基频无源晶振，标称 `CL=12pF`；当前 `C3/C4=5.1pF`，采购选 C0G/NP0 |
| VBUS TVS | `SMF5.0A` | 用于 VBUS 瞬态保护，不替代长期过压保护 |
| 自恢复保险丝 | `C46640983` PPTC | 仅适合当前 5V USB 输入边界；Vmax=6V |
| ADC 钳位 | `BAT54S` | SOT-23，上下轨钳位到 GND / VDDA_3V3；注意反灌风险 |
| MOSFET | `AO3400A` | 3.3V GPIO 直接驱动；仅用于小电流低边开关 |
| 续流二极管 | `SS14` | 色带端/阴极接 VLOAD_EXT，阳极接 MOS_OUT |

## 5. 关键网络摘要

| 网络 | 含义 / 用途 | 主要审查点 |
|---|---|---|
| `VBUS_RAW` | USB-C 母座刚输入的原始 5V | 仅来自 USB-C VBUS；测试点 `TP_VBUS1` |
| `VBUS_FUSED` | 经过 F1 自恢复保险丝后的 5V | D5 TVS 并联到 GND；后接 SW3 电源开关 |
| `+5V_SYS` | 经过 F1 和 SW3 后的系统 5V | 供 AP2112 VIN；测试点 `TP_1`，表示 5V 测试点 |
| `3.3V` | AP2112K 输出的板级 3.3V | 供 MCU、CH340C、接口上拉、LED 等 |
| `VDDA_3V3` | MCU 模拟电源网络 | 由 `3.3V` 经 `0Ω` 接入；靠近 VDDA/VSSA 去耦 |
| `USB_DP / USB_DM` | USB2.0 数据线 | 只接 CH340C 和 USB ESD，不接 STM32 PA11/PA12 |
| `SHIELD` | USB-C 外壳屏蔽网络 | `SHIELD -> (R15 1MΩ || C18 1nF) -> GND`；R15 提供直流参考/泄放，C18 提供高频噪声回流，不替代专用 ESD 保护 |
| `MCU_TX / MCU_RX` | MCU 视角 USART1 TX/RX | CH340C TXD -> PA10，CH340C RXD <- PA9 |
| `UART2_TX / UART2_RX` | 外部 USART2 扩展 | PA2 为 MCU 发送 TX2，接外部模块 RX；PA3 为 MCU 接收 RX2，接外部模块 TX |
| `I2C1_SCL / I2C1_SDA` | 外部 I2C1 扩展 | PB6/PB7；`R19/R20=4.7kΩ` 默认装配，上拉到 3.3V |
| `SPI1_CS / SPI1_SCK / SPI1_MISO / SPI1_MOSI` | 外部 SPI1 扩展 | PA4/PA5/PA6/PA7；接口当前只带 GND 和信号，外设 3.3V 从公用扩展排针取电 |
| `ADC12_IN0 / ADC12_IN1` | MCU 实际 ADC 输入节点 | PA0/ADC12_IN0 对应 `TP_ADC1`；PA1/ADC12_IN1 对应 `TP_ADC2` |
| `MOS_CTRL1 / MOS_CTRL2` | MOSFET 控制 GPIO | PB0/PB1 控制两路低边输出，保留 TIM3_CH3/TIM3_CH4 双路硬件 PWM 能力 |
| `MOS_OUT1 / MOS_OUT2` | MOSFET 低边输出节点 | 接 AO3400A Drain、接口 OUT、SS14 阳极 |
| `VLOAD_EXT1 / VLOAD_EXT2` | 外部负载电源正端 | 建议 `5V-12V`，最大不超过 `12V` |

## 6. 当前 MCU 引脚分配

| 引脚 | 功能 / 网络 | 说明 |
|---|---|---|
| `PA0` | `ADC1` 输入 | 第一路 ADC 输入 |
| `PA1` | `ADC2` 输入 | 第二路 ADC 输入 |
| `PA2` | `UART2_TX` | 外部 UART2，MCU 发送，接模块 RX |
| `PA3` | `UART2_RX` | 外部 UART2，MCU 接收，接模块 TX |
| `PA4` | `SPI1_CS` | SPI1 片选 / NSS |
| `PA5` | `SPI1_SCK` | SPI1 时钟 |
| `PA6` | `SPI1_MISO` | SPI1 主入从出 |
| `PA7` | `SPI1_MOSI` | SPI1 主出从入 |
| `PA8` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PA9` | `CH340 / USART1_TX` | 板载 CH340C USB-UART，不接外部 UART 排针 |
| `PA10` | `CH340 / USART1_RX` | 板载 CH340C USB-UART，不接外部 UART 排针 |
| `PA13` | `SWDIO` | SWD 下载调试 |
| `PA14` | `SWCLK` | SWD 下载调试 |
| `PB0` | `MOS_CTRL1` | 第一路 MOSFET 控制 |
| `PB1` | `MOS_CTRL2` | 第二路 MOSFET 控制 |
| `PB5` | `USER_LED` | 用户 LED，低电平点亮 |
| `PB6` | `I2C1_SCL` | I2C1 时钟 |
| `PB7` | `I2C1_SDA` | I2C1 数据 |
| `PB8` | `USER_KEY` | 用户按键，内部上拉输入，按下为低 |
| `PB12` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB13` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB14` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB15` | `GPIO_EXT` | 公用 GPIO 扩展 |

## 7. 当前已确认设计决定

- MCU 为 `STM32F103C8T6`，当前封装方向按 LQFP48 审查。
- Rev A 当前唯一 USB-C 为 `TYPE-C-31-M-12`，立创 `C165948`；据用户确认，旧 `TYPE-C 16PIN 2MD(073)` 的安装结构仅适配约 `0.8mm` 板厚，因此被替代并仅保留历史资料。
- USB-C Shield 当前实现为 `SHIELD -> (R15 1MΩ || C18 1nF) -> GND`：`R15` 提供直流参考/泄放，`C18` 提供高频噪声回流；该 RC 支路不替代 `USB_DP/USB_DM` 的专用 ESD 保护。
- 当前整板原理图继续保持单页模块化结构，不拆成多张层次原理图。
- 用户 LED 使用 `PB5`，当前低电平点亮：`3.3V -> 1kΩ -> LED_USER -> PB5`。
- `MOS_CTRL1 = PB0`，`MOS_CTRL2 = PB1`，不改为 PB2/PB10；PB0/PB1 保留 TIM3_CH3/TIM3_CH4 双路硬件 PWM 能力。
- ADC 测试点对应关系固定为 `PA0 / ADC12_IN0 -> TP_ADC1`，`PA1 / ADC12_IN1 -> TP_ADC2`。
- PA9/PA10 保持作为板载 CH340C 的 USART1 USB-UART；外部 UART 扩展使用 USART2。
- I2C1 使用 PB6/PB7，`R19/R20=4.7kΩ` 板载上拉到 3.3V，当前默认装配。
- Rev A 当前暂不建立 `USB_FS` Differential Pair，不配置 USB Differential Pair Routing、Matched Length 或阻抗规则。
- 原因是当前 `USB_DP/USB_DM` 走向存在交叉，先按普通信号规则和人工布局检查处理；这不表示 USB 布线已经完成或已经验证可用。
- 后续调整器件方向或走线关系后，再单独讨论是否建立差分对规则。
- BOOT0 由 `R2=10kΩ` 下拉到 GND，并通过 `H2` 三针排针选择启动状态；`PB2/BOOT1` 已通过 `R21=10kΩ` 下拉到 GND，确保 BOOT0 拉高时 BOOT1 仍保持低电平，便于进入系统 Bootloader。
- HSE 晶振为 `X1 XC53G2-8.000-F12NJHP`，8MHz，`CL=12pF`；当前负载电容为 `C3/C4=5.1pF`，采购时选择 C0G/NP0。
- VDDA_3V3 通过 `R5=0Ω` 由 3.3V 供电，VDDA 去耦为 `C7=100nF` 和 `C8=1uF`；数字 VDD 去耦包括 `C2/C5/C9=100nF`，`C1=4.7uF` 作为局部储能。

## 8. 主要风险点

- USB-C 只支持 5V 输入，不支持 USB-PD 9V/12V；PCB 丝印建议标注 `USB-C 5V ONLY`。
- `R15/C18` 只定义 Shield 到 GND 的参考与高频回流路径，不得把它描述为 USB 数据线或 VBUS 的专用 ESD 保护。
- AP2112K 不能按 600mA 长期满载设计，3.3V 总电流和外部 3.3V 取电需要保守。
- `+5V_SYS` 来自 USB-C 输入经过保护/开关后的系统 5V，接到扩展排针时更适合作为 5V 输出取电点，不建议作为外部反灌供电入口。
- CH340C 必须按 3.3V UART 电平设计，避免 5V 串口电平直接进入 STM32。
- PA9/PA10 保持作为板载 CH340C 的 USART1 USB-UART，不再接外部 UART 扩展排针，避免外部模块和 CH340C 同时驱动导致冲突。
- I2C1 当前已有板载 4.7kΩ 上拉；如果外部模块也自带上拉，多个上拉会并联，连接多个模块前应检查等效上拉阻值和低电平灌电流。
- ADC 外部输入仅限 `0-5V` 正常输入，不支持长期过压；BAT54S 上钳位存在未上电反灌 VDDA 风险。
- MOSFET 输出只用于小电流低边开关；外部 VLOAD 必须与板子 GND 共地。
- SS14 续流二极管极性不能反接，色带端/阴极应接 `VLOAD_EXT`。
- HSE 晶振 PCB 布局要求仍需落实：晶振和负载电容靠近 `OSC_IN/OSC_OUT`，走线短且对称、无过孔、远离大电流和高速信号；可低风险预留 `OSC_OUT` 串联电阻焊盘，但不是必须修改项，也不表示当前已实现。
- 当前主要电气问题已经完成修改，原理图电气设计基本定稿；但关键器件封装、引脚、焊盘映射、接口朝向、丝印和测试点可达性仍需 Altium 人工核对，不能写成已具备直接打样条件。

## 9. 后续审查入口

阶段 11 下一步建议按以下顺序推进：

1. 以当前原理图 PDF `hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf`、BOM `hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx`、USB-C 规格书和用户 Altium 确认为问题关闭依据。
2. 使用 [docs/pcb_review.md](docs/pcb_review.md) 继续关闭阶段 11 的未关闭问题与制造门禁。
3. 对照 [docs/module_design/](docs/module_design/) 和 [references.md](references.md) 保持 USB-C、Shield、接口定义和资料路径一致。
4. 由用户在 Altium 中完成剩余规则核对、Repour 和完整 Batch DRC；AI/Codex 不声称代为完成。
5. 制造门禁关闭前不生成 Gerber、钻孔、坐标或制造包，不推进到阶段 12。

## 10. 相关文档

- [requirements.md](requirements.md)
- [block_diagram.md](block_diagram.md)
- [references.md](references.md)
- [docs/component_selection_plan.md](docs/component_selection_plan.md)
- [docs/schematic_review.md](docs/schematic_review.md)
- [docs/user/project_overview.md](docs/user/project_overview.md)
