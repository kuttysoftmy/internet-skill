# Source Map

Pick sources by the claim type, not by convenience. Use low-quality sources for leads, not proof.

## Source Tiers

Tier 1:

- Official docs, specs, standards, filings, court records, regulator databases, company status pages, release notes, source repos, audited statements, peer-reviewed papers, systematic reviews, government datasets, package registry metadata, security advisories.

Tier 2:

- Reputable reporting, expert analysis, maintainer blogs, institutional pages, conference talks, analyst notes, books, recognized professional bodies, independent benchmarks with methodology.

Tier 3:

- Community forums, Reddit, Hacker News, GitHub issues, Stack Overflow, Discord or Slack exports provided by the user, app reviews, customer reviews, social media, comments, YouTube transcripts.

Tier 4:

- SEO pages, affiliate lists, scraped summaries, AI-generated pages, unverified reposts, anonymous claims, thin content farms, listicles without methodology.

Use Tier 4 only for query discovery unless the research question is specifically about those pages.

## Claim Type To Source Type

Current fact:

- Official page, status page, press release, regulator page, news wire, recent reputable reporting.

Technical behavior:

- Official docs, source code, changelog, release notes, issues, PRs, tests, package registry, standards.

Product recommendation:

- Official docs/pricing, changelog, user reviews, forums, GitHub issues, benchmark reports, support pages, competitor pages.

Company or market:

- Company site, filings, funding announcements, credible reporting, job posts, customer pages, reviews, analyst notes, pricing pages.

Person:

- Official bio, profile pages, GitHub, publications, interviews, talks, filings, public social accounts. Resolve aliases and impersonation risk.

News or incident:

- Original reporting, official statements, status pages, police/regulator/court records, timestamps, corrections, local reporting.

Academic or medical:

- Peer-reviewed papers, systematic reviews, clinical guidelines, regulators, major institutions. Check sample size, conflicts, and applicability.

Legal or regulatory:

- Statutes, regulations, agency guidance, court records, docket entries, official notices. Always capture jurisdiction.

Financial:

- Filings, audited statements, official pricing, exchange/regulator data, current market data. Capture currency, units, and date.

Security:

- CVE/NVD, vendor advisory, patch notes, exploit status from reputable sources, maintainer issue, incident report.

## Query Patterns

Entity resolution:

- `"exact name" official`
- `"exact name" aliases`
- `"exact name" site:github.com`
- `"exact name" twitter OR x.com OR linkedin`
- `"exact name" company OR founder OR repo OR product`

Primary source:

- `"exact name" "release notes"`
- `"exact name" changelog`
- `"exact name" pricing`
- `"exact name" documentation`
- `"exact name" site:sec.gov`
- `"exact name" filetype:pdf`

Technical:

- `site:docs.vendor.com "feature name"`
- `site:github.com/org/repo "issue keyword"`
- `"package-name" changelog version`
- `"error message exact fragment"`
- `"RFC" "protocol feature"`
- `"CVE-ID" vendor advisory`

Market:

- `"company" competitors`
- `"product category" pricing`
- `"company" customers`
- `"company" funding OR acquisition OR layoffs`
- `"product category" "G2" OR "Capterra" OR Reddit OR "Hacker News"`

Recent:

- `"topic" after:YYYY-MM-DD`
- `"topic" "2026"`
- `"topic" "today" OR "yesterday" OR "this week"`
- `"topic" site:status.vendor.com`

Contradiction:

- `"topic" criticism`
- `"topic" debunked`
- `"topic" not working`
- `"topic" alternatives`
- `"topic" correction`
- `"topic" lawsuit`
- `"topic" outage`
- `"topic" security advisory`
- `"topic" pricing change`
- `"topic" reddit`

Documents:

- `"topic" filetype:pdf`
- `"topic" filetype:doc OR filetype:docx`
- `"topic" site:gov`
- `"topic" site:courtlistener.com`
- `"topic" site:sec.gov`

## Source-Specific Tactics

Official websites:

- Check docs, changelog, pricing, terms, press releases, status, security, trust, and support pages.
- Compare marketing claims against docs, limitations, support pages, and changelogs.

GitHub:

- Check releases, commits, issues, discussions, PRs, stars, forks, contributors, license, security advisories, open maintenance signals, and commit recency.
- For active bugs, prefer issues/PRs over old blog posts.

Package registries:

- Check latest version, publish date, download trend, maintainers, deprecation notices, dependencies, and package integrity signals.

Social and forums:

- Use for sentiment, lived experience, failure modes, workarounds, and the vocabulary users actually use.
- Do not use as sole proof for factual claims unless the claim is about sentiment.

News:

- Separate original reporting from rewritten syndication.
- Prefer reports that link to documents, quote named sources, provide primary records, or include corrections.

Academic:

- Prefer review papers, guidelines, meta-analyses, and recent primary research.
- Check publication date, study design, sample size, conflicts, and applicability.

Video and podcasts:

- Prefer transcripts when available.
- Cite the episode or video URL and include timestamp when exact wording matters.

Maps and local recommendations:

- Check official venue pages, recent reviews, opening hours, maps, local news, and date of review.
- Verify current availability before recommending travel or bookings.

## Disambiguation Checklist

Before deep research, resolve:

- Canonical name and aliases.
- Legal entity versus product name.
- Repo owner/name and package name.
- Handles across X, GitHub, YouTube, TikTok, LinkedIn, Bluesky, Reddit, and domain.
- Region, jurisdiction, language, and date window.
- Competitors or comparison set.
- Official source of truth for updates.
