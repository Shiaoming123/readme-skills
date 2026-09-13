# Audit — PulseParse

## Important — installation and runtime claims drifted

| Field | Finding |
| --- | --- |
| README evidence | `README.md` installs `pulseparse@1.0.0` and states Node.js 16 or later. |
| Repository evidence | `package.json` and `CHANGELOG.md` identify version `2.0.0` and Node.js `>=18`. |
| README treatment | Do not edit in `audit-only` mode; report the claims as stale. |
| Recommended project-side resolution | Confirm the public package release, then update the installation example and Node.js prerequisite together. |

The unsupported “production-ready” statement has no release, support, security, or runtime evidence in this fixture and should be narrowed or removed in a later edit.

No repository files were changed.
