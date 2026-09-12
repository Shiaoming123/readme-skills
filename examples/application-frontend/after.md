# amFOSS Website — archived 2019 codebase

[![Status: archived](https://img.shields.io/badge/status-archived-6e7781.svg)](https://github.com/amfoss/club-website-2019) [![License: MIT](https://img.shields.io/badge/license-MIT-2da44e.svg)](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/LICENSE)

> **README Skills optimization demo.** This is not an upstream README or an amFOSS publication. It preserves the useful material from the original README while documenting the fixed commit [`674e138`](https://github.com/amfoss/club-website-2019/tree/674e138a209ac21d815147e77c4401a06c9e9930).

Website for amFOSS (FOSS@Amrita), powered by Next.js 10 and React 17.

## Project status

This GitHub repository is archived. Current deployment, dependency security, browser behavior, and compatibility with modern Node.js versions have not been verified.

The original README's social, CI, contributor, and license badges all targeted a different `amfoss/website` repository. They remain visible in the [fixed original README](before.md) but are not reused as current status signals here.

## Historical local setup

The original instructions require Node.js and npm and link to the historical [installation wiki](https://github.com/amfoss/website/wiki/Installation). For this fixed repository, [`package.json`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/package.json) supports the following local path:

```bash
git clone https://github.com/amfoss/club-website-2019.git
cd club-website-2019
npm install
npm run dev
```

Use the URL printed by Next.js. The original `https://localhost:8000` statement is retained as historical evidence in [the source snapshot](before.md), but it is not supported by the inspected scripts or [`next.config.js`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/next.config.js).

This path was recovered from source but was **not run** for the showcase. Runtime evidence also conflicts: the [`Dockerfile`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/Dockerfile) uses Node 10 while [GitLab CI](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/.gitlab-ci.yml) uses Node 16.

## Available scripts

| Command | Source-defined behavior |
| --- | --- |
| `npm run dev` | Start the Next.js development server |
| `npm run build` | Create a Next.js build |
| `npm run export` | Build and export static output |
| `npm run lint-check` | Check JavaScript formatting with Prettier |

## Historical Surge deployment notes

The original README included this deployment path. It is preserved for context, not recommended as a current release procedure:

1. Create a [Surge](https://surge.sh/help/getting-started-with-surge) account.
2. Clone the historical [amFOSS Website](http://gitlab.com/amfoss/website) and enter its root directory.
3. Run `surge`.
4. Enter the requested account credentials and verify the account.
5. Generate a token.
6. In GitLab, open **Settings → CI/CD → Variables**.
7. Add `SURGE_TOKEN` and `SURGE_LOGIN`.

The inspected CI moved the exported `out` directory to `public` before deploying. Review the old repository target, credentials, domain, dependencies, and provider behavior before attempting that flow.

## License

The fixed snapshot includes an [MIT license](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/LICENSE). Third-party dependencies and hosted content retain their own terms.
