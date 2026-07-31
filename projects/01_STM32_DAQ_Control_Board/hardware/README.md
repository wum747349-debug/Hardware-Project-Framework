# Hardware 目录说明

> 文档状态：当前有效
> 适用阶段：阶段 3 至阶段 7
> 适用对象：STM32 DAQ Control Board Rev A 的硬件源文件、实现证据与输出
> 最后核对依据：当前 hardware 目录结构

本目录保存当前项目的 Altium 源文件、硬件导出文件和图片资料。不要把 datasheet 放入本目录；datasheet 统一维护在 `../references/`。

## 当前目录结构

| 路径                             | 用途                            | 当前说明                                                                                  |
| ------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------- |
| `altium_project/PCB_Project/`  | Altium 权威工程源文件                | 当前工作区存在工程文件；不在本次任务中移动或修改                                                              |
| `outputs/schematic_pdf/`       | 完整原理图 PDF                     | 当前审查输入为 `outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf`；文件存在不表示原理图已审查通过 |
| `outputs/bom/`                 | 当前版本 BOM                      | 当前 BOM 为 `outputs/bom/STM32_DAQ_Control_Board.xlsx`；BOM 至少应包含位号、数量、参数或型号、PCB 封装       |
| `outputs/netlist/`             | 条件触发的网表输出                     | 仅在默认输入或对话信息不足以判断具体网络问题时按需提供                                                           |
| `outputs/erc/`                 | 条件触发的 ERC 报告、Messages 导出或相关截图 | 仅在用户提供并要求分析具体 ERC 问题时使用                                                               |
| `outputs/component_reports/`   | 条件触发的元件属性报告                   | BOM 信息不足或需额外核对元件属性时按需提供                                                               |
| `outputs/footprint_reports/`   | 条件触发的封装或映射报告                  | 关键器件引脚、焊盘或封装映射存在具体问题时按需提供                                                             |
| `outputs/gerber/`              | Gerber 层文件                    | 阶段 7 制造输出与 Release Review 活动中使用                                                        |
| `outputs/drill/`               | NC Drill、PTH/NPTH 钻孔文件及相关钻孔输出 | 阶段 7 制造输出与 Release Review 活动中使用                                                        |
| `outputs/pick_place/`          | 贴片坐标                          | 阶段 7 装配输出与 Release Review 活动中使用                                                        |
| `outputs/fabrication_package/` | 最终制造归档包                       | 阶段 7 制造门禁完成后整理                                                                          |
| `images/pcb/`                  | 少量供人工和 AI 辅助审查的 PCB 图片        | 在重要审查节点或具体问题需要时更新                                                                     |

标准目录：

```text
hardware/
├─ README.md
├─ altium_project/
│  └─ PCB_Project/
├─ outputs/
│  ├─ schematic_pdf/
│  ├─ bom/
│  ├─ netlist/
│  ├─ erc/
│  ├─ component_reports/
│  ├─ footprint_reports/
│  ├─ gerber/
│  ├─ drill/
│  ├─ pick_place/
│  └─ fabrication_package/
└─ images/
   └─ pcb/
```

## 默认审查输入

AI 日常默认只读取：

- 完整原理图 PDF；
- 当前 BOM；
- PCB 阶段必要的顶层、底层及无铺铜视图。

PCB 图片建议放在：

```text
hardware/images/pcb/
```

以下文件名仅为命名示例，不表示文件已经存在：

```text
STM32_DAQ_Control_Board_PCB_Top_RevA.png
STM32_DAQ_Control_Board_PCB_Bottom_RevA.png
STM32_DAQ_Control_Board_PCB_Top_NoPolygon_RevA.png
STM32_DAQ_Control_Board_PCB_Bottom_NoPolygon_RevA.png
```

- 顶层和底层视图用于总体布局、布线、铺铜和器件分区审查。
- 无铺铜视图用于更清楚地查看实际走线、过孔、换层和未布线关系。
- 不要求每次小改动都重新导出；只在重要审查节点或具体问题需要时更新。

## 条件触发内容

以下目录保留，但不是默认必需输入：

- `outputs/netlist/`
- `outputs/erc/`
- `outputs/component_reports/`
- `outputs/footprint_reports/`

只有在原理图 PDF、BOM、PCB 图片或对话信息不足以判断具体问题时，才按需提供相应报告或截图。

Pin/Pad Mapping、封装映射、3D 视图、安装孔局部图和机械图均不是默认导出项；出现具体问题时再单独提供。

## PCB 规则与 DRC 协作方式

- [项目级 PCB 规则文档](../docs/pcb_design_rules.md) 用于记录经需求和制造规格确认的 PCB 规则建议，是用户在 Altium Designer 中人工配置规则的依据。
- AI 负责协助确定规则值、适用对象、Scope、优先级和风险。
- 用户负责在 Altium Designer 中手动配置并核对实际规则。
- 默认不要求导出规则文件（包括 `.RUL`）、规则截图或规则汇总表。
- 用户负责在 Altium Designer 中运行 Batch DRC。
- 默认不创建或归档专门的 DRC 输出文件，DRC 报告也不是默认导出项。
- 用户可直接在对话中提供 DRC 总数、违规类别、关键报错文本或必要截图，由 AI 辅助判断。
- 最终由用户确认 DRC 已完整运行，所有问题均已解决或有明确、合理的豁免。

在本协作模式中，AI 或 Codex 不得声称实际运行过 Altium Designer、配置过规则或完成过 DRC。

## 制造输出

- `outputs/gerber/`：Gerber 层文件。
- `outputs/drill/`：NC Drill、PTH/NPTH 钻孔输出。
- `outputs/pick_place/`：贴片坐标。
- `outputs/fabrication_package/`：最终制造归档包。

这些目录在阶段 7 的制造输出和 Release Review 活动中使用。用户可以导出待放行输出用于审查；目录或文件存在不代表项目已经达到可制造状态，制造门禁完成前不得提交板厂或建立最终制造归档包。

## AI、用户和 Codex 的职责边界

- AI：需求分析、规则建议、辅助审查、问题分类和文档审查。
- 用户：Altium GUI 操作、封装及方向核对、布局布线、铺铜、规则配置、DRC 和制造文件导出。
- Codex：目录与文本维护、链接同步、Git 验证、commit 和 push。
- 任何代理不得把计划、人工操作或未提供的证据写成已完成事实。

## 输出命名规范

正式输出建议使用：

```text
<Project>_<OutputType>_<Revision>.<ext>
```

当前项目命名示例：

```text
STM32_DAQ_Control_Board_Schematic.pdf
STM32_DAQ_Control_Board_Netlist_RevA.<ext>
STM32_DAQ_Control_Board_ERC_RevA.<ext>
STM32_DAQ_Control_Board_BOM_RevA.<ext>
STM32_DAQ_Control_Board_Component_Report_RevA.<ext>
STM32_DAQ_Control_Board_Footprint_Report_RevA.<ext>
```

原则：

- 正式输出应包含项目名称、输出类型和硬件版本。
- 临时审查文件可增加 `Draft01`、`Draft02`；正式复核文件可增加 `Reviewed`。
- 示例文件名只表示命名格式，不表示文件已经存在。
- 文档中记录实际文件名，不得把示例名称写成已存在文件。
- 同一轮审查使用的不同输出应对应同一源版本。
- Git 中只保留当前有效版本和必要的正式审查版本。
- 中间临时导出版本不必全部提交。
- 当前 `STM32_DAQ_Control_Board_Schematic.pdf` 作为 Rev A 原理图审查输入；若后续重新导出，应同步更新引用路径和审查记录。
- 当前 `STM32_DAQ_Control_Board.xlsx` 作为 Rev A BOM 审查输入；若后续器件新增、删除、数量、参数、型号、料号或 PCB 封装发生变化，应同步重新导出 BOM 并更新引用路径。
- Altium `History/`、`Project Logs for*/`、预览、自动保存、缓存和锁文件不提交。
- 如果未来重命名或移动正式输出文件，必须同步更新 Markdown 链接。
