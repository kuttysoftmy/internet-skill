---
name: internet
description: Deep, iterative internet research for current facts, source triangulation, contradiction checks, due diligence, competitive analysis, claim verification, "latest" lookups, and cited reports. Use when the user asks to browse, search, research the web, verify claims, compare sources, gather primary sources, investigate companies, people, products, technical topics, news, events, markets, or create AKBP-ready durable research evidence.
---

# Internet

Use this skill to turn an open internet question into a sourced, evidence-weighted answer. Treat web research as an investigation, not a lookup: define the target, plan the source map, search in passes, read the strongest sources, extract claims, verify against independent evidence, and synthesize with citations and caveats.

Prime directive: do not answer a web-backed request from memory unless the user explicitly says not to browse. Search, open, read, compare, and cite.

## Quick Start

1. Restate the research contract: question, decision or deliverable, recency window, geography or jurisdiction, audience, constraints, and output shape.
2. Run the preflight traps below. Ask one concise clarifying question only when a bad assumption would materially change the answer.
3. Choose depth: quick, standard, deep, or exhaustive. Read [research-depth.md](references/research-depth.md) for detailed thresholds.
4. Build a plan before browsing. Include source classes, query passes, target entities, contradiction searches, acceptance criteria, and stopping conditions.
5. Search broad first, then primary, then independent, then community or ground truth, then contradiction, then gap-fill.
6. Open sources. Do not cite snippets. Record exact dates, source type, incentive, and what each source actually supports.
7. Synthesize with inline citations, confidence, conflicts, and gaps. Separate source claims from your inference.
8. If the research should persist for future agents, use the AKBP preview workflow. Do not silently write durable memory.

For long investigations, create a workspace and populate it as you browse. The recorder commands update both the structured ledgers and `research.md` activity log:

```bash
WORKSPACE="$(python3 skills/internet/scripts/research_workspace.py create "topic or question" --depth deep | sed -n '1p')"
python3 skills/internet/scripts/research_workspace.py add-query "$WORKSPACE" --pass-label orientation --query "exact search query" --tool web --why "what this pass should prove" --result "what changed"
python3 skills/internet/scripts/research_workspace.py add-source "$WORKSPACE" --url "https://example.com/source" --title "source title" --type official --tier 1 --published YYYY-MM-DD --notes "what this source supports"
python3 skills/internet/scripts/research_workspace.py add-claim "$WORKSPACE" --claim "material claim" --evidence "specific evidence" --source-id S001 --confidence High --publication-date YYYY-MM-DD
python3 skills/internet/scripts/research_workspace.py add-evidence "$WORKSPACE" --source-id S001 --claim-id C001 --evidence "structured evidence note" --confidence High
python3 skills/internet/scripts/research_workspace.py summary "$WORKSPACE"
```

## Preflight Traps

Catch bad research prompts before wasting search passes.

- **Demographic shopping**: prompts like "gift for 40 year old" need relationship, interests, budget, region, and constraints. Ask for missing context or state assumptions.
- **Generic ranking**: prompts like "best AI tools" need criteria, user profile, price sensitivity, platform, and time horizon. If the user wants a broad scan, define categories before searching.
- **Ambiguous entity**: resolve names, aliases, tickers, handles, repos, legal names, countries, and date ranges before searching. Example: "Apple", "Claude", "Warriors", "Gemini".
- **Numeric trap**: market size, revenue, downloads, salaries, benchmarks, prices, and popularity claims need units, date, geography, and original source.
- **Temporal trap**: "latest", "today", "current", "recent", and "last month" require explicit absolute dates in the answer.
- **Tutorial phrase trap**: "how to", "setup", and error-message prompts should prioritize official docs, source repos, changelogs, issue trackers, and exact error strings.
- **High-stakes trap**: medical, legal, financial, safety, and security topics require authoritative sources, jurisdiction or scope, and careful disclaimers.
- **Single-source trap**: if only one source supports a material claim, label it as single-source and say what could not be verified.

## Research Plan

Before searching, write a compact plan in this shape, mentally or in `research.md`:

```json
{
  "question": "what the user needs answered",
  "depth": "quick|standard|deep|exhaustive",
  "recency_window": "absolute dates or evergreen",
  "entities": ["canonical names, aliases, handles, repos"],
  "source_classes": ["official", "independent", "community", "contradiction"],
  "query_passes": [
    {"label": "orientation", "queries": ["broad discovery query"]},
    {"label": "primary", "queries": ["official/source-specific query"]},
    {"label": "contradiction", "queries": ["criticism/problem/correction query"]}
  ],
  "acceptance_criteria": ["what evidence is enough"],
  "stop_conditions": ["saturation or inaccessible gaps"]
}
```

Use [source-map.md](references/source-map.md) when choosing sources and queries. Use [output-templates.md](references/output-templates.md) when the deliverable is a report, comparison, evidence pack, timeline, or recommendation.

## Search Passes

Run search iteratively. Each pass should change the evidence state.

1. **Orientation**: discover names, aliases, timeline, major sources, and likely disputes.
2. **Primary-source**: official docs, filings, repos, release notes, standards, papers, status pages, datasets, regulatory pages.
3. **Independent-source**: reputable reporting, expert analysis, institutional pages, maintainer blogs, analyst notes, conference talks.
4. **Ground-truth/community**: GitHub issues, HN, Reddit, Stack Overflow, forums, app reviews, social posts, comments, package registries, video transcripts.
5. **Contradiction**: search for criticism, correction, lawsuit, outage, vulnerability, pricing change, "not working", "alternative", "debunked", "limitations", and exact disputed claims.
6. **Gap-fill**: target missing dates, unclear numbers, unsupported claims, stale pages, and source conflicts.

When the source trail crosses web pages, PDFs, code, videos, and forums, keep a source ledger. Do not let one source class dominate the answer unless that is the point of the question.

## Proof Contract

Read [verification.md](references/verification.md) for claim grading and contradiction handling.

Every material claim should have:

- A source URL or user-provided artifact.
- Source type and quality tier.
- Publication date, event date, version date, or access date when relevant.
- Confidence: high, medium, or low.
- Caveat: what would weaken, supersede, or contradict the claim.

Prefer two independent confirmations for claims that drive a recommendation. Prefer primary sources for current, technical, legal, financial, medical, security, or regulatory claims. Treat community evidence as sentiment or lived experience unless independently verified.

## Synthesis Contract

Answer the user's actual question first, then show the evidence.

- Use inline Markdown citations.
- Use exact dates for time-sensitive claims.
- Say "I found" for source-backed evidence and "I infer" for analysis.
- Surface contradictions instead of smoothing them away.
- Label old, paywalled, inaccessible, single-source, or jurisdiction-specific evidence.
- Do not include a raw link dump unless the user asks for an evidence pack.
- Do not quote long passages. Use short excerpts only when wording matters.
- For recommendations, state the decision criteria and who the recommendation fits.

Default answer shape:

1. Direct answer in 2-5 sentences.
2. Evidence-backed findings with citations.
3. Uncertainty, conflicts, and gaps.
4. Recommendation or next step when useful.
5. Source notes only when auditability matters.

## Depth Controls

Default to **standard** for research requests. Upgrade to **deep** when the user asks for "detailed", "as detailed as possible", "exhaustive", "due diligence", "market map", "investigate", "compare", "should we", or when the decision is high-cost or high-stakes.

Stop only when one of these is true:

- Evidence meets the acceptance criteria.
- Three consecutive targeted searches add no new material source, contradiction, or claim.
- Remaining gaps are inaccessible, private, paywalled, or require user credentials.
- The user requested a quick answer.

Before final synthesis, do one final gap pass:

- Search the strongest counterclaim.
- Search the newest update.
- Search official source plus exact claim terms.
- Search date-bounded queries when timeline matters.

## AKBP Integration

Read [akbp-protocol.md](references/akbp-protocol.md) when the user says AKBP, when the research should become durable knowledge, or when the work needs reviewed claims, source hashes, audit history, lifecycle updates, context packs, or export bundles.

AKBP workflow:

1. Discover evidence.
2. Preview memory with dry-run behavior.
3. Ask for approval before durable writes unless a trusted local policy already grants it.
4. Apply approved writes only.
5. Rebuild or update the index.
6. Recall cited context for follow-up work.
7. Use lifecycle relations for superseded or contradicted claims.
8. Export and check bundles before another agent trusts them.

Never store secrets, cookies, tokens, private URLs, personal data, or sensitive material in AKBP unless the user explicitly approves the scope and storage.

## Workspace Artifacts

Use `scripts/research_workspace.py` for investigations that need persistence, many sources, or multiple passes. It creates and populates:

- `research.md`: contract, plan, method, and synthesis draft.
- `plan.json`: machine-readable plan skeleton.
- `queries.md`: query ledger.
- `claims.md`: claim ledger.
- `sources.csv`: source ledger.
- `evidence.jsonl`: structured evidence notes.
- `contradictions.md`: conflict ledger.
- `gaps.md`: open questions and follow-up searches.
- `akbp-intake.md`: AKBP source and claim preview checklist.
- `manifest.json`: metadata.

Minimum populated workspace for standard, deep, or exhaustive work:

- One `queries.md` row for each search pass actually run.
- One `sources.csv` row for every opened source considered for evidence.
- One `claims.md` row for each material claim in the synthesis.
- One `evidence.jsonl` row for each source-backed claim.
- `contradictions.md` rows when sources conflict.
- `gaps.md` rows for unresolved but decision-relevant unknowns.

Before final synthesis, run `summary` and open `research.md`. If sources, claims, or evidence are zero after a workspace-backed investigation, or if `research.md` still contains only blank template headings, the workspace is incomplete.

## Failure Modes To Avoid

- Answering from memory when the user asked for current or web-backed research.
- Treating search snippets as sources.
- Reading only sources that agree with the hypothesis.
- Ignoring entity ambiguity.
- Mixing old and new facts without dates.
- Citing an article for a claim it merely repeats from another source.
- Letting SEO pages outrank primary sources.
- Treating social posts as factual proof rather than sentiment.
- Hiding thin evidence because the answer sounds cleaner.
- Creating durable AKBP memory without preview and approval.
