# Before-and-after showcase

These eight cases exercise README Skills against different repository contracts. Each case uses a fixed public GitHub snapshot with a materially incomplete README and enough repository evidence to write a narrower, more useful alternative.

“Incomplete” describes the cited README snapshot, not the project or its maintainers. Every selected repository was archived and MIT-licensed at the research date, and none of the rewrites were submitted upstream.

Each visual comparison is built from two 1440×2400 screenshots, not a synthetic summary card: the original README page at the fixed commit and the corresponding demonstration rewrite rendered from `after.md` through GitHub's Markdown API. The long comparison preserves a large content viewport and multiple heading levels; the linked Markdown file remains the complete output.

| Category | Fixed source README | Complete rewrite | Screenshot comparison |
| --- | --- | --- | --- |
| Application / frontend | [amfoss/club-website-2019](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/README.md) | [after](application-frontend/after.md) | [view](../assets/showcase/application-frontend-comparison.png) |
| Library / non-JS SDK | [mattilyra/LSH](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/README.md) | [after](library-sdk/after.md) | [view](../assets/showcase/library-sdk-comparison.png) |
| CLI / automation | [thebigmunch/gmusicapi-scripts](https://github.com/thebigmunch/gmusicapi-scripts/blob/5492593db20efb0ea5ad5dcf1b2e1a0e4d0349e8/README.md) | [after](cli-scaffold/after.md) | [view](../assets/showcase/cli-scaffold-comparison.png) |
| Fork / downstream | [bitcoin/libbase58](https://github.com/bitcoin/libbase58/blob/b1dd03fa8d1be4be076bb6152325c6b5cf64f678/README.md) | [after](fork-downstream/after.md) | [view](../assets/showcase/fork-downstream-comparison.png) |
| Research / reproducibility | [IBM/adaptive-federated-learning](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md) | [after](research-reproducibility/after.md) | [view](../assets/showcase/research-reproducibility-comparison.png) |
| Dataset / scientific artifact | [fredzzhang/hicodet](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md) | [after](dataset-artifact/after.md) | [view](../assets/showcase/dataset-artifact-comparison.png) |
| Skills / awesome / resources | [cmda-vr/awesome-webvr](https://github.com/cmda-vr/awesome-webvr/blob/125aa5ac8af706fcf886de81e93ca2c3d69bcb28/README.md) | [after](resource-collection/after.md) | [view](../assets/showcase/resource-collection-comparison.png) |
| Design resources | [ibrahimraimi-archive/free-frontend-resources](https://github.com/ibrahimraimi-archive/free-frontend-resources/blob/57216cd446a7364db0daf926a1ebd1493bc21f9f/README.md) | [after](design-resource/after.md) | [view](../assets/showcase/design-resource-comparison.png) |

The candidate research, backup set, source files, licenses, and selection rationale are recorded in [candidate-cases.md](../research/candidate-cases.md). Machine-readable snapshot metadata lives in [cases.json](cases.json).

## Review method

For each case, the rewrite:

1. identifies the artifact, primary visitor action, and archived lifecycle;
2. checks the README against source, manifest, configuration, tests, or governance files;
3. marks important claims as verified, inferred, missing, or conflicting;
4. rebuilds the opening around identity, status, safest first action, and trust boundary;
5. keeps unverified execution, compatibility, service availability, and data rights visible.

The “after” files are documentation demonstrations, not maintained forks and not recommendations to run archived software.
