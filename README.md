<div align="center">

# README Skills

**An evidence-first Codex Skill that matches the repository before it writes the README.**

[![English README](https://img.shields.io/badge/README-English-0969da.svg)](README.md) [![简体中文 README](https://img.shields.io/badge/README-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-8250df.svg)](README.zh-CN.md)

[Research](research/top-100-readme-study-2026-09-11.md) · [Skill entrypoint](SKILL.md)

[![Version v0.2.0](https://img.shields.io/badge/version-v0.2.0-0969da.svg)](VERSION) [![MIT License](https://img.shields.io/badge/license-MIT-2da44e.svg)](LICENSE)

</div>

README Skills inspects the actual project, identifies the reader's most useful first action, and then creates or improves the repository front page. It adapts the structure to the artifact and lifecycle instead of filling a universal template.

> **Release:** `v0.2.0`. The Skill is distributed under the MIT License and validated as a complete repository package.

![README Skills turns repository evidence into a matched README through inspection, classification, writing, and validation.](assets/workflow.svg)

## Why this Skill exists

A polished README can still be wrong. Install commands drift, roadmap items become "supported" features, template projects inherit sample branding, and visual decoration can hide the path to first success.

README Skills makes three decisions before writing:

1. **Mode:** audit, generate, optimize, restructure, or release-sync.
2. **Repository profile:** what the artifact is, what visitors came to do, and where it is in its lifecycle.
3. **Evidence boundary:** which claims are verified, inferred, missing, or conflicting.

It asks at most one bundled question, and only when the answer would materially change project identity, audience, legal meaning, or an external action.

## Quick start

Place this repository at `~/.codex/skills/readme-skills` (or the equivalent `skills/readme-skills` directory under `CODEX_HOME`), then begin a new Codex task so the Skill catalog refreshes.

Invoke it explicitly:

```text
$readme-skills Inspect this repository and create the most appropriate professional README. Minimize questions.
```

Or ask naturally:

```text
Optimize the existing README without replacing valid branding or inventing unsupported features.
```

The Skill allows implicit invocation, so repository README work can match it automatically.

## Operating modes

| Mode | Selected when | Default behavior |
| --- | --- | --- |
| `audit-only` | The request is review or analysis only | Report evidence-backed findings without editing |
| `generate` | No usable root README exists | Inspect the repository, then create the smallest complete README |
| `optimize` | The README is accurate but weak in clarity, navigation, or presentation | Preserve valid content and destinations, then make focused improvements |
| `restructure` | The README is stale, contradictory, or organized around implementation | Preserve valid material and rebuild the reader journey |
| `release-sync` | A release changes version, support, migration, screenshots, or availability | Update only the release-affected claims and links |

## Repository matching

README Skills chooses a primary profile and adds only relevant overlays.

| Profile family | What changes in the README |
| --- | --- |
| Application / frontend | Outcome, real product proof, local run path, delivery targets, privacy and accessibility boundaries |
| Library / SDK / API | Installation, minimal integration, compatibility, stability, and canonical API docs |
| CLI / scaffold / automation | First successful command, expected output, generated structure, configuration, and side effects |
| Service / self-hosted / infrastructure | Architecture, requirements, deployment, operations, upgrade, backup, and security boundaries |
| Fork / mirror / downstream | Upstream identity, reason for divergence, current delta, compatibility, sync, and support route |
| Research / model / dataset | Contribution, reproduction, provenance, evaluation, limitations, citation, and usage rights |
| Skill / resource / design collection | Scope, taxonomy, curation rules, installation or formats, trust, attribution, and maintenance |
| Monorepo / documentation / hardware / archived | Package map, reading path, physical constraints, or visible lifecycle and migration status |

Technology affects commands and prerequisites, but it does not become the document's identity. The Skill derives stack details from manifests, lockfiles, source, tests, and CI.

## Evidence before prose

The Skill checks sources in roughly this order:

1. verified behavior;
2. executable source and public entrypoints;
3. manifests, lockfiles, and release configuration;
4. tests, examples, CI, and deployment files;
5. maintained canonical documentation;
6. existing README and promotional prose.

Material claims are tracked as `verified`, `inferred`, `missing`, or `conflicting`. A project is never described as secure, production-ready, cross-platform, published, or officially maintained without corresponding evidence.

If README claims disagree with code, manifests, tests, CI, or release artifacts, the Skill uses the narrowest supported wording and finishes with a discrepancy report: the conflicting evidence, how the document handled it, and the smallest recommended project-side resolution.

All existing localized READMEs are treated as one documentation set. A material edit updates every discovered locale by default—including unlinked localized files—unless the user explicitly narrows the language scope. Synchronization preserves meaning, commands, versions, links, support, security, and legal boundaries without forcing literal translations.

## Presentation without decoration debt

The default is portable GitHub Flavored Markdown with repository-hosted assets. The Skill can use bounded HTML, theme-aware `<picture>` sources, tables, `<details>`, SVG diagrams, demos, badges, and dynamic trend components when they improve a reader decision.

Dynamic providers remain optional and require a stable text or static fallback. Badges provide compact status or high-value navigation, not the introduction. Diagrams include a readable overview and an equivalent text explanation.

A badge pass runs by default for generated, optimized, restructured, and release-synchronized READMEs. It adds only status whose version, workflow, package, license, or documentation target can be verified; missing evidence never becomes a decorative “passing” badge. Existing localized README files are also candidates for linked language-navigation badges, as demonstrated above.

## Before-and-after showcase

The showcase uses fixed public README snapshots whose documentation is materially incomplete for its repository type. It evaluates the README snapshot—not the quality of the project—and preserves a source URL, commit SHA, license evidence, and factual audit for every case.

Every case is an `optimize` example, not a replacement exercise. Its versioned `before.md` preserves the fixed source README, while `after.md` retains valid source content and destinations, reorganizes them, and adds evidence-backed context. Both panels are rendered through GitHub's Markdown API and capture only the README body—never repository navigation, file trees, or sidebars. Width stays consistent at 1440 pixels; height follows the document up to the documented capture limit, avoiding artificial blank space.

<!-- showcase:start -->

<table>
<tr>
<td width="100%" valign="top">
<h3>Application / frontend</h3>
<a href="examples/application-frontend/after.md"><img src="assets/showcase/application-frontend-comparison.png" alt="Before and after README comparison for the archived amfoss club website"></a>
<p><a href="https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/README.md">Fixed source</a> · <a href="examples/application-frontend/after.md">Optimized README</a></p>
<p>Preserves the original setup and Surge notes, while separating stale cross-repository badges and conflicting runtime evidence.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Library / SDK</h3>
<a href="examples/library-sdk/after.md"><img src="assets/showcase/library-sdk-comparison.png" alt="Before and after README comparison for the archived pylsh Python library"></a>
<p><a href="https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/README.md">Fixed source</a> · <a href="examples/library-sdk/after.md">Optimized README</a></p>
<p>Preserves installation, dependency, notebook, and attribution content, then adds a source-backed API example and version-conflict boundary.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>CLI / automation</h3>
<a href="examples/cli-scaffold/after.md"><img src="assets/showcase/cli-scaffold-comparison.png" alt="Before and after README comparison for the archived gmusicapi scripts CLI"></a>
<p><a href="https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/README.md">Fixed source</a> · <a href="examples/cli-scaffold/after.md">Optimized README</a></p>
<p>Routes readers to the successor, recovers five real entry points, and makes credential and network boundaries visible.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Fork / downstream</h3>
<a href="examples/fork-downstream/after.md"><img src="assets/showcase/fork-downstream-comparison.png" alt="Before and after README comparison for the archived bitcoin libbase58 fork"></a>
<p><a href="https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/README.md">Fixed source</a> · <a href="examples/fork-downstream/after.md">Optimized README</a></p>
<p>Preserves the complete C API guidance, then adds the missing upstream relationship, build path, version, and support boundary.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Research / reproducibility</h3>
<a href="examples/research-reproducibility/after.md"><img src="assets/showcase/research-reproducibility-comparison.png" alt="Before and after README comparison for IBM adaptive federated learning research code"></a>
<p><a href="https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md">Fixed source</a> · <a href="examples/research-reproducibility/after.md">Optimized README</a></p>
<p>Preserves the paper, citation, datasets, experiment flow, outputs, and contributor credit while making the reproduction boundary explicit.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Dataset / scientific artifact</h3>
<a href="examples/dataset-artifact/after.md"><img src="assets/showcase/dataset-artifact-comparison.png" alt="Before and after README comparison for the HICO-DET scientific dataset repository"></a>
<p><a href="https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md">Fixed source</a> · <a href="examples/dataset-artifact/after.md">Optimized README</a></p>
<p>Retains all nine utility links, installation steps, three citations, dataset-class route, and license while adding schema and rights context.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Skills / resource collection</h3>
<a href="examples/resource-collection/after.md"><img src="assets/showcase/resource-collection-comparison.png" alt="Before and after README comparison for the archived Awesome WebVR resource collection"></a>
<p><a href="https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md">Fixed source</a> · <a href="examples/resource-collection/after.md">Optimized README</a></p>
<p>Keeps all ten resource destinations clickable and reorganizes them into a counted taxonomy with maintenance and licensing guidance.</p>
</td>
</tr>
<tr>
<td width="100%" valign="top">
<h3>Design resources</h3>
<a href="examples/design-resource/after.md"><img src="assets/showcase/design-resource-comparison.png" alt="Before and after README comparison for an archived frontend design resource collection"></a>
<p><a href="https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/README.md">Fixed source</a> · <a href="examples/design-resource/after.md">Optimized README</a></p>
<p>Preserves the banner, contribution route, original taxonomy, and all three resources while visualizing which categories are actually populated.</p>
</td>
</tr>
</table>

The full [case index](examples/README.md) records the review method. [Candidate research](research/candidate-cases.md) preserves the primary and backup sets, selection rationale, fixed SHAs, source files, and license evidence. These are documentation demonstrations; no optimization was submitted upstream.

<!-- showcase:end -->

### Reproduce the gallery

The renderer uses Python's standard library and a local Microsoft Edge installation. Capturing the source page and rendering `after.md` through GitHub need network access; composing the comparison from existing screenshots and running repository checks are local.

```powershell
python scripts/render_showcase.py --capture
python scripts/render_showcase.py --render
python scripts/check_repo.py
```

## Research basis

The design is grounded in two local studies. The first collected and analyzed 100 README documents from GitHub's most-starred public repositories at a fixed snapshot:

- [Top 100 README study and capability blueprint](research/top-100-readme-study-2026-09-11.md): a fixed three-minute GitHub snapshot, source-level feature extraction across all 100 READMEs, 25 manual visual reviews, and 10 type-balancing supplements.
- [README Skill ecosystem study](research/skill-ecosystem-study-2026-09-11.md): existing README-focused Skills, official adjacent capabilities, evidence gaps, and provenance boundaries.

The Top 100 sample found images in 92 repositories, raw HTML in 75, badges in 67, multilingual entry signals in 43, and dynamic components in 22. These are prevalence signals, not quality scores; the Skill selects presentation based on reader value and failure behavior.

## Package structure

```text
readme-skills/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── workflow-and-structure.md
│   ├── repository-profiles.md
│   ├── evidence-and-validation.md
│   └── presentation-and-governance.md
├── examples/
├── research/
├── assets/
├── scripts/
├── PROVENANCE.md
├── VERSION
└── LICENSE
```

`SKILL.md` contains routing and safety boundaries. Supporting rules load only when the selected mode and repository profile need them.

## Boundaries

README Skills does not automatically:

- invent project behavior, commands, compatibility, metrics, maintainers, or releases;
- select or create a license;
- install dependencies or execute unsafe, costly, production, or secret-dependent commands;
- modify GitHub metadata, create remote resources, commit, push, or publish;
- replace full documentation sites, API references, or personal profile READMEs.

## License

The original README Skills package is available under the [MIT License](LICENSE). Third-party repository names, screenshots, source material, and documentation excerpts remain attributed to their owners and subject to their respective licenses; see [Provenance](PROVENANCE.md).
