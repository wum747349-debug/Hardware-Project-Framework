# 原理图审查记录

## 1. 文档定位

本文用于记录 `STM32F103C8T6 数据采集/控制开发板` 的原理图系统审查过程。

当前状态：待审查 / 待确认。

本文件不是“审查通过”结论。下一步需要基于实际 Altium 原理图、PDF 原理图输出、datasheet、[design_notes.md](../design_notes.md) 和 [docs/module_design/](module_design/) 逐项审查并记录问题。

## 2. 审查输入

| 输入 | 状态 | 备注 |
|---|---|---|
| Altium 原理图工程 | 待提供 / 待确认 | 需以实际工程为准 |
| PDF 原理图输出 | 待提供 / 待确认 | 建议用于逐页审查和记录问题 |
| 设计总览 | 已有 | [../design_notes.md](../design_notes.md) |
| 模块设计文档 | 已有 | [module_design/](module_design/) |
| datasheet / reference manual | 部分已收集 | 见 [../references.md](../references.md) |

## 3. 总体审查原则

- 不伪造“已通过”结论。
- 每个问题应记录所在模块、网络/器件、问题描述、风险、建议修改和状态。
- 关键参数必须回到 datasheet、reference manual 或 application note 核对。
- 立创商品页只能作为 C 编号、库存、价格、封装和资料入口参考，不能替代 datasheet。
- 原理图审查完成并处理关键问题前，不进入 PCB Layout 结论。

## 4. 问题记录表

| 编号 | 模块 | 网络 / 器件 | 问题描述 | 风险 | 建议修改 | 状态 |
|---|---|---|---|---|---|---|
| SCH-001 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待审查 |

## 5. MCU 最小系统审查项

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

## 6. 电源与 USB-C 审查项

参考：[module_design/02_usb_c_power_ap2112.md](module_design/02_usb_c_power_ap2112.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| USB-C A4/A9/B4/B9 是否合并为 `VBUS_RAW` | 待审查 | 仅 5V 输入 |
| CC1/CC2 是否各自通过 5.1kΩ 下拉到 GND | 待审查 | UFP 取电设备 |
| SBU 是否 NC，Shield 是否按 `R7 0Ω -> GND` | 待审查 | Shield 策略后续可调整 |
| `VBUS_RAW -> F1 -> VBUS_FUSED -> SW2 -> +5V_SYS` 是否正确 | 待审查 | 确认电源开关脚位 |
| `SMF5.0A` TVS 极性是否正确，是否只保护 VBUS | 待审查 | 阴极接 VBUS_FUSED，阳极接 GND |
| PPTC Vmax=6V 是否仅用于当前 5V USB 输入边界 | 待审查 | 不支持 9V/12V |
| AP2112K VIN/GND/EN/NC/VOUT 连接是否正确 | 待审查 | EN 通过 10k 上拉到 +5V_SYS |
| C10/C11/C12 是否容量正确并靠近相关电源脚 | 待审查 | 输入/输出电容需核对 datasheet |
| 3.3V 外供 `<=100mA` 和热耗散边界是否在文档/丝印体现 | 待审查 | 不能按 600mA 长期满载 |
| 是否预留 `TP_VBUS`、`TP_5V`、`TP_3V3`、`TP_GND` | 待审查 | 便于上电测量 |

## 7. CH340C / USB 转 UART 审查项

参考：[module_design/03_usb_uart_ch340c.md](module_design/03_usb_uart_ch340c.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| CH340C 是否按 3.3V 供电，VCC/V3/GND 是否正确 | 待审查 | 避免 5V UART 电平风险 |
| C13/C14/C15 是否靠近 VCC/V3 | 待审查 | 去耦和局部储能 |
| `USB_DP/USB_DM` 是否只接 CH340C 和 ESD，不接 STM32 PA11/PA12 | 待审查 | 第一版不使用 STM32 原生 USB |
| TPD2EUSB30DRTR-N 是否为并联钳位，GND 是否短路径接地 | 待审查 | 不接 3.3V/VBUS |
| CH340C TXD/RXD 与 STM32 PA10/PA9 是否交叉连接 | 待审查 | 网络名需从 MCU 视角说明 |
| `R232` 是否接 GND | 待审查 | TTL UART 模式 |
| 未用握手脚和 NC 脚是否加 No Connect 标记 | 待审查 | 不做 DTR/RTS 自动下载 |

## 8. ADC 输入审查项

参考：[module_design/04_adc_input_protection.md](module_design/04_adc_input_protection.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| ADC1/ADC2 是否分别接 PA0/ADC12_IN0、PA1/ADC12_IN1 | 待审查 | 避免交叉命名 |
| 外部输入是否先经 `10kΩ/18kΩ` 分压 | 待审查 | 5V 输入约 3.21V |
| `330Ω` 串联限流是否在 ADC 节点前 | 待审查 | 不应被短接或绕过 |
| `10nF` 滤波电容是否接 ADC 节点到 GND | 待审查 | 低速采集使用 |
| BAT54S 是否为正确型号和引脚映射 | 待审查 | Pin3 ADC 节点，Pin1 GND，Pin2 VDDA_3V3 |
| `TP_ADC1/TP_ADC2` 是否接 MCU 实际 ADC 输入节点 | 待审查 | 不接分压前节点 |
| ADC 接口是否标注 `ADC IN 0-5V` | 待审查 | 不支持长期过压 |
| 是否记录未上电反灌 VDDA 风险 | 待审查 | 上钳位导入 VDDA_3V3 |

## 9. MOSFET 低边输出审查项

参考：[module_design/05_mosfet_low_side_output.md](module_design/05_mosfet_low_side_output.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| PB0/PB1 是否分别控制 `MOS_CTRL1/MOS_CTRL2` | 待审查 | 避开 ADC、USART、SWD |
| AO3400A 引脚映射是否正确 | 待审查 | Gate/Source/Drain 不可接错 |
| 每路 Gate 是否有 `100Ω` 串联电阻和 `100kΩ` 下拉 | 待审查 | 默认关断 |
| H3/H4 是否为 `VLOAD_EXT / MOS_OUT / GND` 三针 | 待审查 | 引脚顺序需丝印清楚 |
| SS14 极性是否正确 | 待审查 | 阴极/色带端接 VLOAD_EXT，阳极接 MOS_OUT |
| VLOAD 是否限制为 `5V-12V`，最大不超过 `12V` | 待审查 | 不做大电流输出 |
| 外部 VLOAD 是否要求与板子 GND 共地 | 待审查 | 丝印建议 `COMMON GND` |
| `TP_GATE1/2`、`TP_OUT1/2` 是否便于测量 | 待审查 | 关注开关节点干扰 |

## 10. 接口 / 测试点 / 封装 / 丝印审查项

参考：[module_design/06_interfaces_testpoints.md](module_design/06_interfaces_testpoints.md)

| 审查项 | 当前状态 | 备注 |
|---|---|---|
| UART/I2C/SPI 扩展接口是否均标注 3.3V 逻辑 | 待审查 | 不直接兼容 5V |
| SWD、UART、I2C、SPI、ADC、MOSFET 排针脚位是否与网络一致 | 待审查 | 避免丝印和网络不一致 |
| 用户 LED / 用户按键 GPIO 是否避开关键功能脚冲突 | 待审查 | 需结合实际原理图 |
| 关键测试点是否覆盖电源、复位、SWD、UART、ADC、MOSFET | 待审查 | 便于上电和调试 |
| USB-C、CH340C、AP2112K、AO3400A、SS14、BAT54S 封装是否与 datasheet 匹配 | 待审查 | 需检查封装库 |
| 丝印是否包含 `USB-C 5V ONLY`、`ADC IN 0-5V`、`VLOAD 5-12V`、`COMMON GND` | 待审查 | 空间不足时优先保留安全边界 |

## 11. 审查结论

当前结论：待审查。

后续在完成实际原理图逐项审查后，应在这里记录：

- 是否允许进入 PCB Layout。
- 必须修改的问题。
- 可接受但需 PCB 阶段关注的问题。
- 仍需 datasheet / 封装 / 采购可得性复核的问题。
