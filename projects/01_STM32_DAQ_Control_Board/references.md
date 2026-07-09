# 参考资料

## 1. 资料使用原则

- 官方 datasheet / reference manual / application note 优先。
- 立创商城用于用户手动搜索器件、检查库存/价格/封装/基础库状态、记录 C 编号和下载 datasheet。
- AI/Codex 不默认自动爬取或批量下载立创商城资料。
- 立创商品页不能替代 datasheet。
- 开源项目只能作为结构、模块划分、接口组织和检查项参考，不能照抄原理图、PCB、BOM、Gerber 或文字说明。
- 如果资料来源、版本或器件型号不确定，应标记“来源待确认”，并在关键参数定稿前回到厂商官网核对。

## 2. 本地 datasheet 目录

| 目录 | 用途 |
|---|---|
| `references/datasheets/mcu/` | STM32 datasheet、reference manual、application note、硬件设计指南 |
| `references/datasheets/usb_uart/` | USB 转 UART 芯片 datasheet 和应用资料 |
| `references/datasheets/power/` | LDO、电源开关、保险丝、TVS、电源保护等资料 |
| `references/datasheets/usb_c/` | USB-C 母座、封装图、USB-C 取电相关资料 |
| `references/datasheets/crystal/` | HSE 晶振、负载电容和封装资料 |
| `references/datasheets/adc_input/` | ADC 输入保护、钳位、专用 TVS 等资料 |
| `references/datasheets/mosfet_output/` | MOSFET、续流二极管、输出 TVS 等资料 |
| `references/datasheets/connectors/` | 排针、按键、LED、测试点、跳帽和普通连接器等资料 |

## 3. 模块设计文档索引

以下文档用于承接设计说明和原理图审查入口；datasheet 路径、来源和阅读状态仍以本文后续资料表为准。

| 模块 | 模块设计文档 |
|---|---|
| MCU 最小系统 | `docs/module_design/01_mcu_minimum_system.md` |
| USB-C 供电与 AP2112K 电源 | `docs/module_design/02_usb_c_power_ap2112.md` |
| USB 转 UART / CH340C | `docs/module_design/03_usb_uart_ch340c.md` |
| ADC 输入保护 | `docs/module_design/04_adc_input_protection.md` |
| MOSFET 低边输出 | `docs/module_design/05_mosfet_low_side_output.md` |
| 接口、测试点与丝印 | `docs/module_design/06_interfaces_testpoints.md` |

## 4. 当前已收集资料

| 文件名 | 所属模块 | 资料/器件名称 | 本地路径 | 来源说明 | 用途 | 是否已阅读 | 备注 |
|---|---|---|---|---|---|---|---|
| `STM32F103产品手册（中文）.pdf` | MCU 最小系统 | STM32F103 产品手册中文资料 | `references/datasheets/mcu/STM32F103产品手册（中文）.pdf` | ST 官方资料，来源路径待确认 | MCU 供电、引脚、外设、ADC、时钟等参数核对 | 未系统阅读 | 需确认版本/日期 |
| `STM32F103产品手册（英文）.pdf` | MCU 最小系统 | STM32F103 datasheet 英文资料 | `references/datasheets/mcu/STM32F103产品手册（英文）.pdf` | ST 官方资料，来源路径待确认 | MCU 参数主依据 | 未系统阅读 | 优先以英文版核对关键参数 |
| `STM32中文参考手册V10.pdf` | MCU 最小系统 | STM32F10x reference manual 中文资料 | `references/datasheets/mcu/STM32中文参考手册V10.pdf` | ST 官方资料，来源路径待确认 | 外设、时钟、ADC、USART、GPIO 配置依据 | 未系统阅读 | 需确认适用系列和版本 |
| `C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | USB-C 输入与保护 | TYPE-C 16PIN 2MD(073) USB-C 母座规格书 | `references/datasheets/usb_c/C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | 疑似立创商城下载，来源待确认 | USB-C 封装、引脚、机械尺寸、VBUS/GND/CC/D+/D- 连接核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；CC1/CC2 需各接 5.1kΩ 下拉到 GND；额定 5V 3A 满足本项目 5V 输入；需评估 ESD、防反接/过流保护、Shield 接地和 0.5mm pitch 可焊接性 |
| `C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 晶振 | XC53G2-8.000-F12NJHP 8MHz 晶振规格书 | `references/datasheets/crystal/C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 疑似立创商城下载，来源待确认 | HSE 晶振频率、ESR、负载电容范围、封装核对 | 已初步阅读 / 待进一步核对关键参数 | 进入候选；8MHz 属于基频范围，8MHz-12MHz ESR 约 80Ω；当前资料未能仅凭型号确认 CL=12pF，需结合 STM32 datasheet / reference manual / 硬件设计指南进一步核对 |
| `C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 3.3V 电源 | HR73L33V / HR73 系列 LDO 规格书 | `references/datasheets/power/C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 疑似立创商城下载，来源待确认 | 3.3V LDO 输入输出、电容、热耗散核对 | 已初步阅读 / 待进一步核对关键参数 | 备选，不作为当前主选；输出电流 300mA，余量小于 AP2112；典型外围电容为 10µF；需确认具体封装、热阻和采购状态 |
| `C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` | MOSFET 低边输出 | AO3400A N-MOSFET 规格书 | `references/datasheets/mosfet_output/C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` | 疑似立创商城下载，来源待确认 | 2 路 N-MOSFET 低边输出的 VDS、RDS(on)、3.3V GPIO 驱动能力和封装热能力核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；30V N-Channel MOSFET，SOT-23；VDS=30V，满足 VLOAD 5V-12V、最大不超过 12V；ID=5.7A @ VGS=10V 为规格条件值，不作为本项目大电流设计依据；VGS=4.5V 时 RDS(on) 小于约 32mΩ，VGS=2.5V 时小于约 48mΩ；当前模块设计使用 PB0/PB1 通过 100Ω 栅极电阻和 100kΩ 下拉驱动 2 路低边开关；感性负载使用 SS14 续流保护 |
| `C83852_肖特基二极管_SS14_规格书_WJ201776.PDF` | MOSFET 低边输出 | SS14 肖特基整流二极管规格书 | `references/datasheets/mosfet_output/C83852_肖特基二极管_SS14_规格书_WJ201776.PDF` | 疑似立创商城下载，来源待确认 | MOSFET 低边输出感性负载续流保护、封装、极性、反向耐压、正向电流和正向压降核对 | 已初步阅读 / 待进一步核对封装与 PCB 焊盘 | 进入 D4/D5 续流二极管主选；SMA / DO-214AC；色带端为阴极 K，接 VLOAD_EXT；阳极 A 接 MOS_OUT；关键参数包括 VRRM=40V、IF(AV)=1A、IFSM=40A、VF=500mV max @1A、PD=1.1W、RθJA=88°C/W |
| `C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` | 3.3V 电源 | AP2112K-3.3TRG1 LDO 规格书 | `references/datasheets/power/C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` | 疑似立创商城下载，来源待确认 | USB-C 5V 输入转 3.3V 的输出电压、电流能力、输入/输出电容、EN 和热耗散核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；3.3V 输出、600mA 能力；典型应用输入/输出各 1µF，建议 X5R/X7R；SOT25 线性稳压热耗散需按 P=(5V-3.3V)*Iout 评估 |
| `C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` | USB 转 UART | CH340C USB 转 UART 规格书 | `references/datasheets/usb_uart/C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` | 疑似立创商城下载，来源待确认 | USB2.0 全速、UART 波特率、内置时钟、3.3V 供电、USB D+/D- 和 TX/RX 连接核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；本次模块设计按 SOP-16、3.3V 供电方案记录，VCC 接 3.3V，V3 接 3.3V，VCC/V3 各 100nF 去耦并加 1uF 局部储能；USB_DP 接 D+/UD+，USB_DM 接 D-/UD-，不串 22Ω；TXD 接 STM32 PA10/USART1_RX，RXD 接 PA9/USART1_TX；R232 接 GND；未用握手脚加 No Connect；第一版不做 DTR/RTS 自动下载 |
| `TPD2EUSB30DRTR-N datasheet` | USB 数据线 ESD | TPD2EUSB30DRTR-N 双路低电容 USB ESD 保护器件 | 待用户保存到 `references/datasheets/usb_c/` 或 `references/datasheets/usb_uart/` 后补充路径 | 厂商 datasheet 待补充本地文件 | USB_DP/USB_DM 双路 ESD 防护、VRWM、结电容、IEC 61000-4-2、封装、方向、GND 引脚和焊盘核对 | 本地 datasheet 路径待补充 / 资料项未关闭 | 进入 USB 数据线 ESD 主选；当前模块设计记录 D2 Pin1/I/O 接 USB_DP、Pin2/I/O 接 USB_DM、Pin3/GND 接 GND；D2 为并联钳位器件，不接 3.3V，也不接 VBUS/5V；当前待复核参数包括 VRWM=5V、I/O-to-GND 结电容典型 0.45pF/最大 0.6pF、接触放电 ±20kV、空气放电 ±25kV；封装、方向、GND 引脚和焊盘仍需基于本地 datasheet 复核 |
| `C7420333_肖特基二极管_BAT54S_规格书_BAT54+THRU+BAT54S_REV2.0.PDF` | ADC 输入保护 | BAT54S 肖特基二极管规格书 | `references/datasheets/adc_input/C7420333_肖特基二极管_BAT54S_规格书_BAT54+THRU+BAT54S_REV2.0.PDF` | 疑似立创商城下载，来源待确认 | ADC 输入上下轨钳位、封装、VF、漏电、结电容和钳位电流核对 | 已初步阅读 / 待进一步核对封装与引脚映射 | 进入 ADC 输入上下轨钳位主选；SOT-23；Pin3 接 ADC 节点，Pin1 接 GND，Pin2 接 VDDA_3V3；关键参数包括 VR=30V、IF(AV)=200mA、VF=320mV max @1mA、CT=10pF max |
| `C720477_轻触开关_TS-1088-AR02016_规格书_WJ1589447.PDF` | 接口、人机、测试点 | TS-1088-AR02016 轻触按键规格书 | `references/datasheets/connectors/C720477_轻触开关_TS-1088-AR02016_规格书_WJ1589447.PDF` | 疑似立创商城下载，来源待确认 | 按键封装和机械尺寸核对 | 未系统阅读 | 普通外围器件，非第一轮重点 |

## 5. 下一步优先核对资料 / 仍需补充资料

当前 CH340C、AP2112K-3.3TRG1、HR73L33V、AO3400A、USB-C 母座和 8MHz 晶振已进入初步阅读记录。下一步重点从“收集候选资料”转为“关闭原理图前关键问题”，同时按需补充尚未下载或尚未确定的保护器件资料。

- STM32F103C8T6 官方资料：继续核对 datasheet、reference manual、硬件设计 application note 的版本、适用范围、最小系统、HSE、ADC、USART、BOOT、NRST、SWD 和 VDDA/VSSA 要求。
- MCU 最小系统原理图审查前核对：重点确认 LQFP48 的 pin5/pin6 HSE、pin7 NRST、pin8 VSSA、pin9 VDDA、VDD/VSS/VBAT、BOOT0、PA13/PA14 SWD 连接是否与官方资料一致。
- USB-C 与 USB2.0 保护资料：补充或核对 USB ESD/TVS、VBUS TVS、保险丝/自恢复保险丝、电源开关和输入滤波器件资料。
- USB-C 供电模块资料：补充或核对 `SMF5.0A` VBUS TVS、`C46640983` PPTC 自恢复保险丝、HCTL / 华灿天禄插件船型开关的 datasheet / 封装图；重点确认 TVS 极性、PPTC Vmax=6V 只适合 5V 输入、船型开关实际导通脚和孔距。
- CH340C 应用资料：重点核对 3.3V 供电方案、V3/VCC 连接、D+/D- 接法、去耦和 USB ESD 防护。
- AP2112K-3.3TRG1 电源资料：继续核对 EN、输入/输出电容、ESR/陶瓷电容要求、热阻、功耗和 3.3V 总电流预算。
- 原理图前电源网络核对项：统一使用 `VBUS_RAW`、`VBUS_FUSED`、`+5V_SYS`、`3.3V`、`GND`；确认 USB-C 仅支持 5V 输入，不支持 USB-PD 9V/12V，并在后续 PCB 丝印中标注 `USB-C 5V ONLY`。
- HSE 晶振资料：继续核对 XC53G2-8.000-F12NJHP 的负载电容 CL、匹配电容、ESR、频率精度和 STM32 HSE 匹配性。
- 原理图前待核对项：确认 `C6/C7=10pF` 仅为临时标注值，最终需由晶振 `CL`、PCB 寄生电容和 STM32 硬件设计资料反推；确认 `PC14/PC15` 为 LSE 32.768kHz 引脚，本项目 8MHz HSE 不使用它们。
- MOSFET 输出保护资料：SS14 datasheet 已补充并初步阅读，当前确认其用于 D4/D5 感性负载续流保护；后续 PCB 前重点复核 SMA / DO-214AC 封装、色带端/阴极接 `VLOAD_EXT`、阳极接 `MOS_OUT`、焊盘方向和丝印方向；若未来驱动更高能量感性负载，再评估 TVS、栅极保护、走线宽度和热耗散。
- ADC 输入保护资料：补充分压、限流、RC 滤波、钳位/TVS 方案相关 datasheet，重点关注漏电、电容、钳位电流和采样误差。

## 6. 立创商城搜索记录

立创商城搜索记录统一维护在：

`projects/01_STM32_DAQ_Control_Board/references/lcsc_parts/lcsc_search_notes.md`

搜索记录只作为候选筛选和资料入口记录。最终设计参数必须回到 datasheet、reference manual 或 application note 核对。

当前已初步核对的关键器件仅表示进入主选、备选或候选记录，不等同于最终 BOM。后续原理图参数、外围阻容、保护器件和封装焊盘仍必须以 datasheet、reference manual 或 application note 为准，立创商品页只作为 C 编号、库存、价格、封装和资料入口参考。
