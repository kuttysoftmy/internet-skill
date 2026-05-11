# AKBP Protocol

AKBP means Agent Knowledge Base Protocol: [github.com/rohitg00/akbp](https://github.com/rohitg00/akbp). It is a local-first, file-backed knowledge base for agents to read, write, verify, export, and carry source-backed knowledge across tools.

Use AKBP when internet research should become durable memory instead of a one-off answer.

## Core Idea

AKBP makes project knowledge reviewable before it becomes durable, cited when it is recalled, and explicit when it changes.

The AKBP workflow is:

1. Discover evidence.
2. Preview memory.
3. Approve write.
4. Recall cited context.
5. Update lifecycle.
6. Export bundle.

## Research Fit

For web research, map the investigation into AKBP objects:

- Sources: URLs, PDFs, videos, transcripts, issues, commits, screenshots, files, or folders.
- Claims: atomic facts, decisions, observations, warnings, workflows, preferences, or open questions.
- Evidence: source IDs attached to claims.
- Entities: companies, tools, people, repos, standards, APIs, products, files, or concepts.
- Relations: supersedes, contradicts, depends on, derived from, blocks, or related lifecycle links.
- Context packs: compact cited context for the next agent session.
- Export bundles: portable reviewed research memory for another tool or repo.

## When To Use It

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

Before running the apply command without `--dry-run`, get explicit approval unless the user has already granted trusted local policy.

## JSONL Tool Server Shape

If an AKBP tool server is available, start with capabilities and context:

```json
{"id":"caps-1","method":"akbp.capabilities"}
{"id":"ctx-1","method":"akbp.context","path":"./research-kb","params":{"task":"continue the research","limit":5}}
```

For writes, preview first:

```json
{"id":"preview-1","method":"akbp.ingest","path":"./research-kb","dry_run":true,"params":{"file":"notes.md","claim":"Claim to preserve.","claim_type":"observation"}}
```

Apply only after review:

```json
{"id":"apply-1","method":"akbp.ingest","path":"./research-kb","approved":true,"params":{"file":"notes.md","claim":"Claim to preserve.","claim_type":"observation"}}
{"id":"index-1","method":"akbp.index","path":"./research-kb","approved":true,"params":{"incremental":true}}
```

Branch on `ok` and `error.code`, not free-form text.

## Safety Rules

- Claims should cite source IDs, not uncited memory.
- Write methods should use dry-run first.
- Treat `review_required` and `apply_instruction` as the trust boundary.
- Do not store secrets, cookies, tokens, private URLs, or personal data unless the user explicitly approves.
- Use `akbp.source.verify` before relying on old file sources.
- Use `akbp.export_check` or `akbp.import_check` before trusting or applying a portable bundle.
- Use lifecycle updates instead of overwriting history when a claim changes.

## Output Guidance

When AKBP is part of the task, include:

- The AKBP path or bundle used.
- Sources registered or proposed.
- Claims previewed or applied.
- Which writes were dry-run only.
- Which writes were approved.
- Any source verification or export-check result.

If the user did not approve writes, keep the output as an AKBP-ready preview rather than claiming durable memory was updated.
