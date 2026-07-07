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

## 3. 当前已收集资料

| 文件名 | 所属模块 | 资料/器件名称 | 本地路径 | 来源说明 | 用途 | 是否已阅读 | 备注 |
|---|---|---|---|---|---|---|---|
| `STM32F103产品手册（中文）.pdf` | MCU 最小系统 | STM32F103 产品手册中文资料 | `references/datasheets/mcu/STM32F103产品手册（中文）.pdf` | ST 官方资料，来源路径待确认 | MCU 供电、引脚、外设、ADC、时钟等参数核对 | 未系统阅读 | 需确认版本/日期 |
| `STM32F103产品手册（英文）.pdf` | MCU 最小系统 | STM32F103 datasheet 英文资料 | `references/datasheets/mcu/STM32F103产品手册（英文）.pdf` | ST 官方资料，来源路径待确认 | MCU 参数主依据 | 未系统阅读 | 优先以英文版核对关键参数 |
| `STM32中文参考手册V10.pdf` | MCU 最小系统 | STM32F10x reference manual 中文资料 | `references/datasheets/mcu/STM32中文参考手册V10.pdf` | ST 官方资料，来源路径待确认 | 外设、时钟、ADC、USART、GPIO 配置依据 | 未系统阅读 | 需确认适用系列和版本 |
| `C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | USB-C 输入与保护 | TYPE-C 16PIN 2MD(073) USB-C 母座规格书 | `references/datasheets/usb_c/C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | 疑似立创商城下载，来源待确认 | USB-C 封装、引脚、机械尺寸、VBUS/GND/CC/D+/D- 连接核对 | 已初步阅读 / 待进一步核对关键参数 | 进入候选；CC1/CC2 需各接 5.1kΩ 下拉到 GND；额定 5V 3A 满足本项目 5V 输入；需评估 ESD、防反接/过流保护、Shield 接地和 0.5mm pitch 可焊接性 |
| `C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 晶振 | XC53G2-8.000-F12NJHP 8MHz 晶振规格书 | `references/datasheets/crystal/C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 疑似立创商城下载，来源待确认 | HSE 晶振频率、ESR、负载电容范围、封装核对 | 已初步阅读 / 待进一步核对关键参数 | 进入候选；8MHz 属于基频范围，8MHz-12MHz ESR 约 80Ω；当前资料未能仅凭型号确认 CL=12pF，需结合 STM32 datasheet / reference manual / 硬件设计指南进一步核对 |
| `C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 3.3V 电源 | HR73L33V / HR73 系列 LDO 规格书 | `references/datasheets/power/C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 疑似立创商城下载，来源待确认 | 3.3V LDO 输入输出、电容、热耗散核对 | 已初步阅读 / 待进一步核对关键参数 | 备选，不作为当前主选；输出电流 300mA，余量小于 AP2112；典型外围电容为 10µF；需确认具体封装、热阻和采购状态 |
| `C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` | MOSFET 低边输出 | AO3400A N-MOSFET 规格书 | `references/datasheets/mosfet_output/C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` | 疑似立创商城下载，来源待确认 | 2 路 N-MOSFET 低边输出的 VDS、RDS(on)、3.3V GPIO 驱动能力和封装热能力核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；VDS=30V，满足 VLOAD 5V-12V、最大不超过 12V；VGS=4.5V 时 RDS(on) 小于约 32mΩ，VGS=2.5V 时小于约 48mΩ；感性负载必须额外考虑续流二极管或 TVS |
| `C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` | 3.3V 电源 | AP2112K-3.3TRG1 LDO 规格书 | `references/datasheets/power/C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` | 疑似立创商城下载，来源待确认 | USB-C 5V 输入转 3.3V 的输出电压、电流能力、输入/输出电容、EN 和热耗散核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；3.3V 输出、600mA 能力；典型应用输入/输出各 1µF，建议 X5R/X7R；SOT25 线性稳压热耗散需按 P=(5V-3.3V)*Iout 评估 |
| `C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` | USB 转 UART | CH340C USB 转 UART 规格书 | `references/datasheets/usb_uart/C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` | 疑似立创商城下载，来源待确认 | USB2.0 全速、UART 波特率、内置时钟、3.3V 供电和 TX/RX 连接核对 | 已初步阅读 / 待进一步核对关键参数 | 进入主选；应按 3.3V 供电方案设计，VCC 接 3.3V，V3 与 VCC/3.3V 连接；TXD 接 STM32 PA10/USART1_RX，RXD 接 PA9/USART1_TX；不建议 5V 供电后直连 STM32 UART |
| `C720477_轻触开关_TS-1088-AR02016_规格书_WJ1589447.PDF` | 接口、人机、测试点 | TS-1088-AR02016 轻触按键规格书 | `references/datasheets/connectors/C720477_轻触开关_TS-1088-AR02016_规格书_WJ1589447.PDF` | 疑似立创商城下载，来源待确认 | 按键封装和机械尺寸核对 | 未系统阅读 | 普通外围器件，非第一轮重点 |

## 4. 下一步优先收集资料

只列第一轮关键器件资料，不列所有外围器件：

- STM32F103C8T6 官方资料补充/核对：确认 datasheet、reference manual、硬件设计 application note 的版本和适用范围。
- USB 转 UART 候选 datasheet：CH340C、CH340N、CP2102N、FT232RL、FT230X 等。
- 3.3V LDO 候选 datasheet：根据 5V 输入、3.3V 输出、负载电流、压差、热耗散和输入输出电容要求筛选。
- USB-C 母座 datasheet / 封装图：确认 VBUS/GND/CC1/CC2/D+/D-、固定脚、焊盘尺寸和机械强度。
- 8MHz 晶振 datasheet：确认负载电容、ESR、频率精度、封装和 STM32 HSE 匹配性。
- 逻辑电平 N-MOSFET datasheet：确认 3.3V 栅极驱动下的 Rds(on)、Vds、Id、封装热能力和感性负载保护需求。

## 5. 立创商城搜索记录

立创商城搜索记录统一维护在：

`projects/01_STM32_DAQ_Control_Board/references/lcsc_parts/lcsc_search_notes.md`

搜索记录只作为候选筛选和资料入口记录。最终设计参数必须回到 datasheet、reference manual 或 application note 核对。

当前已初步核对的关键器件仅表示进入主选、备选或候选记录，不等同于最终 BOM。后续原理图参数、外围阻容、保护器件和封装焊盘仍必须以 datasheet、reference manual 或 application note 为准，立创商品页只作为 C 编号、库存、价格、封装和资料入口参考。
