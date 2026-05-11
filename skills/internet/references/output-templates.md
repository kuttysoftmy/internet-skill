# Output Templates

Choose the smallest shape that satisfies the user's goal. Always include inline citations for factual claims that came from the web.

## Direct Answer

Use for quick factual questions.

```markdown
Answer in 2-5 sentences with citations.

Confidence: High/Medium/Low.
```

## Research Brief

Use for standard research.

```markdown
**Bottom Line**
Short answer and recommendation.

**Key Findings**
- Finding with inline citation. Confidence: High/Medium/Low.
- Finding with inline citation. Confidence: High/Medium/Low.

**Uncertainty**
What is disputed, thin, unavailable, date-sensitive, or inferred.

**Sources Checked**
Short note on source classes, not a raw link dump unless requested.
```

## Deep Report

Use for due diligence, market maps, investigations, and "as detailed as possible" prompts.

```markdown
**Executive Summary**
Decision-grade summary.

**Method**
Search passes, source classes, date window, inclusion criteria, and saturation status.

**Findings**
Numbered findings with citations and confidence labels.

**Evidence Table**
| Claim | Evidence | Source | Date | Confidence | Caveat |
|---|---|---|---|---|---|

**Contradictions**
Where sources disagree and how to interpret it.

**Gaps**
What remains unknown, inaccessible, private, paywalled, stale, or out of scope.

**Recommendation**
Actionable next step.
```

## Comparison

Use for vendor, tool, product, company, model, framework, or option comparisons.

```markdown
**Recommendation**
Best choice by use case and criteria.

| Option | Best For | Strengths | Weaknesses | Evidence | Confidence |
|---|---|---|---|---|---|

**Decision Criteria**
Price, reliability, ecosystem, lock-in, migration cost, compliance, maintenance, UX, or other relevant criteria.

**Notes**
Pricing, availability, regional limits, risks, and unresolved gaps.
```

## Timeline

Use for incidents, news, legal matters, launches, outages, investigations, and fast-changing topics.

```markdown
**Timeline**
- YYYY-MM-DD: Event with citation.
- YYYY-MM-DD: Event with citation.

**Current State**
What is true now, with access date if content can change.

**What Changed**
What superseded earlier facts.

**Open Questions**
What still has not been confirmed.
```

## Evidence Pack

Use when the user wants auditability more than prose.

```markdown
| ID | Source | Type | Date | Key Evidence | Supports | Limits |
|---|---|---|---|---|---|---|
```

## Claim Ledger

Use when preparing AKBP claims or serious reports.

```markdown
| ID | Claim | Evidence | Source IDs | Confidence | Status |
|---|---|---|---|---|---|
```

## Recommendation Memo

Use when the user asks "should we" or needs a decision.

```markdown
**Recommendation**
Do X / Do not do X / Do X only if Y.

**Why**
Top 3 evidence-backed reasons.

**Risks**
What could make the recommendation wrong.

**Decision Boundary**
What new evidence would change the recommendation.

**Next Step**
Concrete action.
```

## Tone Rules

- Be direct.
- Separate fact from inference.
- Use "I found" for evidence and "I infer" for analysis.
- Avoid pretending certainty when sources are thin.
- Prefer human-readable link labels over raw URLs.
- Keep source notes short unless the user asks for auditability.
