---
name: internet
description: Deep iterative web research for any question, topic, company, person, product, technical issue, news event, market, document trail, or decision that benefits from current internet evidence. Use when the user asks to search the web, research anything deeply, verify a claim, compare sources, find latest information, produce a cited brief, investigate a topic, map a market, gather primary sources, or answer questions where recency, provenance, or source triangulation matters.
license: MIT
allowed-tools: WebSearch, WebFetch, Bash, Read, Write
metadata:
  tags:
    - research
    - web-search
    - deep-research
    - citations
    - verification
    - osint
    - source-triangulation
---

# Internet

## Overview

Use this skill to turn an open internet question into a sourced, evidence-weighted answer. Treat web research as an iterative investigation: define the target, build a source map, search in passes, extract claims, verify against independent evidence, and synthesize with citations and caveats.

If the user asks for "AKBP", use the AKBP loop defined here: Ask, Know, Browse, Prove. If they do not mention AKBP, still use the loop implicitly for non-trivial research.

## Quick Start

1. Restate the research question, scope, recency window, geography, and output target.
2. Decide depth:
   - **Quick**: 3-5 high-quality sources, 1-2 search passes.
   - **Standard**: 8-15 sources, 3-4 search passes, at least one contradiction pass.
   - **Deep**: 20+ sources, source-type coverage, contradiction pass, claim ledger, and gap fill.
3. Search broad first, then source-specific, then adversarially.
4. Open and read the strongest sources. Use primary sources whenever possible.
5. Extract claims into a claim ledger: claim, source, evidence, confidence, caveats.
6. Fill gaps with targeted follow-up searches.
7. Answer with inline citations, confidence, and unresolved questions.

For long investigations, create a scratch workspace:

```bash
python3 skills/internet/scripts/research_workspace.py "topic or question"
```

## AKBP Loop

### Ask

Pin down the question before searching. Identify:

- User's decision or deliverable.
- Required freshness: current, last 24 hours, last 30 days, historical, evergreen.
- Source needs: official, academic, news, social, forums, code, filings, docs, pricing pages, maps, videos, podcasts, PDFs.
- Constraints: jurisdiction, region, budget, audience, technical stack, risk tolerance.
- Missing clarification. Ask one concise question only when a reasonable assumption would materially change the result.

### Know

Write a short baseline before browsing:

- Known facts from the prompt.
- Hypotheses to test.
- Likely source classes.
- Search terms, aliases, ticker symbols, handles, product names, project names, competitors, authors, agencies, and dates.
- Risky assumptions that need verification.

### Browse

Run searches in passes:

1. **Orientation pass**: broad queries, current overview, entity disambiguation.
2. **Primary-source pass**: official docs, filings, repos, regulatory pages, papers, release notes, press rooms, datasets.
3. **Independent-source pass**: reputable reporting, expert blogs, analyst notes, standards bodies, academic sources.
4. **Ground-truth/community pass**: forums, issues, Reddit, HN, social posts, reviews, comments, app stores, package registries.
5. **Contradiction pass**: search for "criticism", "problem", "lawsuit", "outage", "pricing change", "not working", "alternative", "debunked", "correction", and source-specific disputes.
6. **Gap-fill pass**: targeted queries for unanswered claims, missing dates, unclear numbers, and source conflicts.

Use available tools in this order:

- Search tools for query discovery and recent results.
- Scrape or fetch tools for exact page content.
- Browser tools for JavaScript-heavy, interactive, or visual pages.
- Official documentation tools for libraries, frameworks, APIs, and SDKs.
- Local files or user-provided documents when the answer depends on supplied material.

### Prove

Do not stop at search snippets. Prove the answer:

- Every important factual claim should trace to a source URL or user-provided artifact.
- Prefer two independent confirmations for high-impact claims.
- Label single-source claims as such.
- Preserve dates: publication date, event date, access date when relevant.
- Separate what sources say from your inference.
- Track source quality and incentives.
- Include uncertainty when sources conflict or evidence is thin.

## Depth Controls

Read [research-depth.md](references/research-depth.md) when the user asks for deep, exhaustive, detailed, investigative, report-grade, due-diligence, or "anything required" research.

Default stopping rule: continue iterating until one of these is true:

- The answer is supported by enough independent, high-quality evidence for the user's decision.
- Additional searches return repeats rather than new evidence.
- The remaining gaps are inaccessible, private, paywalled, or require user credentials.
- The user asked for a quick answer.

## Source Strategy

Read [source-map.md](references/source-map.md) when choosing where to search. Match source classes to the question:

- Current facts: official pages, news wires, regulator pages, company blogs, status pages.
- Technical docs: official docs, specs, source repos, issue trackers, changelogs, package registries.
- Product research: pricing pages, reviews, forums, app stores, social posts, docs, support pages.
- Market research: competitors, analyst reports, job posts, funding databases, customer reviews, newsletters.
- People or companies: official bios, profile pages if accessible, GitHub, social posts, interviews, podcasts, filings.
- Academic or medical: peer-reviewed papers, systematic reviews, clinical guidelines, regulatory agencies.
- Legal or financial: primary law, court records, regulator filings, audited statements, official datasets.

## Verification Rules

Read [verification.md](references/verification.md) for claim grading, contradiction handling, and citation hygiene.

Core rules:

- Use primary sources over summaries when stakes are high.
- Use current sources for current claims.
- Do not rely on AI-generated summaries as evidence unless explicitly evaluating the summary itself.
- Do not bypass paywalls, access controls, robots restrictions, or private systems.
- Ask before using credentials, private accounts, or anything that could expose personal data.
- For medical, legal, financial, safety, or security topics, state limits clearly and ground claims in authoritative sources.

## Output Shapes

Read [output-templates.md](references/output-templates.md) when the user asks for a report, memo, comparison, source table, brief, timeline, recommendation, or evidence pack.

Default answer shape:

1. Direct answer in 2-5 sentences.
2. Evidence-backed findings with inline citations.
3. What is uncertain or disputed.
4. Practical recommendation or next step when useful.
5. Source notes only when the user needs auditability.

Use inline Markdown links for citations. Do not dump raw URLs when a readable link label is available.

## Workspace Artifacts

Use `scripts/research_workspace.py` for investigations that need persistence, many sources, or multiple research passes. The script creates:

- `research.md`: working brief and synthesis outline.
- `queries.md`: query log and iteration notes.
- `claims.md`: claim ledger.
- `sources.csv`: source ledger.
- `gaps.md`: open questions and follow-up searches.
- `manifest.json`: machine-readable metadata.

Run:

```bash
python3 skills/internet/scripts/research_workspace.py "Should we use X for Y?" --depth deep
```

## Failure Modes To Avoid

- Answering from memory when the user asked for current or web-backed research.
- Treating search snippets as sources.
- Reading only the first page that agrees with the hypothesis.
- Hiding uncertainty because the final answer sounds cleaner.
- Citing an article for a claim that came from another article's embedded quote, chart, or source.
- Mixing old and new facts without dates.
- Over-researching after the answer is already solid enough for the user's goal.
