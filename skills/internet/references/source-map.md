# Source Map

Pick sources by the claim type, not by convenience.

## Source Tiers

Tier 1:

- Official docs, specs, standards, filings, court records, regulator databases, company status pages, source repos, release notes, audited statements, peer-reviewed papers, government datasets.

Tier 2:

- Reputable reporting, expert analysis, conference talks, maintainer blogs, institutional pages, analyst notes, books, recognized professional bodies.

Tier 3:

- Community forums, Reddit, Hacker News, GitHub issues, Stack Overflow, Discord exports provided by the user, app reviews, social media, comments, customer reviews.

Tier 4:

- SEO pages, affiliate lists, scraped summaries, AI-generated pages, unverified reposts, anonymous claims, thin content farms.

Use Tier 4 for leads only. Do not treat it as proof unless the topic is specifically about those pages.

## Query Patterns

Entity:

- `"exact name" official`
- `"exact name" site:github.com`
- `"exact name" "release notes"`
- `"exact name" "pricing"`
- `"exact name" review OR comparison`
- `"exact name" problem OR issue OR lawsuit OR outage OR controversy`

Technical:

- `site:docs.vendor.com feature name`
- `site:github.com/org/repo issue keyword`
- `"package-name" changelog version`
- `"error message" "exact fragment"`
- `"RFC" protocol feature`

Market:

- `"company" competitors`
- `"company" customers`
- `"product category" pricing`
- `"product category" "G2" OR "Capterra" OR "Reddit" OR "Hacker News"`
- `"company" funding OR revenue OR acquisition OR layoffs`

Recent:

- `"topic" after:YYYY-MM-DD`
- `"topic" "2026"`
- `"topic" site:status.vendor.com`
- `"topic" "today" OR "yesterday" OR "this week"`

Contradiction:

- `"topic" criticism`
- `"topic" debunked`
- `"topic" not working`
- `"topic" alternatives`
- `"topic" correction`
- `"topic" lawsuit`
- `"topic" security advisory`
- `"topic" reddit`

Documents:

- `"topic" filetype:pdf`
- `"topic" filetype:doc OR filetype:docx`
- `"topic" site:sec.gov`
- `"topic" site:courtlistener.com`
- `"topic" site:gov`

## Source-Specific Tactics

Official websites:

- Find docs, changelog, pricing, terms, press releases, status, and security pages.
- Compare marketing claims against docs and support pages.

GitHub:

- Check releases, commits, issues, discussions, pull requests, stars, forks, contributors, license, security advisories, and open maintenance signals.

Package registries:

- Check latest version, publish date, download trend, maintainers, dependencies, and deprecation notices.

Social and forums:

- Use for sentiment, lived experience, edge cases, complaints, workarounds, and language users actually use.
- Do not use as sole proof for factual claims unless the claim is about sentiment.

News:

- Separate original reporting from rewritten syndication.
- Prefer reports that link to documents, quote named sources, or provide primary records.

Academic:

- Prefer review papers, guidelines, meta-analyses, and recent primary research.
- Check publication date, sample size, conflicts, and whether findings apply to the user's context.

Video and podcasts:

- Prefer transcripts when available.
- Cite the episode or video URL and include timestamp when the exact wording matters.
