# Workflow and structure

Use this reference to select an operating mode and assemble the README without forcing every repository into one template.

## Low-question policy

Proceed from repository evidence. Ask one bundled question only when at least one of these gates is hit:

- two plausible project identities lead to materially different introductions or quick starts;
- the intended audience or primary language cannot be inferred and the choice changes most of the document;
- a requested link, badge, translation, or external component requires an unavailable canonical target;
- the user asks for a license or legal claim that the repository does not already establish;
- an external or destructive action is necessary to complete the requested outcome.

Do not ask about style, section order, badge count, diagram format, or tone when repository conventions support a reasonable default. Choose, implement, and mention the choice afterward.

## Mode contracts

### Audit-only

Inspect without editing. Assess:

- factual accuracy and claim provenance;
- first-screen comprehension and primary call to action;
- successful-path completeness;
- information architecture and duplication;
- maintenance, trust, accessibility, and rendering risks.

Rank findings as blocking, important, or polish. Do not score aesthetics as if they were correctness.

### Optimize

Keep the valid information, project voice, and working destinations. Start with a preservation inventory of headings, links, resource entries, examples, commands, assets, badges, citations, and attribution. Repair the highest-impact gaps with the smallest coherent diff: sharpen the opening, promote the quick start, reorganize dense material, normalize headings, improve examples, and fix presentation defects.

Optimization is not replacement. Every valid source item must remain present or directly reachable in the optimized README. Do not collapse a resource list, API guide, citation block, tutorial, or setup flow into a count, abstract, or source link. Remove or replace an item only when evidence shows it is stale, broken, unsafe, duplicated, misleading, or out of scope, and record that decision.

### Restructure

Use when local edits cannot repair the reader journey. Before rewriting, make a preservation map:

| Action | Meaning |
| --- | --- |
| Preserve | Accurate identity, attribution, links, assets, or project-specific voice |
| Move | Useful content in the wrong stage of the journey |
| Replace | Duplicated, stale, vague, or implementation-first explanation |
| Add | Evidence-supported information required for the primary action |
| Remove | Unsupported, misleading, redundant, or dead content |

Retain recoverable project history in Git; do not overwrite unrelated local changes.

### Generate

Treat repository evidence as the source of truth. Draft a complete but compact README using the primary profile. When material facts are unavailable, omit the section or mark a narrow, honest limitation; never fill gaps with plausible-sounding claims.

### Release-sync

Update only statements affected by the release: version, installation, compatibility, migration, feature availability, screenshots, status, or links. Cross-check the version source, changelog or release notes, and shipped artifacts. Do not silently turn a release sync into a full redesign.

## Professional structure composer

Select sections by user decision, not convention alone.

| Reader need | Preferred README element | Include when |
| --- | --- | --- |
| Identify | Project name plus one-sentence value | Always |
| Qualify | Audience, use case, maturity, limitation | It affects adoption or expectations |
| Trust | Proof image, demo, benchmark, adoption signal | Verifiable and decision-relevant |
| Act | Requirements plus quick start | A safe runnable or usable path exists |
| Learn | Features, concepts, examples, architecture | Needed to understand successful use |
| Operate | Configuration, testing, deployment, troubleshooting | Repository users perform these tasks |
| Evaluate | Alternatives, tradeoffs, compatibility | Comparison affects choice |
| Collaborate | Support, contributing, security | Public or team collaboration exists |
| Attribute | License, citation, acknowledgements | Canonical files or statements exist |

## Opening patterns

Choose the shortest pattern that answers the project type:

- **Product/app**: value + audience + proof + try/run path.
- **Library/SDK**: problem solved + ecosystem + install + minimal example.
- **Tool/CLI**: job performed + installation + one successful command.
- **Research**: question or contribution + result boundary + reproduce/cite path.
- **Collection**: scope + curation rule + browse taxonomy + contribute path.
- **Fork/downstream**: upstream relationship + reason for divergence + current delta + install/sync path.

Avoid generic openings such as "a powerful solution". Name the artifact, the concrete outcome, and the intended user.

## Writing rules

- Match the repository's dominant human language unless the user requests another.
- Use consistent terminology from source, UI, API, and configuration.
- Prefer one copyable happy path; move alternatives after it.
- Keep examples realistic but free of secrets, personal paths, and production credentials.
- Explain what success looks like after a command when it is not obvious.
- Use tables for exact mappings and comparisons, diagrams for relationships, and prose for simple sequences.
- For lists and collections, improve retrieval with a taxonomy, compact index, grouped tables, annotations, and status labels while preserving the underlying entries and destinations.
- Keep the root README navigational. Move exhaustive API, operations, governance, and tutorials to canonical docs when they already exist.
