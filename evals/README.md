# Decision-contract fixtures

These fixtures cover the README modes not represented by the eight preservation-first showcase cases:

| Fixture | Mode | Evidence being exercised | Expected deliverable |
| --- | --- | --- | --- |
| `audit-drift` | `audit-only` | README/package/changelog contradiction | discrepancy report; source files unchanged |
| `generate-cli` | `generate` | manifest, executable entrypoint, sample and license | new evidence-backed README |
| `restructure-bilingual` | `restructure` | stale bilingual README versus current manifest and migration doc | synchronized English and Simplified Chinese READMEs |
| `release-sync` | `release-sync` | version file, changelog and CLI behavior | synchronized release-only README updates |

`request.md` supplies the realistic task boundary, `input/` is the repository evidence provided to an Agent, and `expected/` is a compact decision contract. The contract is not a word-for-word target or a claim of autonomous benchmark coverage: it records the permitted repository changes and facts that every acceptable output must preserve, state, or avoid.

Run the package check:

```powershell
python scripts/check_repo.py
```

For a client evaluation, copy one `input/` directory to a disposable workspace, use its `request.md`, and compare the output diff with the allowed changes and contract in `cases.json`. Record the client version, date, command/prompt, output diff, and validation status in `COMPATIBILITY.md` only after a real run. Do not promote a packaging check to runtime compatibility evidence.

For non-audit fixtures, the same checker can validate an Agent-produced workspace without requiring identical prose:

```powershell
python scripts/check_repo.py --evaluate generate-cli --workspace D:/temp/clipulse-eval
```
