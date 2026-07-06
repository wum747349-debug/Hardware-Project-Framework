
# Codex / Claude 硬件项目任务提示词模板

本文档用于整理在 `Hardware-Practice-Projects` 仓库中使用 Codex / Claude / 其他 AI 编程助手时的常用提示词。

使用原则：

- 每次任务先说明“当前项目”和“当前阶段”。

- 默认要求 AI 按 `docs/AI_Context_Guide.md` 读取最小必要上下文。

- 不要让 AI 默认读取所有项目目录、所有 Skill、所有模板和所有历史记录。

- 不要让 AI 直接修改无关项目。

- 涉及关键硬件参数时，必须回到 datasheet、reference manual 或 application note 核对。

- 如果本次有文件修改并提交，要求 AI 输出修改文件、修改原因、风险点、下一步建议和 commit hash；如果只是审查或分析，则说明未修改仓库文件。


---

## 1. 使用前需要替换的字段

复制下面任一提示词前，建议先替换这些字段：

| 字段 | 替换为 |
|---|---|
| 当前项目 | 本次任务对应的 `projects/...` 路径 |
| 当前阶段 | 需求整理 / datasheet 阅读 / 器件选型 / 原理图设计 / 原理图审查 / PCB Layout / PCB 审查 / 上电调试 / 测试报告 / 文档整理 |
| 目标器件 | 本次要阅读、选型或审查的具体器件型号 |
| 输入资料 | 原理图 PDF、PCB 截图、datasheet 链接、测试记录或用户补充说明 |
| 修改范围 | 本次允许 AI 修改的文件或目录 |
| 禁止范围 | 其他项目目录、`templates/`、Altium 工程、firmware 或硬件输出文件等 |
| 完成后输出 | 是否需要提交；如提交则输出 commit hash，如不修改仓库文件则说明未修改 |

---

## 2. 当前项目路径速查表

| 项目 | 路径 | 优先关注 |
|---|---|---|
| STM32 数据采集/控制开发板 | `projects/01_STM32_DAQ_Control_Board` | MCU 最小系统、USB-C 供电、3.3V 电源、ADC 输入保护、MOSFET 低边驱动、通信接口和测试点 |
| 单节锂电池充电与保护板 | `projects/02_LiIon_Charger_Protection_Board` | 充电管理、保护路径、电池接口、输入输出保护、热风险、安全测试和限流上电 |
| STM32 + 运放 + ADC 模拟采集板 | `projects/03_STM32_OpAmp_ADC_Acquisition_Board` | 模拟前端、运放供电范围、ADC 输入范围、参考电压、输入保护、噪声和布局隔离 |

提示：

- 当前任务只涉及一个项目时，只读取该项目目录下与任务相关的文件。

- 不要因为仓库有三个项目，就默认读取全部项目目录。

- `templates/` 只在新增项目或维护模板时读取。


---

## 3. 通用任务开头模板

适用于所有任务。每次给 Codex / Claude 发任务时，建议先加这一段。

```text
你现在协助我维护 GitHub 仓库：

wum747349-debug/Hardware-Practice-Projects

默认分支：main

当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
【在这里填写：需求整理 / datasheet 阅读 / 器件选型 / 原理图设计 / 原理图审查 / PCB Layout / 上电调试 / 测试报告 / 文档整理】

请按 docs/AI_Context_Guide.md 读取最小必要上下文。

要求：
1. 不要读取其他项目目录，除非本任务明确要求跨项目对比。
2. 不要读取 templates/，除非本任务是新增项目或维护模板。
3. 不要默认读取所有 Skill，只读取当前阶段需要的 Skill。
4. 不要修改与本任务无关的文件。
5. 涉及关键硬件参数时，必须提示需要核对 datasheet / reference manual / application note。
6. 如果本次有文件修改并提交，请输出修改文件、主要修改点、风险点、下一步建议和 commit hash；如果只是审查或分析，请说明未修改仓库文件。
```

---

## 4. 新聊天接手仓库 / 刷新上下文提示词

适用于新开 Codex / Claude 会话，或你刚刚 push 了仓库，需要 AI 重新认识当前仓库规则。

```text
你现在接手并协助维护 GitHub 仓库：

wum747349-debug/Hardware-Practice-Projects

默认分支：main

请以 GitHub 云端仓库为事实源，不要依赖旧聊天记忆。

本次只做上下文刷新和仓库规则理解，不要修改文件。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. README.md
5. docs/08_Project_Workflow.md

请输出：
1. 当前仓库定位；
2. 当前核心项目；
3. AI 协作时的最小必要上下文策略；
4. 硬件项目的标准推进流程；
5. 后续处理具体任务时应如何选择读取文件。
```

---

## 5. 当前项目需求细化提示词

适用于项目刚开始，还没有进入 datasheet 阅读和器件选型前。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
需求细化

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. projects/01_STM32_DAQ_Control_Board/README.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/block_diagram.md
7. projects/01_STM32_DAQ_Control_Board/design_notes.md
8. projects/01_STM32_DAQ_Control_Board/references.md

任务：
1. 审查当前 requirements.md 是否足够支撑后续器件选型和原理图设计。
2. 补充第一版必须明确的参数边界，包括：
   - USB-C 输入方式；
   - 3.3V 电源预计电流；
   - MCU 选型约束；
   - ADC 输入电压范围；
   - ADC 输入保护要求；
   - MOSFET 负载类型和最大电流；
   - UART / I2C / SPI 接口形式；
   - 按键、LED、测试点要求；
   - PCB 层数、尺寸、手焊约束。
3. 更新 requirements.md，使其更适合作为后续设计依据。
4. 如有必要，轻微更新 block_diagram.md 和 design_notes.md。
5. 不要开始画原理图。
6. 不要修改其他项目目录。

完成后请输出：
1. 修改了哪些文件；
2. 需求中已经明确的内容；
3. 仍然待确认的问题；
4. 是否可以进入 datasheet 阅读和器件选型阶段；
5. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 6. MCU 初步选型提示词

适用于在 STM32F103C8T6、STM32G030/G031、STM32G431 等候选型号之间做第一版选择。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
MCU 初步选型

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. skills/hardware-component-selection/SKILL.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/references.md

任务：
1. 对比 STM32F103C8T6、STM32G030/G031、STM32G431 是否适合第一版 STM32 数据采集/控制开发板。
2. 对比维度包括：
   - 资料完整度；
   - CubeMX 支持；
   - Keil MDK 支持；
   - 封装焊接难度；
   - GPIO 数量；
   - ADC 能力；
   - UART / I2C / SPI 数量；
   - SWD 调试；
   - 供电和最小系统复杂度；
   - 第一版项目风险。
3. 给出第一版推荐主控型号。
4. 给出至少一个备选型号。
5. 更新 design_notes.md 中的 MCU 选型部分。
6. 更新 references.md 中需要后续补充的官方资料清单。

注意：
- 不要只凭经验下结论，必须标注后续需要核对的 datasheet / reference manual 项目。
- 不要开始画原理图。
- 不要修改其他项目目录。

完成后请输出：
1. 推荐 MCU；
2. 推荐理由；
3. 不推荐或暂缓使用的型号及原因；
4. 已修改文件；
5. 下一步 datasheet 阅读任务建议；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 7. Datasheet 阅读 / 官方资料提取提示词

适用于确定某个关键器件后，提取 datasheet 关键参数。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
datasheet 阅读 / 官方资料提取

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/，不要读取器件选型 Skill 和原理图审查 Skill，除非确有必要。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. skills/hardware-datasheet-reading/SKILL.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/references.md
7. projects/01_STM32_DAQ_Control_Board/design_notes.md

目标器件：
【填写器件型号，例如 STM32F103C8T6 / AMS1117-3.3 / AO3400A / USB-C 连接器等】

任务：
1. 根据 hardware-datasheet-reading Skill 提取该器件的关键参数。
2. 重点提取：
   - 工作电压范围；
   - 推荐工作条件；
   - 绝对最大额定值；
   - 引脚功能；
   - 典型应用电路；
   - 外围器件推荐值；
   - PCB Layout 注意事项；
   - 风险项；
   - 当前项目是否适用。
3. 明确哪些参数已经确认，哪些参数仍需后续核对。
4. 更新 references.md，记录官方资料来源和需要提取的内容。
5. 更新 design_notes.md，记录与当前项目相关的设计依据。

注意：
- 不要把 Absolute Maximum Ratings 当作正常设计工作点。
- 不要直接照抄典型应用电路，必须结合当前项目需求分析。
- 不要修改其他项目目录。

完成后请输出：
1. 器件结论；
2. 关键参数表；
3. 当前项目适配性；
4. 风险与待确认项；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 8. 器件选型 / BOM 初稿提示词

适用于确定 MCU、电源、MOSFET、接口、保护器件等关键器件。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
器件选型 / BOM 初稿

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. skills/hardware-component-selection/SKILL.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/references.md

按需读取：
- skills/hardware-datasheet-reading/SKILL.md，仅在需要重新提取或核对 datasheet 参数时读取。

任务：
1. 为第一版 STM32 数据采集/控制开发板确定关键器件初稿。
2. 至少覆盖：
   - STM32 MCU；
   - USB-C 供电接口；
   - 3.3V LDO；
   - SWD 调试接口；
   - UART / I2C / SPI 排针；
   - ADC 输入保护和滤波器件；
   - MOSFET 低边驱动器件；
   - LED；
   - 按键；
   - 测试点；
   - 常用电阻电容。
3. 每类关键器件给出主选型号和至少一个替代型号。
4. 说明推荐原因、风险等级和需要核对的 datasheet 项目。
5. 更新 design_notes.md。
6. 如仓库已有 BOM 草稿位置，则新增或更新 BOM 草稿；如果没有，先建议 BOM 草稿文件路径，不要随意新建复杂格式。

注意：
- 不要直接照抄开源项目 BOM。
- 不要推荐明显采购困难、封装过难或资料不完整的器件作为第一版主选。
- 不要忽略替代料。
- 不要修改其他项目目录。

完成后请输出：
1. 当前推荐器件表；
2. 关键参数核对表；
3. 选型风险；
4. 待核对 datasheet 项目；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 9. 单节锂电池充电与保护板专用提示词

适用于推进第二个项目的需求细化、资料提取、器件选型或原理图设计前检查。

```text
当前项目：
projects/02_LiIon_Charger_Protection_Board

当前阶段：
【在这里填写：需求整理 / datasheet 阅读 / 器件选型 / 原理图设计准备 / 原理图审查 / PCB Layout 前检查 / 上电调试 / 测试报告】

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. 当前阶段对应的 Skill：
   - datasheet 阅读：skills/hardware-datasheet-reading/SKILL.md
   - 器件选型 / BOM 初稿：skills/hardware-component-selection/SKILL.md
   - 原理图审查：skills/hardware-schematic-review/SKILL.md
5. projects/02_LiIon_Charger_Protection_Board/requirements.md
6. projects/02_LiIon_Charger_Protection_Board/design_notes.md
7. projects/02_LiIon_Charger_Protection_Board/references.md
8. 如本阶段需要，再读取该项目的 block_diagram.md 或 docs/ 下对应记录

任务：
1. 围绕单节锂电池充电与保护板，审查当前阶段是否具备进入下一步的依据。
2. 重点关注：
   - 输入接口和电源路径；
   - 充电管理芯片资料；
   - 电池保护芯片资料；
   - 电池连接器和极性；
   - MOSFET、保险/保护器件和状态指示；
   - 热风险；
   - 测试点；
   - 限流上电和有人看管测试流程。
3. 只记录已由 datasheet / application note 支撑的结论。
4. 对充电电流、保护阈值、热设计、MOSFET 参数等关键内容，标注资料来源或待核对项。
5. 根据当前阶段更新 requirements.md、design_notes.md、references.md 或对应 docs 记录。

注意：
- 不要直接照抄开源锂电池项目电路或 BOM。
- 不要在没有 datasheet 依据时确定充电电流、保护阈值、热设计或 MOSFET 选型结论。
- 不要修改其他项目目录。
- 不要读取 templates/。

完成后请输出：
1. 当前结论；
2. 已确认依据；
3. 高风险项；
4. 待核对 datasheet / application note 项目；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 10. STM32 + 运放 + ADC 模拟信号采集板专用提示词

适用于推进第三个项目的需求细化、资料提取、器件选型、原理图设计前检查或原理图审查。

```text
当前项目：
projects/03_STM32_OpAmp_ADC_Acquisition_Board

当前阶段：
【在这里填写：需求整理 / datasheet 阅读 / 器件选型 / 原理图设计准备 / 原理图审查 / PCB Layout 前检查 / 上电调试 / 测试报告】

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. 当前阶段对应的 Skill：
   - datasheet 阅读：skills/hardware-datasheet-reading/SKILL.md
   - 器件选型 / BOM 初稿：skills/hardware-component-selection/SKILL.md
   - 原理图审查：skills/hardware-schematic-review/SKILL.md
5. projects/03_STM32_OpAmp_ADC_Acquisition_Board/requirements.md
6. projects/03_STM32_OpAmp_ADC_Acquisition_Board/design_notes.md
7. projects/03_STM32_OpAmp_ADC_Acquisition_Board/references.md
8. 如本阶段需要，再读取该项目的 block_diagram.md 或 docs/ 下对应记录

任务：
1. 围绕 STM32 + 运放 + ADC 模拟信号采集板，审查当前阶段是否具备进入下一步的依据。
2. 重点关注：
   - 输入信号范围和保护；
   - 运放供电范围、输入共模范围和输出摆幅；
   - ADC 输入范围、采样接口和参考电压；
   - STM32 与 ADC 的接口电平和通信方式；
   - 模拟地、数字地、参考电压和噪声隔离；
   - 测试点和校准记录；
   - PCB Layout 前的模拟/数字区域规划。
3. 只记录已由 datasheet / reference manual / application note 支撑的结论。
4. 对运放输入输出范围、ADC 满量程、参考电压精度、滤波参数和保护参数等关键内容，标注资料来源或待核对项。
5. 根据当前阶段更新 requirements.md、design_notes.md、references.md 或对应 docs 记录。

注意：
- 不要在没有 datasheet 依据时确定运放、ADC、参考电压或输入保护的关键参数。
- 不要忽略输入保护、限流、参考电压稳定性、模拟噪声和 PCB 回流路径。
- 不要修改其他项目目录。
- 不要读取 templates/。

完成后请输出：
1. 当前结论；
2. 已确认依据；
3. 信号链风险点；
4. 待核对 datasheet / reference manual / application note 项目；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 11. 原理图绘制前准备提示词

适用于正式打开 Altium 画原理图前，先规划模块、网络名和页面结构。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
原理图绘制前准备

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. projects/01_STM32_DAQ_Control_Board/requirements.md
5. projects/01_STM32_DAQ_Control_Board/block_diagram.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/references.md

任务：
1. 根据当前需求和器件选型，规划第一版原理图模块。
2. 建议原理图按以下模块组织：
   - USB-C 5V 输入；
   - 输入保护 / 滤波；
   - 3.3V 电源；
   - STM32 最小系统；
   - SWD 调试接口；
   - UART / I2C / SPI 扩展接口；
   - ADC 输入 × 2；
   - MOSFET 低边驱动输出 × 2；
   - LED；
   - 按键；
   - 测试点。
3. 给出每个模块需要包含的器件、关键信号、测试点和注意事项。
4. 给出推荐网络命名。
5. 给出建议的 Altium 原理图页面组织方式。
6. 更新 design_notes.md 中的原理图设计规划部分。

注意：
- 不要直接生成未经核对的最终原理图连接结论。
- 涉及关键参数时标注需要核对 datasheet。
- 不要修改其他项目目录。

完成后请输出：
1. 原理图模块划分；
2. 每个模块的设计依据；
3. 网络命名建议；
4. 测试点建议；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 12. 原理图审查提示词

适用于你已经在 Altium 中画出原理图，导出 PDF 或截图后，让 AI 审查。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
原理图审查

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. skills/hardware-schematic-review/SKILL.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/references.md
8. 当前项目的原理图 PDF / 图片 / Altium 导出文件

按需读取：
- skills/hardware-datasheet-reading/SKILL.md，仅在需要核对关键器件参数时读取。
- skills/hardware-component-selection/SKILL.md，仅在需要追溯选型依据时读取。
- projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md，仅在继续审查或追踪历史问题时读取。

任务：
1. 按 hardware-schematic-review Skill 审查当前原理图。
2. 重点检查：
   - USB-C 供电和 CC 电阻；
   - 输入保护和滤波；
   - 3.3V 电源芯片外围电路；
   - STM32 VDD / VDDA / VSS / VSSA；
   - 去耦电容；
   - NRST；
   - BOOT；
   - SWD；
   - UART / I2C / SPI；
   - ADC 输入保护和滤波；
   - MOSFET 低边驱动；
   - LED 和按键；
   - 测试点；
   - 封装和可制造性。
3. 输出“可以进入 PCB Layout / 修改后再进入 PCB Layout / 存在高风险暂不建议进入 PCB Layout”三种结论之一。
4. 将审查结果写入 projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md。
5. 如有必要，更新 design_notes.md 中的问题和修改依据。

注意：
- 不要只说“看起来没问题”。
- 不要跳过电源、电池、ADC、MOSFET、运放、参考电压等高风险模块。
- 不要在没有 datasheet 依据时确认关键连接完全正确。
- 不要修改其他项目目录。

完成后请输出：
1. 当前结论；
2. 问题清单；
3. 高风险项；
4. 需要核对 datasheet 的项目；
5. 建议增加的测试点；
6. 是否可以进入 PCB Layout；
7. 已修改文件；
8. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 13. PCB Layout 前检查提示词

适用于原理图审查通过后，进入 PCB Layout 前做布局规划。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
PCB Layout 前检查

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. docs/08_Project_Workflow.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md
8. 当前项目原理图 PDF / 图片

任务：
1. 根据原理图和审查结果，给出 PCB Layout 前的布局规划建议。
2. 重点规划：
   - USB-C 接口位置；
   - 电源路径；
   - 3.3V LDO 和输入输出电容；
   - STM32 位置；
   - SWD 接口可达性；
   - UART / I2C / SPI 排针位置；
   - ADC 输入区域；
   - MOSFET 输出和负载接口；
   - 测试点位置；
   - 安装孔和丝印；
   - 模拟输入与数字开关输出的隔离。
3. 给出 2 层 PCB 的布局优先级和走线注意事项。
4. 更新 design_notes.md 或新增 PCB Layout 规划记录。

注意：
- 不要直接修改 Altium PCB 文件，除非用户明确要求。
- 不要忽略回流路径、去耦电容位置、电源线宽和测试点可达性。
- 不要修改其他项目目录。

完成后请输出：
1. PCB 布局分区建议；
2. 走线优先级；
3. 风险点；
4. 需要在 PCB 审查阶段重点检查的项目；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 14. PCB 审查提示词

适用于 PCB Layout 初版完成后，让 AI 根据截图、PDF 或导出文件审查。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
PCB 审查

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. docs/08_Project_Workflow.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md
8. 当前项目 PCB 截图 / PDF / Altium 导出文件

任务：
1. 审查 PCB Layout 是否适合进入打样。
2. 重点检查：
   - 电源线宽；
   - GND 回流路径；
   - 去耦电容是否靠近芯片电源脚；
   - USB-C 和电源入口布局；
   - STM32 周边晶振、复位、BOOT、SWD；
   - ADC 输入走线是否远离开关噪声；
   - MOSFET 大电流路径；
   - 测试点是否可接触；
   - 丝印是否清晰；
   - 接插件方向是否防呆；
   - 安装孔和板边间距；
   - DRC/ERC 报告问题。
3. 将审查结果写入 projects/01_STM32_DAQ_Control_Board/docs/pcb_review.md。
4. 给出是否可以输出制造文件的结论。

注意：
- 不要只看美观，要重点检查可制造性、可焊接性、可调试性和安全风险。
- 不要修改其他项目目录。

完成后请输出：
1. 当前结论；
2. PCB 问题清单；
3. 高风险项；
4. 建议修改；
5. 是否可以输出 Gerber；
6. 已修改文件；
7. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 15. 制造文件输出检查提示词

适用于准备打样前，检查输出文件是否完整。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
制造文件输出检查

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. docs/08_Project_Workflow.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md
8. projects/01_STM32_DAQ_Control_Board/docs/pcb_review.md
9. projects/01_STM32_DAQ_Control_Board/hardware/outputs/ 下的输出文件

任务：
1. 检查制造输出是否完整。
2. 至少检查：
   - PDF 原理图；
   - BOM；
   - Gerber；
   - 钻孔文件；
   - 贴片坐标；
   - DRC/ERC 报告；
   - fabrication package；
   - 版本说明；
   - 下单参数记录。
3. 检查输出文件命名是否清晰。
4. 检查是否有不应提交的大型临时文件。
5. 给出是否可以提交打样的结论。

完成后请输出：
1. 输出文件完整性检查表；
2. 缺失文件；
3. 下单前必须确认的问题；
4. 是否可以打样；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 16. 上电调试提示词

适用于板子焊接完成后，记录首次上电和功能验证。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
上电调试

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. docs/08_Project_Workflow.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md
8. projects/01_STM32_DAQ_Control_Board/docs/pcb_review.md
9. projects/01_STM32_DAQ_Control_Board/docs/bringup_log.md

任务：
1. 生成或更新上电调试计划。
2. 首次上电必须使用限流电源。
3. 按以下顺序设计调试步骤：
   - 外观检查；
   - 短路检查；
   - 电源入口检查；
   - 3.3V 电源检查；
   - 静态电流检查；
   - STM32 供电检查；
   - NRST / BOOT 检查；
   - SWD 下载检查；
   - LED 检查；
   - 按键检查；
   - UART / I2C / SPI 检查；
   - ADC 输入检查；
   - MOSFET 输出检查。
4. 将调试记录写入 docs/bringup_log.md。
5. 对异常现象记录：现象、可能原因、排查步骤、结果、后续修改建议。

注意：
- 不允许无人看管上电测试。
- 不要跳过限流电源和短路检查。
- 不要修改其他项目目录。

完成后请输出：
1. 上电调试步骤；
2. 安全注意事项；
3. 已记录的测试结果；
4. 异常问题清单；
5. 下一步测试建议；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 17. 测试报告提示词

适用于功能测试完成后整理测试报告。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
测试报告

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. docs/08_Project_Workflow.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/docs/bringup_log.md
7. projects/01_STM32_DAQ_Control_Board/docs/test_report.md

任务：
1. 根据需求和调试记录整理测试报告。
2. 测试报告应包括：
   - 测试目的；
   - 测试环境；
   - 测试仪器；
   - 测试项目；
   - 测试步骤；
   - 测试结果；
   - 异常现象；
   - 结论；
   - 后续改进建议。
3. 将内容写入 docs/test_report.md。
4. 标注哪些功能已经验证，哪些功能未验证。

完成后请输出：
1. 测试覆盖情况；
2. 已通过项目；
3. 未通过或未测试项目；
4. 风险点；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 18. 改版记录提示词

适用于发现硬件问题后，整理 V1.1 / V2 修改依据。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
改版记录

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. projects/01_STM32_DAQ_Control_Board/design_notes.md
5. projects/01_STM32_DAQ_Control_Board/docs/schematic_review.md
6. projects/01_STM32_DAQ_Control_Board/docs/pcb_review.md
7. projects/01_STM32_DAQ_Control_Board/docs/bringup_log.md
8. projects/01_STM32_DAQ_Control_Board/docs/test_report.md
9. projects/01_STM32_DAQ_Control_Board/docs/revision_history.md

任务：
1. 根据审查、调试和测试记录整理改版问题。
2. 每个问题记录：
   - 问题编号；
   - 现象；
   - 原因分析；
   - 修改方案；
   - 影响范围；
   - 验证方法；
   - 是否必须改；
   - 优先级。
3. 将内容写入 docs/revision_history.md。
4. 区分“必须修改”和“建议优化”。

完成后请输出：
1. 改版问题清单；
2. 高优先级修改项；
3. 建议优化项；
4. 下一版设计重点；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 19. 简历项目整理提示词

适用于项目完成一个闭环后，整理成简历项目描述。

```text
当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
简历项目整理

请按 docs/AI_Context_Guide.md 读取最小必要上下文，不要读取其他项目目录，不要读取 templates/。

请读取：
1. PROJECT_RULES.md
2. AGENTS.md
3. docs/AI_Context_Guide.md
4. projects/01_STM32_DAQ_Control_Board/README.md
5. projects/01_STM32_DAQ_Control_Board/requirements.md
6. projects/01_STM32_DAQ_Control_Board/design_notes.md
7. projects/01_STM32_DAQ_Control_Board/docs/bringup_log.md
8. projects/01_STM32_DAQ_Control_Board/docs/test_report.md
9. projects/01_STM32_DAQ_Control_Board/docs/revision_history.md

任务：
1. 根据项目实际完成情况整理简历项目描述。
2. 输出两个版本：
   - 简历版，3 到 5 条 bullet；
   - 面试讲解版，按项目背景、个人工作、关键设计、调试问题、结果总结组织。
3. 不要夸大未完成内容。
4. 不要把开源项目成果写成本项目成果。
5. 标注哪些内容需要等实际测试完成后再补充。

完成后请输出：
1. 简历版项目描述；
2. 面试讲解版；
3. 可量化成果占位；
4. 仍需补充的实测数据；
5. 已修改文件；
6. 如果本次有文件修改并提交，则输出 commit hash；如果只是审查或分析，则说明未修改仓库文件。
```

---

## 20. 通用审查 Codex / Claude 执行结果提示词

适用于 Codex / Claude 做完任务后，把它的结果发给另一个 AI 审查。

```text
这是 Codex / Claude 对 Hardware-Practice-Projects 仓库的执行结果。

当前项目：
projects/01_STM32_DAQ_Control_Board

当前阶段：
【填写阶段】

请你以 GitHub 云端仓库为事实源审查这次修改，不要依赖旧聊天记忆。

请重点检查：
1. 是否遵守 docs/AI_Context_Guide.md 的最小必要上下文策略；
2. 是否只修改了当前任务相关文件；
3. 是否误读或修改了其他项目目录；
4. 是否误读或修改了 templates/；
5. 是否引入未经 datasheet 支撑的硬件结论；
6. 是否更新了该阶段应该更新的项目文档；
7. Markdown 格式是否正常；
8. 是否还有需要继续优化的问题。

请输出：
1. 当前结论：通过 / 基本通过但建议小修 / 不建议通过；
2. 做得好的地方；
3. 存在的问题；
4. 是否需要立刻修复；
5. 下一步建议。
```
