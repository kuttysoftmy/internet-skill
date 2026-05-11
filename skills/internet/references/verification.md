# Verification

Verification is the difference between search and research. Every important claim needs provenance, date context, and a confidence label.

## Claim Ledger

Use this shape for material claims:

| ID | Claim | Evidence | Source | Date | Confidence | Caveat |
|---|---|---|---|---|---|---|
| C1 | Atomic factual claim | Quote, number, observation, or source-supported summary | URL/source ID | Event and publication date | High/Medium/Low | What could weaken it |

Make claims atomic. Split "X launched Y and users love it" into separate launch and sentiment claims.

## Confidence Grades

High:

- Supported by a Tier 1 source, or multiple independent Tier 1/Tier 2 sources.
- Dates, units, and scope are clear.
- No credible unresolved contradiction.

Medium:

- Supported by credible evidence but partial, indirect, source-limited, or context-dependent.
- One material detail is uncertain, stale, paywalled, or inferred.

Low:

- Single-source, indirect, old, disputed, unverifiable, or mostly community/social evidence.
- Use low confidence for leads and sentiment unless the question is about sentiment.

Do not upgrade confidence because many low-quality sources repeat the same claim.

## Triangulation

For claims that drive a recommendation, try to collect:

- One primary source.
- One independent confirmation.
- One source likely to reveal downside, disagreement, or failure.

If triangulation is not possible, say why.

## Date Discipline

Track:

- Publication date: when the source was published.
- Event date: when the thing happened.
- Version date: release, package, model, regulation, or documentation version.
- Access date: today, when source content may change.

Never blend old and new evidence without explaining the timeline. When a user says "today", "current", "latest", or "recent", include absolute dates in the answer.

## Contradictions

When sources conflict:

1. Identify the exact claim under dispute.
2. Compare source type and incentive.
3. Check whether sources refer to different regions, versions, names, dates, or definitions.
4. Prefer primary records over commentary.
5. Prefer newer records only when they supersede older records.
6. Quote or paraphrase the disagreement neutrally.
7. Assign confidence based on provenance, not popularity.

Record contradictions in this shape:

| Claim | Source A | Source B | Conflict | Likely Explanation | Confidence |
|---|---|---|---|---|---|

## Citation Hygiene

- Cite the exact page that supports the claim.
- Use inline Markdown links.
- Do not cite search result snippets.
- Do not cite a source for claims it merely repeats when the original is available.
- Do not overquote. Use short excerpts only when wording matters.
- If a source is paywalled, blocked, or inaccessible, identify it as inaccessible and do not pretend to have read it.
- If using a source's chart, table, filing, or embedded document, cite the original embedded source when possible.

## Source Incentive Check

Before relying on a source, ask:

- Who produced it?
- What do they gain if the reader believes it?
- Is it primary evidence, analysis, marketing, syndication, user sentiment, or speculation?
- Does it link to the underlying data?
- Does it include corrections or update history?

## High-Stakes Domains

Medical:

- Prefer clinical guidelines, regulators, systematic reviews, major medical institutions, and recent high-quality studies.
- State that the answer is not medical advice.

Legal:

- Prefer statutes, regulations, court records, agency guidance, and jurisdiction-specific primary sources.
- State jurisdiction and that the answer is not legal advice.

Financial:

- Prefer filings, audited statements, official pricing, regulator pages, and current market data.
- State that the answer is not financial advice.

Security:

- Prefer advisories, CVE records, vendor notices, patches, and exploit status from reputable sources.
- Avoid operational instructions that would enable abuse.

Safety:

- Prefer regulators, standards bodies, official advisories, recalls, manuals, and emergency guidance.
- Tell the user when real-world professional help is needed.
