# 参考资料

## 官方资料与器件资料

后续进入器件选型和原理图设计阶段时，需要优先查阅官方 datasheet、reference manual 和 application note。关键参数不得仅凭教程或开源项目确定。

需要查阅的资料包括：

- STM32F103C8T6 datasheet
- STM32F103 reference manual
- ST 硬件设计指南 / application note
- STM32 最小系统、HSE 晶振、BOOT、NRST、SWD、VDDA/VSSA 和 ADC 相关官方资料
- USB-C 取电与 CC 电阻相关资料
- USB-C ESD/TVS 保护器件 datasheet
- USB 转 UART 芯片 datasheet
- 3.3V LDO datasheet
- 保险丝或自恢复保险丝 datasheet
- ADC 输入保护、钳位或 TVS 器件 datasheet
- N-MOSFET datasheet
- 排针、USB-C 座、按键、LED 等连接器和结构器件资料

## 开源硬件参考项目

> 开源项目只作为结构、设计思路、接口组织、文档组织和制造输出组织参考，不能直接复制原理图、PCB、BOM、Gerber、生产文件、源工程文件或文字说明。

更多开源参考项目统一记录在：`references/open_source_hardware_projects.md`

| 仓库名称 | GitHub 地址 | 参考用途 | 注意事项 |
| --- | --- | --- | --- |
| `devnithw/stm32-devboard` | <https://github.com/devnithw/stm32-devboard> | 参考 STM32F103 最小系统、USB 供电、3.3V 稳压、SWD、UART/I2C 引出和 KiCad 文档组织。 | 本仓库使用 Altium Designer，只参考结构；STM32 具体型号、时钟、BOOT、复位、SWD、USB 和接口必须重新核对 datasheet / reference manual。 |
| `phonght32/openSTM32F4_LQFP64` | <https://github.com/phonght32/openSTM32F4_LQFP64> | 参考完整 STM32 控制板结构、多电源输入、3.3V 电源、调试和外设接口组织，以及 BOM/Gerber/文档输出组织。 | 复杂度高于第一版项目，不能照搬；第一版仍优先简单、可焊接、可调试。 |

## 可提炼的学习点

- MCU 最小系统需要覆盖供电、去耦、时钟、复位、BOOT、下载调试接口和测试点。
- USB-C 供电需要明确 5V 输入、CC 电阻、ESD/TVS、保险丝、电源开关、输入滤波和 3.3V 稳压。
- 第一版 USB 通信采用 USB 转 UART，不采用 STM32 原生 USB CDC；USB-C D+ / D- 不接 STM32 PA11 / PA12。
- UART、I2C、SPI、ADC、MOSFET 输出等接口应按功能分组，方便调试和后续扩展。
- ADC 外部 0-5V 输入必须经过分压、滤波、限流和保护后再进入 STM32 ADC 引脚。
- MOSFET 低边输出应明确 VLOAD / OUT / GND，共地要求、栅极电阻、下拉电阻和感性负载续流路径。
- 制造输出应包含 PDF 原理图、BOM、Gerber、贴片坐标、装配说明和版本记录。

## 不可直接照抄的内容

- 第三方原理图、PCB、BOM、Gerber、生产文件和源工程文件。
- 第三方项目的文字说明、README 和设计文档。
- MCU 供电、晶振、BOOT、复位、SWD、USB、接口保护和测试点参数。
- 与本项目目标型号、封装、层数、板厂工艺、接口定义不一致的布局布线细节。
- 未经本项目需求、器件 datasheet、封装、供电、接口和 PCB 工艺重新核对的任何开源电路片段。
