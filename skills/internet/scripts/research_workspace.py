#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from io import StringIO
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

SOURCE_FIELDS = [
    "id",
    "url",
    "title",
    "author",
    "published",
    "event_date",
    "accessed",
    "type",
    "tier",
    "opened",
    "notes",
]


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:80] or "research"


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def md_cell(value):
    text = str("" if value is None else value).replace("\n", "<br>")
    return text.replace("|", "\\|")


def append_text(path, text):
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def csv_line(values):
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow(values)
    return buffer.getvalue()


def read_source_rows(workspace):
    path = workspace / "sources.csv"
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def next_id(workspace, filename, prefix):
    path = workspace / filename
    if not path.exists():
        return f"{prefix}001"
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"| {prefix}"):
            count += 1
    return f"{prefix}{count + 1:03d}"


def activity_item(label, value):
    if not value:
        return ""
    return f"- {label}: {value}\n"


def append_activity(workspace, title, rows):
    path = workspace / "research.md"
    if not path.exists():
        return
    existing = path.read_text(encoding="utf-8")
    prefix = ""
    if "## Activity Log" not in existing:
        prefix = "\n## Activity Log\n"
    append_text(path, f"{prefix}\n### {title}\n\n{rows}".rstrip() + "\n")


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

Use `research_workspace.py add-query` after each search pass and `add-source` for every opened source.

- Orientation:
- Primary:
- Independent:
- Community or ground truth:
- Contradiction:
- Gap-fill:

## Activity Log

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
        "schema": "internet-research-workspace/v3",
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
        "sources.csv": ",".join(SOURCE_FIELDS) + "\n",
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


def update_plan_with_query(workspace, pass_label, query):
    path = workspace / "plan.json"
    if not path.exists():
        return
    plan = json.loads(path.read_text(encoding="utf-8"))
    for item in plan.get("query_passes", []):
        if item.get("label") == pass_label:
            item.setdefault("queries", []).append(query)
            item["status"] = "in_progress"
            break
    path.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")


def add_query(workspace, pass_label, query, tool="", why="", result="", follow_up=""):
    append_text(
        workspace / "queries.md",
        f"| {md_cell(pass_label)} | {md_cell(query)} | {md_cell(tool)} | {md_cell(why)} | {md_cell(result)} | {md_cell(follow_up)} |\n",
    )
    update_plan_with_query(workspace, pass_label, query)
    append_activity(
        workspace,
        f"Query Pass: {pass_label}",
        activity_item("Query", query)
        + activity_item("Tool", tool)
        + activity_item("Why", why)
        + activity_item("Result", result)
        + activity_item("Follow-up", follow_up),
    )


def add_source(workspace, url, title="", source_type="", tier="", author="", published="", event_date="", opened="yes", notes=""):
    rows = read_source_rows(workspace)
    source_id = f"S{len(rows) + 1:03d}"
    values = [
        source_id,
        url,
        title,
        author,
        published,
        event_date,
        today(),
        source_type,
        tier,
        opened,
        notes,
    ]
    append_text(workspace / "sources.csv", csv_line(values))
    append_activity(
        workspace,
        f"Source {source_id}",
        activity_item("Title", title)
        + activity_item("URL", url)
        + activity_item("Type", source_type)
        + activity_item("Tier", tier)
        + activity_item("Published", published)
        + activity_item("Event date", event_date)
        + activity_item("Notes", notes),
    )
    return source_id


def add_claim(workspace, claim, evidence, source_id, confidence, event_date="", publication_date="", caveat=""):
    claim_id = next_id(workspace, "claims.md", "C")
    append_text(
        workspace / "claims.md",
        f"| {claim_id} | {md_cell(claim)} | {md_cell(evidence)} | {md_cell(source_id)} | {md_cell(event_date)} | {md_cell(publication_date)} | {md_cell(confidence)} | {md_cell(caveat)} |\n",
    )
    append_activity(
        workspace,
        f"Claim {claim_id}",
        activity_item("Claim", claim)
        + activity_item("Evidence", evidence)
        + activity_item("Source ID", source_id)
        + activity_item("Confidence", confidence)
        + activity_item("Event date", event_date)
        + activity_item("Publication date", publication_date)
        + activity_item("Caveat", caveat),
    )
    return claim_id


def add_evidence(workspace, source_id, evidence, claim_id="", url="", quote="", confidence="", notes=""):
    row = {
        "time": now_iso(),
        "source_id": source_id,
        "claim_id": claim_id,
        "url": url,
        "evidence": evidence,
        "quote": quote,
        "confidence": confidence,
        "notes": notes,
    }
    append_text(workspace / "evidence.jsonl", json.dumps(row, ensure_ascii=True) + "\n")
    append_activity(
        workspace,
        "Evidence Note",
        activity_item("Claim ID", claim_id)
        + activity_item("Source ID", source_id)
        + activity_item("Evidence", evidence)
        + activity_item("URL", url)
        + activity_item("Confidence", confidence)
        + activity_item("Notes", notes),
    )


def add_contradiction(workspace, claim, source_a, source_b, conflict, explanation="", confidence=""):
    append_text(
        workspace / "contradictions.md",
        f"| {md_cell(claim)} | {md_cell(source_a)} | {md_cell(source_b)} | {md_cell(conflict)} | {md_cell(explanation)} | {md_cell(confidence)} |\n",
    )
    append_activity(
        workspace,
        "Contradiction",
        activity_item("Claim", claim)
        + activity_item("Source A", source_a)
        + activity_item("Source B", source_b)
        + activity_item("Conflict", conflict)
        + activity_item("Likely explanation", explanation)
        + activity_item("Confidence", confidence),
    )


def add_gap(workspace, gap, why="", search="", status="", next_step=""):
    append_text(
        workspace / "gaps.md",
        f"| {md_cell(gap)} | {md_cell(why)} | {md_cell(search)} | {md_cell(status)} | {md_cell(next_step)} |\n",
    )
    append_activity(
        workspace,
        "Gap",
        activity_item("Gap", gap)
        + activity_item("Why it matters", why)
        + activity_item("Search tried", search)
        + activity_item("Status", status)
        + activity_item("Next step", next_step),
    )


def count_table_rows(path, prefix=None):
    if not path.exists():
        return 0
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("|---") or line.startswith("| Pass ") or line.startswith("| ID ") or line.startswith("| Claim ") or line.startswith("| Gap "):
            continue
        if prefix and not line.startswith(f"| {prefix}"):
            continue
        count += 1
    return count


def workspace_summary(workspace):
    evidence_path = workspace / "evidence.jsonl"
    evidence_count = 0
    if evidence_path.exists():
        evidence_count = sum(1 for line in evidence_path.read_text(encoding="utf-8").splitlines() if line.strip())
    return {
        "workspace": str(workspace),
        "queries": count_table_rows(workspace / "queries.md"),
        "sources": len(read_source_rows(workspace)),
        "claims": count_table_rows(workspace / "claims.md", "C"),
        "evidence": evidence_count,
        "contradictions": count_table_rows(workspace / "contradictions.md"),
        "gaps": count_table_rows(workspace / "gaps.md"),
    }


def build_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    create = sub.add_parser("create")
    create.add_argument("topic")
    create.add_argument("--root", default=str(Path.home() / "Documents" / "InternetResearch"))
    create.add_argument("--depth", choices=["quick", "standard", "deep", "exhaustive"], default="standard")
    create.add_argument("--overwrite", action="store_true")

    query = sub.add_parser("add-query")
    query.add_argument("workspace")
    query.add_argument("--pass-label", required=True)
    query.add_argument("--query", required=True)
    query.add_argument("--tool", default="")
    query.add_argument("--why", default="")
    query.add_argument("--result", default="")
    query.add_argument("--follow-up", default="")

    source = sub.add_parser("add-source")
    source.add_argument("workspace")
    source.add_argument("--url", required=True)
    source.add_argument("--title", default="")
    source.add_argument("--type", default="")
    source.add_argument("--tier", default="")
    source.add_argument("--author", default="")
    source.add_argument("--published", default="")
    source.add_argument("--event-date", default="")
    source.add_argument("--opened", default="yes")
    source.add_argument("--notes", default="")

    claim = sub.add_parser("add-claim")
    claim.add_argument("workspace")
    claim.add_argument("--claim", required=True)
    claim.add_argument("--evidence", required=True)
    claim.add_argument("--source-id", required=True)
    claim.add_argument("--confidence", required=True)
    claim.add_argument("--event-date", default="")
    claim.add_argument("--publication-date", default="")
    claim.add_argument("--caveat", default="")

    evidence = sub.add_parser("add-evidence")
    evidence.add_argument("workspace")
    evidence.add_argument("--source-id", required=True)
    evidence.add_argument("--evidence", required=True)
    evidence.add_argument("--claim-id", default="")
    evidence.add_argument("--url", default="")
    evidence.add_argument("--quote", default="")
    evidence.add_argument("--confidence", default="")
    evidence.add_argument("--notes", default="")

    contradiction = sub.add_parser("add-contradiction")
    contradiction.add_argument("workspace")
    contradiction.add_argument("--claim", required=True)
    contradiction.add_argument("--source-a", required=True)
    contradiction.add_argument("--source-b", required=True)
    contradiction.add_argument("--conflict", required=True)
    contradiction.add_argument("--explanation", default="")
    contradiction.add_argument("--confidence", default="")

    gap = sub.add_parser("add-gap")
    gap.add_argument("workspace")
    gap.add_argument("--gap", required=True)
    gap.add_argument("--why", default="")
    gap.add_argument("--search", default="")
    gap.add_argument("--status", default="")
    gap.add_argument("--next-step", default="")

    summary = sub.add_parser("summary")
    summary.add_argument("workspace")

    return parser


def run_create(args):
    target, written, skipped = create_workspace(args.topic, Path(args.root), args.depth, args.overwrite)
    print(target)
    if written:
        print("written: " + ", ".join(written))
    if skipped:
        print("skipped: " + ", ".join(skipped))
    return 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    if argv and argv[0] not in {
        "create",
        "add-query",
        "add-source",
        "add-claim",
        "add-evidence",
        "add-contradiction",
        "add-gap",
        "summary",
    }:
        argv = ["create"] + argv
    args = parser.parse_args(argv)
    command = args.command
    if command == "create":
        return run_create(args)
    workspace = Path(args.workspace)
    if command == "add-query":
        add_query(workspace, args.pass_label, args.query, args.tool, args.why, args.result, args.follow_up)
    elif command == "add-source":
        print(add_source(workspace, args.url, args.title, args.type, args.tier, args.author, args.published, args.event_date, args.opened, args.notes))
    elif command == "add-claim":
        print(add_claim(workspace, args.claim, args.evidence, args.source_id, args.confidence, args.event_date, args.publication_date, args.caveat))
    elif command == "add-evidence":
        add_evidence(workspace, args.source_id, args.evidence, args.claim_id, args.url, args.quote, args.confidence, args.notes)
    elif command == "add-contradiction":
        add_contradiction(workspace, args.claim, args.source_a, args.source_b, args.conflict, args.explanation, args.confidence)
    elif command == "add-gap":
        add_gap(workspace, args.gap, args.why, args.search, args.status, args.next_step)
    elif command == "summary":
        print(json.dumps(workspace_summary(workspace), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
