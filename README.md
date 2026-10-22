# 颖学 Skill

**让 AI 学会一本正经地胡说八道。**

> 正经研究幽默，严肃对待胡说八道。

颖学是一套中文幽默创作与练习 Skill。可以用来写有趣的聊天回复、改写文字、创作搞笑故事，也可以帮你分析笑点、练习反转、自嘲和 Running Gag。

它整合了预期违背、语义转换、夸张反差、良性冒犯等幽默技巧，并提供创作、分析、改写和陪练流程。

## 🎭 能拿来干什么？

| 场景 | 你可以这样说 |
| --- | --- |
| 微信聊天 | “朋友问我怎么天天加班，帮我想一句好笑又不油腻的回复。” |
| 幽默改写 | “把‘今天又赖床了’改得一本正经又离谱，给我 3 种思路。” |
| 搞笑创作 | “把我点外卖失败的经历写成一次重大外交危机。” |
| 分析笑点 | “这句话为什么好笑？帮我拆解预期、反转和节奏。” |
| 练习幽默 | “你当我的幽默教练，出一道日常聊天题，我先回答，你再点评。” |
| 连续笑梗 | “设计一个自称文学大师的虚构角色，让他的固定笑梗每次都能变出新花样。” |

## ⚡ 把这段话发给 Claude Code / Codex，帮你安装

如果你正在使用具备终端和文件操作能力的 Claude Code、Codex 等工具，可以直接复制下面这段话给它，让它检查环境并安装，**不必自己研究文件路径**：

> 请帮我安装这个 Agent Skill：https://github.com/ZondaR-K/yingxue-skill
>
> 先阅读仓库的 README.md 和 SKILL.md，确认当前工具支持的个人 Skills 安装目录。获取完整仓库并安装，保留 references/、workflows/ 等所有文件。检查 SKILL.md 是否处在正确位置、引用文件是否完整，并告诉我安装后该如何调用。不要覆盖已有同名 Skill；需要权限时请先提醒我。

安装完成后，试试说：

> 使用颖学 Skill，把“我今天又加班了”写成三个好笑又自然的版本。

**提示：** AI 编程工具需要能访问 GitHub 并有本地文件写入权限。Claude 网页对话不一定能直接执行本地安装，可按照后面的网页版导入方式操作。

## 🚀 其他安装与体验方式

### 方法一：不安装，先体验

1. 打开 [SKILL.md](./SKILL.md)，复制文件中的内容。
2. 粘贴到你正在使用的 AI 对话里。
3. 告诉 AI：“请遵循上述颖学 Skill 的规则，帮我写一段幽默内容。”

这是快捷体验方式。完整功能涉及其他规则文件，推荐按下方步骤安装整个项目。

### 方法二：Claude 网页版

1. 点击 GitHub 页面右上角 **Code → Download ZIP**。
2. 在支持自定义 Skills 的 Claude 中，进入相应的 Skills 设置入口，上传 ZIP。
3. 新建对话，提出幽默创作、改写或练习请求即可。

具体上传入口、可用性和权限以 Claude 当前界面为准。若上传要求 ZIP 根目录包含 `SKILL.md`，请先解压下载的仓库，再将文件夹内所有内容重新压缩，确保包的根目录直接是 `SKILL.md`、`references/`、`workflows/` 等。

### 方法三：Claude Code

将完整仓库复制到个人 Skill 目录：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.claude/skills/yingxue
```

之后在 Claude Code 中试试：

```text
使用 yingxue Skill，把“我减肥又失败了”写成一段一本正经的搞笑故事。
```

如果原目录已存在，请在目录里执行 `git pull`，不要重复克隆。Claude Code 会根据请求内容和 Skill 描述判断何时使用，也可在支持的客户端中显式调用。

### 方法四：Codex

将项目放到 Codex 的个人 Skills 目录：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.agents/skills/yingxue
```

然后在 Codex 中使用：

```text
$yingxue 帮我写三个轻松有趣的微信聊天回复，不要刻意抖机灵。
```

部分客户端需要重新打开会话以加载新 Skill。Windows 用户可以将 `~` 理解为当前用户主目录，并使用 PowerShell 或 Git Bash 安装 Git。

## ✍️ 试试这些提示词

**直接创作**

> 帮我把今天上班迟到的经历写成一份严肃的新闻通稿，要有明确笑点，不要硬凑金句。

**日常聊天**

> 朋友说“你最近怎么越来越宅了”，帮我想 5 种自然又有趣的回答，别太油腻。

**练习反转**

> 给我出 5 道“先建立预期，再突然转弯”的练习题，我先写结尾，你再点评。

**看懂别人的幽默**

> 分析这句话为什么好笑，指出铺垫、意外转折和人物语气；最后告诉我可以借鉴什么。

## 🧠 工作原理

```text
理解用户意图、受众和语境
  → 选择幽默机制
  → 生成不同角度的候选
  → 检查自然度、逻辑和分寸
  → 精简与修订
  → 输出或陪练反馈
```

项目包含：

- `SKILL.md`：技能入口和调用规则。
- `references/`：幽默机制、风格、人设、Running Gag 与参考笔记。
- `workflows/`：生成、改写、分析、陪练、批评修订。
- `examples/`：原创示例与结构化候选。
- `schemas/`：结构化数据规范。
- `evals/`：评价规则、练习样例与评测设计。
- `scripts/`、`tests/`：辅助校验工具、自动化测试。

## 🔧 开发与测试

创作时通常无需运行任何脚本。下面这些命令面向希望研究或改进项目的开发者，使用 Python 3.10+ 标准库：

```bash
python scripts/validate_dataset.py evals/dataset.jsonl examples/candidates.json
python scripts/score_candidates.py examples/candidates.json
python scripts/summarize_ratings.py evals/example-ratings.csv
python -m unittest discover -s tests -v
```

其中的分数与示例仅用于检查格式、展示评测方式；真实幽默效果仍需结合具体语境和人的反馈判断。

## 🤝 一起完善颖学

如果你发现了特别好笑的表达、遇到明显不好笑的生成结果，或对幽默机制有新的理解，欢迎通过 Issue 和 Pull Request 一起改进。

本项目为独立创作的幽默学习与创作工具；与曾颖本人不存在官方合作或授权关系。请勿将 AI 创作内容冒充真实人物的原话。

## License

MIT License，详见 [LICENSE](./LICENSE)。
