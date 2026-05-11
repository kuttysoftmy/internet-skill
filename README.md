# Internet Skill

Deep iterative web research for any question.

`internet` turns broad research prompts into a disciplined investigation loop: Ask, Know, Browse, Prove. It is built for current facts, source triangulation, contradiction searches, claim ledgers, and cited synthesis.

## Install

```bash
/plugin marketplace add rohitg00/internet-skill
/plugin install internet@internet-skill
```

## What It Does

- Plans search passes before answering.
- Searches broad, primary, independent, community, contradiction, and gap-fill sources.
- Tracks claims, confidence, source quality, dates, and unresolved gaps.
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

The helper creates a working folder with query, claim, source, and gap ledgers.
