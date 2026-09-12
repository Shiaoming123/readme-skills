# 全面 README Skills 集合调研与设计蓝图

> 2026-09-11（Asia/Shanghai）。Top 100 快照：23:21:50–23:24:58 UTC+8。
> 本轮只做调研与能力设计：没有创建 Skill、修改 README、提交或发布。

> **实施更新（2026-09-12）：** 本文保留调研时的提案名称与结构作为设计记录。最终实现采用 `readme-skills` 名称、四份按需参考和独立案例校验脚本；以仓库中的 [`SKILL.md`](../SKILL.md) 与实际目录为准。

## 结论

- 建一个主 Skill，以 `audit-only / optimize / restructure / generate / release-sync` 路由；仓库类型、视觉与 i18n 是条件模块，不拆成重复 Skills。
- README 先解决事实与读者任务，再谈视觉。重要声明必须追到源码、manifest、测试、CI、产物、发布或许可证。
- 不存在通用长模板。统一读者链是：判断适配 → 建立信任 → 最短首次成功 → 深入文档 → 求助/贡献。
- Top 100 中图片、HTML、badge 常见，但中位数只有 5 张图和 3 个 badge；纯文本路由页也可以专业。
- 根 README 中 Mermaid 为 0。架构图默认“小 SVG 总览 + 完整图链接 + 等价文字 + 可编辑源”。
- 动态热度图只能 opt-in；第三方故障、限流、缓存和跟踪不能成为状态的唯一来源。

## 方法与边界

- GitHub Search API：`q=stars:>0 is:public&sort=stars&order=desc&per_page=100&page=1`，API `2022-11-28`，`incomplete_results=false`。
- GitHub 默认搜索不含 Fork，需显式 `fork:true` / `fork:only`；本次 100 个结果全部 `fork=false`。[搜索规则](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- 每仓固定默认分支 SHA，再取 `GET /repos/{owner}/{repo}/readme?ref={sha}`。[README API](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-a-repository-readme)
- 全 100 份做源码提取；25 份跨类型 README 人工复核展示；十个缺失类型补样不混入统计。
- 图片计数含 badge/头像；视频指链接/引用；章节数指显式标题，不直接代表质量。

## Top 100 统计

| 指标 | 结果 |
| --- | ---: |
| 取得默认 README | 100/100 |
| 大小 | 中位 12,137 B；P90 105,090 B；最大 415,214 B |
| 标题 | 中位 15；P90 61 |
| 图片 / badge | 92 / 67；中位 5 / 3；P90 20 / 10 |
| 原始 HTML / 居中 HTML | 75 / 57 |
| theme-picture / details | 25 / 17 |
| 表格 / SVG 引用 | 37 / 61 |
| screenshot/demo / 架构标题+视觉 | 49 / 9 |
| GIF / 视频链接 | 2 / 21 |
| Mermaid fenced block | **0** |
| 动态组件 / Star History | 22 / 9 |
| 多语言入口信号 | 43 |

最大图片数 660 来自 [openclaw](https://github.com/openclaw/openclaw/blob/69bde3225e80127361d2ee634dd8d869edaef30f/README.md)，其中 648 个为头像，说明数量不能当质量分。

| 显式章节族 | 数量 | 显式章节族 | 数量 |
| --- | ---: | --- | ---: |
| Quick start / Install / Usage | 28 / 39 / 17 | Features / Examples / Docs | 24 / 10 / 37 |
| Architecture / API / Config | 10 / 16 / 15 | Requirements / Roadmap | 13 / 7 |
| Contributing / Security / License | 64 / 23 / 51 | Community / Sponsor / FAQ | 46 / 19 / 16 |
| Citation / Benchmark / Deploy | 4 / 8 / 8 | 手写目录 | 18 |

GitHub 自带 Outline，README 超过 500 KiB 会截断；手写目录与超长单页不应默认生成。[About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

人工主类：知识/学习/集合 35，Agent/AI workflow/Skills 22，语言/框架/库 17，开发工具/CLI 11，应用/服务 10，设计 2，OS/基础设施 2，倡议 1。前两类占 57%，样本明显偏斜。

## 25 仓视觉矩阵摘要

人工复核：badge 16/25、`picture/source` 8/25、`details` 6/25、表格约 9/25、logo/banner/截图/图 21/25、动态趋势 2/25、Mermaid 0/25。

- 克制 badge：[React](https://github.com/react/react/blob/019019be403c3269e15b8d7ebefb57d30f84086b/README.md)；纯文本路由：[Linux](https://github.com/torvalds/linux/blob/08df884136f1c1197bab2a27814404fd329d9aac/README)。
- 产品证明：[VS Code](https://github.com/microsoft/vscode/blob/0ac867d1f00150db3a91c10edc1295eccd75c16d/README.md)；图解长文：[System Design Primer](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md)。
- 主题图：[Rust](https://github.com/rust-lang/rust/blob/ada41e1ce81819f01577c0ee40ccbd6fc41384e8/README.md)；折叠示例：[Transformers](https://github.com/huggingface/transformers/blob/3f601734a3580f55484720770850966bba060e4f/README.md)。
- 视觉索引：[PowerToys](https://github.com/microsoft/PowerToys/blob/71340eed47f7cf6f53b68b86a7939ad1240c3de7/README.md)；视频 poster：[Spec Kit](https://github.com/github/spec-kit/blob/c173bf19a6654e3b05386ec3599349a55282b897/README.md)。
- 富表现上限：[Dify](https://github.com/langgenius/dify/blob/e7981a6f19435d52ef4b92f71054739ebc2b593e/README.md) 的 26 个 badge 适合作噪声上限。

| 级别 | 规则 |
| --- | --- |
| 默认稳定 | GFM、少量证据 badge、仓库内图片/SVG、picture、details；检查 alt、暗色、窄屏 |
| 可移植但需回退 | Mermaid/GeoJSON/TopoJSON/STL；关键图同时提交静态 SVG |
| 可选脆弱 | Star History、Repobeats、github-readme-stats、Trendshift、contrib.rocks；需静态/文字回退 |
| 避免 | badge 墙、超大 GIF、图中命令、整页 HTML table、iframe/script/custom canvas、临时附件唯一源 |

GitHub 支持原生图表，但 HTML 会清洗，README 不是网页运行时。[Diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) · [github/markup](https://github.com/github/markup)
Star History #539 记录 2026-06-30 后 hosted SVG 可能因 API 权限变化为空；github-readme-stats 也说明公共端点受限流/流量影响。[#539](https://github.com/star-history/star-history/issues/539) · [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)

## 能力扩充

| 维度 | Skill 契约 |
| --- | --- |
| 基础 | 名称、价值、受众、真实状态、最短成功、要求、安装、用法、文档、求助、贡献、安全、许可 |
| optimize | 保留声音/品牌/资产，只修漂移、首屏、命令、链接、alt、冗余 |
| restructure | 先列保留/移动/删除/新增，再重排读者路径，长内容下沉 docs |
| generate | 全仓审计后新建；未知项降级或 TODO，不猜功能 |
| 理论/学术 | 主张、论文/DOI、阅读、复现、数据/代码许可、CITATION、局限 |
| Library/SDK | 兼容版本、安装、最小 import、API/docs、SemVer/迁移 |
| CLI/Service | 平台安装、首条命令、I/O/exit code、配置；托管/自托管、鉴权、成本、安全 |
| App/前端 | 下载与源码运行分开、平台成熟度、截图、env、构建/部署、a11y、隐私 |
| Template | Use Template/生成命令、包含项、替换清单、首次构建、升级/脱离 |
| Fork/mirror | 上游、目的、基线+日期、差异、兼容、同步、issue/security、商标/NOTICE、只读警告 |
| Skills/资源 | 宿主兼容、安装/触发、分类、收录/去重/失效、第三方信任和逐项许可 |
| 设计资料 | 预览、格式、编辑源、工具版本、字体/素材授权、下载、a11y |
| Model/Dataset | intended use、限制/偏差、训练/来源、评测条件、schema/版本/PII、各类许可 |
| Monorepo/archive | 根地图+包级用法；弃用首屏写替代、迁移和安全截止 |
| i18n | canonical 可选；命令/版本/平台/状态/链接/许可对齐，叙事自然本地化 |
| 证据 | claims ledger：observed / verified-now / inferred / unknown；交付链分 source→built→packaged→signed→published→deployed |
| 安全/法律 | 图有文字等价；扫秘密/本地路径；不自动选许可证；Security 指向私密渠道 |
| 社区/发现 | 链接 health files；Description/Topics/social preview 只建议，外部修改另授权 |
| 维护 | 检查易漂移字段；输出幂等；不用统一分数制造改动 |

参考平台原生契约：[Community Profile](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories) · [CITATION](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) · [Model Cards](https://huggingface.co/docs/hub/model-cards) · [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards)

## 十个补样（不计入统计）

| 类型 | 固定 README | 校正点 |
| --- | --- | --- |
| continuation | [Valkey](https://github.com/valkey-io/valkey/blob/98f91521245b8ca20523616e3243799ca5d1a08e/README.md) | 首屏说明上游事件与自身定位 |
| downstream | [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/blob/e71b91c6e336d0f25cfc6b9ef09298a9d2506e24/README.md) | 目标、差异、平台构建来源 |
| staged mirror | [kubectl](https://github.com/kubernetes/kubectl/blob/996345ff414b11dc7a5d30d0ff5e23cd5c9b35ab/README.md) | 只读警告和 canonical PR 入口 |
| literal Fork | [qBittorrent Enhanced](https://github.com/c0re100/qBittorrent-Enhanced-Edition/blob/80f544d0b4efbe0a04edc57784c771ecf2b1b90e/README.md) | 差异清楚，仍需基线/兼容 |
| 学术社区 | [papers-we-love](https://github.com/papers-we-love/papers-we-love/blob/7143d9a06b76d86f48fd46b4400bbb9c3d843a6a/README.md) | 阅读、活动、论文版权 |
| 研究 monorepo | [google-research](https://github.com/google-research/google-research/blob/08a8d6736475776f42ffac23b2c13111a28e5795/README.md) | 根路由；数据/源码许可分开 |
| 应用脚手架 | [electron-react-boilerplate](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/484a66bda78ea3ead4b693ab9dca3e96baf4fdcc/README.md) | 开发、打包、template 身份 |
| 模板集合 | [devcontainers/templates](https://github.com/devcontainers/templates/blob/0d90e81192547f6464cf2ed84f56bcf2e558f526/README.md) | 工具、CLI、集合与贡献 |
| 设计资源 | [design-resources](https://github.com/bradtraversy/design-resources-for-developers/blob/e71627409ec9df19337048897b5bbb9b7d6b75df/readme.md) | 许可和失效维护 |
| 设计工具 | [Awesome-Design-Tools](https://github.com/goabstract/Awesome-Design-Tools/blob/dc60e63c248c44acb42f09fb0c985b77b5fe4bf5/README.md) | 视觉入口与陈旧 CDN 风险 |

临时贡献 Fork 默认保留上游 README；长期 user-facing 差异才重写身份契约。

## Skill 架构

```text
readme-craft/
├── SKILL.md
├── references/
│   ├── core-contract.md
│   ├── evidence-maturity.md
│   ├── repository-profiles.md
│   ├── visual-gfm.md
│   └── governance-release-i18n.md
└── scripts/audit_readme.py
```

| 模式 | 行为 |
| --- | --- |
| audit-only | 只读证据、claims ledger、缺口、断链 |
| optimize | 对基本正确 README 做最小补丁 |
| restructure | 先列变更清单再重排 |
| generate | 无 README 时全仓审计后新建 |
| release-sync | 同步版本/下载/兼容/截图/i18n；不发布或 Git 写入 |

`SKILL.md` 只放路由、证据门槛和授权边界。五 references 按需加载。唯一脚本用 Python 标准库、只读、JSON 输出，检查 README 选择/大小、链接/资产/alt/标题、语言、manifest/version drift、health/license、秘密/本地路径和第三方动态资源；默认不运行 README 命令。

初版不建模板海洋、assets、图片生成器或动态服务；只有工具权限、remote write/public publish/付费凭据、独立维护节奏或实测上下文过载时才拆 Skill。

## 风险与验收

- 功能、命令、版本、平台、License、发布状态逐项有来源；无证据就降级/删除。
- 默认 audit + surgical edit；保留人工叙事、品牌、历史和有效链接；第二次运行幂等。
- 不自动装依赖、选许可证、改 GitHub 元数据、提交、推送或发布。
- 主 fixture：良好 README 优化、混乱 README 重构、无 README 生成；另测双语、研究、Fork/mirror/archive、富视觉、release-sync。
- 最小验证：链接/锚点/资产/alt、秘密扫描、manifest/命令/版本、仓库 docs check；可见内容再测 GitHub 渲染、暗亮与窄屏。
- 限制：Top 100 是类型偏斜的三分钟流行度快照；源码检测不等同 100 份像素验收；补样不参与百分比。

## 附录：Top 100 固定快照

| # | 仓库固定 README | Stars | SHA |
| ---: | --- | ---: | --- |
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x/blob/aa17439b62f384511a5561ce308e9598b94d8989/README.md) | 546,551 | `aa17439b62f3` |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome/blob/bc98e517ddca672f55f9857d714fc3ea3c3540b2/readme.md) | 505,060 | `bc98e517ddca` |
| 3 | [public-apis/public-apis](https://github.com/public-apis/public-apis/blob/7ee71f04dd42720f7f4130aa70f804aa95c53164/README.md) | 478,896 | `7ee71f04dd42` |
| 4 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/blob/b2565781d756e4ba0bc92d3742f398999d115242/README.md) | 455,309 | `b2565781d756` |
| 5 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books/blob/0ddc9758e62a4134b5b924c8aad1a3c62ef345ec/README.md) | 396,523 | `0ddc9758e62a` |
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw/blob/69bde3225e80127361d2ee634dd8d869edaef30f/README.md) | 389,437 | `69bde3225e80` |
| 7 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md) | 369,403 | `ae9bbd7b02d9` |
| 8 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap/blob/89fdaad9c151a8c2584cf0db1bd34c19a4cf8c59/readme.md) | 366,891 | `89fdaad9c151` |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university/blob/717298bf219a30d7fb0671285c5f057b1bb74b27/README.md) | 360,745 | `717298bf219a` |
| 10 | [vinta/awesome-python](https://github.com/vinta/awesome-python/blob/bba56e8aa5058c54112319ebbe84447596591159/README.md) | 319,968 | `bba56e8aa505` |
| 11 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/d9c09ec5c508c1e8fbd208782eab5d4cf1b64c08/README.md) | 318,512 | `d9c09ec5c508` |
| 12 | [obra/superpowers](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md) | 285,167 | `b36e0829c6d0` |
| 13 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning/blob/f5fb43039feabcab87838ab8226a8a9c2d6313a0/README.md) | 282,961 | `f5fb43039fea` |
| 14 | [996icu/996.ICU](https://github.com/996icu/996.ICU/blob/f5e35f48d769bf92ed885888bfe911d3e5b5a63d/README.md) | 276,970 | `f5e35f48d769` |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/README.md) | 259,515 | `3cca18b368ae` |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/README.md) | 256,291 | `c9148d0bb239` |
| 17 | [react/react](https://github.com/react/react/blob/019019be403c3269e15b8d7ebefb57d30f84086b/README.md) | 250,039 | `019019be403c` |
| 18 | [torvalds/linux](https://github.com/torvalds/linux/blob/08df884136f1c1197bab2a27814404fd329d9aac/README) | 248,243 | `08df884136f1` |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/ad03f20dd61919ca2135d6904e787a94284aacaf/README.md) | 244,490 | `ad03f20dd619` |
| 20 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge/blob/7d37069a361d3fd9f214480755f7969744e866fa/README.md) | 243,158 | `7d37069a361d` |
| 21 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python/blob/742f93919150d9b741d8fc42d496a7a688af8336/README.md) | 224,476 | `742f93919150` |
| 22 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/README.md) | 220,300 | `c291e7961a51` |
| 23 | [vuejs/vue](https://github.com/vuejs/vue/blob/9e88707940088cb1f4cd7dd210c9168a50dc347c/README.md) | 212,462 | `9e8870794008` |
| 24 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/README.md) | 212,280 | `2c606141936f` |
| 25 | [ossu/computer-science](https://github.com/ossu/computer-science/blob/33d44a44e3526ede8e862bf1ad50ae5ae7a2f112/README.md) | 208,924 | `33d44a44e352` |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode/blob/95daf90670b7c039c436c85537da5fbfe2205b41/README.md) | 206,689 | `95daf90670b7` |
| 27 | [n8n-io/n8n](https://github.com/n8n-io/n8n/blob/13b8f22fd0cd84d923710b32a2be9bcd82f55fbe/README.md) | 204,004 | `13b8f22fd0cd` |
| 28 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow/blob/d4218f359a137300769de4cbd83bc22744e31233/README.md) | 199,708 | `d4218f359a13` |
| 29 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain/blob/9c7c54110705760267b07b6e6a6d406d1172a1bf/README.md) | 198,740 | `9c7c54110705` |
| 30 | [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms/blob/85293e3e2b88f4d2ce330d956b139cf628aa1e82/README.md) | 196,673 | `85293e3e2b88` |
| 31 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md) | 195,199 | `08106b0c3771` |
| 32 | [microsoft/vscode](https://github.com/microsoft/vscode/blob/0ac867d1f00150db3a91c10edc1295eccd75c16d/README.md) | 192,005 | `0ac867d1f001` |
| 33 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/bbc809a1161d3bfca51fa36f59dda35556ee85a0/README.md) | 190,430 | `bbc809a1161d` |
| 34 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts/blob/6401d2f36975dc07bcb6d22ea823a8498a75ec01/README.md) | 190,179 | `6401d2f36975` |
| 35 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/blob/c6e66edee824d83e84473ec666917b58323630df/README.md) | 189,668 | `c6e66edee824` |
| 36 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT/blob/98381ab27f733468bfe1f9c4f4942b4b416d9a8b/README.md) | 187,260 | `98381ab27f73` |
| 37 | [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days/blob/44b2575bf42a02d0a38d9dada3f60335c95c5ec2/README.md) | 186,292 | `44b2575bf42a` |
| 38 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes/blob/b70121d377cb6005eb65f12b098cd5decd905669/README.md) | 185,998 | `b70121d377cb` |
| 39 | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS/blob/044120ef55564939cd35f5ddaf3f6c0a45d7b02c/README.md) | 184,854 | `044120ef5556` |
| 40 | [avelino/awesome-go](https://github.com/avelino/awesome-go/blob/1ed3a46319b9e85d2fedcacc8cece2e0faf456b6/README.md) | 183,806 | `1ed3a46319b9` |
| 41 | [microsoft/markitdown](https://github.com/microsoft/markitdown/blob/9480644d9c3b7397b9bf0156f858fa3a5aad7d2c/README.md) | 182,619 | `9480644d9c3b` |
| 42 | [ollama/ollama](https://github.com/ollama/ollama/blob/b68b112bd8868d6278250d7d4bdfafa5cbf035c8/README.md) | 180,665 | `b68b112bd886` |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl/blob/30a9697084c8b6ce4392795c965022df31c5036b/README.md) | 179,078 | `30a9697084c8` |
| 44 | [flutter/flutter](https://github.com/flutter/flutter/blob/dda542f1dc7ba4812d2b88d04ec3c65358436f23/README.md) | 178,892 | `dda542f1dc7b` |
| 45 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub/blob/75c87e759278c36c479849d65eae8e2a08bb9c33/README.md) | 176,024 | `75c87e759278` |
| 46 | [anthropics/skills](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/README.md) | 175,798 | `34040c9c5685` |
| 47 | [github/gitignore](https://github.com/github/gitignore/blob/9e86bc12f67365b8dd974d3b3f09d166265c5530/README.md) | 175,711 | `9e86bc12f673` |
| 48 | [twbs/bootstrap](https://github.com/twbs/bootstrap/blob/dc109898919ffec835e87ab1e6bee130757d67e1/README.md) | 174,756 | `dc109898919f` |
| 49 | [f/prompts.chat](https://github.com/f/prompts.chat/blob/f78a1c5136fa080155d928e0d7e2b4a41ddef03e/README.md) | 169,963 | `f78a1c5136fa` |
| 50 | [huggingface/transformers](https://github.com/huggingface/transformers/blob/3f601734a3580f55484720770850966bba060e4f/README.md) | 165,119 | `3f601734a358` |
| 51 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/82a973c04367123ae98bd9abdf80d9eda9b910e2/README.md) | 164,896 | `82a973c04367` |
| 52 | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line/blob/6b50745d2e788add2e8f1ed29010e72659a9a074/README.md) | 162,336 | `6b50745d2e78` |
| 53 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide/blob/d76264cb4e000416c4adca06770ce014bd309150/README.md) | 158,450 | `d76264cb4e00` |
| 54 | [langgenius/dify](https://github.com/langgenius/dify/blob/e7981a6f19435d52ef4b92f71054739ebc2b593e/README.md) | 155,429 | `e7981a6f1943` |
| 55 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow/blob/595cd72a2b2021f2375fa31109af02d20bb17648/README.md) | 154,585 | `595cd72a2b20` |
| 56 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/blob/6d29a9b08785a0e49ffc9818bbdd381164c2df5f/README.md) | 151,668 | `6d29a9b08785` |
| 57 | [open-webui/open-webui](https://github.com/open-webui/open-webui/blob/0a7c15832fb30b1903753e83f81dc7d27e5b0944/README.md) | 151,640 | `0a7c15832fb3` |
| 58 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy/blob/19c1261d2e2cbf2b5e6a71a8b64cc1dd3ede06ac/README.md) | 149,389 | `19c1261d2e2c` |
| 59 | [airbnb/javascript](https://github.com/airbnb/javascript/blob/8ed19247bef145e3cc41b24a02dd1fe6d9b5e681/README.md) | 148,200 | `8ed19247bef1` |
| 60 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain/blob/67ee6cb63dd9ae7f3a4dfedc3095652bce15a125/README.md) | 146,124 | `67ee6cb63dd9` |
| 61 | [anthropics/claude-code](https://github.com/anthropics/claude-code/blob/536a2e23d9e28586f81f17b3535281b5f2995a70/README.md) | 144,749 | `536a2e23d9e2` |
| 62 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/blob/f624ffc382a03fea21d39e7130000bce96678189/README.md) | 143,816 | `f624ffc382a0` |
| 63 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/1e4203a7d88873c1b37ab2d1c07074fea498c274/README.md) | 143,537 | `1e4203a7d888` |
| 64 | [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook/blob/e1d28e8886c0b6ff3e50da991ce0e895134ddc59/README.md) | 142,560 | `e1d28e8886c0` |
| 65 | [vercel/next.js](https://github.com/vercel/next.js/blob/d155ba9ebfffe4742efefda8d68c2e0e8e490924/readme.md) | 142,236 | `d155ba9ebfff` |
| 66 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl/blob/956b8c585591b401a543e409accb163eeaaa1193/README.md) | 141,183 | `956b8c585591` |
| 67 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys/blob/71340eed47f7cf6f53b68b86a7939ad1240c3de7/README.md) | 138,560 | `71340eed47f7` |
| 68 | [golang/go](https://github.com/golang/go/blob/ffee23ff7c795472f0b4d5384580723565d122bf/README.md) | 138,416 | `ffee23ff7c79` |
| 69 | [iptv-org/iptv](https://github.com/iptv-org/iptv/blob/1caa8ac9b4ff151e4188de9c7b74a55d29cf3471/README.md) | 138,331 | `1caa8ac9b4ff` |
| 70 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/f08663526b912003e84923b35c97d08c3f1e9ca4/README.md) | 137,194 | `f08663526b91` |
| 71 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev/blob/fe17ac7bbc0335fbf637d5ced8574edf29918269/README.md) | 137,125 | `fe17ac7bbc03` |
| 72 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm/blob/b1f23cb9605f6146ff78bafad71e795176439b99/README.md) | 135,845 | `b1f23cb9605f` |
| 73 | [github/spec-kit](https://github.com/github/spec-kit/blob/c173bf19a6654e3b05386ec3599349a55282b897/README.md) | 135,600 | `c173bf19a665` |
| 74 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/356918eba965ee1eac64bd3a7f0dd02108350de5/README.md) | 135,540 | `356918eba965` |
| 75 | [garrytan/gstack](https://github.com/garrytan/gstack/blob/71f6048e8ada25180e61438abc1d98cb151fe9a7/README.md) | 132,555 | `71f6048e8ada` |
| 76 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI/blob/1d48d9cf7bcecb6022a87b3cb13e0fb435bf9b8a/README.md) | 132,547 | `1d48d9cf7bce` |
| 77 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch/blob/d695a2d77fd9081eafd3e9eedcbf2a97b3410928/README.md) | 132,339 | `d695a2d77fd9` |
| 78 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw/blob/afa3a653fc5d2b742adcbd5a6063187b056d2419/README.md) | 131,605 | `afa3a653fc5d` |
| 79 | [krahets/hello-algo](https://github.com/krahets/hello-algo/blob/28c1e74c1d3594fca7cc41b78a6bd18b700c5ce9/README.md) | 130,010 | `28c1e74c1d35` |
| 80 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code/blob/bd756f8b2283a38560efe83cb30af38324d4e9e9/README.md) | 129,036 | `bd756f8b2283` |
| 81 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp/blob/8172e6577ac2b35de1ec1e5d1c0aaad6c4a2129f/README.md) | 127,852 | `8172e6577ac2` |
| 82 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/blob/b4b4a788790ed13563d7f48a187e32cc7f2ffd89/README.md) | 127,332 | `b4b4a788790e` |
| 83 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7f69fed6a2717900085f1bc3b263721f8ba025e2/README.md) | 126,848 | `7f69fed6a271` |
| 84 | [react/react-native](https://github.com/react/react-native/blob/ea2ca1b9211176bc482e33eef0118f1aefce2593/README.md) | 126,555 | `ea2ca1b92111` |
| 85 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui/blob/3ba91b1cc83e1bbe4ab35a422ff2a694849c5048/README.md) | 123,571 | `3ba91b1cc83e` |
| 86 | [openai/codex](https://github.com/openai/codex/blob/654b0a77d0d2f81aa21f61caf7af4be88fe550bb/README.md) | 123,359 | `654b0a77d0d2` |
| 87 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk/blob/e82dd12350479b848630d1e500c2f6870609a884/README.md) | 123,179 | `e82dd1235047` |
| 88 | [electron/electron](https://github.com/electron/electron/blob/ce11ce44da49f775619679b34267ce38f60b4589/README.md) | 122,993 | `ce11ce44da49` |
| 89 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo/blob/436b0e9cc830ef7639e33388917e389cf30d3307/README.md) | 122,437 | `436b0e9cc830` |
| 90 | [nodejs/node](https://github.com/nodejs/node/blob/c14304154e4b5c35ebdcc8c73f26a8e1c00d1b5b/README.md) | 121,583 | `c14304154e4b` |
| 91 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking/blob/b2bb13aa69b4f568a1bab0cbb17b7a00a350dc36/README.md) | 120,146 | `b2bb13aa69b4` |
| 92 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners/blob/c9657f3fdb6e4f50a168b1d026eadf4cda2f0d07/README.md) | 119,545 | `c9657f3fdb6e` |
| 93 | [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN/blob/cc1108ac90f53a1fd4f773b61f5c6b91b91389ca/README.md) | 118,805 | `cc1108ac90f5` |
| 94 | [rust-lang/rust](https://github.com/rust-lang/rust/blob/ada41e1ce81819f01577c0ee40ccbd6fc41384e8/README.md) | 118,388 | `ada41e1ce818` |
| 95 | [godotengine/godot](https://github.com/godotengine/godot/blob/cb41ea115914c61a8329087b4cffbad7477b8427/README.md) | 116,968 | `cb41ea115914` |
| 96 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/blob/23f2ffaa43fd12f25d9eabe91e6d184b5d89b474/README.md) | 116,928 | `23f2ffaa43fd` |
| 97 | [2dust/v2rayN](https://github.com/2dust/v2rayN/blob/4f5a6be12da72ebce3babe2dacf7549aff5daddf/README.md) | 115,910 | `4f5a6be12da7` |
| 98 | [mrdoob/three.js](https://github.com/mrdoob/three.js/blob/090c7a9f3c966cfcdc0ef2161560233bab9a40ad/README.md) | 115,407 | `090c7a9f3c96` |
| 99 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md/blob/8147538b4226ae41e2487a9179e3bcc1f68e8554/README.md) | 115,357 | `8147538b4226` |
| 100 | [browser-use/browser-use](https://github.com/browser-use/browser-use/blob/50f205533fe10ba35b553d2a3689c77b87bd5d0a/README.md) | 114,200 | `50f205533fe1` |
