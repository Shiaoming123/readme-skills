# amFOSS Website — archived 2019 codebase

> **README Skills showcase rewrite.** This is not an upstream README or an amFOSS publication. It documents the fixed commit [`674e138`](https://github.com/amfoss/club-website-2019/tree/674e138a209ac21d815147e77c4401a06c9e9930).

Historical source for the amFOSS community website, implemented with Next.js 10 and React 17.

## Project status

This GitHub repository is archived. Current deployment, dependency security, browser behavior, and compatibility with modern Node.js versions have not been verified.

The original README linked badges and setup instructions for a different `amfoss/website` repository. Those signals are intentionally omitted here.

## Historical local evaluation

The fixed [`package.json`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/package.json) defines the following path:

```bash
npm install
npm run dev
```

Use the URL printed by Next.js. The original README's `https://localhost:8000` claim is not supported by the inspected scripts or [`next.config.js`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/next.config.js).

This command was recovered from source but was **not run** for this showcase. The repository contains conflicting runtime signals: its [`Dockerfile`](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/Dockerfile) uses Node 10 while [GitLab CI](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/.gitlab-ci.yml) uses Node 16.

## Available scripts

| Command | Source-defined behavior |
| --- | --- |
| `npm run dev` | Start the Next.js development server |
| `npm run build` | Create a Next.js build |
| `npm run export` | Build and export static output |
| `npm run lint-check` | Check JavaScript formatting with Prettier |

The historical CI moved the exported `out` directory to `public` and deployed with Surge. Do not reuse that deployment flow without reviewing its credentials, domains, and obsolete dependencies.

## License

The fixed snapshot includes an [MIT license](https://github.com/amfoss/club-website-2019/blob/674e138a209ac21d815147e77c4401a06c9e9930/LICENSE). Third-party dependencies and hosted content retain their own terms.
