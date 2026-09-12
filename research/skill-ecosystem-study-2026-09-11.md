# README Agent Skill 生态调研

> 调研日期：2026-09-11（Asia/Shanghai）
> 范围：面向 Codex、Claude Code 等 Agent 的 `SKILL.md` 能力；同时对照通用文档 Skill、README 规范与生成工具。结论基于本地安装内容、官方仓库和代表项目源码，不以搜索摘要或 Star 数作为能力证据。

> **实施更新（2026-09-12）：** 本文保留最初生态判断作为调研快照。后续 Top 100 调研与用户需求证明，需要的是覆盖多仓库类型、证据边界、展示和发布治理的完整工作流，因此已经实现为本仓库的 `readme-skills`。

## 结论

**已经有人做 README 专用 Skill，并非生态空白。** 社区里至少有五条清晰路线：

1. **证据优先的 create/update/audit**：pekral `github-readme-generator` 建立 claim → source 映射，限制修改范围，并带场景测试与 Agent eval。
2. **仓库事实驱动**：AgentsCamp `readme-generator` 从 manifest、脚本、入口和目录生成或刷新 README，未知项保留 TODO。
3. **模板 + 检测 + lint**：JayRHa `readme-generator` 带项目探测、README lint、模板、章节目录和示例。
4. **作品集/视觉传播**：geekjourneyx `readme-generator` 强调叙事、视觉资产、GitHub Description 与 Topics。
5. **规范合规**：tenequm `standard-readme` 按 Standard Readme 规范写作或审计。

但截至本次固定提交扫描，**已弃用的 OpenAI 官方 `openai/skills` 快照与 Anthropic 官方 `anthropics/skills` 均没有 README 专项 Skill**。Anthropic 的 `doc-coauthoring` 能协作写文档，OpenAI/本地的文档能力也能写作，但它们没有针对仓库 README 的事实提取、增量维护和发布前验证契约。OpenAI 当前已把 Skill/Plugin 示例迁往 [`openai/plugins`](https://github.com/openai/plugins)，旧仓库 README 明确标记 deprecated。

因此：

- 若目标只是“帮项目写或维护一份可信 README”，**不值得从零再造**；应先试用 pekral `github-readme-generator`，它已经覆盖最关键的事实、范围与 Git 副作用护栏。
- 只有拾学/Meow 所需的**多语言事实对齐、成熟度声明、平台/发布证据**在真实试跑中反复缺失时，才值得创建一个窄扩展或清晰标注来源的衍生 Skill。定位应是“README release-evidence maintainer”，而不是“更漂亮的 README 生成器”。

## 本地能力盘点

本次扫描了可用 Skill 清单及以下本地来源的 `SKILL.md` frontmatter：

- `~/.codex/skills`
- `~/.agents/skills`
- `~/.codex/skills/.system`
- 已安装的 OpenAI bundled / curated plugin cache

结果：**没有名称或 description 明确声明“创建、刷新或审计项目 README”的专用 Skill。** 可组合的相邻能力如下：

| 本地能力 | 能做什么 | 为什么不能替代 README 专用 Skill |
| --- | --- | --- |
| `documents` | 写作与渲染校验 `.docx` | 输出载体与目标不同，不读取仓库事实生成 `README.md` |
| `technical-blog-writing` | 基于证据写技术文章、复盘、部署指南 | 面向长文，不负责 README 首屏、安装、使用、贡献和许可证结构 |
| `claude-md-improver` | 审计和改进 `CLAUDE.md` | 面向 Agent 上下文，不是面向用户/贡献者的仓库首页 |
| `skill-creator` | 创建或更新 Agent Skill | 生成的是 `SKILL.md`；官方指导还明确要求 Skill 包内不要额外塞无关 `README.md` |
| `tech-resume-optimizer` | 建议求职项目完善 README | 只提出建议，没有仓库读取、生成和验证流程 |

这说明本地模型“能写 README”，但缺少可复用、可触发、可验证的专门工作流。

## 公开生态代表项目

### README 专用 Agent Skills

| 项目 | 实际能力 | 优点 | 主要缺口/偏向 | 许可证证据 |
| --- | --- | --- | --- | --- |
| [pekral `github-readme-generator`](https://github.com/pekral/github-readme-generator/blob/d8bdac94d1a9488751d65e55e78eeabd47895bd0/skills/github-readme-generator/SKILL.md) | 从 README、manifest、入口、公共 API、测试、示例、CI、配置和许可证建立 claim → source 映射；支持 create/update/audit；默认只改指定 README，无隐式 Git 操作 | 与本次目标最接近；有 evidence/structure/validation references、场景 fixture、测试和 Agent eval；还把仓库文本视为不可信数据 | 项目自述为 beta；已记录 Claude Code 子集 eval，但 Codex/Cursor 等打包目标尚不能等同已验证；未见双语一致性与成熟度/发布证据专门契约 | Skill 内 [MIT](https://github.com/pekral/github-readme-generator/blob/d8bdac94d1a9488751d65e55e78eeabd47895bd0/skills/github-readme-generator/LICENSE.md) |
| [AgentsCamp `readme-generator`](https://github.com/imtiazrayhan/agentscamp-library/blob/51600a860e4d20409679c373531c9014a84d0a67/skills/readme-generator/SKILL.md) | 读取现有 README、manifest、锁文件、入口、脚本和浅层目录；刷新机械章节；未知项写 TODO；复核脚本和路径 | 边界小、强调不编造、适合常规工程仓库 | 只覆盖常见栈与基础章节；没有行为/成熟度声明的证据台账、双语同步、发布产物或截图验证 | 仓库根 [MIT](https://github.com/imtiazrayhan/agentscamp-library/blob/51600a860e4d20409679c373531c9014a84d0a67/LICENSE) |
| [JayRHa `readme-generator`](https://github.com/JayRHa/AgentSkills/blob/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/readme-generator/SKILL.md) | 项目探测、章节选择、模板、徽章、CLI 示例、质量清单；附 `detect_project.py` 与 `lint_readme.py` | 配套资源最完整，可做确定性基础检查 | 默认 4–7 个徽章及固定“优秀 README”启发式未必适合所有项目；lint 不能证明命令、功能和发布声明真实可用 | 仓库根 [MIT](https://github.com/JayRHa/AgentSkills/blob/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/LICENSE) |
| [geekjourneyx `readme-generator`](https://github.com/geekjourneyx/readme-generator/blob/3d6eb09b68978b4f4c98c07c14c30ca77dacc57a/SKILL.md) | README 叙事、最多两张视觉资产、图片压缩、Description/Topics 推荐及可选 GitHub CLI 建议 | 对作品集展示、视觉设计和传播很强 | “100 分”“推荐星级”“趋势 Topics”等目标容易把 README 推向营销化；事实核验需额外加强 | 仓库根 [MIT](https://github.com/geekjourneyx/readme-generator/blob/3d6eb09b68978b4f4c98c07c14c30ca77dacc57a/LICENSE) |
| [tenequm `standard-readme`](https://github.com/tenequm/skills/tree/c0866c58c4c6df579b305a9546a1e7cf4b974358/skills/standard-readme) | 写作模式与审计模式；严格执行 Standard Readme 的章节、顺序、标题、描述、安装、使用和许可证规则 | 规范明确，适合需要一致格式的开源库 | 规范优先于项目真实用户旅程；严格顺序未必适合产品、应用、研究或多语言仓库 | 仓库根 [MIT](https://github.com/tenequm/skills/blob/c0866c58c4c6df579b305a9546a1e7cf4b974358/LICENSE)；市场元数据需单独复核 |

### 官方与通用文档 Skills

| 来源 | 证据 | 判断 |
| --- | --- | --- |
| OpenAI 官方 Skills（旧仓库） | [`openai/skills` 固定提交](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills)，本次扫描 44 个 `SKILL.md` | 旧仓库已 deprecated，并指向 `openai/plugins`；该快照没有 README 专项 Skill；`skill-creator` 是创建 Agent Skill，不是创建项目 README |
| Anthropic 官方 Skills | [`anthropics/skills` 固定提交](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills)，本次扫描 20 个 `SKILL.md` | 没有 README 专项 Skill；[`doc-coauthoring`](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/doc-coauthoring/SKILL.md) 可协作文档、做读者测试，但不会自动建立仓库事实基线 |
| OpenAI Skill 规范 | [`skill-creator`](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md) | 支持用 `SKILL.md`、references、scripts、assets 封装专门流程；强调只加入能改变模型决策的非显然指导，适合做小而专的 README 维护 Skill |

### README 规范与生成工具（不是 Agent Skill）

| 项目 | 类别 | 可借鉴之处 | 不能直接替代的原因 |
| --- | --- | --- | --- |
| [GitHub：About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | 官方平台规范 | README 应回答项目做什么、为何有用、如何开始、如何求助、谁维护；说明 GitHub 的展示位置、相对链接与大小边界 | 是平台说明，不会检查具体仓库或生成内容 |
| [Standard Readme](https://github.com/RichardLitt/standard-readme/blob/0ebca6e613f215dd4111debd512670065e7ecbd8/spec.md) | 社区规范 | 明确章节状态、顺序、短描述、安装、使用、贡献和许可证要求 | 主要为开源库设计，不能证明项目事实或运行命令正确 |
| [ReadmeAI](https://github.com/eli64s/readme-ai/tree/6f507b5f87795799649cfe5eb78d8644f8c2eac8) | CLI/生成工具 | 可扫描本地或远程仓库，支持模板、多模型、Ollama 与离线模式 | 是需要安装和运行的独立工具；LLM 生成仍需事实审查，API 模式还涉及代码上传、密钥和成本边界 |
| [Best README Template](https://github.com/othneildrew/Best-README-Template) | 人工模板 | 快速获得常见开源项目结构 | 模板不能判断章节是否适用，也不会验证命令、链接和功能声明 |

## 能力矩阵

符号：✅ 明确覆盖；△ 部分覆盖或依赖 Agent 自行发挥；— 未发现明确流程。

| 能力 | pekral | AgentsCamp | JayRHa | geekjourneyx | standard-readme Skill | ReadmeAI 工具 | 拟议增量 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 新建 README | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 审计/增量刷新现有 README | ✅ | ✅ | △ | ✅ | ✅ | △ | ✅ |
| 从 manifest/代码/测试提取事实 | ✅ | △ | ✅ | △ | △ | ✅ | ✅ |
| 保留人工叙事与现有风格 | ✅ | ✅ | △ | △ | △ | — | ✅ |
| 命令/代码示例实际执行验证 | △ | △ | — | △ | △ | — | ✅ |
| 功能、平台、成熟度声明证据分级 | △ | — | — | — | — | — | ✅ |
| 多语言 README 语义对齐 | — | — | — | — | — | △ | ✅ |
| 链接、锚点、图片 alt 基础检查 | ✅ | △ | ✅ | △ | ✅ | △ | ✅ |
| 许可证只按真实文件表述 | ✅ | △ | ✅ | △ | ✅ | △ | ✅ |
| 视觉资产/营销包装 | △ | — | △ | ✅ | — | ✅ | 非 MVP |
| 无外部 API 也可工作 | ✅ | ✅ | ✅ | △ | ✅ | ✅（离线模式） | ✅ |

## 真实缺口

pekral 已经覆盖通用场景里最关键的证据映射、增量修改和副作用边界，因此“证据优先”本身不再是空缺。跨候选仍未被专门、完整覆盖的是：

1. **交付声明的分层证据**：README 中“已支持”“可发布”“跨平台”“安全”“性能”等陈述，需要分别追到代码、测试、构建产物、工作流或正式发布，而不是只建立普通 claim → source 链接。
2. **成熟度边界**：把已验证、Preview、Roadmap、Blocked、未验证分开，避免把配置接缝或计划写成已交付能力。
3. **增量维护**：默认保存作者声音、品牌、截图和历史说明，只替换过时事实；先报告差异，再按授权修改。
4. **多语言一致性**：双语 README 的功能、命令、链接、版本和成熟度必须对齐，但文案可以自然本地化，不能机械逐句翻译。
5. **可运行验证**：README 中的安装/启动/测试命令至少与仓库脚本一致；高风险或核心路径应实际运行最小验证，并如实记录未运行项。
6. **许可证与来源边界**：不能因为仓库公开或 README 写着 MIT，就自动替用户新增 MIT；必须读取真实 LICENSE、版权和第三方素材来源。
7. **去营销化**：视觉、徽章、Topics、社会证明只能服务理解，不能生成虚构指标、夸大推荐或掩盖未交付状态。

这组缺口与“文笔好不好”关系不大，属于可复用的工程判断；但应先验证它们是否能作为 pekral Skill 的项目级补充规则解决，再决定是否单独固化。

## 是否创建：建议与最小 MVP

### 建议

**当前不建议从零创建。先采用并试跑 pekral `github-readme-generator`；满足不了再做窄扩展。**

先用 2–3 个真实仓库做试运行，并保留原 Skill 的 MIT 许可证与来源证据。如果一段项目级补充约束就能稳定满足需求，则停止开发。只有当它在双语一致性、成熟度或发布证据上重复失败时，才把差异固化为独立 Skill；若复用其文本、references 或测试，应按 MIT 保留版权与许可声明，并在 provenance 中标明修改。

### 最小 MVP 边界

增量 MVP 用一个 `SKILL.md` 足以开始；复用现有 Skill 能力，没有重复机械工作前，不加脚本、模板库、图片生成、GitHub API 或发布自动化。

MVP 只做四件事：

1. **发现**：读取仓库规则、现有 README、manifest/锁文件、入口、公共 API、测试、CI、LICENSE、发布配置及必要 Git 状态。
2. **建账**：为重要 README 声明建立 `声明 → 证据 → 状态` 小表；无证据则降级表述或标为未知，不补想象。
3. **写/改**：按受众和项目类型选择必要章节；默认增量更新并保护人工内容；需要时同步多语言 README。
4. **验证**：复查路径、链接、锚点、图片 alt、脚本名、版本、许可证；实际运行仓库已有的最小文档/示例检查；分开报告 passed、failed、blocked、not run。

明确不进入 MVP：

- 自动生成 Logo、封面、架构图或 GIF
- 自动创建许可证、徽章、Topics、GitHub Description
- 自动 commit、push、发布或调用付费模型
- 为每种语言维护独立模板
- 以统一评分代替项目受众与证据判断

### MVP 成功标准

- 在“无 README”“README 陈旧”“双语 README 不一致”三类样例上分别试跑。
- 输出中不存在无法指向仓库证据的功能、命令、版本、平台或许可证声明。
- 对一个已有品牌化 README，修改集中在真实过时部分，不把它重写成通用模板。
- 新读者仅靠 README 能完成一条经过验证的最短上手路径；无法验证时明确写出限制。

## 风险与护栏

| 风险 | 常见失败 | 最小护栏 |
| --- | --- | --- |
| 幻觉 | 根据依赖、文件名或 Roadmap 猜测功能已实现 | 重要声明必须有源码/测试/产物/发布证据；否则降级或标未知 |
| 仓库事实漂移 | README 命令、版本、目录、平台支持落后于代码 | 每次从当前 worktree 和 manifest 重建事实；修改后运行现有 docs 检查 |
| 许可证误写 | 自动补 MIT，或把上游 Skill 的 MIT 当作目标项目许可证 | 只读取目标仓库实际 LICENSE/版权；缺失时说明未授权，不替用户选许可证 |
| 营销化 | 堆徽章、虚构指标、生成“推荐星级”、把 Preview 写成 Stable | 不生成不可验证社会证明；首屏先回答对象、用途、边界和最短路径 |
| 破坏人工内容 | 全量套模板，丢失品牌、说明、历史和有效链接 | 默认 audit + surgical update；重写前展示将保留/删除/新增的内容 |
| 多语言漂移 | 一份 README 更新功能，另一份仍保留旧命令或夸大声明 | 对事实字段做逐项对齐检查，文案允许本地化而非逐句复制 |
| 隐私与凭据 | 把本地绝对路径、日志、用户名、token 或私有端点写入公开 README | 公开前扫描敏感信息；命令使用占位符；不展示原始私密日志 |
| 外部执行副作用 | 为验证 README 自动部署、发布、改 GitHub 设置 | 验证默认本地、只读或使用现有安全命令；外部变更继续单独授权 |

## 最终判断

“帮别人写 README”已有可用 Skill，其中 pekral 已经把 README 当作可验证的工程入口来维护。当前最省事且风险最低的动作是先采用、审计并试跑它，而不是新建同类项目。对拾学、Meow Starter 及未来需要双语、成熟度和发布证据的开源项目，只有真实试跑证明这些差异反复存在时，再创建一个小型增量 maintainer；MVP 只需一个经过真实样例验证的 `SKILL.md`。

## 调研边界

- 官方仓库与社区仓库会继续变化；本文用固定提交链接保存本次证据快照。
- “没有官方 README 专项 Skill”只表示在上述固定提交的 `SKILL.md` 树中未发现，不等于不存在未公开、市场私有或之后新增的能力。
- 本文没有安装或执行任何第三方 Skill，也没有提交、推送或修改仓库 README。
