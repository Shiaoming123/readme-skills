# README Skills showcase candidate cases

Research snapshot: 2026-09-12. This shortlist uses only public GitHub repository, GitHub API, fixed-commit README, license, and project-file evidence. “Incomplete” below describes the README at the cited commit, not the quality of the project or its maintainers.

## Selection and capture rules

- Every primary and backup candidate is archived according to its [GitHub repository metadata](https://docs.github.com/en/rest/repos/repos#get-a-repository), and has a repository-level MIT license at the cited commit.
- Treat the archived lifecycle as part of the rewrite: the improved README must not imply current maintenance, support, packaging, or compatibility.
- Capture only the rendered README area, crop out account/navigation UI where practical, and caption it with repository, fixed commit, date, and source link. Do not reuse external logos or screenshots as standalone assets.
- Keep the “after” example in this repository. Do not open pull requests or modify the source repository.
- The primary cases give the clearest category contrast. Backups are retained in case a page becomes unavailable or a category needs a second layout.

## Recommended primary set

| Category | Primary snapshot | Why it gives a useful before/after |
| --- | --- | --- |
| Application / frontend | [`amfoss/club-website-2019`](https://github.com/amfoss/club-website-2019) | The README has runnable-looking instructions and badges, but they point at a differently named repository and omit the archived lifecycle. |
| Library / non-JS SDK | [`mattilyra/LSH`](https://github.com/mattilyra/LSH) | The source exposes package metadata and dependencies, while the README lacks a minimal API example, compatibility boundary, and lifecycle status. |
| CLI / scaffold | [`thebigmunch/gmusicapi-scripts`](https://github.com/thebigmunch/gmusicapi-scripts) | The README is only a deprecation sentence although the package declares five console commands and a successor. |
| Fork / downstream | [`bitcoin/libbase58`](https://github.com/bitcoin/libbase58) | GitHub records an upstream parent, but the README starts inside the C API and never explains the fork relationship or build path. |
| Research / reproducibility | [`IBM/adaptive-federated-learning`](https://github.com/IBM/adaptive-federated-learning) | The README identifies the paper and a manual run, but does not turn repository configuration and outputs into a reproducibility contract. |
| Dataset / scientific artifact | [`fredzzhang/hicodet`](https://github.com/fredzzhang/hicodet) | Good utility documentation can be reframed as an artifact card with provenance, intended-use, data-rights, environment, and limitations boundaries. |
| Awesome / resource collection | [`cmda-vr/awesome-webvr`](https://github.com/cmda-vr/awesome-webvr) | The list calls itself curated but provides no selection rules, contribution path, maintenance date, or link/license fields. |
| Design-resource collection | [`ibrahimraimi-archive/free-frontend-resources`](https://github.com/ibrahimraimi-archive/free-frontend-resources) | The README promises a broad taxonomy, but the cited snapshot contains only the first populated category and does not define design-resource metadata. |

## 1. Application / frontend

### Primary — amfoss/club-website-2019

- Repository and state: [`amfoss/club-website-2019`](https://github.com/amfoss/club-website-2019); GitHub reports `master` as the default branch and `archived: true` in the [repository API record](https://api.github.com/repos/amfoss/club-website-2019).
- Fixed current commit: [`674e138a209ac21d815147e77c4401a06c9e9930`](https://github.com/amfoss/club-website-2019/commit/674e138a209ac21d815147e77c4401a06c9e9930), committed 2023-04-02T09:53:42Z.
- License evidence: [`LICENSE` at the fixed commit](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/LICENSE) is MIT.
- README snapshot: [rendered](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/README.md) · [raw](https://raw.githubusercontent.com/amfoss/club-website-2019/674e138a209ac21d815147e77c4401a06c9e9930/README.md).
- Project evidence to inspect: [`package.json`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/package.json) defines the Next.js scripts and dependencies; [`Dockerfile`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/Dockerfile), [`.gitlab-ci.yml`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/.gitlab-ci.yml), and [`next.config.js`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/next.config.js) define the actual build/deployment context.
- README gaps: the [snapshot](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/README.md) omits the archived status, points badges and setup links at `amfoss/website` instead of this repository, tells readers to `cd website/`, and states a local URL without tying it to the [`next dev` script](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/package.json).
- Safe demonstrator: it is a fixed, archived, MIT-licensed snapshot with enough manifest and deployment evidence to replace misleading actions with a concise archival notice and evidence-backed historical setup.

### Backup — App-Lobby/Taskey

- Repository and state: [`App-Lobby/Taskey`](https://github.com/App-Lobby/Taskey); `main`, archived, per the [repository API record](https://api.github.com/repos/App-Lobby/Taskey).
- Fixed current commit: [`78019553fca57403fc675692e4f22d9ed4b50b59`](https://github.com/App-Lobby/Taskey/commit/78019553fca57403fc675692e4f22d9ed4b50b59), committed 2021-05-24T12:59:38Z.
- License: [MIT `LICENSE`](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/LICENSE). README: [rendered](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/README.md) · [raw](https://raw.githubusercontent.com/App-Lobby/Taskey/78019553fca57403fc675692e4f22d9ed4b50b59/README.md).
- Evidence: the [Xcode project](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/Taskey.xcodeproj/project.pbxproj), [Swift package lock](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/Taskey.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved), and [`ContentView.swift`](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/Taskey/View/ContentView.swift) support a precise historical build/feature description.
- Gaps and use: the [README](https://github.com/App-Lobby/Taskey/blob/78019553fca57403fc675692e4f22d9ed4b50b59/README.md) has a product image and stack summary but no archived status, platform/Xcode requirements, build/run path, tested target, data behavior, or image alt text. Its small, MIT-licensed snapshot is suited to an application-card rewrite without claiming App Store delivery.

## 2. Library / SDK in a non-JavaScript stack

### Primary — mattilyra/LSH

- Repository and state: [`mattilyra/LSH`](https://github.com/mattilyra/LSH); `master`, archived, per the [repository API record](https://api.github.com/repos/mattilyra/LSH).
- Fixed current commit: [`a57069bfb70f4b620d47931f81966b5a73c1b480`](https://github.com/mattilyra/LSH/commit/a57069bfb70f4b620d47931f81966b5a73c1b480), committed 2023-06-11T08:03:23Z.
- License: [MIT `LICENSE`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/LICENSE). README: [rendered](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/README.md) · [raw](https://raw.githubusercontent.com/mattilyra/LSH/a57069bfb70f4b620d47931f81966b5a73c1b480/README.md).
- Project evidence to inspect: [`setup.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/setup.py) declares package name `lsh`, version `0.3.0`, NumPy/Cython dependencies, and pytest test dependency; the [`lsh` package tree](https://github.com/mattilyra/LSH/tree/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh) and [example notebook](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/examples/Introduction.ipynb) expose actual API and usage material.
- README gaps: the [snapshot](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/README.md) gives a legacy `setup.py install` flow, but no archived status, compatibility range, smallest import/API example, expected result, test command, package/version identity, or clear boundary between required NumPy and source-regeneration Cython.
- Safe demonstrator: archived + MIT, with manifest, package source, and example evidence sufficient for an honest library README while clearly labelling unverified modern-Python compatibility.

### Backup — gregoryv/draw

- Repository and state: [`gregoryv/draw`](https://github.com/gregoryv/draw); `main`, archived, per the [repository API record](https://api.github.com/repos/gregoryv/draw).
- Fixed current commit: [`49cbf37031a1f36fac00dc2b06c8a5aea9b434cb`](https://github.com/gregoryv/draw/commit/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb), committed 2025-12-21T09:13:17Z.
- License: [MIT `LICENSE`](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/LICENSE). README: [rendered](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/README.md) · [raw](https://raw.githubusercontent.com/gregoryv/draw/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/README.md).
- Evidence: [`go.mod`](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/go.mod), [`package_test.go`](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/package_test.go), and [`overview.svg`](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/overview.svg) establish the module, examples/tests, and output.
- Gaps and use: the [README](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/README.md) says “No external dependencies,” while [`go.mod`](https://github.com/gregoryv/draw/blob/49cbf37031a1f36fac00dc2b06c8a5aea9b434cb/go.mod) lists direct modules; it also lacks an install/import example, supported Go boundary, and successor migration detail. That evidence conflict makes a strong claim-ledger example.

## 3. CLI or scaffold / template

### Primary — thebigmunch/gmusicapi-scripts

- Repository and state: [`thebigmunch/gmusicapi-scripts`](https://github.com/thebigmunch/gmusicapi-scripts); `master`, archived, per the [repository API record](https://api.github.com/repos/thebigmunch/gmusicapi-scripts).
- Fixed current commit: [`5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8`](https://github.com/thebigmunch/gmusicapi-scripts/commit/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8), committed 2018-10-20T00:36:26Z.
- License: [MIT `LICENSE`](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/LICENSE). README: [rendered](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/README.md) · [raw](https://raw.githubusercontent.com/thebigmunch/gmusicapi-scripts/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/README.md).
- Project evidence to inspect: [`setup.py`](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/setup.py) sets the Python floor and exposes `gmdelete`, `gmdownload`, `gmsearch`, `gmsync`, and `gmupload`; [`CHANGELOG.md`](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/CHANGELOG.md) and the [`gmusicapi_scripts` source](https://github.com/thebigmunch/gmusicapi-scripts/tree/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/gmusicapi_scripts) provide command evidence.
- README gaps: the [snapshot](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/README.md) is only a deprecation/successor sentence; it does not identify the five historical commands, requirements, credential/network implications, migration mapping, or what remains usable.
- Safe demonstrator: the one-line before image creates an obvious contrast, while archived state, MIT license, manifest, and successor link allow a careful historical CLI README without presenting deprecated tooling as current.

### Backup — jacobdeichert/svelvet

- Repository and state: [`jacobdeichert/svelvet`](https://github.com/jacobdeichert/svelvet); `master`, archived, per the [repository API record](https://api.github.com/repos/jacobdeichert/svelvet).
- Fixed current commit: [`2e60523d0f665c884cd3cebd616de419f350f530`](https://github.com/jacobdeichert/svelvet/commit/2e60523d0f665c884cd3cebd616de419f350f530), committed 2022-05-01T03:06:08Z.
- License: [MIT `LICENSE`](https://github.com/jacobdeichert/svelvet/blob/2e60523d0f665c884cd3cebd616de419f350f530/LICENSE). README: [rendered](https://github.com/jacobdeichert/svelvet/blob/2e60523d0f665c884cd3cebd616de419f350f530/README.md) · [raw](https://raw.githubusercontent.com/jacobdeichert/svelvet/2e60523d0f665c884cd3cebd616de419f350f530/README.md).
- Evidence: [`package.json`](https://github.com/jacobdeichert/svelvet/blob/2e60523d0f665c884cd3cebd616de419f350f530/package.json) declares a CLI bin, Node floor, Svelte peer dependency, and build/test scripts.
- Gaps and use: the [README](https://github.com/jacobdeichert/svelvet/blob/2e60523d0f665c884cd3cebd616de419f350f530/README.md) explains discontinuation but not invocation, expected output, requirements, or local verification. Because the package name is blank in [`package.json`](https://github.com/jacobdeichert/svelvet/blob/2e60523d0f665c884cd3cebd616de419f350f530/package.json), it is a useful example of narrowing claims instead of inventing an npm install command.

## 4. Fork / mirror / downstream

### Primary — bitcoin/libbase58

- Repository and state: [`bitcoin/libbase58`](https://github.com/bitcoin/libbase58); GitHub reports `master`, `archived: true`, `fork: true`, and parent [`luke-jr/libbase58`](https://github.com/luke-jr/libbase58) in the [repository API record](https://api.github.com/repos/bitcoin/libbase58).
- Fixed current commit: [`b1dd03fa8d1be4be076bb6152325c6b5cf64f678`](https://github.com/bitcoin/libbase58/commit/b1dd03fa8d1be4be076bb6152325c6b5cf64f678), committed 2020-10-02T15:49:46Z.
- License: [MIT `COPYING`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/COPYING). README: [rendered](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/README.md) · [raw](https://raw.githubusercontent.com/bitcoin/libbase58/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/README.md).
- Project evidence to inspect: [`configure.ac`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/configure.ac) identifies libbase58 `0.1.4` and the optional CLI tool; [`INSTALL`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/INSTALL), [`libbase58.h`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/libbase58.h), and [`clitool.c`](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/clitool.c) provide build and API evidence.
- README gaps: the [snapshot](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/README.md) starts with SHA-256 initialization and API calls, but provides no project title/purpose, archived status, upstream relationship, divergence/sync basis, build path, version, support channel, or license link.
- Safe demonstrator: GitHub itself supplies the parent relationship, and the fixed MIT snapshot contains enough build/API evidence to show the fork overlay without speculating about why the organization forked it.

### Backup — vuetifyjs/nuxt

- Repository and state: [`vuetifyjs/nuxt`](https://github.com/vuetifyjs/nuxt); GitHub reports `master`, archived, forked from [`nuxt-community/starter-template`](https://github.com/nuxt-community/starter-template) in the [repository API record](https://api.github.com/repos/vuetifyjs/nuxt).
- Fixed current commit: [`9e9f33268e3d8a3463ce62da6e22b906e254228c`](https://github.com/vuetifyjs/nuxt/commit/9e9f33268e3d8a3463ce62da6e22b906e254228c), committed 2018-11-08T21:39:07Z.
- License: [MIT `LICENSE`](https://github.com/vuetifyjs/nuxt/blob/9e9f33268e3d8a3463ce62da6e22b906e254228c/LICENSE). README: [rendered](https://github.com/vuetifyjs/nuxt/blob/9e9f33268e3d8a3463ce62da6e22b906e254228c/README.md) · [raw](https://raw.githubusercontent.com/vuetifyjs/nuxt/9e9f33268e3d8a3463ce62da6e22b906e254228c/README.md).
- Evidence: [`meta.js`](https://github.com/vuetifyjs/nuxt/blob/9e9f33268e3d8a3463ce62da6e22b906e254228c/meta.js) defines scaffold questions and completion commands.
- Gaps and use: the [README](https://github.com/vuetifyjs/nuxt/blob/9e9f33268e3d8a3463ce62da6e22b906e254228c/README.md) documents an old scaffold flow but omits archived status, upstream relationship, divergence, placeholder/customization map, and update/migration strategy. It is a compact example combining fork and template overlays.

## 5. Research / academic / reproducibility

### Primary — IBM/adaptive-federated-learning

- Repository and state: [`IBM/adaptive-federated-learning`](https://github.com/IBM/adaptive-federated-learning); `master`, archived, per the [repository API record](https://api.github.com/repos/IBM/adaptive-federated-learning).
- Fixed current commit: [`b6bc482bf2aac15c28b50125ecc6f3e0096c5149`](https://github.com/IBM/adaptive-federated-learning/commit/b6bc482bf2aac15c28b50125ecc6f3e0096c5149), committed 2023-04-12T15:42:14Z.
- License: [MIT `LICENSE`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/LICENSE). README: [rendered](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md) · [raw](https://raw.githubusercontent.com/IBM/adaptive-federated-learning/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md).
- Project evidence to inspect: [`requirements.txt`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/requirements.txt) constrains TensorFlow 1.x but leaves other versions open; [`config.py`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/config.py) defines client count, datasets, models, seeds, time model, and output paths; [`server.py`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/server.py) and [`client.py`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/client.py) define the actual orchestration.
- README gaps: the [snapshot](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md) cites the paper and gives manual steps, but omits archived status, license link, operating-system/hardware boundary, a reproducibility matrix connecting configurations to paper figures, exact expected artifact names/content, verification tolerances, and explicit limitations.
- Safe demonstrator: archived + MIT with a paper citation, configuration, dependencies, and executable entrypoints, so an improved README can distinguish “code exists” from “paper result reproduced” without rerunning legacy TensorFlow.

### Backup — bytedance/midi_melody_extraction

- Repository and state: [`bytedance/midi_melody_extraction`](https://github.com/bytedance/midi_melody_extraction); `master`, archived, per the [repository API record](https://api.github.com/repos/bytedance/midi_melody_extraction).
- Fixed current commit: [`106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72`](https://github.com/bytedance/midi_melody_extraction/commit/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72), committed 2023-09-27T14:50:35Z.
- License: [MIT `LICENCE`](https://github.com/bytedance/midi_melody_extraction/blob/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/LICENCE). README: [rendered](https://github.com/bytedance/midi_melody_extraction/blob/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/README.md) · [raw](https://raw.githubusercontent.com/bytedance/midi_melody_extraction/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/README.md).
- Evidence: [`run.sh`](https://github.com/bytedance/midi_melody_extraction/blob/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/run.sh) reveals the POP909 path placeholder and output stages; [`requirements.txt`](https://github.com/bytedance/midi_melody_extraction/blob/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/requirements.txt) supplies the legacy runtime constraints.
- Gaps and use: the [README](https://github.com/bytedance/midi_melody_extraction/blob/106f1d9a6e96f9e9d0ad9cbacb47f9ae17c60c72/README.md) lists filenames without arguments, prerequisites, artifact flow, expected outputs, evaluation method, hardware, limitations, license, or a copyable citation. It is a clean pipeline-diagram and reproducibility-contract example.

## 6. Model / dataset / scientific artifact

### Primary — fredzzhang/hicodet

- Repository and state: [`fredzzhang/hicodet`](https://github.com/fredzzhang/hicodet); `main`, archived, per the [repository API record](https://api.github.com/repos/fredzzhang/hicodet).
- Fixed current commit: [`e4e234045e0a4128995a2e45e841b3ebe64eda0b`](https://github.com/fredzzhang/hicodet/commit/e4e234045e0a4128995a2e45e841b3ebe64eda0b), committed 2023-12-14T05:27:11Z.
- License: [MIT `LICENSE`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/LICENSE). README: [rendered](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md) · [raw](https://raw.githubusercontent.com/fredzzhang/hicodet/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md).
- Project evidence to inspect: [`DOC.md`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/DOC.md) documents annotation fields and examples; [`hicodet.py`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/hicodet.py), [`download.sh`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/download.sh), and the fixed [annotation JSON files](https://github.com/fredzzhang/hicodet/tree/e4e234045e0a4128995a2e45e841b3ebe64eda0b) provide format and data-flow evidence.
- README gaps: the [snapshot](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md) documents utilities and code citation, but omits archived status, intended/non-intended uses, dataset provenance/version/checksums, environment/hardware boundaries, evaluation caveats, and a clear distinction between this repository’s MIT code license and the separately downloaded dataset’s usage terms.
- Safe demonstrator: it has real schema documentation and citations, so the rewrite can demonstrate a scientific-artifact card while explicitly leaving unknown dataset rights as unknown rather than treating public download as permission.

### Backup — fcakyon/midv500

- Repository and state: [`fcakyon/midv500`](https://github.com/fcakyon/midv500); `master`, archived, per the [repository API record](https://api.github.com/repos/fcakyon/midv500).
- Fixed current commit: [`2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c`](https://github.com/fcakyon/midv500/commit/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c), committed 2020-08-19T15:24:33Z.
- License: [MIT `LICENSE`](https://github.com/fcakyon/midv500/blob/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/LICENSE). README: [rendered](https://github.com/fcakyon/midv500/blob/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/README.md) · [raw](https://raw.githubusercontent.com/fcakyon/midv500/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/README.md).
- Evidence: [`setup.py`](https://github.com/fcakyon/midv500/blob/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/setup.py) supplies package identity and Python floor; [`requirements.txt`](https://github.com/fcakyon/midv500/blob/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/requirements.txt) and [`midv500` source](https://github.com/fcakyon/midv500/tree/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/midv500) support the documented download/conversion flow.
- Gaps and use: the [README](https://github.com/fcakyon/midv500/blob/2f1cd74e0bb8da2301a96e3fb0cd9f17005ed08c/README.md) has install/use examples and paper links but omits archived status, data-license/privacy boundary, download size/storage needs, checksums/version pinning, output-schema validation, limitations, and code-license link. It can show that “longer” is not the same as artifact-complete.

## 7. Skills / awesome / resource collection

### Primary — cmda-vr/awesome-webvr

- Repository and state: [`cmda-vr/awesome-webvr`](https://github.com/cmda-vr/awesome-webvr); `master`, archived, per the [repository API record](https://api.github.com/repos/cmda-vr/awesome-webvr).
- Fixed current commit: [`125aa5ac8af706fcf886de81e93ca2c3d69bcb28`](https://github.com/cmda-vr/awesome-webvr/commit/125aa5ac8af706fcf886de81e93ca2c3d69bcb28), committed 2018-03-01T10:08:04Z.
- License: [MIT `LICENSE`](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/LICENSE). README: [rendered](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md) · [raw](https://raw.githubusercontent.com/cmda-vr/awesome-webvr/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md).
- Project evidence to inspect: the fixed [README list itself](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md) is the collection data; [`LICENSE`](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/LICENSE) establishes repository reuse terms.
- README gaps: it claims “curated” but the [snapshot](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md) provides no inclusion/exclusion criteria, item annotation standard, contribution workflow, archived/last-reviewed notice, link-health signal, or per-resource license/status metadata.
- Safe demonstrator: a short MIT-licensed list makes it practical to show taxonomy, maintenance status, and trust-boundary improvements without copying the linked resources themselves.

### Backup — botwayorg/resources

- Repository and state: [`botwayorg/resources`](https://github.com/botwayorg/resources); `main`, archived, per the [repository API record](https://api.github.com/repos/botwayorg/resources).
- Fixed current commit: [`3c5d09cafc7d34316a103105cd37cc044fac8ce9`](https://github.com/botwayorg/resources/commit/3c5d09cafc7d34316a103105cd37cc044fac8ce9), committed 2023-01-19T14:18:05Z.
- License: [MIT `LICENSE`](https://github.com/botwayorg/resources/blob/3c5d09cafc7d34316a103105cd37cc044fac8ce9/LICENSE). README: [rendered](https://github.com/botwayorg/resources/blob/3c5d09cafc7d34316a103105cd37cc044fac8ce9/README.md) · [raw](https://raw.githubusercontent.com/botwayorg/resources/3c5d09cafc7d34316a103105cd37cc044fac8ce9/README.md).
- Evidence: [`bot-readme.md`](https://github.com/botwayorg/resources/blob/3c5d09cafc7d34316a103105cd37cc044fac8ce9/bot-readme.md) documents the generated-template sections and Botway commands.
- Gaps and use: the root [README](https://github.com/botwayorg/resources/blob/3c5d09cafc7d34316a103105cd37cc044fac8ce9/README.md) is one descriptive sentence and omits scope, inventory, discovery/install path, template trust boundary, archived status, contribution, and maintenance. It is the smallest backup for a skills/resources landing-page transformation.

## 8. Design-resource collection

### Primary — ibrahimraimi-archive/free-frontend-resources

- Repository and state: [`ibrahimraimi-archive/free-frontend-resources`](https://github.com/ibrahimraimi-archive/free-frontend-resources); `main`, archived, per the [repository API record](https://api.github.com/repos/ibrahimraimi-archive/free-frontend-resources).
- Fixed current commit: [`57216cd446a7364db0daf926a1ebd1493bc21f9f`](https://github.com/ibrahimraimi-archive/free-frontend-resources/commit/57216cd446a7364db0daf926a1ebd1493bc21f9f), committed 2022-11-17T13:23:03Z.
- License: [MIT `LICENSE.md`](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/LICENSE.md). README: [rendered](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/README.md) · [raw](https://raw.githubusercontent.com/ibrahimraimi-archive/free-frontend-resources/57216cd446a7364db0daf926a1ebd1493bc21f9f/README.md).
- Project evidence to inspect: [`CONTRIBUTING.md`](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/CONTRIBUTING.md) defines a minimal submission rule; [`CODE_OF_CONDUCT.md`](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/CODE_OF_CONDUCT.md), [`LICENSE.md`](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/LICENSE.md), and the repo-hosted [`assets` directory](https://github.com/ibrahimraimi-archive/free-frontend-resources/tree/57216cd446a7364db0daf926a1ebd1493bc21f9f/assets) define governance and presentation inputs.
- README gaps: the [snapshot](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/README.md) presents a large design/front-end taxonomy, but only populates the first section in that commit; it omits archived/last-reviewed status, curation criteria, item format, license/price/editability fields, preview convention, attribution guidance, and completeness boundaries.
- Safe demonstrator: archived + MIT, with an existing banner, taxonomy, and contribution file. The after example can visibly improve navigation and resource metadata while retaining attribution and avoiding claims that external assets are free for every use.

### Backup — ONSdigital/design

- Repository and state: [`ONSdigital/design`](https://github.com/ONSdigital/design); `master`, archived, per the [repository API record](https://api.github.com/repos/ONSdigital/design).
- Fixed current commit: [`3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9`](https://github.com/ONSdigital/design/commit/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9), committed 2020-12-22T10:24:24Z.
- License: [MIT `LICENSE.md`](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/LICENSE.md). README: [rendered](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/README.md) · [raw](https://raw.githubusercontent.com/ONSdigital/design/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/README.md).
- Evidence: [`principles.md`](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/principles.md), [`content.md`](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/content.md), [`logo.md`](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/logo.md), and [`_config.yml`](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/_config.yml) show the repository’s design-material scope and published-site framing.
- Gaps and use: the [README](https://github.com/ONSdigital/design/blob/3c9b7b8ca8482de09f2dcab4dde4bfed11294fb9/README.md) is mostly community/contact links and does not expose the internal material map, archived status, intended audience, version/last-review date, contribution boundary, or availability/editability metadata. It is a compact alternative focused on institutional design knowledge rather than link curation.

## Capture priority

For the eight-category README showcase, capture the primary set first. Use a consistent viewport and two crops per case:

1. **Before:** the fixed GitHub-rendered README, with repository name and commit caption outside the image.
2. **After:** the locally rendered `readme-skills` rewrite at the same width, showing the first reader journey and one category-specific section.

Keep full source links in the surrounding README rather than inside the image. For repositories whose before state contains third-party art, crop to text/structure or leave the art in the GitHub-hosted page capture; do not extract or redistribute the image file.
