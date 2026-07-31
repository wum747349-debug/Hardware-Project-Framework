# hardware 目录说明

> 文档状态：草稿
> 适用阶段：阶段 3 至阶段 7
> 适用对象：<项目名称与硬件版本>
> 最后核对依据：<当前 hardware 目录>

- `altium_project/`：保存 `.PrjPcb`、`.SchDoc`、`.PcbDoc` 等权威 EDA 源文件。
- `outputs/`：保存可追溯的原理图、BOM、报告和制造输出。
- `images/`：保存审查、装配、调试和展示图片。

模板只预建上述父目录及其说明文件。`outputs/` 和 `images/` 下的分类子目录在实际产生对应内容时创建，具体路径见各父目录 README。

`.SchDoc` 与 `.PcbDoc` 分别是原理图和 PCB 权威源文件。目录或输出存在不表示已审查、已运行 DRC 或已批准制造。

正式输出建议：

```text
<Project>_<OutputType>_<HardwareRevision>_<YYYYMMDD>.<ext>
```

同一制造批次必须能追溯到同一源版本。不要使用 `final`、`latest` 等无法长期追溯的名称。
