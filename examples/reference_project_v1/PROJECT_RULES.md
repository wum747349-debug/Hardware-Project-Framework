# PROJECT_RULES

1. Current Project facts come only from this repository（本 fixture facts 只来自本目录）。
2. The Framework version is the Release + Commit recorded in `FRAMEWORK.md`（Framework version 以该绑定为准）。
3. 不自动采用或读取 Framework `main`。
4. Framework 升级必须执行 explicit migration and validation。
5. 关键硬件参数必须回到官方 datasheet、reference manual 或 application note 核对；本 fixture 不声明任何关键硬件参数。
6. `.SchDoc` and `.PcbDoc` are the authoritative EDA implementation sources；本 fixture 不包含 EDA source。
7. AI/Codex 不得伪造 EDA、ERC、DRC、Manufacturing、Bring-up 或 Test 结果。
8. Maintain the current Project stage only in the root `README.md`（当前 Project stage 只在根 README 维护）。
9. 其他 Project 不能作为当前 fixture 的 fact source。
10. Read only the Stage Skill and evidence required for the current task（只读取当前任务所需 Stage Skill 与 Evidence）。
