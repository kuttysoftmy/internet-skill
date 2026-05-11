# Internet Skill

Deep iterative web research for any question.

`internet` turns broad research prompts into a disciplined investigation loop for current facts, source triangulation, contradiction searches, claim ledgers, and cited synthesis. When the user wants durable research memory, it uses AKBP: the Agent Knowledge Base Protocol from [github.com/rohitg00/akbp](https://github.com/rohitg00/akbp).

## Install

```bash
/plugin marketplace add rohitg00/internet-skill
/plugin install internet@internet-skill
```

## What It Does

- Plans search passes before answering.
- Searches broad, primary, independent, community, contradiction, and gap-fill sources.
- Tracks claims, confidence, source quality, dates, and unresolved gaps.
- Prepares AKBP source and claim previews for durable, review-gated research memory.
- Produces cited briefs, deep reports, comparisons, timelines, and evidence packs.
- Includes a workspace helper for long-running investigations.

## Example Prompts

```text
Use $internet to research whether we should adopt Bun for a TypeScript monorepo in 2026.
```

```text
Use $internet to build a detailed competitor map for AI browser automation tools.
```

```text
Use $internet to verify the latest Kubernetes Gateway API production readiness claims.
```

## Workspace Helper

```bash
python3 skills/internet/scripts/research_workspace.py "AI browser automation tools" --depth deep
```

The helper creates a working folder with query, claim, source, gap, and AKBP intake ledgers.
