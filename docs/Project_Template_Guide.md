# Project Template Guide

> 文档状态：Framework v1 Contract
> 适用对象：Standalone Project Template 的维护、发布与同步
> 权威职责：Template 操作边界；结构与 Lifecycle 分别引用权威文档

## 1. Template 定位

`templates/hardware_project_template/` 是 [Project Structure Standard](Project_Structure_Standard.md) 的可复制实现，不是结构 Contract 的权威源。它必须可以从固定 Framework Release 独立复制为 Standalone Project Repository，不依赖当前 monorepo `projects/...`、本地绝对路径、Framework 工作树或同级目录。

Template 只提供 Project container、Binding/Runtime 入口、事实入口、职责说明和 Project Validator 发布快照，不提供任何真实 Project 的器件、网络、板框、规则值、板厂参数、Review、DRC、Manufacturing 或 Test 事实。

## 2. 获取与复制规则

正式 Project Bootstrap 必须从已发布的固定 Framework Release 获取 Template，不复制漂移的 Framework `main`。Framework 尚未发布时，只允许自测或明确预发布评估使用 Structure Standard 定义的 Development Binding。

复制完成后，Project 必须能够脱离 Framework checkout 独立理解和运行 `scripts/validate_project_repository.py`。Template 与 Project Repository 不要求位于同一个父目录。

详细 Bootstrap、Stage 1 与 Gate 1.5 顺序以 [Workflow](08_Project_Workflow.md) 为准；[Project Initialization Guide](Project_Initialization_Guide.md) 只提供操作步骤，不重复本 Contract。

## 3. Template 内容分类

Template 必须实现 Structure Standard 定义的三类：

- Required：全部存在，并以有职责的文件保留 Required 目录；
- Conditional：默认不创建，包括 `firmware/`；
- Stage-enabled：默认不预建，在进入相应 Stage 时创建。

禁止为目录整齐创建空目录、低信息量 README、空 Stage 报告或假输出。`docs/README.md`、`hardware/README.md` 与 `references/README.md` 是 Required 父目录的真实职责说明，不是低信息量占位。

## 4. 必须替换的 Template Placeholder

Template 使用明确尖括号 placeholder，例如：

```text
<PROJECT_NAME>
<FRAMEWORK_REPOSITORY>
<FRAMEWORK_RELEASE>
<FRAMEWORK_COMMIT>
<PROJECT_STRUCTURE_VERSION>
<INITIALIZATION_FRAMEWORK_RELEASE>
```

Bootstrap 必须替换全部 Template placeholder，Project Validator 必须识别残留。不得使用假 SHA、假 Release 或其他 Project facts 伪装有效 binding。

`TBD`、`待确认`、`Draft` 是允许的真实未决状态，不属于 Template placeholder。不得为消除未决状态而虚构器件、参数、EDA、DRC、制造或实测结果。

## 5. Project Runtime Files

Template `AGENTS.md` 必须只实现 Structure Standard 的轻量启动路由；Template `PROJECT_RULES.md` 必须只实现十条 Project Runtime Rules；Template `FRAMEWORK.md` 必须使用唯一 schema。

三者均不得：

- 复制完整 Framework Workflow、Skill 或 Checklist；
- 引用当前 monorepo `projects/...`；
- 引用其他真实 Project；
- 默认读取 Framework `main`；
- 依赖 Windows 或其他本地绝对路径。

## 6. Project Validator 发布快照

Framework 中 `scripts/validate_project_repository.py` 是唯一开发源。Template 中 `scripts/validate_project_repository.py` 是发布快照，不允许人工维护另一套逻辑。

每次修改开发源后必须同步快照并由 Framework Validator 做 byte-for-byte 一致性检查。Project Validator 运行时只依赖 Project 自身和 Python 标准库。

## 7. Template 维护顺序

1. 先修改权威 Contract 并通过 Contract Gate。
2. 更新 Framework 唯一 Project Validator 开发源。
3. 按 Contract 更新 Template Required files 与内容。
4. 从开发源同步 Template validator snapshot。
5. 运行 Framework Validator、Template validation 和 clean bootstrap smoke test。
6. 如果实现暴露 Contract 必须改变，先回到权威文档修正并重新执行 Contract Gate，再同步实现。

禁止在 Template、Skill、Checklist 或 Validator 中偷偷改变 Contract。

## 8. Gate 1.5 与迁移边界

从 Template 复制只表示 Bootstrap container 已建立。Stage 1 完成第一版 Requirements Baseline 后，必须使用 Initialization Checklist 和 Project Validator 执行 Gate 1.5；只有 Gate PASS 才能进入 Stage 2。

旧 Project 迁移不是普通 Template copy。迁移必须保留原权威源，建立事实映射，验证 Standalone Repository，并按 Structure Standard 显式执行 Authority Cutover；禁止长期双写。

## 9. 相关权威文档

- [Project Structure Standard](Project_Structure_Standard.md)
- [Hardware Project Workflow](08_Project_Workflow.md)
- [AI Context Guide](AI_Context_Guide.md)
- [Framework Rules](../PROJECT_RULES.md)
