# 颖学 Skill v6.1

**输出 · 拆解 · 陪练**｜先看真正有意思的作品，再让有趣的人物开口。

从用户提供的六篇曾颖作品中研究一种「一本正经地荒唐」的**文本喜剧人格**，帮助创作原创中文幽默、分析笑点与互动练习。虚构角色不等于曾颖现实中的性格；生成内容不可冒充本人发言。

## 调用方法

| 要做什么 | 直接怎么说 |
| --- | --- |
| 写推文或故事 | `用颖学生成：写一个……` |
| 回复评论 | `用颖学回复：曾颖是个有趣的娘们` |
| 拆解幽默 | `用颖学拆解：这句话为什么好笑？` |
| 自由对练 | `用颖学陪练：跟我聊天，练习接梗` |
| 系统训练 | `用颖学训练：一题一题练幽默表达` |

支持显式 Skill 的客户端可用 `/yingxue`（Claude Code）或 `$yingxue`（Codex），后面接对应任务。普通聊天里打字「用颖学」**并不能证明**完整仓库被加载。

## v6.1 做了什么

- `SKILL.md` **大幅缩短**；三种模式保留，生成默认为人物思维。
- 生成前**必须读取** `references/observed-humor-cases.md`（六篇作品的逐篇研究）、`references/comic-persona.md`（虚构喜剧人物卡）、`examples/approved-original-demo.md`（最初获用户认可的**原创全文**）。
- `workflows/create.md` 与 `workflows/reply.md` 只管相应题型，避免向模型灌大量失败段子、对仗禁令和强制反转步骤。
- 本地另可安装**私人研究包**：`references/private/zy-six-originals.md` 和 `references/private/zy-original-analysis.md`。它们包含用户提供的完整原文与早期分析，**不会上传本公开 GitHub 仓库**；现有公共研究文件可在没有私有包时正常使用。
- 结构检查与读者笑感是不同指标。真实提升请用 `evals/ablation-v6.1.md` 的 A/B/C/D 对照实验判断。

## 目录怎么理解

```text
yingxue/
├── SKILL.md                          # 唯一入口，模式和加载指令
├── references/
│   ├── observed-humor-cases.md       # 公开的六篇逐篇分析
│   ├── comic-persona.md              # 人物声音和心理
│   └── private/                      # 仅在本地放个人研究原文
│       ├── zy-six-originals.md
│       └── zy-original-analysis.md
├── examples/
│   └── approved-original-demo.md     # 最初被用户认可的原创全文
├── workflows/
│   ├── create.md                     # 长文和推文
│   ├── reply.md                      # 短评论
│   ├── analyze.md                    # 拆解
│   ├── roleplay.md                   # 虚构人物对话
│   └── coach.md                      # 系统训练
└── evals/
    └── ablation-v6.1.md              # 同模型对照实验方案
```

**放置原则：** `references/` 是研究素材与人物资料；`examples/` 放经用户认可、可作为创作参照的范文；`assets/` 更适合静态素材或模板，目前不必为了凑目录而创建。

## 安装或更新

把下面这段交给能访问 GitHub 并能写入本地文件的 Claude Code / Codex：

> 将 https://github.com/ZondaR-K/yingxue-skill 安装/更新为本地 Skill。先检查我已有安装路径和未提交修改；不要覆盖个人文件；验证上述三个公共研究文件与五个 workflow 都可读取。若我随后提供私有研究 ZIP，再将其 `references/private/` 目录合并到 Skill 根目录并验证两个文件；最后告诉我实际读到的文件路径。不要声称结果已通过真人好笑度评测。

本地首次安装示例：

```bash
# Claude Code
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.claude/skills/yingxue
# Codex 可安装在 ~/.agents/skills/yingxue
```

已克隆仓库，确认没有本地修改后执行 `git pull --ff-only`。更新后开启**新会话**，再通过工具的文件读取记录核对 Skill 是否真的加载。私人资料 ZIP 解压后文件应位于 `yingxue/references/private/`。

## 验证方式

至少比较四组：**A** 普通模型、**B** 仅公共 v6.1、**C** 原始六篇＋早期分析、不用 Skill、**D** Skill＋完整私人上下文。固定模型、题目、篇幅和采样参数，按原先长篇题与新短评题分别多次生成，再由人匿名选哪个真的好笑。

**尚未完成该盲评，不宣称 v6.1 恢复了原始喜剧效果。** 此 Skill 独立开发，不代表曾颖本人合作、授权或代言。公开仓库不完整转载其作品。
