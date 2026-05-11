# Internet Skill

Deep iterative web research for current facts, verification, due diligence, comparisons, market maps, and cited synthesis.

`internet` turns broad research prompts into a disciplined investigation loop: preflight the question, plan source classes, search in passes, read primary evidence, check contradictions, track claims, and synthesize with citations. When research should become durable memory, it prepares review-gated AKBP source and claim previews.

## Install

Install this repository with any skill-capable agent or skill manager that can consume a `skills/` directory. The skill itself lives at `skills/internet/SKILL.md` and is intentionally agent-portable.

With SkillKit:

```bash
npx skillkit install rohitg00/internet-skill
```

With an agent-specific plugin marketplace, add `rohitg00/internet-skill` and install the `internet` skill using that agent's normal plugin flow.

## What It Does

- Plans research before searching.
- Catches ambiguous prompts, generic rankings, numeric traps, temporal traps, and high-stakes edge cases.
- Searches orientation, primary, independent, community, contradiction, and gap-fill passes.
- Tracks claims, source tiers, dates, confidence, caveats, contradictions, and unresolved gaps.
- Prepares AKBP source and claim previews without silently writing durable memory.
- Produces cited briefs, reports, comparisons, timelines, recommendation memos, and evidence packs.
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

The helper creates a working folder with `research.md`, `plan.json`, query, claim, source, evidence, contradiction, gap, and AKBP intake ledgers.
