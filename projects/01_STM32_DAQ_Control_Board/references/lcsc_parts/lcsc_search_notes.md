# 立创商城搜索记录

## 使用原则

- 用户手动在立创商城搜索器件。
- AI/Codex 提供搜索关键词和筛选条件。
- 立创商品页用于查看 C 编号、库存、价格、封装、基础库/扩展库、资料入口。
- 最终设计参数必须回到 datasheet 核对。
- 不凭商品页截图或简介直接确定关键参数。
- AI/Codex 不默认自动爬取或批量下载立创商城资料。

## 搜索记录模板

| 日期 | 模块 | 搜索关键词 | 筛选条件 | 候选器件 | 立创 C 编号 | 厂商 | MPN | 封装 | 基础库/扩展库 | 库存情况 | 下载的 datasheet 路径 | 初步结论 | 放弃原因 | 下一步动作 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 2026-07-07 关键器件搜索记录

| 日期 | 模块 | 搜索关键词 | 筛选条件 | 候选器件 | 立创 C 编号 | 厂商 | MPN | 封装 | 基础库/扩展库 | 库存情况 | 下载的 datasheet 路径 | 初步结论 | 放弃原因 | 下一步动作 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-07-07 | MOSFET 低边输出 | AO3400A N-MOSFET SOT-23 逻辑电平 | VDS >= 30V；RDS(on) 需有 2.5V/4.5V 条件；适合 3.3V GPIO 驱动；小电流低边开关 | AO3400A | C20917 | 待用户在立创商城确认 | AO3400A | SOT-23，待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/mosfet_output/C20917_场效应管(MOSFET)_AO3400A_规格书_WJ180398.PDF` | 进入主选；适合作为 2 路 N-MOSFET 低边输出，推荐使用电流 <=300mA，设计预留 <=500mA；感性负载必须额外加续流二极管或 TVS | 无 | 原理图阶段预留栅极串联电阻、栅极下拉电阻、Gate/OUT/GND 测试点，并继续核对热耗散和感性负载保护 |
| 2026-07-07 | 3.3V 电源 | AP2112K-3.3 LDO 600mA SOT25 | USB 5V 输入；3.3V 输出；输出能力 >=300mA；外围简单；资料完整 | AP2112K-3.3TRG1 | C51118 | 待用户在立创商城确认 | AP2112K-3.3TRG1 | SOT25，待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/power/C51118_线性稳压器(LDO)_AP2112K-3.3TRG1_规格书_WJ19433.PDF` | 进入主选；3.3V 输出、600mA 能力，适合 USB-C 5V 输入转 3.3V；输入/输出各 1µF 电容，建议 X5R/X7R；EN 需明确处理 | 无 | 核对 SOT25 热阻和 5V->3.3V 线性稳压功耗，第一版 3.3V 总电流长期建议控制在 150mA-200mA 以内 |
| 2026-07-07 | 3.3V 电源 | HR73L33V LDO 3.3V 低静态电流 | 3.3V 输出；宽输入/低静态电流作为备选；输出电流和外围电容需核对 | HR73L33V | C54560861 | 待用户在立创商城确认 | HR73L33V | 待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/power/C54560861_线性稳压器(LDO)_HR73L33V_规格书_HR73+SERIES_REV1.0.PDF` | 进入备选，不作为当前主选；输入耐压高、静态电流低，但输出电流 300mA，余量小于 AP2112；典型外围电容为 10µF | 输出电流余量和项目匹配度不如 AP2112 | 保留为备选；后续仅在需要宽输入或低功耗方案时重新评估 |
| 2026-07-07 | USB 转 UART | CH340C USB UART 内置晶振 3.3V | 支持 USB2.0 全速；UART 满足调试；无需外部晶振；可按 3.3V UART 电平连接 STM32 | CH340C | C84681 | 待用户在立创商城确认 | CH340C | 待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/usb_uart/C84681_USB转换芯片_CH340C_规格书_CH340DS1_CN.PDF` | 进入主选，但必须 3.3V 供电；VCC 接 3.3V，V3 与 VCC/3.3V 连接；TXD 接 STM32 PA10/USART1_RX，RXD 接 STM32 PA9/USART1_TX，TX/RX 必须交叉 | 无 | 原理图阶段核对 3.3V 供电应用、电源去耦、D+/D- 连接和 USB ESD 防护；不采用 5V 供电后直连 STM32 UART |
| 2026-07-07 | USB-C 输入与 USB2.0 数据 | TYPE-C 16PIN 2MD 073 USB-C 母座 | 5V 输入；USB2.0 D+/D-；需 CC1/CC2 引脚；封装可用于 2 层板第一版 | TYPE-C 16PIN 2MD(073) | C2765186 | 待用户在立创商城确认 | TYPE-C 16PIN 2MD(073) | 0.5mm pitch，待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/usb_c/C2765186_USB连接器_TYPE-C+16PIN+2MD(073)_规格书_TYPE-C+16PIN+2MD(073).PDF` | 历史候选 / 已替代；据用户确认，其安装结构仅适配约 0.8mm 板厚，不作为 Rev A 当前型号 | 板厚不适配当前 1.6mm nominal 基线 | 保留历史资料，不作为当前封装依据 |
| 2026-07-29 | USB-C 输入与 USB2.0 数据 | TYPE-C-31-M-12 C165948 USB-C 母座 | 5V 输入；USB2.0 D+/D-；需适配当前 1.6mm nominal 板厚及现有封装 | TYPE-C-31-M-12 | C165948 | 用户已确认 | TYPE-C-31-M-12 | 以当前规格书为准 | 待投产前复核 | 待投产前复核 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/usb_c/C165948_USB连接器_TYPE-C-31-M-12_规格书_WJ310728.PDF` | Rev A 唯一当前型号；与用户 Altium 确认及当前 PDF/BOM 一致 | 无 | 阶段 11 继续核对安装孔、板边和关键器件机械间隙 |
| 2026-07-07 | HSE 晶振 | 8MHz SMD passive crystal 5.0x3.2 | 8MHz；无源晶振；ESR、CL、封装和 STM32 HSE 匹配性需核对 | XC53G2-8.000-F12NJHP | C2842269 | 待用户在立创商城确认 | XC53G2-8.000-F12NJHP | 5.0mm x 3.2mm x 1.3mm 两焊盘贴片，待用户在立创商城确认 | 待用户在立创商城确认 | 待用户在立创商城确认 | `projects/01_STM32_DAQ_Control_Board/references/datasheets/crystal/C2842269_无源晶振_XC53G2-8.000-F12NJHP_规格书_WJ72563.PDF` | 进入候选，负载电容待确认；8MHz 属于基频范围，8MHz-12MHz ESR 约 80Ω；当前资料未能只根据 F12 确认 CL=12pF | 无 | 结合 STM32 datasheet / reference manual / 硬件设计指南核对 HSE 负载电容、匹配电容、启动裕量和布局要求 |
