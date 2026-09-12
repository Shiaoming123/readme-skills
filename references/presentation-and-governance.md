# Presentation and governance

Apply these rules only when they help the reader decide, understand, or act.

## GitHub rendering baseline

Prefer portable GitHub Flavored Markdown. Use supported HTML narrowly for layout that Markdown cannot express well, such as centered identity blocks, bounded image sizing, `<picture>` sources, `<details>` disclosure, or compact tables.

Do not depend on custom CSS, JavaScript, script tags, iframes, forms, or arbitrary canvas behavior. Assume sanitization, mobile width, light and dark themes, and image failure.

## Badges

Badges can expose compact status metadata or high-value navigation, but they are not the introduction.

- Perform a badge pass by default for generate, optimize, restructure, and release-sync tasks. When authoritative evidence and stable targets exist, place a compact badge row near the identity block; an evidence gap means omitting that badge, not omitting the badge pass.
- Keep only decision-relevant signals such as CI, package version, license, coverage, documentation, release, maintained compatibility, or an existing localized README destination.
- Link each badge to its authoritative target.
- Keep ordering stable and avoid duplicate vanity metrics.
- Verify branch names, workflow names, package identifiers, and endpoints.
- Never manufacture a passing, current, supported, secure, or released state merely to fill the row. Preserve nearby text so the document remains understandable when badges fail.
- Treat third-party badge services as external dependencies; the README must remain understandable when they fail.
- Treat language badges as navigation rather than project-status evidence. When two or more localized README files already exist and badges fit the repository style, default to a compact linked language row near the identity block. Use explicit language names, link every badge to the corresponding file, and keep the destination understandable through alt text when the image service fails.

## Images and demos

- Prefer repository-hosted, versioned assets for identity, screenshots, and architecture.
- Use descriptive alt text that communicates the purpose, not "image" or the filename.
- Bound very large media dimensions and check mobile readability.
- Use `<picture>` with light/dark sources when contrast requires it, with a normal fallback `<img>`.
- Prefer short, compressed, captioned demos. Provide an adjacent text explanation for motion or complex visuals.
- Do not add screenshots containing secrets, private data, personal paths, or unlicensed third-party content.
- For before/after README evidence, use equivalent content boundaries. Capture the rendered README body rather than repository navigation, file trees, sidebars, or unrelated host chrome; size each capture to its actual content with a documented maximum instead of padding short documents to a fixed height.
- Present before/after captures side by side at readable native panel widths when the purpose is visual comparison. Let the shorter panel end naturally instead of padding it to match the taller document, and link the embedded preview to the full-size comparison asset.

## Architecture and diagrams

Add a diagram only when it explains a relationship that prose or a small table cannot.

Preferred delivery chain:

1. a small readable overview in the README;
2. a larger linked SVG or raster asset;
3. editable source when maintained by the project;
4. a nearby text description or legend.

Use Mermaid only when the target renderer is known to support the required syntax. Static SVG is more predictable for a repository front page. Keep labels readable, colors theme-safe, and semantics understandable without color alone.

## Dynamic components

Star history, contributor charts, live metrics, and generated cards are optional enhancements. Add them only when the metric answers a real reader question, the provider is stable and appropriate, and a text link or explanation survives provider failure. Do not let dynamic components dominate the first screen or become evidence for quality by themselves.

## Tables, details, and navigation

- Use tables for exact mappings, compatibility, package roles, or feature comparisons; avoid paragraph-heavy cells.
- Use `<details>` for secondary troubleshooting, long platform alternatives, or exhaustive examples, never for prerequisites, warnings, license, or the primary action.
- Add a table of contents only when the README is long enough that navigation materially improves use.
- Use stable descriptive headings and verify generated anchors after changing them.

## Multilingual README strategy

Choose one canonical source language from repository convention or user direction. Provide visible language navigation near the top.

- Inventory the full existing README language set from filenames, links, and repository conventions before editing, including localized files not linked from the canonical README.
- Use separate localized README files for full translations.
- Treat the discovered language set as one atomic documentation surface. By default, every material README change must update all existing localized files in the same task.
- Keep identity, status, features, installation, commands, versions, links, support, security, compatibility, release state, and legal meaning semantically synchronized. Natural wording and section length may differ by language.
- Do not create a new locale only because other translations exist. Add languages when the user requests them or the repository already establishes the target locale.
- Exclude an existing localized README only when the user explicitly narrows the language scope. Name each excluded file and the resulting parity risk in the handoff.
- Allow a shorter localized overview only when it is clearly labeled and links to the canonical document.
- Do not mix two full translations into one long root README unless the repository explicitly follows that convention.
- Preserve code, identifiers, CLI flags, configuration keys, and canonical link targets during translation.
- Validate every in-scope locale after editing. Report untranslated, stale, failed, or unverified sections; do not silently present partial parity as complete or call the task complete while a localized file remains stale.

## Community and governance

The README should route to canonical governance files rather than duplicate them:

- `CONTRIBUTING.md` for contribution setup and process;
- `SECURITY.md` for vulnerability reporting and supported versions;
- support templates or discussions for help;
- code of conduct and governance documents for community rules;
- `LICENSE`, `NOTICE`, and `CITATION.cff` for legal and scholarly attribution.

Create or change these files only when explicitly in scope. Missing legal or security policy is a gap to report, not permission to invent one.

## Repository-page metadata

Description, topics, social preview, homepage, release assets, and pinned links affect the README experience but are external repository metadata. Recommend them separately. Change them only with explicit authorization and verified repository ownership.

## Release synchronization

When a release changes the README, check all affected surfaces: install commands, version pins, compatibility tables, screenshots, migration notes, status badges, changelog links, download links, and localized copies. Keep roadmap language separate from shipped behavior.
