# 开源硬件参考项目索引

> 本索引只记录可学习的开源硬件项目来源和参考方向。禁止直接复制第三方项目的原理图、PCB、BOM、Gerber、生产文件、源工程文件或文字说明作为本仓库成果。

## 01_STM32_DAQ_Control_Board

| 仓库名称                           | GitHub 地址                                         | 参考用途                                                                        | 可参考内容                                    | 注意事项                                                                                                                            | 是否允许直接复用           |
| ------------------------------ | ------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `devnithw/stm32-devboard`      | <https://github.com/devnithw/stm32-devboard>      | 参考 STM32F103 最小系统、USB 供电、3.3V 稳压、SWD 调试接口、UART/I2C 引出和 KiCad 项目文档组织方式。      | MCU 最小系统模块划分、电源与调试接口组织、外设引出思路、项目目录和文档组织。 | 该项目是 KiCad 项目，本仓库使用 Altium Designer，只参考结构，不直接复制文件。STM32 具体型号、供电、时钟、BOOT、复位、SWD、USB 和接口设计必须重新根据 datasheet / reference manual 核对。 | 否，只能参考结构和思路，不能直接照抄 |
| `phonght32/openSTM32F4_LQFP64` | <https://github.com/phonght32/openSTM32F4_LQFP64> | 参考完整 STM32F4 控制板结构，以及多电源输入、3.3V 电源、JTAG/SWD、UART、I2C、SPI、ADC、DAC、PWM 等接口组织。 | 控制板系统结构、接口分组方式、BOM/Gerber/文档/制造输出的组织方式。  | 项目复杂度高于本仓库第一版 STM32 数据采集/控制开发板，不能照搬。第一版项目仍应优先保持简单、可焊接、可调试。                                                                      | 否，只能参考结构和思路，不能直接照抄 |

## 02_LiIon_Charger_Protection_Board

| 仓库名称 | GitHub 地址 | 参考用途 | 可参考内容 | 注意事项 | 是否允许直接复用 |
| --- | --- | --- | --- | --- | --- |
| `SolderedElectronics/Li-ion-charger-with-protection-hardware-design` | <https://github.com/SolderedElectronics/Li-ion-charger-with-protection-hardware-design> | 参考 USB-C 输入、单节锂电池充电、保护电路、充电状态 LED，以及 BOM、Gerber、3D 文件和制造输出文件组织。 | 充电与保护功能块划分、状态指示、输出文件分类方式。 | 锂电池充电电流、热设计、保护阈值、接口极性必须根据目标芯片 datasheet 和实际电池规格重新计算。不允许直接照抄电源路径和保护参数。 | 否，只能参考结构和思路，不能直接照抄 |
| `SolderedElectronics/1S-Li-Ion-battery-protection-hardware-design` | <https://github.com/SolderedElectronics/1S-Li-Ion-battery-protection-hardware-design> | 参考 1S 锂电池保护电路、CAD/OUTPUTS 文件夹组织，以及 BOM、iBOM、PDF 原理图、STEP、Gerber 等输出物管理。 | 保护板功能边界、输出资料命名、制造输出管理方式。 | 保护芯片型号、MOSFET 型号、过充、过放、过流、短路保护参数必须重新核对。本仓库只记录学习点，不复制对方生产文件。 | 否，只能参考结构和思路，不能直接照抄 |
| `sparkfun/Lipo_Charger_Basic-microUSB` | <https://github.com/sparkfun/Lipo_Charger_Basic-microUSB> | 参考简单单节 LiPo/Li-Ion 充电板、充电 IC、状态 LED、电池接口、micro-USB 输入的最小实现，以及 Eagle 硬件工程和生产文件组织。 | 最小充电板功能组成、状态 LED 设计思路、电池接口和生产文件组织方式。 | 该项目是 micro-USB，本仓库计划 USB-C 输入，不能直接照搬接口部分。充电电流、USB-C CC 电阻、热设计和电池接口极性必须重新设计。 | 否，只能参考结构和思路，不能直接照抄 |

## 03_STM32_OpAmp_ADC_Acquisition_Board

| 仓库名称 | GitHub 地址 | 参考用途 | 可参考内容 | 注意事项 | 是否允许直接复用 |
| --- | --- | --- | --- | --- | --- |
| `JacobParent7/Mixed-Signal-STM32-Dev-Board` | <https://github.com/JacobParent7/Mixed-Signal-STM32-Dev-Board> | 参考 STM32 混合信号硬件设计、USB-C 供电、模拟电源、ADC/DAC、偏置、滤波、混合信号 PCB 布局、模拟/数字区域划分、回流路径控制，以及项目 README 中的系统级需求、框图、Layout 展示和制造结果记录。 | 混合信号系统需求组织、模拟/数字功能分区、ADC/DAC 与偏置/滤波模块划分、布局检查项和制造结果记录方式。 | 该项目是 4 层混合信号 PCB，本仓库第三个项目可以参考思路，但不要一开始追求同等复杂度。运放供电范围、输入共模范围、输出摆幅、ADC 输入阻抗、参考电压、滤波截止频率都必须重新计算和验证。 | 否，只能参考结构和思路，不能直接照抄 |
