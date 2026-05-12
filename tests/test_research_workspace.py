import importlib.util
import json
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "internet" / "scripts" / "research_workspace.py"


def load_module():
    spec = importlib.util.spec_from_file_location("research_workspace", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_slugify_keeps_safe_length():
    module = load_module()
    slug = module.slugify("AI Browser Automation Tools: 2026 / Deep Research!")
    assert slug == "ai-browser-automation-tools-2026-deep-research"
    assert len(slug) <= 80


def test_md_cell_preserves_falsy_values():
    module = load_module()
    assert module.md_cell(0) == "0"
    assert module.md_cell(False) == "False"
    assert module.md_cell(None) == ""
    assert module.md_cell("a|b\nc") == "a\\|b<br>c"


def test_create_workspace(tmp_path):
    module = load_module()
    target, written, skipped = module.create_workspace("Should we use Bun?", tmp_path, "deep", False)
    assert target.exists()
    assert set(written) == {
        "research.md",
        "plan.json",
        "queries.md",
        "claims.md",
        "sources.csv",
        "evidence.jsonl",
        "contradictions.md",
        "gaps.md",
        "akbp-intake.md",
        "manifest.json",
    }
    assert skipped == []

    manifest = json.loads((target / "manifest.json").read_text())
    assert manifest["topic"] == "Should we use Bun?"
    assert manifest["depth"] == "deep"
    assert manifest["schema"] == "internet-research-workspace/v3"
    assert "plan.json" in manifest["files"]

    plan = json.loads((target / "plan.json").read_text())
    assert plan["topic"] == "Should we use Bun?"
    assert plan["depth"] == "deep"
    assert "contradiction" in [item["label"] for item in plan["query_passes"]]
    assert "stop_conditions" in plan

    research = (target / "research.md").read_text()
    assert "Preflight" in research
    assert "Contradiction" in research
    assert "Activity Log" in research
    assert "Final Answer" in research

    assert "Agent Knowledge Base Protocol" in (target / "akbp-intake.md").read_text()
    assert (target / "sources.csv").read_text().startswith("id,url,title")


def test_legacy_cli_invocation_creates_workspace(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "Gateway API production readiness",
            "--depth",
            "deep",
            "--root",
            str(tmp_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    cli_out = result.stdout.strip()
    workspace = Path(cli_out.splitlines()[0])
    assert workspace.exists()
    assert "written:" in result.stdout
    manifest = json.loads((workspace / "manifest.json").read_text())
    assert manifest["schema"] == "internet-research-workspace/v3"


def test_no_args_prints_help_without_creating_workspace():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "add-query" in result.stdout


def test_recording_helpers_populate_workspace(tmp_path):
    module = load_module()
    target, _written, _skipped = module.create_workspace("Gateway API", tmp_path, "deep", False)

    module.add_query(
        target,
        "orientation",
        "Gateway API production readiness",
        "web",
        "discover latest release",
        "found official release",
        "open release notes",
    )
    source_id = module.add_source(
        target,
        "https://example.com/release",
        title="Gateway API release",
        source_type="official",
        tier="1",
        published="2026-03-14",
        notes="release notes",
    )
    claim_id = module.add_claim(
        target,
        "Gateway API has a current stable release.",
        "Release page lists stable release.",
        source_id,
        "High",
        publication_date="2026-03-14",
    )
    module.add_evidence(
        target,
        source_id,
        "Release notes identify stable release.",
        claim_id=claim_id,
        url="https://example.com/release",
        confidence="High",
    )
    module.add_contradiction(
        target,
        "All implementations are equally ready.",
        source_id,
        "S002",
        "Conformance varies by implementation.",
        "Readiness is controller-specific.",
        "High",
    )
    module.add_gap(
        target,
        "Controller choice",
        "User did not name a controller.",
        "implementation conformance table",
        "open",
        "Ask for target controller.",
    )

    summary = module.workspace_summary(target)
    assert summary["queries"] == 1
    assert summary["sources"] == 1
    assert summary["claims"] == 1
    assert summary["evidence"] == 1
    assert summary["contradictions"] == 1
    assert summary["gaps"] == 1

    plan = json.loads((target / "plan.json").read_text())
    orientation = [item for item in plan["query_passes"] if item["label"] == "orientation"][0]
    assert orientation["queries"] == ["Gateway API production readiness"]
    assert orientation["status"] == "in_progress"

    research = (target / "research.md").read_text()
    assert "Gateway API production readiness" in research
    assert "Gateway API release" in research
    assert "Gateway API has a current stable release." in research
    assert "Controller choice" in research
