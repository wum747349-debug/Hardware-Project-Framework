# 器件选型计划与历史记录

> 文档状态：历史选型记录
> 适用阶段：阶段 2：关键器件选型阶段（历史记录）
> 适用对象：STM32 DAQ Control Board Rev A 的第一轮关键器件选型过程
> 最后核对依据：第一轮候选记录、当时 datasheet 与后续替代说明

## 1. 文档定位

本文合并保存第一轮关键器件选型计划、候选比较、替代关系和风险证据，不是最终 BOM，也不维护当前项目状态或完整当前参数。

当前主选摘要、模块电路和资料状态分别以 [../design_notes.md](../design_notes.md)、[module_design/](module_design/) 和 [../references.md](../references.md) 为准；实际实现以当前 Altium 源文件及可追溯 PDF/BOM 为准。本文与当前方案不同的内容均按历史语境理解。

## 2. 第一轮范围与方法

第一轮只选择会影响架构、供电、接口、外围、封装和 PCB Layout 的关键器件，普通阻容、LED、按键、排针、测试点和跳帽在模块参数明确后再选。用户负责在采购平台核对库存、价格、封装和 C 编号；关键参数必须回到 datasheet、reference manual 或 application note。

当时重点覆盖 MCU、USB-C、USB-UART、3.3V LDO、8MHz HSE、逻辑电平 N-MOSFET，以及 ADC 保护方向。

## 3. 历史选型结果

| 模块 | 当时器件 / C 编号 | 当时结论 | 关键比较结果 | 资料来源 |
| --- | --- | --- | --- | --- |
| MCU | `STM32F103C8T6` / C 编号当时待确认 | 已确定器件系列与 LQFP48 方向，仍需持续按 ST 官方资料核对 | 决定 3.3V 供电、BOOT、NRST、SWD、HSE、ADC 和 USART | `../references/datasheets/mcu/` 下 STM32F103 datasheet / reference manual |
| USB-C | `TYPE-C 16PIN 2MD(073)` / `C2765186` | 当时主选，后续替代 | 额定 DC 5V 3A 当时满足 5V 输入，但安装结构只适配约 0.8mm 板厚 | `../references/datasheets/usb_c/C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` |
| USB-UART | `CH340C` / `C84681` | 主选 | 内置时钟、无需外部 12MHz 晶振；必须采用 3.3V 供电并核对 V3/VCC | `../references/datasheets/usb_uart/C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` |
| 3.3V LDO | `AP2112K-3.3TRG1` / `C51118` | 主选 | 3.3V、标称 600mA；相比备选余量更大，但线性热耗散限制长期电流 | `../references/datasheets/power/C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` |
| 3.3V LDO | `HR73L33V` / `C54560861` | 备选 | 300mA，输出余量小于 AP2112K；外围 10µF、封装和采购状态当时待核对 | `../references/datasheets/power/C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` |
| HSE | `XC53G2-8.000-F12NJHP` / `C2842269` | 当时采用，后续延续 | 8MHz、`CL=12pF`、8–12MHz ESR 约 80Ω；当时确定 `C3/C4=5.1pF`，采购选 C0G/NP0 | `../references/datasheets/crystal/C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` |
| MOSFET | `AO3400A` / `C20917` | 主选 | 30V；RDS(on) 在 VGS=4.5V 时小于约 32mΩ、2.5V 时小于约 48mΩ，适合 3.3V GPIO 小电流低边开关 | `../references/datasheets/mosfet_output/C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` |
| ADC 保护 | 当时器件未完全确定 | 方向确定、器件后续收敛 | 需平衡分压、输入阻抗、采样时间、钳位漏电/电容与反灌风险；后续采用 BAT54S 及 12kΩ/18kΩ、330Ω、10nF 组合 | 当前依据见 ADC 模块文档与 `references.md` |

当时电源入口还选择了 `SMF5.0A` VBUS TVS、`C46640983` 0805 PPTC 和 HCTL/华灿天禄插件船型开关。它们的完整当前连接与参数由电源模块文档和资料索引维护。

## 4. 历史候选与替代关系

- USB-C：`TYPE-C 16PIN 2MD(073)`（C2765186）是第一轮主选。后续用户确认其安装结构仅适配约 0.8mm 板厚，因此退出 Rev A；当前唯一型号为 `TYPE-C-31-M-12`（C165948）。替代后的封装、Shield 和机械结论不由本文维护。
- LDO：`AP2112K-3.3TRG1` 为主选，`HR73L33V` 为备选；主要差异是输出电流余量、外围电容和热/采购条件。
- USB-UART：早期比较方向包含 CH340C、CH340N、CP2102N、FT232RL 和 FT230X，最终以外围少且有 3.3V 应用路径的 CH340C 收敛。
- MOSFET：早期搜索逻辑电平、30V、SOT-23 器件，AO3400A 因具有 2.5V/4.5V RDS(on) 数据而进入主选。
- HSE：早期比较 3225/5032 8MHz 无源晶振，最终采用上述 8MHz 器件；负载电容需结合晶振与 MCU 要求，而不是只按频率选择。

## 5. 历史风险与后续处理

| 编号 | 历史风险 | 等级 | 当时处理方向 / 当前边界 |
| --- | --- | --- | --- |
| R-01 | AP2112K 从 5V 线性降至 3.3V，负载上升会发热 | 中 | 按 `P=(5V-3.3V)×Iout` 评估；600mA 是能力上限，不是长期设计电流 |
| R-02 | CH340C 若以 5V UART 电平直连 STM32 会有风险 | 高 | 采用 3.3V 供电方案，TX/RX 与 USART1 交叉连接；当前实现仍以模块文档和 EDA 证据为准 |
| R-03 | 旧 USB-C 0.5mm pitch 手焊困难且安装结构不匹配当前板厚 | 中 | 型号已替代；旧器件仅保留历史追溯价值 |
| R-04 | HSE 的 CL、ESR、寄生与负载电容匹配影响起振和频偏 | 中 | 后续确认 `CL=12pF` 和 `C3/C4=5.1pF`；布局和起振仍需实际验证 |
| R-05 | AO3400A 驱动感性负载会产生反向能量和尖峰 | 高 | 必须提供续流路径或适用 TVS，不能依赖 MOSFET 本体 |
| R-06 | ADC 钳位器件的漏电、电容和钳位电流可能影响采样或造成反灌 | 中 | 后续模块设计需结合 MCU ADC 采样要求、保护器件资料和未上电场景核对 |
| R-07 | SMF5.0A 只提供瞬态保护，PPTC 不是精确限流器 | 中 | 均不能扩展为长期过压或精确限流能力；USB-C 维持 5V-only 边界 |
| R-08 | 船型开关孔距、外形和导通脚关系影响 PCB 机械与连接 | 中 | 由用户在 EDA/实物资料中核对，历史选型结论不能证明已实现 |

## 6. 当时结论与当前方案边界

第一轮结论支持后续模块设计，但不证明外围参数、封装映射、PCB 实现或制造验证已经完成。以下内容必须回到当前事实源：

- 当前器件与网络摘要：`design_notes.md`；
- 模块连接、局部计算和 Layout 要求：`docs/module_design/`；
- datasheet 路径和阅读状态：`references.md`；
- 实际器件、位号、封装和连接：当前 Altium 源文件及同版 PDF/BOM；
- PCB 问题、DRC 与制造结论：`docs/pcb_review.md`。

本文保留的数值均用于说明当时比较和决策依据，不应被自动视为当前 BOM 或已验证实现。
