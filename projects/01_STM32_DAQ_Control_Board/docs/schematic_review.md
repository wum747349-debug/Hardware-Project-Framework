# 原理图审查记录

> 文档状态：当前进行中
> 适用阶段：阶段 4：原理图审查阶段、阶段 7：PCB 审查阶段（问题追溯）
> 适用对象：STM32 DAQ Control Board Rev A 的原理图审查与 PCB 问题追溯
> 最后核对依据：当前原理图 PDF、当前 BOM 与用户人工确认事项

## 1. 文档定位

本文用于记录 `STM32F103C8T6 数据采集/控制开发板` 的原理图系统审查结论、已关闭问题，以及阶段 7 仍需结合 PCB 审查继续跟踪的事项。

本文件不表示 AI 已经读取或解析 `.SchDoc` 内部电路。当前结论基于完整原理图 PDF、当前 BOM、项目文档和用户人工确认事项；关键器件原理图库 Pin 与 PCB 封装 Pad Mapping、封装方向、接口朝向、丝印和测试点可达性仍需用户在 Altium 中人工核对。

## 2. 审查输入

| 输入类型 | 状态 | 当前文件或目录 | 审查用途 | 限制或备注 |
|---|---|---|---|---|
| Altium 工程目录 | 工作区已有 | `../hardware/altium_project/PCB_Project/` | 人工编辑、版本追踪和后续导出来源 | AI 当前未解析 `.SchDoc` 内部电路 |
| `.SchDoc` 源文件 | 工作区存在 | `../hardware/altium_project/PCB_Project/STM32_DAQ_Control_Board.SchDoc` | Altium 原理图权威源文件 | 只能由 Altium 或可靠解析器核对内部实现 |
| 原理图 PDF | 当前审查输入 | `../hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf` | 整板系统审查、图形连线和网络名辅助核对 | 局部截图不能代替完整 PDF |
| BOM | 当前审查输入 | `../hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx` | 位号、数量、参数或型号、PCB 封装核对 | 普通阻容不强制制造商料号；关键器件型号和封装需人工复核 |
| 网表 | 条件触发 / 未导出 | `../hardware/outputs/netlist/` | 复杂网络、跨页网络、网络标签或实际引脚连接核对 | 当前无有效输出；按需提供 |
| ERC 报告 / Messages 导出 | 条件触发 / 未提供 | `../hardware/outputs/erc/` | 用户提供时补充分析 ERC 问题 | 当前不能声称 ERC 已核对 |
| 元件报告 | 条件触发 / 未导出 | `../hardware/outputs/component_reports/` | 元件属性、位号、型号一致性核对 | BOM 信息不足时按需提供 |
| 封装映射报告 | 条件触发 / 未导出 | `../hardware/outputs/footprint_reports/` | 原理图器件与 PCB 封装映射核对 | 当前关键封装仍待人工核对 |
| 设计总览 | 已有 | [../design_notes.md](../design_notes.md) | 设计意图、Pin Map、接口约定和已确认设计决定 | 不能单独证明 EDA 实现已经同步 |
| 模块设计文档 | 已有 | [module_design/](module_design/) | 模块参数、计算依据和 PCB 检查项 | 不能单独证明 EDA 实现已经同步 |

## 3. 当前结论

当前原理图的主要电气问题已经完成修改，项目已进入阶段 7：PCB 审查阶段。Rev A USB-C 当前唯一型号和 Shield RC 实现已由用户结合 Altium 确认，并与当前规格书、原理图 PDF 和 BOM 同步；其余未关闭制造门禁继续在 [pcb_review.md](pcb_review.md) 跟踪。不得写成 PCB、DRC 或制造输出已经通过。

## 4. 已关闭问题

| 编号 | 模块 | 问题描述 | 关闭依据 | 当前状态 |
|---|---|---|---|---|
| SCH-001 | I2C | I2C1 原先缺少板载上拉或依赖外部模块上拉。 | 当前 BOM/PDF 显示 `R19/R20=4.7kΩ`，上拉到 3.3V。 | 已关闭 |
| SCH-002 | HSE | 晶振型号、负载电容和旧 `C6/C7=10pF` 表述不一致。 | 当前 BOM/PDF 显示 `X1=8MHz`、`XC53G2-8.000-F12NJHP`、`C3/C4=5.1pF`；用户确认 `CL=12pF`，C3/C4 采购选 C0G/NP0。 | 已关闭 |
| SCH-003 | BOOT | `PB2/BOOT1` 原先存在悬空风险。 | 当前 BOM/PDF 显示 `R21=10kΩ`；用户确认 PB2/BOOT1 已下拉到 GND。 | 已关闭 |
| SCH-004 | ADC | ADC 分压旧方案 `10kΩ/18kΩ` 使 5V 输入约 3.21V。 | 当前 BOM/PDF 显示 `R8/R9=12kΩ`、`R12/R13=18kΩ`，5V 标称输入映射为 `5V * 18kΩ / (12kΩ + 18kΩ) = 3.0V`。 | 已关闭 |
| SCH-005 | USB-C VBUS TVS | D5 网络和极性映射需要确认。 | 用户人工确认 D5 为 `SMF5.0A`，阴极接 `VBUS_FUSED`、阳极接 GND，符号、封装焊盘和实物极性映射一致。 | 已关闭 |
| SCH-006 | 硬件输出 | 最新原理图 PDF 和 BOM 需要重新导出并放入项目输出目录。 | 当前工作区存在 `hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf` 和 `hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx`。 | 已关闭 / 版本管理状态仍需用户确认 |
| SCH-007 | USB-C 型号 | 设计文档中的旧型号与当前 PDF/BOM 的 `TYPE-C-31-M-12` 不一致。 | 用户在 Altium 中确认 Rev A 当前唯一 USB-C 为 `TYPE-C-31-M-12`、立创 `C165948`；当前规格书、原理图 PDF、BOM 和设计文档已同步。据用户确认，旧 `TYPE-C 16PIN 2MD(073)` 的安装结构仅适配约 `0.8mm` 板厚，现仅保留为历史/已替代资料。 | 已关闭 |
| SCH-008 | USB Shield | 旧文档将 Shield 记录为 `R15=0Ω`，与 PDF/BOM 的 R15/C18 不一致。 | 用户确认当前实现为 `SHIELD -> (R15 1MΩ || C18 1nF) -> GND`；R15 提供直流参考/泄放，C18 提供高频噪声回流，该支路不替代专用 ESD 保护。 | 已关闭 |

## 5. 仍待 Altium 人工核对

| 编号 | 模块 | 待核对事项 | 风险等级 | 建议动作 | 状态 |
|---|---|---|---|---|---|
| EDA-001 | 关键器件封装 | STM32F103C8T6、AP2112K、CH340C、TPD2EUSB30、AO3400A、BAT54S、SS14、USB-C、开关和连接器的原理图库 Pin 与 PCB 封装 Pad Mapping。 | 中 | 在 Altium 中逐个核对库引脚号、焊盘号、封装模型和实际采购料号。 | 待 EDA 人工核对 |
| EDA-003 | U6 USB ESD | `TPD2EUSB30DRTR-N` 完整型号与实际 datasheet 的一致性，以及 U6 原理图针号与 SOT-723 封装焊盘映射。 | 中 | 对照 datasheet 和 Altium 封装逐脚核对。 | 待 EDA 人工核对 |
| EDA-004 | 极性和方向 | AO3400A、BAT54S、SS14、AP2112、CH340C、开关和连接器的封装方向、极性、丝印方向。 | 中 | 阶段 7 / 制造放行前逐项核对封装 1 脚、二极管色带、MOSFET G/S/D、LDO pin1 和 USB-C 方向。 | 待 EDA 人工核对 |
| EDA-005 | 接口与测试点 | PCB 接口朝向、丝印可读性、`TP_VBUS1/TP_1/TP_2/TP_GND1` 与 ADC/MOSFET 测试点可达性。 | 低/中 | 结合 PCB 布局检查接线习惯、探针空间和安全边界丝印。 | 待 EDA 人工核对 |
| EDA-006 | ERC | Altium ERC 是否存在未连接、重复驱动、电源端口、电气类型或 NC 标记问题。 | 视结果而定 | 仅在导出最新 ERC 报告或 Messages 截图后记录结果。 | 未提供报告，不声称已完成 |

## 6. 关键模块复核摘要

| 模块 | 当前实现摘要 | 后续关注 |
|---|---|---|
| MCU 最小系统 | `U1=STM32F103C8T6 LQFP48`；`R2=10kΩ` 下拉 BOOT0，`H2` 选择启动状态；`R21=10kΩ` 下拉 PB2/BOOT1；`SW2+C6=100nF` 复位；`H4` 为 SWD。 | LQFP48 pin mapping、BOOT 跳帽丝印、SWD 方向。 |
| HSE | `X1=8MHz XC53G2-8.000-F12NJHP`，`CL=12pF`，`C3/C4=5.1pF`。 | 晶振靠近 OSC_IN/OSC_OUT，短且对称、无过孔、远离大电流和高速信号；可选预留 OSC_OUT 串联电阻焊盘。 |
| VDDA / 去耦 | `R5=0Ω` 连接 3.3V 到 `VDDA_3V3`；`C7=100nF`、`C8=1uF`；数字 VDD 去耦 `C2/C5/C9=100nF`，`C1=4.7uF`。 | 去耦位置和回流路径。 |
| ADC | CH1：`U2`、`R8=12kΩ`、`R12=18kΩ`、`R10=330Ω`、`C10=10nF`、`D3=BAT54S`、`TP_ADC1 -> PA0`；CH2：`U3`、`R9=12kΩ`、`R13=18kΩ`、`R11=330Ω`、`C11=10nF`、`D4=BAT54S`、`TP_ADC2 -> PA1`。 | BAT54S 上钳位存在板卡断电、外部输入带电时反灌 VDDA 风险；固件采样时间建议 28.5 周期或更长。 |
| I2C | `U5` 使用 PB6/PB7，`R19/R20=4.7kΩ` 上拉到 3.3V，默认装配。 | 外部模块若自带上拉，会与板载上拉并联；连接多个模块前检查等效上拉和低电平灌电流。 |
| USB-C / 电源 | `USB1=TYPE-C-31-M-12`（立创 `C165948`）、`R14/R16=5.1kΩ` CC 下拉、`SHIELD -> (R15 1MΩ || C18 1nF) -> GND`、`F1`、`D5=SMF5.0A`、`SW3`，路径为 `VBUS_RAW -> F1 -> VBUS_FUSED -> SW3 -> +5V_SYS`；`U8=AP2112K-3.3TRG1`，`R17=10kΩ` EN 上拉，`C15/C16=1uF`，`C17=4.7uF`，`R18+LED2` 电源指示。 | USB-C 仅 5V；R15 提供直流参考/泄放、C18 提供高频回流且不替代专用 ESD；AP2112 热耗散和剩余制造门禁继续在 PCB 审查中跟踪。 |
| CH340C / USB ESD | `U7=CH340C`，`U6=TPD2EUSB30DRTR-N`，`C12/C14=100nF`，`C13=1uF`；CH340C TXD 接 `MCU_RX/PA10`，RXD 接 `MCU_TX/PA9`；CH340C 不需要外部晶振。 | U6 完整型号、SOT-723 pad mapping、USB-C/CH340C 封装方向。 |
| MOSFET 输出 | CH1：`R1=100Ω`、`R3=100kΩ`、`Q1=AO3400A`、`D1=SS14`、`H1`、`TP_GATE1/TP_OUT1`；CH2：`R6=100Ω`、`R7=100kΩ`、`Q2=AO3400A`、`D2=SS14`、`H3`、`TP_GATE2/TP_OUT2`。 | AO3400A G/S/D、SS14 色带方向、接口丝印和外部共地提示。 |
| 扩展接口 / 测试点 | `U4=SPI`，`U5=I2C`，`H6=USART2`，`H5=公用电源+GPIO`，`SW1` 用户按键，`LED1/R4` 用户 LED；电源测试点为 `TP_VBUS1 -> VBUS_RAW`、`TP_1 -> +5V_SYS`、`TP_2 -> 3.3V`、`TP_GND1 -> GND`。 | 不修改原理图测试点名称；文档中说明 `TP_1/TP_2` 分别代表 5V 和 3.3V。 |

## 7. BOM 记录原则

- 普通电阻、电容只要求具有明确阻值/容值。
- 普通阻容封装统一为 0603。
- 电阻采购时优先选择 1% 精度，ADC 分压电阻必须优先选择 1% 精度。
- 本轮不要求给所有普通阻容补齐完整耐压、功率、介质和容差字段。
- `C3/C4` 晶振负载电容采购时选 C0G/NP0。
- MCU、电源芯片、接口芯片、MOSFET、二极管、连接器等关键器件仍需明确型号、封装和方向。

## 8. 下一步操作

1. 在 [pcb_review.md](pcb_review.md) 中继续关闭阶段 7 的未关闭问题和制造门禁。
2. 由用户在 Altium 中完成剩余规则、封装方向、接口朝向、丝印、机械间隙和测试点可达性核对；AI/Codex 不声称代为完成。
3. 制造门禁关闭前不得写成 PCB、DRC 或制造输出已通过；用户可导出待放行制造输出用于阶段 7 Release Review，但不得提交板厂或建立最终制造归档包，放行完成后再进入阶段 8：焊接和硬件调试阶段。
