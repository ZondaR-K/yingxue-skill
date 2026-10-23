# 颖学 Skill v4.2

**让 AI 帮你输出幽默、拆解幽默、训练幽默。**

**v4.2 核心修复：** 解决“以前写得好笑，后来 Skill 只有理论却写不出来”的几个已发现缺口：`SKILL.md` 内置完整创作引擎，保留最初 v1 人物欲望与荒诞推理；新增[六类原作幽默结构研究](./references/observed-humor-cases.md)，另有[用颖学介绍颖学的原创候选范例](./examples/hero-demo.md)。现有[原创示例库](./examples/original-examples.md)统一标注为**待用户验证的候选**，不能自称经测试的高质量语料。

> 正经研究幽默，严肃对待胡说八道。

颖学是一套中文幽默创作与训练 Skill。从一本正经的荒诞推理、预期违背、人物姿态、语义转换中提炼创作方法。**输出作品是第一优先级**：用户只想发个好笑的评论时，直接拿到可用文本；需要理解或提高能力时，再进入拆解与训练。

## 🎭 三种能力，三种用法

| 模式 | 用途 | 安装后直接输入 |
| --- | --- | --- |
| **① 输出** | 写搞笑评论、推文、微信回复、朋友圈、故事、幽默改写 | `用颖学输出：帮我搞笑地回复“你怎么天天加班？”` |
| **② 拆解** | 拆出一句话为什么好笑、用了什么转折、哪些词关键 | `用颖学拆解：“这句话……”为什么好笑？` |
| **③ 训练** | AI 当教练，一次一题，等你回答再反馈修改 | `用颖学训练：我想提高日常聊天的幽默感。` |

无需记住固定命令：`用颖学帮我评论这条推文` 会自动进入**输出**；`用颖学分析这个梗` 进入**拆解**；`用颖学陪我练习反转` 进入**训练**。显式说“输出 / 拆解 / 训练”更精确。

### 输出：直接拿成品

输入：`用颖学输出：我做了一篇研究幽默的文章，结果阅读量只有 20，帮我写一段搞笑的自嘲。`

输出（原创示例）：

> 文章发表三天，学术界始终保持沉默。
>
> 我原本很失落，后来想通了。
>
> 这么重大的理论突破，同行们一时接受不了，也是人之常情。
>
> 唯一让我困惑的是，后台统计显示只有二十个人看过，其中十八个还是我自己。

你还可以说：`用颖学写 10 条不同角度的评论，每条不超过 40 字，不要解释。` 输出遵守字数、数量、平台与修改范围；不默认追加笑点分析。

### 拆解：把好笑变成可以理解的技巧

输入：`用颖学拆解：为什么“他竟然选择了独自长高”这么好笑？`

得到：正常情境中的身高误报，被叙述者严肃地解释成爱情背叛。“独自”从共同面对命运的爱情语境被移到“长高”，形成具体的语义错位。还能学到如何把琐事放进不相称的宏大解释框架。

### 训练：自己练出幽默感

输入：`用颖学训练：练习一句话神转折。`

颖学会先出**一道题**，例如“朋友问你怎么又迟到了”，让你从外交谈判的角度写一句话。你答完，它才指出有效的点、最需要改进的一点、最小修改和另一种示范，再继续下一轮。还可指定“训练聊天 / 推文 / 自嘲 / 荒诞推理”。

## ✅ 先用三种方式试验

```text
/yingxue 输出：把今天又错过健身计划写成一个荒诞的短故事。
/yingxue 拆解：为什么“一本正经地把小事写成大事”会好笑？
/yingxue 训练：陪我练习一句话神转折，一题一题来。
```

上面是 Claude Code 等支持斜杠 Skill 客户端的形式。Codex 的相应前缀一般为 `$yingxue`；也可以用普通自然语言「使用颖学 Skill，输出……」，前提是客户端确实识别了已安装 Skill。

**重点回归题：**

```text
使用颖学 Skill 的输出模式：请从一位虚构、对自己幽默才华极其自信的写作者视角，写一篇“我发现别人把我的幽默研究做成了 AI Skill”的自我介绍。让他和开发者争论才华、尊严、版权和商业利益；事件至少升级三次，最后回到一个具体而荒唐的现实后果。约 400 字，不要说明写作手法。
```

若效果仍然普通，把**实际成品、使用模型、客户端、加载到的文件列表**留下，和上一次版本在相同题目下比较。见[复现实验说明](./evals/humor-reproduction.md)。

## ⚡ 安装：把这段话复制给 Claude Code 或 Codex

> 请帮我安装并验证这个 Agent Skill：https://github.com/ZondaR-K/yingxue-skill
>
> 阅读 README.md 和 SKILL.md，确定本机工具支持的个人 Skill 目录，获取完整仓库并保留 workflows/、references/、examples/、evals/ 等目录。若发现旧版本，先提示并更新现有安装，注意不覆盖用户修改。检查三个入口（输出、拆解、训练）引用的文件均存在，特别确认 references/observed-humor-cases.md 与 examples/hero-demo.md 已安装，并告知安装后如何调用。

也可以手动安装：

**Claude Code（macOS / Linux 终端）**
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.claude/skills/yingxue
```

**Codex（macOS / Linux 终端）**
```bash
mkdir -p ~/.agents/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.agents/skills/yingxue
```

安装后的示例：

```text
使用 yingxue Skill：输出一条幽默的 X 评论
使用 yingxue Skill：拆解这段笑话的转折
使用 yingxue Skill：陪我练习聊天幽默
```

在支持显式 Skill 引用的 Codex 环境中，也可以试：`$yingxue 用输出模式帮我写评论`。具体语法以当前客户端为准。

### 已安装旧版，怎样更新？

进入原先克隆的目录执行 `git pull --ff-only`（前提是无未提交本地改动）。例如：

```bash
cd ~/.claude/skills/yingxue
git pull --ff-only
```

Codex 把路径换成 `~/.agents/skills/yingxue`。Windows PowerShell 使用个人用户目录中对应的 `.claude/skills/yingxue` 或 `.agents/skills/yingxue` 路径。重开对话或重启客户端，以便 Skill 发现机制重新加载。

**GitHub 更新不等于客户端里的 Skill 自动更新。** 必须确认本地目录已经拉取到最新版，且当前会话确实加载了 Skill。

### Claude 网页版：ZIP 导入

1. GitHub 页面选择 **Code → Download ZIP**。
2. 若所用 Claude 版本支持自定义 Skills，在对应设置中上传 ZIP。
3. 如果系统要求 ZIP 根目录直接包含 `SKILL.md`，先解压再把仓库内容重新压缩。
4. 新对话里通过“三种用法”的例句调用。

是否支持、入口与权限以当前产品界面为准。

### 想在普通 ChatGPT / 其他聊天模型试试

普通聊天模型不会因为你在 GitHub 上传文件就自动拥有 Skill。可复制 `SKILL.md` 和对应 `workflows/`、`references/` 的内容作为上下文，或在支持自定义技能的工具里导入完整仓库。只复制入口文件时，部分细节规则不会被加载。

## 🧠 为什么是这套方法？

输出的关键在于：**现实锚点 → 不相称的解释框架 → 一本正经的人物 → 荒诞但自洽的因果升级 → 意料之外的收尾**。

拆解则反向研究这些环节。训练用具体场景反复练习，从“看得懂”进步到“自己写得出”。

三种模式共享幽默机制，但相互隔离：**输出时不自动讲理论，拆解时不替你抢答，训练时让你先尝试。**

## 📁 项目结构与评估

- `SKILL.md`：三模式路由、核心输出原则。
- `workflows/create.md`：恢复 v1 荒诞创作能力，覆盖短评、推文、故事。
- `workflows/analyze.md`：拆解预期、解释转弯与迁移方法。
- `workflows/coach.md`：逐轮练习、反馈和递进。
- `references/`：幽默机制、文风、人物及固定笑梗。
- `references/observed-humor-cases.md`：最初六则作品的机制性研究梗概（不复制原文）。
- `examples/original-examples.md`：各篇幅的 AI 原创候选与反例，**尚未经真人验证**。
- `examples/hero-demo.md`：“用颖学介绍颖学”的长篇原创复现参考稿（待盲测）。
- `evals/rubric.md`、`evals/three-modes-regression.md`：三模式人工评估与防退化测试。
- `evals/humor-quality-ab.md`、`evals/humor-reproduction.md`：对比无 Skill、旧 Skill、当前 Skill 的人工对照实验设计，**尚未完成真人盲测**。
- `tests/test_yingxue_contract.py`：检测路由、文件依赖、示例与文档是否齐全的结构性回归测试。
- `scripts/`、`tests/`：原有格式与校验工具。

本地 Python 3.10+ 可运行：

```bash
python scripts/validate_dataset.py evals/dataset.jsonl examples/candidates.json
python scripts/score_candidates.py examples/candidates.json
python scripts/summarize_ratings.py evals/example-ratings.csv
python -m unittest discover -s tests -v
```

**仓库更新不等于你本地安装的 Skill 自动更新。** 已安装用户需要重新拉取或导入，并新开会话验证版本及示例文件已加载。

**自动化测试只检查文件、模式、关键规则，无法证明用户会笑。** 目前尚无可信的提升百分比；真正的幽默质量需要同条件人评与实际发布反馈。

代码测试通过不代表笑话一定好笑。比较效果时最好保持相同模型、温度、提示与上下文，使用人工匿名评分记录好笑程度、意外程度、自然度和使用意愿。

## 🤝 关于署名与授权

颖学是独立的幽默学习与创作方法，灵感来自对中文幽默表现手法的分析；与曾颖本人没有官方合作或授权。使用第三方作品时请遵守署名及版权要求，不将生成文字冒充真人原话，也不编造真人负面事实。

## License

MIT License，详见 [LICENSE](./LICENSE)。
