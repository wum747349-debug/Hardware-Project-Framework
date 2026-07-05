# 参考资料

## 官方资料

> 后续补充 MCU datasheet、reference manual、application note、芯片数据手册等。

- STM32 目标型号 datasheet
- STM32 reference manual
- ST 官方硬件设计 application note
- USB-C 取电、3.3V 稳压、SWD、晶振、复位和 BOOT 相关官方资料

## 开源硬件参考项目

> 开源项目只作为结构、设计思路、文档组织和输出文件组织参考，不直接复制原理图、PCB、BOM、Gerber 或源文件。

更多开源参考项目统一记录在：`references/open_source_hardware_projects.md`

| 仓库名称 | GitHub 地址 | 参考用途 | 注意事项 |
| --- | --- | --- | --- |
| `devnithw/stm32-devboard` | <https://github.com/devnithw/stm32-devboard> | 参考 STM32F103 最小系统、USB 供电、3.3V 稳压、SWD、UART/I2C 引出和 KiCad 文档组织。 | 本仓库使用 Altium Designer，只参考结构；STM32 具体型号、时钟、BOOT、复位、SWD、USB 和接口必须重新核对 datasheet / reference manual。 |
| `phonght32/openSTM32F4_LQFP64` | <https://github.com/phonght32/openSTM32F4_LQFP64> | 参考完整 STM32F4 控制板结构、多电源输入、3.3V 电源、调试和外设接口组织，以及 BOM/Gerber/文档输出组织。 | 复杂度高于第一版项目，不能照搬；第一版仍优先简单、可焊接、可调试。 |

## 需要提取的学习点

- MCU 最小系统需要覆盖供电、去耦、时钟、复位、BOOT、下载调试接口和测试点。
- USB 供电和 3.3V 稳压需要明确输入保护、压降、热耗散、输出电流和指示方式。
- UART、I2C、SPI、ADC、MOSFET 输出等接口应按功能分组，方便调试和后续扩展。
- 制造输出应包含 PDF 原理图、BOM、Gerber、贴片坐标、装配说明和版本记录。

## 不可直接照抄的内容

- 第三方原理图、PCB、BOM、Gerber、生产文件和源工程文件。
- MCU 供电、晶振、BOOT、复位、SWD、USB、接口保护和测试点参数。
- 与本项目目标型号、封装、层数、板厂工艺、接口定义不一致的布局布线细节。
