#!/usr/bin/env python3
"""Validate Framework v0.9 implementation against the Framework v1 Contract."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates/hardware_project_template"
FINAL_REFERENCE_ROOT = ROOT / "examples/reference_project_v1"

REQUIRED_FRAMEWORK_FILES = (
    "PROJECT_RULES.md",
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "docs/Project_Structure_Standard.md",
    "docs/08_Project_Workflow.md",
    "docs/AI_Context_Guide.md",
    "docs/Project_Template_Guide.md",
    "docs/Project_Initialization_Guide.md",
    "docs/Framework_Migration_Guide.md",
    "skills/hardware-project-initialization/SKILL.md",
    "checklists/project_initialization_checklist.md",
    "scripts/validate_project_repository.py",
    "scripts/validate_framework_repository.py",
    "templates/hardware_project_template/scripts/validate_project_repository.py",
    ".github/workflows/repository-framework-check.yml",
)

REQUIRED_TEMPLATE_FILES = {
    "AGENTS.md",
    "FRAMEWORK.md",
    "PROJECT_RULES.md",
    "README.md",
    "requirements.md",
    "block_diagram.md",
    "design_notes.md",
    "references.md",
    "docs/README.md",
    "hardware/README.md",
    "references/README.md",
    "scripts/validate_project_repository.py",
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ABSOLUTE_LOCAL_PATH = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:[A-Z]:[\\/]|/Users/|/home/|/mnt/[a-z]/)"
)

LEGACY_PROJECT_RESIDUE = (
    "projects/01_STM32_DAQ_Control_Board",
    "projects/02_LiIon_Charger_Protection_Board",
    "projects/03_STM32_OpAmp_ADC_Acquisition_Board",
    "01_STM32_DAQ_Control_Board",
    "02_LiIon_Charger_Protection_Board",
    "03_STM32_OpAmp_ADC_Acquisition_Board",
    "STM32 DAQ Control Board",
    "Li-Ion Charger Protection Board",
    "STM32 OpAmp ADC Acquisition Board",
    "Hardware-Practice-Projects/projects",
)

SMOKE_STAGE_PATHS = (
    "docs/component_selection_plan.md",
    "docs/module_design",
    "docs/schematic_review.md",
    "docs/pcb_design_rules.md",
    "docs/pcb_review.md",
    "docs/bringup_log.md",
    "docs/test_report.md",
    "docs/revision_history.md",
)


class Validator:
    def __init__(self, mode: str) -> None:
        self.mode = mode
        self.errors: list[str] = []
        self.check_count = 0

    def check(self, condition: bool, path: str, reason: str) -> None:
        self.check_count += 1
        if not condition:
            self.errors.append(f"{path}: {reason}")

    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def framework_markdown_files() -> list[Path]:
    files = [ROOT / name for name in ("PROJECT_RULES.md", "AGENTS.md", "README.md", "CHANGELOG.md")]
    for directory in ("docs", "skills", "checklists", "templates"):
        files.extend((ROOT / directory).rglob("*.md"))
    return sorted(set(files))


def check_required_files(validator: Validator) -> None:
    for relative_path in REQUIRED_FRAMEWORK_FILES:
        validator.check((ROOT / relative_path).is_file(), relative_path, "missing Framework v0.9 required file")

    actual_template_files = {
        path.relative_to(TEMPLATE_ROOT).as_posix()
        for path in TEMPLATE_ROOT.rglob("*")
        if path.is_file()
    }
    validator.check(actual_template_files == REQUIRED_TEMPLATE_FILES, "templates/hardware_project_template", "Template must contain exactly the Contract Required files")


def check_markdown_links(validator: Validator) -> None:
    for markdown_file in framework_markdown_files():
        text = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK.finditer(line):
                target = normalize_link_target(match.group(1))
                if not target or target.startswith("#"):
                    continue
                if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                    continue
                target_path = (markdown_file.parent / target).resolve()
                try:
                    target_path.relative_to(ROOT.resolve())
                except ValueError:
                    validator.check(False, f"{markdown_file.relative_to(ROOT)}:{line_number}", f"relative link escapes Framework root: {match.group(1)}")
                    continue
                validator.check(target_path.exists(), f"{markdown_file.relative_to(ROOT)}:{line_number}", f"relative link target does not exist: {match.group(1)}")


def check_contract_authorities(validator: Validator) -> None:
    rules = validator.read("PROJECT_RULES.md")
    structure = validator.read("docs/Project_Structure_Standard.md")
    workflow = validator.read("docs/08_Project_Workflow.md")
    context = validator.read("docs/AI_Context_Guide.md")
    template_guide = validator.read("docs/Project_Template_Guide.md")
    init_guide = validator.read("docs/Project_Initialization_Guide.md")
    migration_guide = validator.read("docs/Framework_Migration_Guide.md")
    changelog = validator.read("CHANGELOG.md")
    init_skill = validator.read("skills/hardware-project-initialization/SKILL.md")
    init_checklist = validator.read("checklists/project_initialization_checklist.md")
    readme = validator.read("README.md")

    for phrase in (
        "Framework 定义硬件项目的方法和契约，不作为真实 Project 的活动事实源",
        "一个正式 Project 只能有一个活动权威仓库",
        "framework-pre-v1-migration",
        "禁止长期双写",
    ):
        validator.check(phrase in rules, "PROJECT_RULES.md", f"missing stable authority Contract: {phrase}")

    for field in (
        "Framework Repository:",
        "Framework Release:",
        "Framework Commit:",
        "Project Structure Version:",
        "Repository Model:",
        "Initialization Framework Release:",
        "Initialization Status:",
    ):
        validator.check(field in structure, "docs/Project_Structure_Standard.md", f"FRAMEWORK.md schema drift: {field}")

    for phrase in (
        "Required / Conditional / Stage-enabled",
        "`firmware/` 不再是所有项目 Required",
        "Project Structure Version: 1",
        "不默认跟随 Framework `main`",
        "Template 是实现",
    ):
        validator.check(phrase in structure, "docs/Project_Structure_Standard.md", f"structure Contract drift: {phrase}")

    validator.check("Gate 1.5 — Project Initialization & Requirements Baseline" in workflow, "docs/08_Project_Workflow.md", "Gate 1.5 canonical name missing")
    validator.check("Bootstrap 位于八阶段之前，不是 Stage 0" in workflow, "docs/08_Project_Workflow.md", "Bootstrap boundary drift")
    validator.check("migration provenance 可以保留" in workflow, "docs/08_Project_Workflow.md", "Gate 1.5 migration provenance boundary missing")
    for number, name in {
        1: "Requirements Definition",
        2: "Critical Component Selection",
        3: "Schematic Module Design and Capture",
        4: "Schematic Review",
        5: "PCB Layout",
        6: "Routing and Copper",
        7: "PCB Release Review",
        8: "Assembly, Bring-up and Hardware Test",
    }.items():
        validator.check(f"Stage {number} — {name}" in workflow, "docs/08_Project_Workflow.md", f"canonical Stage {number} missing")

    for layer in (
        "Layer 0 — Framework Binding",
        "Layer 1 — Runtime Rules",
        "Layer 2 — Project Facts",
        "Layer 3 — Stage Method",
    ):
        validator.check(layer in context, "docs/AI_Context_Guide.md", f"four-layer context drift: {layer}")
    validator.check("Project 不默认读取 Framework `main`" in context, "docs/AI_Context_Guide.md", "context routing allows Framework main")

    for phrase, path, text in (
        ("唯一开发源", "docs/Project_Template_Guide.md", template_guide),
        ("固定 Framework Release", "docs/Project_Initialization_Guide.md", init_guide),
        ("不自动升级", "docs/Framework_Migration_Guide.md", migration_guide),
        ("Framework v0.9 Executable Candidate", "CHANGELOG.md", changelog),
        ("Gate 1.5", "skills/hardware-project-initialization/SKILL.md", init_skill),
        ("No Premature Conclusions", "checklists/project_initialization_checklist.md", init_checklist),
        ("Framework v0.9", "README.md", readme),
    ):
        validator.check(phrase in text, path, f"Framework v0.9 alignment missing: {phrase}")


def check_template_contract(validator: Validator) -> None:
    agents = (TEMPLATE_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    rules = (TEMPLATE_ROOT / "PROJECT_RULES.md").read_text(encoding="utf-8")
    binding = (TEMPLATE_ROOT / "FRAMEWORK.md").read_text(encoding="utf-8")
    readme = (TEMPLATE_ROOT / "README.md").read_text(encoding="utf-8")

    for phrase in ("Read `FRAMEWORK.md` first", "bound Framework Release", "Do not default to Framework `main`", "Do not read another Project"):
        validator.check(phrase in agents, "templates/hardware_project_template/AGENTS.md", f"Project AGENTS contract drift: {phrase}")
    validator.check(len(re.findall(r"^\d+\. ", rules, flags=re.MULTILINE)) == 10, "templates/hardware_project_template/PROJECT_RULES.md", "Project Runtime Rules must contain ten rules")
    validator.check("Current Project Stage: Bootstrap" in readme, "templates/hardware_project_template/README.md", "Template must start at Bootstrap")
    validator.check("Repository Model: Standalone Project" in binding, "templates/hardware_project_template/FRAMEWORK.md", "Template binding model drift")

    for path in TEMPLATE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        relative_path = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() == ".md":
            validator.check(ABSOLUTE_LOCAL_PATH.search(text) is None, relative_path, "Template contains a local absolute path")
        for token in LEGACY_PROJECT_RESIDUE:
            if path.suffix.lower() == ".md":
                validator.check(token not in text, relative_path, f"Template contains legacy Project residue: {token}")

    snapshot_text = (TEMPLATE_ROOT / "scripts/validate_project_repository.py").read_text(encoding="utf-8")
    validator.check("D:\\Hardware-Practice-Projects" not in snapshot_text, "templates/hardware_project_template/scripts/validate_project_repository.py", "Project Validator depends on the current local Framework path")


def check_validator_snapshot(validator: Validator) -> None:
    source = ROOT / "scripts/validate_project_repository.py"
    snapshot = TEMPLATE_ROOT / "scripts/validate_project_repository.py"
    if source.is_file() and snapshot.is_file():
        validator.check(source.read_bytes() == snapshot.read_bytes(), str(snapshot.relative_to(ROOT)), "Template Project Validator snapshot differs from the Framework development source")


def run_template_validator(validator: Validator) -> None:
    source = ROOT / "scripts/validate_project_repository.py"
    if not source.is_file():
        return
    result = subprocess.run(
        [sys.executable, str(source), str(TEMPLATE_ROOT), "--template"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    details = (result.stdout + result.stderr).strip()
    validator.check(result.returncode == 0, "scripts/validate_project_repository.py", f"Template fixture validation failed: {details}")


def run_fixture_validator(project_root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(project_root / "scripts/validate_project_repository.py"), *arguments],
        cwd=project_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def prepare_stage_1_fixture(target: Path, framework_commit: str) -> None:
    shutil.copytree(TEMPLATE_ROOT, target)
    replacements = {
        "<PROJECT_NAME>": "Framework Validator Fixture",
        "<HARDWARE_REVISION>": "TEST-REV-A",
        "<FRAMEWORK_REPOSITORY>": "wum747349-debug/Hardware-Practice-Projects",
        "<FRAMEWORK_RELEASE>": "development-v0.9",
        "<FRAMEWORK_COMMIT>": framework_commit,
        "<PROJECT_STRUCTURE_VERSION>": "1",
        "<INITIALIZATION_FRAMEWORK_RELEASE>": "development-v0.9",
        "<INITIALIZATION_STATUS>": "Gate 1.5 Pending",
    }
    for markdown_file in target.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        markdown_file.write_text(text, encoding="utf-8")

    readme = target / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace(
            "Current Project Stage: Bootstrap",
            "Current Project Stage: Stage 1 — Requirements Definition",
        ),
        encoding="utf-8",
    )


def initialize_fixture(target: Path) -> None:
    binding = target / "FRAMEWORK.md"
    binding.write_text(
        binding.read_text(encoding="utf-8").replace(
            "Initialization Status: Gate 1.5 Pending",
            "Initialization Status: Initialized",
        ),
        encoding="utf-8",
    )


def check_project_smoke_tests(validator: Validator) -> None:
    commit_result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    framework_commit = commit_result.stdout.strip()
    validator.check(
        commit_result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", framework_commit) is not None,
        "git rev-parse HEAD",
        "Smoke fixtures require the current immutable Framework commit",
    )
    if commit_result.returncode != 0 or re.fullmatch(r"[0-9a-f]{40}", framework_commit) is None:
        return

    temporary_path: Path | None = None
    with tempfile.TemporaryDirectory(prefix="framework-validator-", dir=ROOT) as temporary_directory:
        temporary_path = Path(temporary_directory)

        clean_project = temporary_path / "clean-bootstrap"
        prepare_stage_1_fixture(clean_project, framework_commit)
        validator.check(not (clean_project / "firmware").exists(), "Clean Bootstrap Smoke", "Conditional firmware directory was pre-created")
        validator.check(
            not any((clean_project / path).exists() for path in SMOKE_STAGE_PATHS),
            "Clean Bootstrap Smoke",
            "Stage-enabled content was pre-created",
        )
        gate_result = run_fixture_validator(clean_project, "--gate-1-5")
        gate_details = (gate_result.stdout + gate_result.stderr).strip()
        validator.check(gate_result.returncode == 0, "Clean Bootstrap Smoke", f"Gate 1.5 Pending validation failed: {gate_details}")

        initialize_fixture(clean_project)
        initialized_gate_result = run_fixture_validator(clean_project, "--gate-1-5")
        initialized_gate_details = (initialized_gate_result.stdout + initialized_gate_result.stderr).strip()
        validator.check(
            initialized_gate_result.returncode != 0 and "Gate 1.5 Pending" in initialized_gate_details,
            "Clean Bootstrap Smoke",
            f"Gate mode accepted a pre-Initialized fixture: {initialized_gate_details}",
        )
        normal_result = run_fixture_validator(clean_project)
        normal_details = (normal_result.stdout + normal_result.stderr).strip()
        validator.check(normal_result.returncode == 0, "Clean Bootstrap Smoke", f"Initialized normal validation failed: {normal_details}")

        stage_enabled_project = temporary_path / "stage-enabled-semantics"
        prepare_stage_1_fixture(stage_enabled_project, framework_commit)
        initialize_fixture(stage_enabled_project)
        stage_readme = stage_enabled_project / "README.md"
        stage_readme.write_text(
            stage_readme.read_text(encoding="utf-8").replace(
                "Current Project Stage: Stage 1 — Requirements Definition",
                "Current Project Stage: Stage 5 — PCB Layout",
            ),
            encoding="utf-8",
        )
        stage_documents = {
            "docs/component_selection_plan.md": "# Component Selection Fixture\n\nFixture activity evidence.\n",
            "docs/module_design/fixture.md": "# Module Design Fixture\n\nFixture activity evidence.\n",
            "docs/schematic_review.md": "# Schematic Review Fixture\n\nFixture activity evidence.\n",
            "docs/pcb_design_rules.md": "# PCB Design Rules Fixture\n\nFixture activity evidence.\n",
        }
        for relative_path, content in stage_documents.items():
            document = stage_enabled_project / relative_path
            document.parent.mkdir(parents=True, exist_ok=True)
            document.write_text(content, encoding="utf-8")
        stage_5_result = run_fixture_validator(stage_enabled_project)
        stage_5_details = (stage_5_result.stdout + stage_5_result.stderr).strip()
        validator.check(
            stage_5_result.returncode == 0 and not (stage_enabled_project / "docs/pcb_review.md").exists(),
            "Stage-enabled Semantics Smoke",
            f"Stage 5 incorrectly required pcb_review.md before review activity: {stage_5_details}",
        )

        (stage_enabled_project / "docs/pcb_review.md").write_text(
            "# PCB Review Fixture\n\nFixture Stage 6/7 activity evidence.\n",
            encoding="utf-8",
        )
        stage_readme.write_text(
            stage_readme.read_text(encoding="utf-8").replace(
                "Current Project Stage: Stage 5 — PCB Layout",
                "Current Project Stage: Stage 8 — Assembly, Bring-up and Hardware Test",
            ),
            encoding="utf-8",
        )
        stage_8_result = run_fixture_validator(stage_enabled_project)
        stage_8_details = (stage_8_result.stdout + stage_8_result.stderr).strip()
        validator.check(
            stage_8_result.returncode == 0
            and not (stage_enabled_project / "docs/bringup_log.md").exists()
            and not (stage_enabled_project / "docs/test_report.md").exists(),
            "Stage-enabled Semantics Smoke",
            f"Stage 8 incorrectly required bring-up/test records before those activities: {stage_8_details}",
        )

        migration_project = temporary_path / "migration-provenance"
        prepare_stage_1_fixture(migration_project, framework_commit)
        migration_readme = migration_project / "README.md"
        migration_readme.write_text(
            migration_readme.read_text(encoding="utf-8")
            + "\n## Migration Provenance\n\n"
            + "Source Repository: wum747349-debug/Hardware-Practice-Projects\n\n"
            + "Legacy Project Path: projects/02_LiIon_Charger_Protection_Board\n\n"
            + "Git History Strategy: Clean Import\n",
            encoding="utf-8",
        )
        migration_gate_result = run_fixture_validator(migration_project, "--gate-1-5")
        migration_gate_details = (migration_gate_result.stdout + migration_gate_result.stderr).strip()
        validator.check(
            migration_gate_result.returncode == 0,
            "Migration Provenance Smoke",
            f"Legal migration provenance was rejected: {migration_gate_details}",
        )

        initialize_fixture(migration_project)
        migration_normal_result = run_fixture_validator(migration_project)
        migration_normal_details = (migration_normal_result.stdout + migration_normal_result.stderr).strip()
        validator.check(
            migration_normal_result.returncode == 0,
            "Migration Provenance Smoke",
            f"Initialized migration fixture failed: {migration_normal_details}",
        )

        migration_readme.write_text(
            migration_readme.read_text(encoding="utf-8")
            + "\nFramework Runtime Path: ../Hardware-Practice-Projects/projects/02_LiIon_Charger_Protection_Board\n",
            encoding="utf-8",
        )
        illegal_result = run_fixture_validator(migration_project)
        illegal_details = (illegal_result.stdout + illegal_result.stderr).strip()
        validator.check(
            illegal_result.returncode != 0 and "runtime path/dependency" in illegal_details,
            "Illegal Runtime Dependency Negative Test",
            f"Illegal runtime dependency was not rejected by the expected check: {illegal_details}",
        )

    if temporary_path is not None:
        validator.check(not temporary_path.exists(), "Temporary Project Fixtures", "Smoke-test temporary directory was not removed")


def check_final_mode(validator: Validator) -> None:
    if validator.mode != "final":
        return
    reference_path = FINAL_REFERENCE_ROOT.relative_to(ROOT).as_posix()
    validator.check(FINAL_REFERENCE_ROOT.is_dir(), reference_path, "Final mode requires the future Reference Project")
    if FINAL_REFERENCE_ROOT.is_dir():
        source = ROOT / "scripts/validate_project_repository.py"
        result = subprocess.run([sys.executable, str(source), str(FINAL_REFERENCE_ROOT)], cwd=ROOT, check=False)
        validator.check(result.returncode == 0, reference_path, "Final Reference Project validation failed")


def validate(mode: str) -> Validator:
    validator = Validator(mode)
    check_required_files(validator)
    check_markdown_links(validator)
    check_contract_authorities(validator)
    check_template_contract(validator)
    check_validator_snapshot(validator)
    run_template_validator(validator)
    check_project_smoke_tests(validator)
    check_final_mode(validator)
    return validator


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("v0.9", "final"), default="v0.9", help="v0.9 does not require the future final Reference Project")
    args = parser.parse_args(argv)
    validator = validate(args.mode)
    if validator.errors:
        print(f"Framework repository validation failed: {len(validator.errors)} error(s)")
        for error in validator.errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Framework repository validation passed ({validator.check_count} checks, mode={args.mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
