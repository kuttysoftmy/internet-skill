import importlib.util
import json
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
    assert manifest["schema"] == "internet-research-workspace/v2"
    assert "plan.json" in manifest["files"]

    plan = json.loads((target / "plan.json").read_text())
    assert plan["topic"] == "Should we use Bun?"
    assert plan["depth"] == "deep"
    assert "contradiction" in [item["label"] for item in plan["query_passes"]]
    assert "stop_conditions" in plan

    research = (target / "research.md").read_text()
    assert "Preflight" in research
    assert "Contradiction" in research
    assert "Final Answer" in research

    assert "Agent Knowledge Base Protocol" in (target / "akbp-intake.md").read_text()
    assert (target / "sources.csv").read_text().startswith("id,url,title")
