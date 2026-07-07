# 设计说明

## 当前设计定位

本项目第一版定位为 `STM32F103C8T6 数据采集/控制开发板`，重点训练低压嵌入式硬件设计的完整流程：需求定义、最小系统、电源输入与保护、通信接口、ADC 输入、MOSFET 输出、PCB Layout、上电调试和测试验证。

第一版优先保证可实现、可焊接、可调试和文档完整，不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

## MCU 选择说明

MCU 确定为 `STM32F103C8T6`。

选择原因：

- 器件常见，资料丰富。
- 适合 STM32 入门、最小系统和基础外设训练。
- LQFP48 方向适合手焊练习和 2 层板布局训练。
- Keil、STM32CubeMX、ST-Link/SWD 调试链路成熟。

后续原理图阶段需要根据 STM32F103C8T6 datasheet / reference manual 核对封装、引脚、电源脚、去耦、BOOT、NRST、SWD、HSE 和 ADC 等细节。

## 时钟设计说明

外部高速晶振确定为 `8MHz`，用于训练 STM32 常见 HSE 时钟设计。

晶振型号、负载电容、匹配电容、启动条件、布线和接地处理后续必须根据 STM32F103C8T6 datasheet、reference manual 和 ST 硬件设计资料核对，本阶段不写死未经验证的具体参数。

## USB-C 与串口通信说明

第一版使用 USB-C 作为 5V 供电入口，同时通过 USB 转 UART 芯片实现电脑与 STM32 的串口通信。

采用 USB 转 UART，而不是 STM32 原生 USB，原因是：

- 降低第一版固件复杂度。
- 降低 USB 硬件调试复杂度。
- 电脑端 COM 串口更适合早期打印日志、调试命令和数据上传。
- 有利于先把电源、最小系统、串口、ADC 和 MOSFET 控制链路跑通。

设计边界：

- USB-C D+ / D- 连接 USB 转 UART 芯片。
- USB-C D+ / D- 不连接 STM32 PA11 / PA12。
- STM32 PA11 / PA12 第一版不作为 USB 功能使用。
- USB 转 UART 与 STM32 之间使用 3.3V UART 电平。
- 推荐使用 USART1，USB 转 UART TXD 接 PA10，USB 转 UART RXD 接 PA9，注意 TX/RX 交叉。

USB-C CC 电阻、ESD/TVS、USB 转 UART 芯片型号、供电方式和逻辑电平后续需要根据 datasheet / application note 核对。

## 电源设计说明

第一版电源路径为 USB-C 输入 5V，经电源保护和电源开关后转换为 3.3V。

3.3V 供电对象包括 STM32、USB 转 UART 芯片逻辑侧、LED、接口上拉和其他低压外围电路。

需要预留或评估：

- 电源开关
- 保险丝或自恢复保险丝
- TVS / ESD 保护
- 输入滤波
- 3.3V 稳压电路
- 电源指示 LED
- 5V、3.3V、GND 测试点

保险丝、TVS、LDO、USB-C CC 电阻、电源指示 LED 限流电阻等参数后续必须根据器件 datasheet / application note 核对。

## ADC 输入设计说明

第一版设计 2 路 ADC 输入。板级外部接口允许接入 `0-5V` 信号，但 STM32 ADC 引脚实际只能接收 `0-3.3V` 范围内的电压。

因此 ADC 前端必须完成：

- 将 0-5V 外部信号通过电阻分压缩放到 0-3.3V 以内。
- 串联限流，降低异常输入或钳位时的风险。
- 加入 RC 低通滤波，满足基础采集和抗干扰需求。
- 预留或评估钳位/TVS 保护。
- 在分压后、进入 MCU 前的节点预留测试点。

第一版 ADC 目标是功能验证和基础采集，不追求高精度测量。分压比例、输入阻抗、RC 参数、采样时间、保护器件漏电和误差预算后续需要根据 STM32 ADC 规格和器件 datasheet 核对。

## MOSFET 输出设计说明

第一版设计 2 路 N-MOSFET 低边开关输出，用于小电流负载控制训练，不做大电流驱动。

当前使用边界：

- 推荐使用电流 `<=300mA`。
- 设计目标可按 `<=500mA` 预留。
- 负载电源允许外部输入。
- 外部负载电源必须与板子 GND 共地。
- 若驱动感性负载，必须考虑续流路径。

每路输出建议包含 GPIO 控制、栅极串联电阻、栅极下拉电阻、输出排针、VLOAD / OUT / GND 标识、MOSFET 栅极测试点和输出节点测试点。

MOSFET 型号后续需要根据 3.3V 栅极驱动能力、Rds(on)、封装散热、负载电流和保护需求核对 datasheet。

## 接口与调试设计说明

第一版接口形式暂定为排针，便于手工连线、示波器/万用表测量和固件调试。

需要保留：

- SWD 下载调试接口
- USB-C 接口
- UART 通信/扩展接口
- I2C 传感器接口
- SPI 扩展接口
- 2 路 ADC 输入排针
- 2 路 MOSFET 输出排针
- 5V / 3.3V / GND 测试点或扩展引脚

测试点优先覆盖 5V、3.3V、GND、NRST、SWDIO、SWCLK、USART TX/RX、USB 转 UART 芯片关键电源、ADC 分压后节点、MOSFET 栅极和 MOSFET 输出端。

## 后续需核对事项

- STM32F103C8T6 datasheet / reference manual 中的供电、时钟、复位、BOOT、SWD、USART 和 ADC 要求。
- ST 硬件设计指南或 application note 中的最小系统、电源、晶振和 PCB Layout 建议。
- USB-C 取电、CC 电阻、ESD/TVS 和 USB 转 UART 芯片应用资料。
- LDO、TVS/ESD、保险丝、MOSFET、分压电阻和接口保护器件 datasheet。
