# AKBP Protocol

AKBP means Agent Knowledge Base Protocol: a local-first, file-backed knowledge base for agents to read, write, verify, export, and carry source-backed knowledge across tools.

Use AKBP when internet research should become durable memory instead of a one-off answer.

## Core Workflow

Use this sequence:

1. Discover evidence.
2. Preview memory.
3. Approve write.
4. Recall cited context.
5. Update lifecycle.
6. Export bundle.

AKBP makes project knowledge reviewable before it becomes durable, cited when it is recalled, and explicit when it changes.

## Research Mapping

Map internet research into AKBP objects:

- Sources: URLs, PDFs, videos, transcripts, issues, commits, screenshots, files, folders, or user-provided documents.
- Claims: atomic facts, decisions, observations, warnings, workflows, preferences, or open questions.
- Evidence: source IDs attached to claims.
- Entities: companies, tools, people, repos, standards, APIs, products, files, or concepts.
- Relations: supersedes, contradicts, depends on, derived from, blocks, or related.
- Context packs: compact cited context for future sessions.
- Export bundles: portable reviewed research memory for another tool or repo.

## When To Use AKBP

Use AKBP for:

- Long-running research projects.
- Market maps and due diligence.
- Competitive intelligence that future agents should reuse.
- Technical research with source-backed decisions.
- Multi-agent handoff.
- Claims that may later be superseded, contradicted, archived, or reverified.
- Research briefs that need auditability beyond inline links.

Skip AKBP for:

- Quick factual lookups.
- One-off answers where durable memory adds ceremony.
- Private or sensitive material unless the user explicitly approves scope and storage.

## CLI Shape

If `akbp` or the repo CLI is available, use dry-run before durable writes:

```bash
python3 cli/akbp.py --path ./research-kb init
python3 cli/akbp.py --path ./research-kb source add notes.md --type file --title "Research notes"
python3 cli/akbp.py --path ./research-kb ingest notes.md --claim "Claim to preserve." --claim-type observation --dry-run
python3 cli/akbp.py --path ./research-kb ingest notes.md --claim "Claim to preserve." --claim-type observation
python3 cli/akbp.py --path ./research-kb index --incremental
python3 cli/akbp.py --path ./research-kb context "next research task"
```

Before running an apply command without `--dry-run`, get explicit approval unless trusted local policy already grants it.

## JSONL Tool Server Shape

If an AKBP tool server is available, start with capabilities and context:

```json
{"id":"caps-1","method":"akbp.capabilities"}
{"id":"ctx-1","method":"akbp.context","path":"./research-kb","params":{"task":"continue the research","limit":5}}
```

Preview writes first:

```json
{"id":"preview-1","method":"akbp.ingest","path":"./research-kb","dry_run":true,"params":{"file":"notes.md","claim":"Claim to preserve.","claim_type":"observation"}}
```

Apply only after review:

```json
{"id":"apply-1","method":"akbp.ingest","path":"./research-kb","approved":true,"params":{"file":"notes.md","claim":"Claim to preserve.","claim_type":"observation"}}
{"id":"index-1","method":"akbp.index","path":"./research-kb","approved":true,"params":{"incremental":true}}
```

Branch on structured `ok` and `error.code`, not free-form text.

## Useful Methods

- `akbp.capabilities`: inspect supported methods.
- `akbp.status`: inspect knowledge base state.
- `akbp.context`: retrieve cited context.
- `akbp.search`: search pages, claims, entities, and evidence.
- `akbp.source.add`: register a source.
- `akbp.source.verify`: re-check recorded file sources against hashes.
- `akbp.ingest`: preview or apply source-backed claims.
- `akbp.remember`: write a claim or observation when supported by the adapter.
- `akbp.supersede`: mark a claim as replaced.
- `akbp.contradict`: mark conflicting knowledge.
- `akbp.export`: create a portable bundle.
- `akbp.export_check`: validate a bundle before trusting it.
- `akbp.import_check`: validate an incoming bundle before applying it.
- `akbp.audit`: inspect operation history.

## Safety Rules

- Claims should cite source IDs, not uncited memory.
- Write methods should support dry-run mode.
- Treat review-required, dry-run, and approval fields as the trust boundary.
- Do not store secrets, cookies, tokens, private URLs, personal data, or sensitive material unless the user explicitly approves.
- Use source verification before relying on old file sources.
- Use export or import checks before trusting portable bundles.
- Use lifecycle updates instead of overwriting history when a claim changes.

## Output Guidance

When AKBP is part of the task, include:

- AKBP path or bundle used.
- Sources registered or proposed.
- Claims previewed or applied.
- Which writes were dry-run only.
- Which writes were approved.
- Any source verification or export-check result.

If the user did not approve writes, keep the output as an AKBP-ready preview rather than claiming durable memory was updated.
