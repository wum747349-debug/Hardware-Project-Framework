# Hardware Practice Projects

本仓库用于记录硬件设计实战项目，重点训练原理图设计、PCB Layout、器件选型、样板调试、测试验证和项目文档整理能力。

本仓库不仅用于当前三个硬件实战项目，也可作为后续低压嵌入式硬件项目的模板工作区。

## 当前项目列表

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
- `docs/08_Project_Workflow.md`：硬件项目标准执行流程，覆盖需求、设计、审查、制造、调试、测试和简历整理
- `docs/AI_Context_Guide.md`：AI 协作上下文读取规则，用于限制不同任务下应读取的项目文件、Skill、模板和历史记录
- `references/`：数据手册、应用笔记、开源项目和学习资料索引
- `references/open_source_hardware_projects.md`：开源硬件参考项目索引，只用于记录结构、设计思路、文档组织和输出文件组织方式
- `common/`：通用模板、复用电路和测试工具说明
- `projects/`：当前硬件实战项目及后续新增项目
- `projects/*/references.md`：每个项目的官方资料、开源参考项目、需要提取的学习点和不可照抄内容
- `skills/`：硬件项目阶段 Skill，只保存阶段方法、输入输出格式和关键风险提醒；细化检查项优先放入 `checklists/`
- `templates/`：可复用硬件项目模板，后续新增项目时可复制使用
- `docs/Project_Template_Guide.md`：硬件项目模板使用说明和新增项目流程
- `checklists/`：原理图、PCB、上电、发布检查表
- `prompts/`：用于 AI 协助硬件设计的提示词模板

## 参考资料原则

- 开源硬件项目只作为结构、设计思路、文档组织和输出文件组织方式参考，不直接照抄原理图、PCB、BOM、Gerber、生产文件或源工程文件。
- 本仓库最终设计必须以 datasheet、reference manual、application note 和实际项目需求为依据。
- 每个项目的 `references.md` 需要记录官方资料、开源参考项目、学习点和不可直接复用的内容。

## 当前优先级

当前优先完成：

1. `01_STM32_DAQ_Control_Board`
2. `02_LiIon_Charger_Protection_Board`
3. `03_STM32_OpAmp_ADC_Acquisition_Board`
