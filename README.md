# Hardware Practice Projects

本仓库用于记录硬件设计实战项目，重点训练原理图设计、PCB Layout、器件选型、样板调试、测试验证和项目文档整理能力。

## 项目列表

1. STM32 数据采集/控制开发板
2. 单节锂电池充电与保护电源板
3. 基于 STM32 + 运放 + ADC 的模拟信号采集板

## 工具链

- EDA 软件：Altium Designer
- STM32 配置工具：STM32CubeMX
- 固件开发：Keil MDK
- 文档：Markdown
- 版本管理：Git / GitHub

## 项目目标

通过三个硬件项目系统强化以下能力：

- MCU 最小系统设计
- USB-C 供电设计
- 3.3V 电源设计
- UART / I2C / SPI 通信接口设计
- ADC 采集与输入保护
- MOSFET 低边驱动设计
- 单节锂电池充电与保护
- 运放模拟前端设计
- 外置 ADC 与参考电压设计
- PCB 布局布线
- 上电调试与测试记录
- 项目文档与简历项目整理

## 仓库结构

- `docs/`：通用项目路线、工具链、设计规范和调试模板
- `references/`：数据手册、应用笔记、开源项目和学习资料索引
- `common/`：通用模板、复用电路和测试工具说明
- `projects/`：三个硬件实战项目
- `checklists/`：原理图、PCB、上电、发布检查表
- `prompts/`：用于 AI 协助硬件设计的提示词模板

## 当前优先级

当前优先完成：

1. `01_STM32_DAQ_Control_Board`
2. `02_LiIon_Charger_Protection_Board`
3. `03_STM32_OpAmp_ADC_Acquisition_Board`
