#!/usr/bin/env python3
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE_FILES = [
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
]


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:80] or "research"


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def plan_json(topic, depth, created):
    return {
        "topic": topic,
        "depth": depth,
        "created": created,
        "research_contract": {
            "question": "",
            "decision_or_deliverable": "",
            "recency_window": "",
            "geography_or_jurisdiction": "",
            "audience": "",
            "constraints": [],
            "assumptions": [],
        },
        "entities": [],
        "source_classes": [
            "orientation",
            "primary",
            "independent",
            "community_or_ground_truth",
            "contradiction",
            "gap_fill",
        ],
        "query_passes": [
            {"label": "orientation", "queries": [], "status": "pending"},
            {"label": "primary", "queries": [], "status": "pending"},
            {"label": "independent", "queries": [], "status": "pending"},
            {"label": "community_or_ground_truth", "queries": [], "status": "pending"},
            {"label": "contradiction", "queries": [], "status": "pending"},
            {"label": "gap_fill", "queries": [], "status": "pending"},
        ],
        "acceptance_criteria": [],
        "stop_conditions": [
            "Evidence meets acceptance criteria",
            "Three consecutive targeted searches add no material evidence",
            "Remaining gaps are inaccessible, private, paywalled, or out of scope",
        ],
    }


def research_markdown(topic, depth, created):
    return f"""# Internet Research: {topic}

Created: {created}
Depth: {depth}

## Research Contract

- User question:
- Decision or deliverable:
- Recency window:
- Geography or jurisdiction:
- Audience:
- Constraints:
- Assumptions:
- Required output:

## Preflight

- Demographic shopping trap:
- Generic ranking trap:
- Ambiguous entity trap:
- Numeric trap:
- Temporal trap:
- Tutorial or error-message trap:
- High-stakes trap:
- Single-source trap:

## Plan

- Entities, aliases, handles, repos, tickers:
- Source classes:
- Acceptance criteria:
- Stop conditions:

## Search Passes

### Orientation

- Queries:
- New entities:
- Notes:

### Primary Sources

- Queries:
- Sources opened:
- Notes:

### Independent Sources

- Queries:
- Sources opened:
- Notes:

### Community Or Ground Truth

- Queries:
- Sources opened:
- Notes:

### Contradiction

- Queries:
- Conflicts found:
- Notes:

### Gap Fill

- Queries:
- Remaining gaps:
- Notes:

## Synthesis Draft

## Final Answer
"""


def akbp_intake_markdown(topic):
    return f"""# AKBP Intake Preview: {topic}

AKBP means Agent Knowledge Base Protocol.

Prepare reviewed sources and durable claim proposals here. Do not apply AKBP writes until dry-run output is reviewed and approved.

## Knowledge Base

- AKBP path:
- Existing context retrieved:
- Source verification status:
- Export or import check status:

## Sources To Register

| Source ID | Type | Locator | Title | Scope | Notes |
|---|---|---|---|---|---|

## Claim Proposals

| Claim | Type | Evidence Source IDs | Confidence | Status | Apply? |
|---|---|---|---|---|---|

## Lifecycle Notes

| Existing Claim | New Claim | Relation | Reason |
|---|---|---|---|

## Dry-Run Review

- Command or JSONL request:
- Review result:
- Redactions:
- Would-write paths:
- Approval status:
"""


def claims_markdown():
    return """# Claim Ledger

| ID | Claim | Evidence | Source ID | Event Date | Publication Date | Confidence | Caveat |
|---|---|---|---|---|---|---|---|
"""


def queries_markdown():
    return """# Query Ledger

| Pass | Query | Tool | Why | Result | Follow-up |
|---|---|---|---|---|---|
"""


def contradictions_markdown():
    return """# Contradictions

| Claim | Source A | Source B | Conflict | Likely Explanation | Confidence |
|---|---|---|---|---|---|
"""


def gaps_markdown():
    return """# Gaps

| Gap | Why It Matters | Search Tried | Status | Next Step |
|---|---|---|---|---|
"""


def manifest_json(topic, depth, created):
    return {
        "topic": topic,
        "depth": depth,
        "created": created,
        "schema": "internet-research-workspace/v2",
        "files": WORKSPACE_FILES,
    }


def write_file(path, content, overwrite):
    if path.exists() and not overwrite:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def create_workspace(topic, root, depth, overwrite):
    created = today()
    target = root / f"{created}-{slugify(topic)}"
    target.mkdir(parents=True, exist_ok=True)
    manifest = manifest_json(topic, depth, created)
    files = {
        "research.md": research_markdown(topic, depth, created),
        "plan.json": json.dumps(plan_json(topic, depth, created), indent=2) + "\n",
        "queries.md": queries_markdown(),
        "claims.md": claims_markdown(),
        "sources.csv": "id,url,title,author,published,event_date,accessed,type,tier,opened,notes\n",
        "evidence.jsonl": "",
        "contradictions.md": contradictions_markdown(),
        "gaps.md": gaps_markdown(),
        "akbp-intake.md": akbp_intake_markdown(topic),
        "manifest.json": json.dumps(manifest, indent=2) + "\n",
    }
    written = []
    skipped = []
    for name, content in files.items():
        if write_file(target / name, content, overwrite):
            written.append(name)
        else:
            skipped.append(name)
    return target, written, skipped


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("--root", default=str(Path.home() / "Documents" / "InternetResearch"))
    parser.add_argument("--depth", choices=["quick", "standard", "deep", "exhaustive"], default="standard")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)
    target, written, skipped = create_workspace(args.topic, Path(args.root), args.depth, args.overwrite)
    print(target)
    if written:
        print("written: " + ", ".join(written))
    if skipped:
        print("skipped: " + ", ".join(skipped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
