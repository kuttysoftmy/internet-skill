# Output Templates

Choose the smallest shape that satisfies the user's goal.

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
- Finding with inline citation.
- Finding with inline citation.
- Finding with inline citation.

**Uncertainty**
What is disputed, thin, unavailable, or date-sensitive.

**Sources Checked**
Short note on source classes, not a raw link dump unless requested.
```

## Deep Report

Use for serious research, due diligence, market maps, and "as detailed as possible" prompts.

```markdown
**Executive Summary**
Decision-grade summary.

**Method**
Search passes, source classes, date window, and inclusion criteria.

**Findings**
Numbered findings with citations and confidence labels.

**Evidence Table**
Claim, source, evidence, confidence, caveat.

**Contradictions**
Where sources disagree and how to interpret it.

**Gaps**
What remains unknown or inaccessible.

**Recommendation**
Actionable next step.
```

## Comparison

Use for vendor, tool, product, company, model, or option comparisons.

```markdown
**Recommendation**
Best choice by use case.

| Option | Best For | Strengths | Weaknesses | Evidence | Confidence |
|---|---|---|---|---|---|

**Notes**
Pricing, availability, risk, lock-in, migration cost, and unresolved gaps.
```

## Timeline

Use for incidents, news, legal matters, product launches, and fast-changing topics.

```markdown
**Timeline**
- YYYY-MM-DD: Event with citation.
- YYYY-MM-DD: Event with citation.

**Current State**
What is true now.

**What Changed**
What superseded earlier facts.
```

## Evidence Pack

Use when the user wants auditability more than prose.

```markdown
| ID | Source | Type | Date | Key Evidence | Supports | Limits |
|---|---|---|---|---|---|---|
```

## Tone Rules

- Be direct.
- Separate fact from inference.
- Use "I found" for evidence and "I infer" for analysis.
- Avoid pretending certainty when sources are thin.
- Prefer links embedded in human-readable text over raw URLs.
