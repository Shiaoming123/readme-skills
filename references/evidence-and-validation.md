# Evidence and validation

Use this reference to keep the README aligned with what the repository can actually support.

## Evidence priority

When sources disagree, prefer the source closest to runnable behavior:

1. verified build, test, package, or application behavior;
2. executable source, public entrypoints, schemas, and generated help;
3. manifests, lockfiles, workspace configuration, and release metadata;
4. tests, examples, CI workflows, deployment configuration, and fixtures;
5. maintained canonical docs and changelog entries;
6. the existing README, issue text, comments, plans, and promotional copy.

A lower-ranked source may still be canonical for ownership, citation, or policy. Surface conflicts instead of silently choosing convenient wording.

## Claim ledger

Track material claims internally:

| Status | Meaning | README treatment |
| --- | --- | --- |
| Verified | Directly supported by inspected evidence or a safe successful check | State plainly |
| Inferred | Strongly implied by multiple consistent artifacts | Qualify or disclose the inference |
| Missing | Needed for the reader journey but not established | Omit, mark unknown, or ask only if it hits a question gate |
| Conflicting | Credible sources disagree | Resolve, narrow the claim, or show the boundary |

Material claims include installation commands, platform support, compatibility, performance, security, offline behavior, pricing, maturity, releases, and project ownership.

## Conflict handling and handoff

When the README and stronger repository evidence disagree, keep a compact discrepancy register with:

| Field | Record |
| --- | --- |
| Claim | The disputed reader-facing statement |
| README evidence | File, section, or line containing the claim |
| Repository evidence | Code, manifest, test, CI, artifact, or runtime result that disagrees or leaves the claim ambiguous |
| README treatment | Corrected, narrowed, qualified, omitted, or blocked |
| Recommendation | The smallest project-side action that would remove the inconsistency |

Complete the safe documentation edit with the narrowest supported wording when possible. Ask only if the conflict changes project identity, legal meaning, the primary reader path, or an authorized external effect. Do not change product code, configuration, releases, or legal files merely to make the README claim true.

Include the discrepancy register and recommendations in the final handoff. Distinguish an actual contradiction from missing evidence, and identify any claim that remains blocked instead of presenting it as resolved.

## Maturity and delivery language

Keep these states distinct:

- **implemented**: code exists;
- **tested**: a relevant automated or manual check passed;
- **packaged**: a distributable artifact is produced;
- **published**: users can obtain the artifact from the stated channel;
- **verified on target**: the claimed platform or environment was exercised;
- **planned**: no current delivery claim.

Do not convert a web preview into native-platform proof, a build into deployment proof, or configuration presence into a working integration.

## Commands and prerequisites

- Derive the package manager and command from manifests, lockfiles, scripts, task runners, or CI.
- Respect monorepo working directories and workspace filters.
- Prefer the repository's established command over a technically possible alternative.
- Show required runtime and system dependencies only when a version or dependency is established.
- Never include real credentials. Use clearly named placeholders and link to the canonical configuration source.
- Verify the shortest safe path where practical. Avoid install, deploy, migration, account, billing, network, or production commands unless already authorized and safe.

## Trust and legal claims

- Link the license only when an actual license file or authoritative package metadata exists. Never choose a license for the project.
- Do not claim "secure", "production-ready", "official", "compliant", or "actively maintained" without current evidence.
- Use benchmarks only with method, environment, date or version, and reproducible source. Otherwise describe behavior without comparative numbers.
- Do not expose private logs, tokens, internal endpoints, personal paths, or user data in examples or screenshots.
- Attribute third-party assets, upstream projects, research, and copied material according to their source and license.

## Validation ladder

Stop after the smallest check that meaningfully catches the relevant regression:

1. repository-provided docs lint, link check, or Markdown test;
2. targeted command/help/example verification;
3. relative link and asset resolution;
4. localized README inventory and material parity for identity, status, commands, versions, compatibility, support, security, and legal meaning;
5. syntax checks for fenced examples, tables, HTML, and diagrams;
6. rendered inspection for layout, theme-aware media, accessibility, or host-specific behavior.

Always inspect the final diff. Confirm that no unrelated files, claims, or user changes were altered.

Report each important validation as passed, failed, blocked, or not run. HTTP success alone is not proof that a demo, image, download, or published page contains the expected project content.
