#!/usr/bin/env python3
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:80] or "research"


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def research_markdown(topic, depth, created):
    return f"""# Internet Research: {topic}

Created: {created}
Depth: {depth}

## Research Contract

- User question:
- Decision or deliverable:
- Recency window:
- Geography or jurisdiction:
- Assumptions:
- Required output:

## Research Loop

### Ask

- Clarifications needed:
- Scope boundaries:

### Know

- Known facts:
- Hypotheses:
- Aliases, handles, products, competitors, dates:

### Browse

- Pass 1 orientation:
- Pass 2 primary sources:
- Pass 3 independent sources:
- Pass 4 community or ground truth:
- Pass 5 contradiction:
- Pass 6 gap fill:

### Prove

- High-confidence claims:
- Medium-confidence claims:
- Low-confidence or single-source claims:
- Contradictions:
- Gaps:

## Synthesis Draft

## Final Answer
"""


def akbp_intake_markdown(topic):
    return f"""# AKBP Intake Preview: {topic}

AKBP means Agent Knowledge Base Protocol.

Use this file to prepare reviewed sources and durable claim proposals. Do not apply AKBP writes until the user approves the dry-run preview.

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

| ID | Claim | Evidence | Source ID | Date | Confidence | Notes |
|---|---|---|---|---|---|---|
"""


def queries_markdown():
    return """# Query Ledger

| Pass | Query | Tool | Why | Result | Follow-up |
|---|---|---|---|---|---|
"""


def gaps_markdown():
    return """# Gaps

| Gap | Why It Matters | Search Tried | Status | Next Step |
|---|---|---|---|---|
"""


def write_file(path, content, overwrite):
    if path.exists() and not overwrite:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def create_workspace(topic, root, depth, overwrite):
    created = today()
    target = root / f"{created}-{slugify(topic)}"
    target.mkdir(parents=True, exist_ok=True)
    manifest = {
        "topic": topic,
        "depth": depth,
        "created": created,
        "files": [
            "research.md",
            "queries.md",
            "claims.md",
            "sources.csv",
            "akbp-intake.md",
            "gaps.md",
        ],
    }
    files = {
        "research.md": research_markdown(topic, depth, created),
        "queries.md": queries_markdown(),
        "claims.md": claims_markdown(),
        "sources.csv": "id,url,title,author,published,accessed,type,tier,notes\n",
        "akbp-intake.md": akbp_intake_markdown(topic),
        "gaps.md": gaps_markdown(),
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
