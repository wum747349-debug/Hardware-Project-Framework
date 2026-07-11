# 原理图审查记录

> 文档状态：当前进行中
> 当前阶段：整板原理图系统审查
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前仓库原理图目录与已确认设计决定

## 1. 文档定位

本文用于记录 `STM32F103C8T6 数据采集/控制开发板` 的原理图系统审查过程。

本文件不是“审查通过”结论。下一步需要基于实际 Altium 原理图、PDF 原理图输出、datasheet、[design_notes.md](../design_notes.md) 和 [module_design/](module_design/) 逐项审查并记录问题。

设计决定、EDA 实现核对、datasheet / 封装映射核对和问题关闭是四类不同状态。已确认设计决定不等于实际原理图已经逐项审查通过。

## 2. 审查输入

| 输入 | 状态 | 备注 |
|---|---|---|
| Altium 工程目录 | 已有 / 待整理 | `../hardware/altium_project/PCB_Project/`；当前可见 `.PrjPcb`、`.PcbDoc`、`.SchLib`、历史 `.SchDoc.Zip`，但未发现当前有效 `.SchDoc` 源文件 |
| Altium `.SchDoc` 源文件 | 未发现 / 待补充 | 当前目录中未发现可直接作为源文件审查的 `.SchDoc`；不能仅凭历史压缩文件确认当前 EDA 实现 |
| PDF 原理图输出 | 已有 / 当前审查输入 | `../hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic_RevA.pdf` |
| 设计总览 | 已有 | [../design_notes.md](../design_notes.md) |
| 模块设计文档 | 已有 | [module_design/](module_design/) |
| datasheet / reference manual | 部分已收集 | 见 [../references.md](../references.md) |

## 3. 总体审查原则

- 不伪造“已通过”结论。
- 每个问题应记录所在模块、问题描述、风险等级、修改建议、状态和证据或关联文件。
- 关键参数必须回到 datasheet、reference manual 或 application note 核对。
- 立创商品页只能作为 C 编号、库存、价格、封装和资料入口参考，不能替代 datasheet。
- PDF 文本层可用于辅助检查网络名，但不能替代图形连线、封装映射和 ERC 审查。
- 原理图审查完成并处理关键问题前，不进入 PCB Layout 结论。

## 4. 问题记录表

| 编号 | 模块 | 问题描述 | 风险等级 | 修改建议 | 状态 | 证据或关联文件 |
|---|---|---|---|---|---|---|
| SCH-001 | 接口 / I2C | I2C1 当前是否需要板载 `R_SCL/R_SDA` 上拉仍未决策，不能写成已完成。 | 中 | 复审时结合外接模块类型、总线速度和线长决定是否补预留焊盘；若依赖模块自带上拉，需在丝印/调试说明中提示。 | 待决策 | [module_design/06_interfaces_testpoints.md](module_design/06_interfaces_testpoints.md) |
| SCH-002 | MCU 最小系统 / HSE | `C6/C7=10pF` 仍为临时标注值，8MHz 晶振负载电容未最终核对。 | 中 | 根据晶振 `CL`、PCB 寄生电容和 STM32 硬件设计资料反推最终值。 | 待核对 | [module_design/01_mcu_minimum_system.md](module_design/01_mcu_minimum_system.md)、[../references.md](../references.md) |
| SCH-003 | 封装 / 可制造性 | USB-C、CH340C、AP2112K、AO3400A、SS14、BAT54S、按键和连接器封装/引脚映射仍需 PCB 前逐项核对。 | 中 | 对照 datasheet、封装库和实际采购型号检查 pin mapping、极性、焊盘和丝印方向。 | 待核对 | [../references.md](../references.md)、`hardware/altium_project/` |
| SCH-004 | 硬件输出 | 原“缺少原理图 PDF”问题已处理，当前 PDF 文件已补充为 `hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic_RevA.pdf`。 | 低 | 将该 PDF 作为当前实际电气实现的审查输入；继续完成正式逐项审查。 | 已补充 / 文件问题关闭，审查未完成 | [../hardware/README.md](../hardware/README.md) |
| SCH-005 | MCU 最小系统 / HSE | PDF 文本层显示 HSE 负载电容为 `C3/C4 10pf`，而当前文档多处写作 `C6/C7=10pF`；位号和最终电容值均需 EDA 核对。 | 中 | 以当前原理图源文件 / PDF 图形 / 网表为准核对实际位号、连接和参数；文档不得静默假设 `C6/C7` 与 PDF 一致。 | 待 EDA 核对 | `../hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic_RevA.pdf`、[module_design/01_mcu_minimum_system.md](module_design/01_mcu_minimum_system.md) |

## 5. 本轮已确认事项

| 事项 | 当前结论 | 状态 | 关联文件 |
|---|---|---|---|
| 用户 LED | `PB5`，低电平点亮，电路为 `3.3V -> 1kΩ -> LED_USER -> PB5`。 | 已确认 | [../design_notes.md](../design_notes.md)、[module_design/06_interfaces_testpoints.md](module_design/06_interfaces_testpoints.md) |
| MOSFET 控制脚 | `MOS_CTRL1 = PB0`，`MOS_CTRL2 = PB1`，不改为 PB2/PB10。 | 已确认 | [../design_notes.md](../design_notes.md)、[module_design/05_mosfet_low_side_output.md](module_design/05_mosfet_low_side_output.md) |
| MOSFET PWM 能力 | PB0/PB1 保留 TIM3_CH3/TIM3_CH4 双路硬件 PWM 能力。 | 已确认 | [module_design/05_mosfet_low_side_output.md](module_design/05_mosfet_low_side_output.md) |
| ADC 测试点 | `PA0 / ADC12_IN0 -> TP_ADC1`，`PA1 / ADC12_IN1 -> TP_ADC2`。 | 已确认 | [module_design/04_adc_input_protection.md](module_design/04_adc_input_protection.md) |
| 原理图组织 | 当前整板原理图保持单页模块化结构，不拆成多张层次原理图。 | 已确认 | [../design_notes.md](../design_notes.md) |

## 6. MCU 最小系统审查项

参考：[module_design/01_mcu_minimum_system.md](module_design/01_mcu_minimum_system.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| STM32F103C8T6 料号、封装和 LQFP48 引脚定义是否匹配 | 待审查 | 需对照官方 datasheet |
| VDD/VSS 是否全部正确连接到 `3.3V` / `GND` | 待审查 | 每个 VDD 附近应有 100nF 去耦 |
| `VBAT` 未用时是否接 `3.3V` 并避免悬空 | 待审查 | 可预留去耦 |
| `VDDA_3V3`、`VSSA`、R2 0Ω 和去耦是否正确 | 待审查 | 注意 VDDA/VSSA 不可接反 |
| `NRST` 是否接按键、100nF、电路网络和 SWD 接口 | 待审查 | 确认没有误接 HSE 脚 |
| `BOOT0` 10k 下拉和 3Pin 跳帽是否不会短接 3.3V/GND | 待审查 | 默认 Flash 启动 |
| HSE 8MHz 是否接 `PD0/OSC_IN` 和 `PD1/OSC_OUT` | 待审查 | `C6/C7=10pF` 仍需复核 |
| SWDIO/SWCLK/NRST/GND/3.3V 接口是否清晰 | 待审查 | 网络名避免 `CLK` 混淆 |

## 7. 电源与 USB-C 审查项

参考：[module_design/02_usb_c_power_ap2112.md](module_design/02_usb_c_power_ap2112.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| USB-C A4/A9/B4/B9 是否合并为 `VBUS_RAW` | 待审查 | 仅 5V 输入 |
| CC1/CC2 是否各自通过 5.1kΩ 下拉到 GND | 待审查 | UFP 取电设备 |
| SBU 是否 NC，Shield 是否按 `R7 0Ω -> GND` | 待审查 | Shield 策略后续可调整 |
| `VBUS_RAW -> F1 -> VBUS_FUSED -> SW2 -> +5V_SYS` 是否正确 | 待审查 | 确认电源开关脚位 |
| `+5V_SYS` 接到 `H_EXT_PWR_GPIO` 时是否标注为 5V 输出取电点 | 待审查 | 不建议作为外部反灌供电入口 |
| `SMF5.0A` TVS 极性是否正确，是否只保护 VBUS | 待审查 | 阴极接 VBUS_FUSED，阳极接 GND |
| PPTC Vmax=6V 是否仅用于当前 5V USB 输入边界 | 待审查 | 不支持 9V/12V |
| AP2112K VIN/GND/EN/NC/VOUT 连接是否正确 | 待审查 | EN 通过 10k 上拉到 +5V_SYS |
| C10/C11/C12 是否容量正确并靠近相关电源脚 | 待审查 | 输入/输出电容需核对 datasheet |
| 3.3V 外供 `<=100mA` 和热耗散边界是否在文档/丝印体现 | 待审查 | 不能按 600mA 长期满载 |
| 是否预留 `TP_VBUS`、`TP_5V`、`TP_3V3`、`TP_GND` | 待审查 | 便于上电测量 |

## 8. CH340C / USB 转 UART 审查项

参考：[module_design/03_usb_uart_ch340c.md](module_design/03_usb_uart_ch340c.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| CH340C 是否按 3.3V 供电，VCC/V3/GND 是否正确 | 待审查 | 避免 5V UART 电平风险 |
| C13/C14/C15 是否靠近 VCC/V3 | 待审查 | 去耦和局部储能 |
| `USB_DP/USB_DM` 是否只接 CH340C 和 ESD，不接 STM32 PA11/PA12 | 待审查 | 第一版不使用 STM32 原生 USB |
| TPD2EUSB30DRTR-N 是否为并联钳位，GND 是否短路径接地 | 待审查 | 不接 3.3V/VBUS；封装、方向、GND 引脚、焊盘和实际 datasheet 仍需复核 |
| CH340C TXD/RXD 与 STM32 PA10/PA9 是否交叉连接 | 待审查 | 网络名需从 MCU 视角说明 |
| PA9/PA10 是否只作为板载 CH340C 的 USART1 使用 | 待审查 | 不再接外部 UART 扩展排针，避免双驱动冲突 |
| `R232` 是否接 GND | 待审查 | TTL UART 模式 |
| 未用握手脚和 NC 脚是否加 No Connect 标记 | 待审查 | 不做 DTR/RTS 自动下载 |

## 9. ADC 输入审查项

参考：[module_design/04_adc_input_protection.md](module_design/04_adc_input_protection.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| ADC1/ADC2 是否分别接 PA0/ADC12_IN0、PA1/ADC12_IN1 | 设计决定已确认，EDA 实现待核对 | 避免交叉命名；PDF 文本层可见 `ADC12_IN0/ADC12_IN1`、`TP_ADC1/TP_ADC2` |
| 外部输入是否先经 `10kΩ/18kΩ` 分压 | 待审查 | 5V 输入约 3.21V |
| `330Ω` 串联限流是否在 ADC 节点前 | 待审查 | 不应被短接或绕过 |
| `10nF` 滤波电容是否接 ADC 节点到 GND | 待审查 | 低速采集使用 |
| BAT54S 是否为正确型号和引脚映射 | 待审查 | Pin3 ADC 节点，Pin1 GND，Pin2 VDDA_3V3 |
| `TP_ADC1/TP_ADC2` 是否接 MCU 实际 ADC 输入节点 | 设计决定已确认，EDA 实现待核对 | `TP_ADC1 -> ADC12_IN0 / PA0`，`TP_ADC2 -> ADC12_IN1 / PA1`；仍需图形连线核对 |
| ADC 接口是否标注 `ADC IN 0-5V` | 待审查 | 不支持长期过压 |
| 是否记录未上电反灌 VDDA 风险 | 待审查 | 上钳位导入 VDDA_3V3 |

## 10. MOSFET 低边输出审查项

参考：[module_design/05_mosfet_low_side_output.md](module_design/05_mosfet_low_side_output.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| PB0/PB1 是否分别控制 `MOS_CTRL1/MOS_CTRL2` | 设计决定已确认，EDA 实现待核对 | 保留 TIM3_CH3/TIM3_CH4 双路硬件 PWM 能力，不改 PB2/PB10；PDF 文本层可见 `PB0/PB1` 与 `MOS_CTRL1/MOS_CTRL2` |
| AO3400A 引脚映射是否正确 | 待审查 | Gate/Source/Drain 不可接错 |
| 每路 Gate 是否有 `100Ω` 串联电阻和 `100kΩ` 下拉 | 待审查 | 默认关断 |
| H3/H4 是否为 `VLOAD_EXT / MOS_OUT / GND` 三针 | 待审查 | 引脚顺序需丝印清楚 |
| SS14 极性是否正确 | 待审查 | 阴极/色带端接 VLOAD_EXT，阳极接 MOS_OUT |
| VLOAD 是否限制为 `5V-12V`，最大不超过 `12V` | 待审查 | 不做大电流输出 |
| 外部 VLOAD 是否要求与板子 GND 共地 | 待审查 | 丝印建议 `COMMON GND` |
| `TP_GATE1/2`、`TP_OUT1/2` 是否便于测量 | 待审查 | 关注开关节点干扰 |

## 11. 接口 / 测试点 / 封装 / 丝印审查项

参考：[module_design/06_interfaces_testpoints.md](module_design/06_interfaces_testpoints.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| UART/I2C/SPI 扩展接口是否均标注 3.3V 逻辑 | 待审查 | 不直接兼容 5V |
| `H_UART2` 是否使用 `PA2/USART2_TX`、`PA3/USART2_RX` | 待审查 | TX2 为 MCU 发送接模块 RX，RX2 为 MCU 接收接模块 TX |
| `H_I2C` 是否使用 `PB6/I2C1_SCL`、`PB7/I2C1_SDA` | 待审查 | 当前未预留板载 4.7k 上拉，依赖外接模块上拉或后续补 `R_SCL/R_SDA` |
| 外接裸 I2C 器件时是否确认 `SCL/SDA` 具备合适 3.3V 上拉 | 待复审 | 当前不能写成已完成 |
| `H_SPI` 是否使用 `PA4/CS`、`PA5/SCK`、`PA6/MISO`、`PA7/MOSI` | 待审查 | 当前只带 GND 和信号，外设 3.3V 从 `H_EXT_PWR_GPIO` 取电 |
| `H_EXT_PWR_GPIO` 2x5 排针脚位是否符合规划 | 待审查 | 1/3 为 3.3V，2/4 为 GND，5/6/7/8/9 为 GPIO，10 为 `+5V_SYS` |
| `+5V_SYS` 外引是否有反灌风险提示 | 待审查 | 不建议外部从该脚反向给板子供电 |
| SWD、UART、I2C、SPI、ADC、MOSFET 排针脚位是否与网络一致 | 待审查 | 避免丝印和网络不一致 |
| 用户 LED 是否为 `3.3V -> 1kΩ -> LED_USER -> PB5` | 设计决定已确认，EDA 实现待核对 | 低电平点亮，用于 GPIO 输出和状态指示；仍需图形连线核对 |
| 用户按键是否为 `PB8 -> KEY_USER -> GND` | 待审查 | 固件内部上拉，未按下高电平，按下低电平；当前无外部上拉 |
| 关键测试点是否覆盖电源、复位、SWD、UART、ADC、MOSFET | 待审查 | 便于上电和调试 |
| USB-C、CH340C、AP2112K、AO3400A、SS14、BAT54S 封装是否与 datasheet 匹配 | 待审查 | 需检查封装库 |
| 丝印是否包含 `USB-C 5V ONLY`、`ADC IN 0-5V`、`VLOAD 5-12V`、`COMMON GND`、`3.3V LOGIC` | 待审查 | 空间不足时优先保留安全边界 |
| `H_UART2`、`H_SPI`、`H_I2C` 丝印是否体现关键脚名 | 待审查 | 建议分别标注 `GND/TX2/RX2`、`GND/CS/SCK/MISO/MOSI`、`3V3/GND/SCL/SDA` |

## 12. 审查结论

当前结论：修改后再进入 PCB Layout。

依据：

- 当前 PDF 已补充，可作为审查输入，但 PDF 文本层解析只能支持有限网络名核对，不能替代图形连线、封装映射和 ERC。
- 当前目录未发现可直接审查的 `.SchDoc` 源文件。
- I2C 上拉、HSE 负载电容、关键器件封装 / pin mapping、接口丝印和正式 ERC 仍未关闭。
- PDF 文本层显示 HSE 负载电容位号与文档记录存在 `C3/C4` vs `C6/C7` 的待核对差异。

完成上述问题核对并更新关闭状态后，才能重新判断是否可以进入 PCB Layout。
