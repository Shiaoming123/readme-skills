# Repository profiles

Select one primary profile from the artifact and primary visitor action. Add only evidence-supported overlays such as monorepo, fork, multilingual, archived, or experimental.

## Application or frontend product

Lead with the user outcome and a real screenshot, short demo, or live preview when available. Then show the shortest local run path. Cover configuration, supported delivery targets, development, testing, and deployment only to the level users need.

Do not present a component preview as a shipped application or list planned platforms as supported. For mobile and desktop targets, distinguish buildable, packaged, published, and verified-on-device states.

## Library, framework, API, or SDK

Lead with the problem solved and ecosystem. Put package installation and the smallest representative example early. State compatibility, stability, error model, and links to full API docs. Use multiple language examples only when each client is maintained.

## CLI, developer tool, or automation

Lead with the job completed. Show installation, one successful command, expected output, then common workflows and configuration. Document filesystem, network, credential, destructive, and dry-run behavior where relevant. Link to generated or canonical command reference instead of copying every flag.

## Service, self-hosted system, infrastructure, or database

Lead with deployment purpose and operating boundary. Include architecture overview, requirements, configuration, local evaluation, deployment, health/observability, backup or migration, upgrades, and security model as applicable. Keep production guidance explicit about what has and has not been verified.

## Template, starter, or scaffold

Lead with what users can create and what is already included. Make "Use this template" or the creation command the primary action. Show generated structure, replacement points, customization, verification, update strategy, and which values are placeholders. Do not describe sample branding as the template's own product identity.

## Fork, mirror, or downstream distribution

Put the relationship near the top:

- canonical upstream URL and original project name;
- why this repository exists;
- current divergence and user-visible consequences;
- compatibility and migration expectations;
- sync method, cadence, or last known upstream basis when established;
- which issue tracker and release channel users should use.

Preserve upstream attribution and license notices. Never imply official status without evidence.

## Research, theory, paper, or reproducibility project

Lead with the research question, contribution, and evidence boundary. Include abstract-level context, method, results or artifacts, reproduction environment, data provenance, limitations, citation, and license. Separate peer-reviewed results from exploratory claims. Prefer exact experiment commands and expected outputs over a product-style feature list.

## Model, dataset, benchmark, or scientific artifact

Use model-card or dataset-card concerns: intended use, source/provenance, format, access, evaluation method, limitations, bias or safety boundaries, hardware/runtime needs, license, and citation. Never infer usage rights from public availability.

## Skills, awesome list, resource, or design collection

Lead with scope and curation promise. Provide a navigable taxonomy, item annotation convention, inclusion/exclusion criteria, contribution process, maintenance status, and last-reviewed signals when available. For Skills collections, explain installation or discovery conventions and trust boundaries. For design resources, include format, license, preview, attribution, and editability metadata when relevant.

Do not call a list "curated" unless selection rules are visible. Avoid unsupported claims of completeness.

## Documentation, standard, specification, or educational repository

Lead with what the reader will learn or implement, assumed knowledge, version/status, reading path, and normative versus explanatory content. For standards, identify authority, conformance language, change process, and implementation references. For tutorials, show prerequisites and a progressive path.

## Monorepo

Explain the shared purpose before package details. Provide a compact package map with responsibility, intended consumer, and primary command. State root versus package working directories and workspace commands. Link to package READMEs for depth; do not duplicate every package manual in the root.

## Hardware or physical-computing project

Show the resulting device or behavior, bill of materials, supported revisions, assembly, firmware/software setup, calibration, safety limits, verification, and troubleshooting. Keep calibration parameters visible because real hardware varies.

## Archived or maintenance-only project

Put status near the top. State what still works, what is unsupported, whether security fixes occur, and the recommended successor or migration path when known. Remove calls to action the maintainers no longer support.

## Technology adaptation

Technology determines factual setup, not the document's identity. Derive commands and compatibility from canonical artifacts such as:

- JavaScript/TypeScript: `package.json`, lockfile, workspace config, runtime declarations;
- Python: `pyproject.toml`, lockfile, package metadata, supported Python classifiers;
- Rust: `Cargo.toml`, workspace metadata, feature flags, MSRV evidence;
- Go: `go.mod`, module packages, build tags, supported Go version;
- JVM: Gradle/Maven configuration and toolchains;
- .NET: solution/project files, target frameworks, workload requirements;
- Apple/mobile: project configuration, signing boundary, simulator/device evidence;
- containers/infrastructure: compose, container, module, provider, and deployment configuration.

Do not recommend an alternative package manager or setup path merely because it is common for the stack.
