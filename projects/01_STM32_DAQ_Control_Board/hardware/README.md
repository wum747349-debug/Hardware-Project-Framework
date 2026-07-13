# Hardware 目录说明

> 文档状态：当前有效
> 当前阶段：整板原理图系统审查
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前 hardware 目录结构

本目录保存当前项目的 Altium 源文件、硬件导出文件和图片资料。不要把 datasheet 放入本目录；datasheet 统一维护在 `../references/`。

## 当前目录结构

| 路径 | 用途 | 当前说明 |
|---|---|---|
| `altium_project/PCB_Project/` | Altium 权威工程源文件 | 当前工作区存在工程文件；不在本次任务中移动 |
| `outputs/schematic_pdf/` | 完整原理图 PDF | 当前审查输入为 `outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic_RevA.pdf`；文件存在不表示原理图已审查通过 |
| `outputs/netlist/` | 条件触发输出，用于核对复杂网络、跨页网络、网络标签或实际引脚连接关系 | 目录已规划，当前未导出；仅在 PDF 和 BOM 无法判断对应问题时按需提供 |
| `outputs/erc/` | 条件触发输出，用于保存用户提供并要求 AI 分析的 ERC 报告、Messages 导出或错误截图 | 目录已规划，当前未提供 ERC 输出；ERC 输出不是默认必需审查输入 |
| `outputs/bom/` | 默认必需审查输入，用于导出当前版本 BOM | 当前 BOM 为 `outputs/bom/STM32_DAQ_Control_Board.csv`；BOM 至少应包含位号、数量、参数或型号、PCB 封装 |
| `outputs/component_reports/` | 条件触发输出，用于补充元件、位号、型号等属性报告 | 目录已规划，当前未导出；BOM 信息不足或需额外核对元件属性时按需提供 |
| `outputs/footprint_reports/` | 条件触发输出，用于原理图器件与 PCB 封装映射、封装核对报告 | 目录已规划，当前未导出；关键器件引脚或封装映射存在风险时按需提供 |
| `outputs/gerber/` | Gerber 和钻孔输出 | 目录已规划，PCB 阶段使用 |
| `outputs/pick_place/` | 贴片坐标 | 目录已规划，装配输出阶段使用 |
| `outputs/fabrication_package/` | 正式制造归档包 | 目录已规划，Gerber、钻孔、BOM、坐标等正式打包输出 |
| `images/` | 原理图局部截图、PCB 截图、装配和测试照片 | 当前仅保留目录占位 |

标准目录：

```text
hardware/
├─ altium_project/
│  └─ PCB_Project/
├─ outputs/
│  ├─ schematic_pdf/
│  ├─ netlist/
│  ├─ erc/
│  ├─ bom/
│  ├─ component_reports/
│  ├─ footprint_reports/
│  ├─ gerber/
│  ├─ pick_place/
│  └─ fabrication_package/
└─ images/
```

## 输出命名规范

正式输出建议使用：

```text
<Project>_<OutputType>_<Revision>.<ext>
```

当前项目示例：

```text
STM32_DAQ_Control_Board_Schematic_RevA.pdf
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
- 当前 `STM32_DAQ_Control_Board_Schematic_RevA.pdf` 作为 Rev A 原理图审查输入；若后续重新导出，应同步更新引用路径和审查记录。
- 当前 `STM32_DAQ_Control_Board.csv` 作为 Rev A BOM 审查输入；若后续器件新增、删除、数量、参数、型号、料号或 PCB 封装发生变化，应同步重新导出 BOM 并更新引用路径。
- Altium `History/`、`Project Logs for*/`、预览、自动保存、缓存和锁文件不提交。
- 如果未来重命名或移动正式输出文件，必须同步更新 Markdown 链接。
