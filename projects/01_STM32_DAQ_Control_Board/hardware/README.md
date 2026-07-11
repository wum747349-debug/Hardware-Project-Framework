# Hardware 目录说明

> 文档状态：当前有效
> 当前阶段：整板原理图系统审查
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前 hardware 目录结构

本目录保存当前项目的 Altium 源文件、硬件导出文件和图片资料。不要把 datasheet 放入本目录；datasheet 统一维护在 `../references/`。

## 当前目录结构

| 路径 | 用途 | 当前说明 |
|---|---|---|
| `altium_project/` | Altium 工程源文件目录 | 当前源文件位于 `altium_project/PCB_Project/`；不在本次任务中移动 |
| `outputs/schematic_pdf/` | 原理图 PDF 导出文件 | 当前未发现正式原理图 PDF；后续导出后放这里 |
| `outputs/gerber/` | Gerber 输出 | PCB 阶段使用 |
| `outputs/bom/` | BOM 导出 | 原理图审查和 BOM 核对后使用 |
| `outputs/pick_place/` | 坐标文件 | 装配输出阶段使用 |
| `outputs/fabrication_package/` | 制造归档包 | Gerber、钻孔、BOM、坐标等正式打包输出 |
| `images/` | 原理图截图、PCB 截图、装配照片、测试照片 | 当前仅保留目录占位 |

## 输出命名规范

正式原理图导出建议命名为：

```text
STM32_DAQ_Control_Board_Schematic_RevA.pdf
```

审查阶段草稿可使用：

```text
STM32_DAQ_Control_Board_Schematic_RevA_Draft01.pdf
STM32_DAQ_Control_Board_Schematic_RevA_Draft02.pdf
STM32_DAQ_Control_Board_Schematic_RevA_Reviewed.pdf
```

原则：

- Git 中只保留当前有效版本和必要的正式审查版本。
- 中间临时导出版本不必全部提交。
- Altium `History/`、`Project Logs for*/`、预览、自动保存、缓存和锁文件不提交。
- 如果未来重命名或移动正式输出文件，必须同步更新 Markdown 链接。
