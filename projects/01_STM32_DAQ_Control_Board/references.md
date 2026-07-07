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
| `C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | USB-C 输入与保护 | USB-C 16P 母座规格书 | `references/datasheets/usb_c/C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | 疑似立创商城下载，来源待确认 | USB-C 封装、引脚、机械尺寸核对 | 未系统阅读 | 商品页不能替代规格书 |
| `C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 晶振 | XC53G2-8.000-F12NJHP 8MHz 晶振规格书 | `references/datasheets/crystal/C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 疑似立创商城下载，来源待确认 | HSE 晶振频率、负载电容、ESR、封装核对 | 未系统阅读 | 需结合 STM32 HSE 要求核对 |
| `C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 3.3V 电源 | HR73L33V / HR73 系列 LDO 规格书 | `references/datasheets/power/C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 疑似立创商城下载，来源待确认 | 3.3V LDO 输入输出、电容、热耗散核对 | 未系统阅读 | 需确认具体 MPN、封装和输出电流 |
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
