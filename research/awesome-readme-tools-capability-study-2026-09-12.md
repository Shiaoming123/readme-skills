# Awesome README Tools capability study

Checked on **2026-09-12** against the curated list and the first-party repositories or documentation of representative tools. The goal is not to vendor these projects. It is to identify reusable README-writing decisions for `readme-skills` and separate safe defaults from optional external integrations.

## Recommendation

Import the **patterns**, not the tools. `readme-skills` should make a compact, evidence-backed badge pass and native Markdown presentation pass part of its default behavior. It should not automatically add profile statistics, visitor counters, external cards, README-mutating Actions, OAuth integrations, or a new README generator dependency.

The current Skill already contains most of the right foundation: verified badges, repository-hosted assets, bounded HTML, diagrams only when useful, fallbacks for dynamic components, multilingual synchronization, and preservation of working links. The useful delta is a clearer provider priority and an explicit block against vanity/profile widgets in ordinary project READMEs.

## What the list actually represents

[`dhyeythumar/awesome-readme-tools`](https://github.com/dhyeythumar/awesome-readme-tools/tree/4d577fcf930a3a40e0cbd01a79efde2514e7c78e) contains **55 entries** at the reviewed commit:

| Section | Entries | Dominant purpose |
| --- | ---: | --- |
| Statistical tools / widgets | 19 | Personal activity, social/profile metrics, and generated SVG cards |
| README generators | 10 | Mostly profile builders, plus several project/multilingual generators |
| GitHub Actions for READMEs | 9 | Scheduled mutation of profile or project README regions |
| Badges | 7 | Status, technology, traffic, achievement, and visitor badges |
| Miscellaneous | 10 | Profile headers, trophies, quotes, music, jokes, and icons |

This distribution is useful as a capability inventory, but it is strongly skewed toward **GitHub profile READMEs**. The source Skill intentionally targets repository READMEs by default, so list frequency is not sufficient evidence that a component belongs in a project README.

Adoption is also concentrated in a few broad primitives. At review time, GitHub reported about 79.8k stars for [`github-readme-stats`](https://api.github.com/repos/anuraghazra/github-readme-stats), 27.2k for [`Shields`](https://api.github.com/repos/badges/shields), and 25.8k for [`Simple Icons`](https://api.github.com/repos/simple-icons/simple-icons). These numbers are only reach signals, not quality or default-use criteria.

## Capability assessment

| Capability family | Primary-source finding | Decision for `readme-skills` |
| --- | --- | --- |
| Workflow, version, package, license, and docs badges | GitHub provides a native workflow-status badge for an existing workflow; [GitHub documents its URL, default-branch behavior, and private-repository limitation](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge). [Shields](https://github.com/badges/shields/tree/bb85d1ef8d88f1552850be8e0c235ed8f9c86597) supports many registries and services, but remains an external image service. | **Default selection pass.** Add only badges backed by an authoritative target. Prefer native GitHub workflow badges for GitHub Actions; otherwise use a stable public provider or a static badge. Every badge must link to the evidence page and have meaningful alt text. |
| Language navigation badges | No service is required: linked Markdown images or static Shields badges are enough. | **Default when two or more localized READMEs already exist and badges fit the repository style.** Keep all locale destinations synchronized; do not create a locale merely to fill the row. |
| Logos, screenshots, diagrams, and responsive imagery | GitHub recommends [relative image paths for repository images and supports `<picture>`](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). GitHub also [renders Mermaid directly in Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams). | **Default presentation review, conditional insertion.** Prefer versioned repository assets, real product proof, and native Mermaid where the target renderer is known. Do not create a diagram or header merely as decoration. |
| Tables, section links, table of contents, and disclosure blocks | GitHub automatically exposes an [outline generated from headings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes). Raw HTML is later sanitized; GitHub's rendering pipeline removes dangerous elements and attributes such as scripts, inline styles, classes, and IDs ([`github/markup`](https://github.com/github/markup/tree/76e2682193828b98471b3a071edf4db0590ccacb)). | **Native default toolkit, used only when it improves navigation or comparison.** Do not duplicate GitHub's built-in outline with a manual TOC for a short README. Keep HTML bounded to GitHub-supported layout elements. |
| Brand/technology icons | [`Simple Icons`](https://github.com/simple-icons/simple-icons/blob/b054428646591252023b9599defb56f6e0b32f10/README.md) supports local SVGs and versioned CDN URLs. Its documentation warns that `@latest` can become a 404 if an icon is removed. Brand ownership and usage rules remain external to the icon's CC0 data. | **Optional visual polish.** Prefer local assets; if CDN delivery is justified, pin a major version and retain readable text. Never replace technology names with unexplained icons or assume an icon license grants trademark rights. |
| Generated GitHub statistics, streaks, trophies, and contribution charts | [`github-readme-stats`](https://github.com/anuraghazra/github-readme-stats/tree/54a7985aeefda00d5eadb55b80c17c7f976c37d2), [`github-readme-streak-stats`](https://github.com/DenverCoder1/github-readme-streak-stats/tree/9202e37665889fdb42d9a7df8501c1800acf761d), and [`github-profile-trophy`](https://github.com/ryo-ma/github-profile-trophy/tree/e3c89df995e92e67cdd4b2acaab9d974583dc1f7) all document self-hosting or static generation to avoid public endpoint reliability or rate-limit problems. Private statistics introduce PAT handling. | **Never default for a project README.** Offer only for a profile README or when the user explicitly requests a project-relevant metric. Prefer checked-in static output or self-hosting; require a text fallback and secret review. |
| Scheduled blog/activity/content regions | [`blog-post-workflow`](https://github.com/gautamkrishnar/blog-post-workflow/blob/28b22c9f8c9f4fa4b1c3e210bd5c3aaa00dff596/README.md) replaces marker-delimited README content and requires `contents: write`. GitHub documents that setting a `permissions` key makes unspecified token scopes `none` ([workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)). | **Optional automation, explicit request only.** Adding a workflow is a repository behavior and permission change, not a normal README optimization. Use minimum permissions, pinned action versions, bounded markers, and a manual/static fallback. |
| Coding telemetry | [`waka-readme`](https://github.com/athul/waka-readme/blob/370590ad8da8f54282ed92aa42b7c25ecbd5a9a6/README.md) requires editor telemetry, a WakaTime-compatible account/API key, repository write permission, and warns that activity data can expose private project/editor/OS information. | **Opt-in only.** Never infer consent from an existing technology section. State the telemetry source and public fields, keep secrets out of Markdown, and avoid private project names. |
| Visitor/hit counters | [`dwyl/hits`](https://github.com/dwyl/hits/tree/f0572ddf057b8616d9069e9311b327e25063d7d4) increments only when user agent or IP differs. [`visitor-badge`](https://github.com/jwenjian/visitor-badge/blob/4d60195152db2b041ab67957641acc64a2ae69b7/README.md) warns that its free deployment can go down under load and records a prior CountAPI outage. | **Never default.** They are not evidence of project quality, add a tracking/reliability dependency, and have no effect on the reader's primary task. Add only after explicit user request and privacy/provider review. |
| Music/social cards | [`spotify-github-profile`](https://github.com/kittinan/spotify-github-profile/blob/0f605fac8dbaac17000b40c6bb8df7c3b89839db/README.md) uses Spotify authorization and says its hosted service stores access tokens, refresh tokens, and expiry timestamps in Firebase. | **Profile-only, explicit opt-in.** Do not add to normal project READMEs. Account authorization and token storage require a separate privacy/security decision. |
| Website-performance cards | [`readme-pagespeed-insights`](https://github.com/ankurparihar/readme-pagespeed-insights/blob/812280424c25399f8d7b46744bfaf9f99dd08b97/README.md) tells users to download the generated SVG rather than embed the live audit endpoint because rendering can time out; its reviewed source commit dates to 2022. | **Optional static evidence.** Prefer a checked-in dated result linked to the current report or CI artifact. Never present an old score as live. |
| Multi-language generators, imports, TOCs, and drift checks | [`NRG`](https://github.com/nanolaba/readme-generator/tree/55feee5ed0ddbf1738a172cefbb4c9d645b028d2) generates multiple locales from one template and supports imports, TOCs, badges, file trees, and a CI drift check. It also adds a Java/tooling lifecycle. | **Adopt the invariant, not the dependency.** Keep every existing locale semantically synchronized by default. Recommend a single-source generator or drift check only when the repository already has documentation generation or the user requests automation. |

## Default behavior to encode

The smallest useful addition to the Skill is a provider-neutral decision rule:

1. Run the existing badge pass, but prioritize **verified project signals** in this order: existing native workflow status, released package/version, license, documentation, then other reader-relevant status. Omit a category when its source does not exist.
2. Prefer **native or repository-owned output**: relative links, checked-in images/SVGs, GitHub's workflow badge, supported Markdown, `<picture>`, `<details>`, tables, and Mermaid. Use an external provider only when it adds information that cannot be represented locally.
3. Keep the first badge row compact and functional. Badge text must remain understandable through alt text, and the surrounding README must still work when images fail.
4. Treat visitor counts, stars, followers, streaks, trophies, contribution graphs, quotes, jokes, music, social cards, and personal activity as **profile decoration**, not project defaults.
5. Before adding any dynamic component, check: current HTTPS endpoint, active upstream, authoritative data source, required credentials, data exposed, cache/freshness semantics, failure fallback, and whether a static snapshot is more honest.
6. Never add a README-mutating Action, hosted deployment, PAT/API key, OAuth connection, telemetry integration, or account authorization as part of an ordinary README rewrite. These need explicit user scope and their own verification.

## Suggested implementation boundary

No new library, generator, service allowlist, or workflow is needed. Two small rule additions are sufficient:

- In presentation governance, add a **default provider order** and a **project-signal versus profile-decoration** distinction.
- In validation, require external component checks for availability, target, fallback, privacy/secrets, and freshness; if any cannot be established, omit the component and mention it as an optional recommendation.

The existing rules for preservation, multilingual parity, link validation, static fallbacks, repository-hosted assets, and explicit authorization should remain unchanged.

## Maintenance signals

The list should not become a hardcoded catalog. Representative entries range from highly active to archived or stale:

- Active at review time: [Shields](https://api.github.com/repos/badges/shields), [Simple Icons](https://api.github.com/repos/simple-icons/simple-icons), [GitHub Readme Stats](https://api.github.com/repos/anuraghazra/github-readme-stats), [Blog Post Workflow](https://api.github.com/repos/gautamkrishnar/blog-post-workflow), and [NRG](https://api.github.com/repos/nanolaba/readme-generator).
- [`profile-readme-stats`](https://api.github.com/repos/teoxoy/profile-readme-stats) is archived.
- [`get-readme`](https://api.github.com/repos/luctst/get-readme) last pushed in 2020, [`readme-pagespeed-insights`](https://api.github.com/repos/ankurparihar/readme-pagespeed-insights) in 2022, and `visitor-badge` documents endpoint instability.

Therefore, `readme-skills` should evaluate a provider at use time instead of promising support for every entry in the awesome list.

## Fixed source index

- Curated list: [`dhyeythumar/awesome-readme-tools@4d577fc`](https://github.com/dhyeythumar/awesome-readme-tools/tree/4d577fcf930a3a40e0cbd01a79efde2514e7c78e)
- GitHub README behavior: [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [formatting and relative images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
- GitHub Actions: [workflow status badges](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge), [workflow permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- Rendering pipeline: [`github/markup@76e2682`](https://github.com/github/markup/tree/76e2682193828b98471b3a071edf4db0590ccacb)
- Broad primitives: [`badges/shields@bb85d1e`](https://github.com/badges/shields/tree/bb85d1ef8d88f1552850be8e0c235ed8f9c86597), [`simple-icons/simple-icons@b054428`](https://github.com/simple-icons/simple-icons/tree/b054428646591252023b9599defb56f6e0b32f10)
- Dynamic cards: [`github-readme-stats@54a7985`](https://github.com/anuraghazra/github-readme-stats/tree/54a7985aeefda00d5eadb55b80c17c7f976c37d2), [`github-readme-streak-stats@9202e37`](https://github.com/DenverCoder1/github-readme-streak-stats/tree/9202e37665889fdb42d9a7df8501c1800acf761d), [`github-profile-trophy@e3c89df`](https://github.com/ryo-ma/github-profile-trophy/tree/e3c89df995e92e67cdd4b2acaab9d974583dc1f7)
- Automation and telemetry: [`blog-post-workflow@28b22c9`](https://github.com/gautamkrishnar/blog-post-workflow/tree/28b22c9f8c9f4fa4b1c3e210bd5c3aaa00dff596), [`waka-readme@370590a`](https://github.com/athul/waka-readme/tree/370590ad8da8f54282ed92aa42b7c25ecbd5a9a6)
- Generators: [`nanolaba/readme-generator@55feee5`](https://github.com/nanolaba/readme-generator/tree/55feee5ed0ddbf1738a172cefbb4c9d645b028d2)
- Tracking and external identity: [`dwyl/hits@f0572dd`](https://github.com/dwyl/hits/tree/f0572ddf057b8616d9069e9311b327e25063d7d4), [`visitor-badge@4d60195`](https://github.com/jwenjian/visitor-badge/tree/4d60195152db2b041ab67957641acc64a2ae69b7), [`spotify-github-profile@0f605fa`](https://github.com/kittinan/spotify-github-profile/tree/0f605fac8dbaac17000b40c6bb8df7c3b89839db)
