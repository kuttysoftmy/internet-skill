from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "internet"
SKILL_MD = SKILL / "SKILL.md"


def frontmatter(text):
    assert text.startswith("---\n")
    end = text.index("\n---\n", 4)
    rows = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, value = line.split(":", 1)
        rows[key.strip()] = value.strip()
    return rows


def test_skill_frontmatter_is_portable():
    meta = frontmatter(SKILL_MD.read_text())
    assert set(meta) == {"name", "description"}
    assert meta["name"] == "internet"
    assert "Deep" in meta["description"]
    assert "AKBP" in meta["description"]


def test_required_references_exist_and_are_linked():
    text = SKILL_MD.read_text()
    for name in [
        "akbp-protocol.md",
        "output-templates.md",
        "research-depth.md",
        "source-map.md",
        "verification.md",
    ]:
        assert (SKILL / "references" / name).is_file()
        assert f"references/{name}" in text


def test_skill_contract_keeps_core_research_stages():
    text = SKILL_MD.read_text()
    for phrase in [
        "Preflight Traps",
        "Research Plan",
        "Search Passes",
        "Proof Contract",
        "Synthesis Contract",
        "AKBP Integration",
        "Failure Modes To Avoid",
    ]:
        assert phrase in text


def test_disallowed_reference_project_name_is_absent():
    forbidden = "".join(["la", "st", "30", "da", "ys"]).lower()
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or ".venv" in path.parts or not path.is_file():
            continue
        if path.suffix not in {".md", ".py", ".yaml", ".yml", ".toml", ".txt"}:
            continue
        assert forbidden not in path.read_text(encoding="utf-8").lower()


def test_no_agent_home_config_paths_are_committed():
    forbidden = [chr(46) + "co" + "dex", chr(46) + "cla" + "ude"]
    for path in ROOT.rglob("*"):
        if {".git", ".venv", "__pycache__", ".pytest_cache"} & set(path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".py", ".yaml", ".yml", ".toml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for needle in forbidden:
            assert needle not in text
