# 颖学 Skill v6.0

**喜剧人格生成 · 幽默拆解 · 角色对练**

v6.0 改造：以曾颖六篇作品中呈现的虚构喜剧叙述者为研究对象，优先学习人物欲望、语言呼吸及自然跑题；补充用户明确认可的早期**原创完整示范** `examples/approved-original-demo.md`；把角色互动对练和结构化课程训练分开。**不会冒充曾颖本人发言。**

一套中文幽默创作与训练 Skill。它从用户研究的六段曾颖作品中提炼可复用机制，重点学习：**人物为什么会一本正经地误读小事，又为什么会突然想到旁人猜不到的私人关切**。不复制原作，也不冒充曾颖本人。

> 正经研究幽默，严肃对待胡说八道。

**v5.1 定点修复：** 用户反馈“已经加载 v5，但评论仍然无聊”。这次从[真实失败回复](evals/comment-replies.md)出发，新增[短评论专用流程](workflows/reply.md)，禁止把复述、工整对偶、普通自嘲误当作强笑点。**长篇创作和短评论分开处理**，每条评论要求有对原话的真实回应与新的观察或意外后果；无法自然产生时允许正常回复，不强行搞笑。

## 先用起来

| 功能 | 直接说 |
| --- | --- |
| **输出幽默**（默认） | `用颖学输出：帮我幽默地回复这条评论……` |
| **拆解幽默** | `用颖学拆解：为什么这段话好笑？……` |
| **角色陪练** | `用颖学陪练：和我来回聊天接梗。` |
| **技巧训练** | `用颖学训练：我想练习一句话反转。` |

如果客户端支持显式 Skill 调用：

```text
# Claude Code
/yingxue 输出：帮我回复……
/yingxue 拆解：这句话为什么好笑？
/yingxue 陪练：和我来回聊天接梗
/yingxue 训练：教我一句话反转

# Codex
$yingxue 输出：帮我回复……
$yingxue 拆解：这句话为什么好笑？
$yingxue 陪练：和我来回聊天接梗
$yingxue 训练：教我一句话反转
```

不同版本的客户端支持情况不同。一般也可以只描述任务，让支持自动识别的环境自行触发 Skill。**直接在普通 ChatGPT 对话中打字“用颖学”，不能证明已经加载了 GitHub 仓库。**

## v6.0 的三个入口

- **生成（默认）**：`用颖学生成：回复这条评论……`。先读 `references/comic-persona.md` 与 `examples/approved-original-demo.md`，长文读 `workflows/create.md`，短评读 `workflows/reply.md`。
- **拆解**：`用颖学拆解：这段为什么好笑？`，依然使用 `workflows/analyze.md`。
- **陪练**：`用颖学陪练：我们聊天练接梗`，进入 `workflows/roleplay.md` 连续对话，只有要求点评/课程时转 `workflows/coach.md`。

**当前状态：** 参考内容和文件结构已更新，尚无同模型、多次生成、真人盲评的幽默质量保证。

## 为什么更新 v5？

**v4.2 存在两个可核对的问题：** 创作规则虽然复杂，却丢失了不少最初 v1 中贴近实际喜剧人物的写法；更严重的是，创作时被引导去读取 AI 自己写的、**未经用户验证**的所谓高质量范例。一个机器人教另一个机器人写笑话，最后两位机器人都觉得自己很幽默，这个流程不够靠谱。

本版修改：

- **恢复 v1 写法的核心：** 小事被庄严解释、具体人物的偏执欲望、荒唐而自洽的连续推理、真事反噬。不是固定的六步模板。
- **允许出乎意料地跑题：** 最初受认可的「用颖学介绍颖学」能从技术、文学绕到美貌和熟人的钱；笑点离开技术领域，但没离开人物的性格。新输出要保留这种意外，而不是总落在 GitHub/Fork/复制之类可预料的技术双关上。
- **优先原始研究：** [六段作品机制与最初成功案例的复盘](references/observed-humor-cases.md)。仅有短摘、梗概和分析；**仓库不包含这六篇作品的完整原稿；最初得到用户认可的原创示范全文现已保存于 `examples/approved-original-demo.md`**。
- **停止默认模仿 AI 候选：** `examples/original-examples.md` 与 `examples/hero-demo.md` 保留供历史复盘，**不作为自动加载的成功范文**。
- **三模式照常保留：** 输出只交付作品；拆解专讲机制；训练先做题再反馈。

### 为什么不承诺“100%恢复”？

截至本次更新，尚未进行同模型、多次采样和真人匿名评分的比较。**本版未经盲测，不声称实际幽默分数已经超过 v1。** 更合适的验证方法是用最初成功的同一道题及完全陌生的新题材，分别测试有无 Skill 与不同版本。详见 [复现实验](evals/humor-reproduction.md)。

## 一句命令安装

把以下内容发给能访问 GitHub 且支持本地文件操作的 Claude Code、Codex：

> 请安装或更新 https://github.com/ZondaR-K/yingxue-skill 的完整 Agent Skill（不要只复制 SKILL.md）；先确认我的 Skill 安装目录。不要覆盖本地未提交的修改。检查 SKILL.md、references/comic-persona.md、examples/approved-original-demo.md、workflows/create.md、workflows/roleplay.md、workflows/analyze.md、workflows/coach.md 均存在，告诉我如何显式调用。

手动安装：

**Claude Code**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.claude/skills/yingxue
```

**Codex**

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/ZondaR-K/yingxue-skill.git ~/.agents/skills/yingxue
```

若本地已克隆，不能再次直接克隆。确认没有待处理的本地修改后，在已有目录中执行：

```bash
git pull --ff-only
```

建议重开对话，以免沿用旧会话已加载的旧规则。Windows 用户使用各客户端对应的用户主目录；也可让 Claude Code / Codex 直接帮你定位。

**Claude 网页版**：若当前产品支持导入自定义 Skill，可下载整个仓库 ZIP 后按照客户端说明导入。ZIP 根目录可能需要直接包含 `SKILL.md`，具体以产品入口为准。

## 立刻测试输出能力

### 老题，复现最初成功场景

```text
使用颖学 Skill，输出一篇有趣的虚构短文《我发现自己被蒸馏成了 Skill》。人物自认为是文学巨匠，认真维护才华、尊严和实际利益；面对开发者，她对技术有很多离谱误会。事件可以不断跑题，但要符合这个人物的心理。400 字左右。不要讲幽默理论，不要照搬已存在的段子。
```

### 新题，检查有没有真正学会迁移

```text
使用颖学 Skill：以一个把自己当成金融天才的普通人视角，把“为了省钱办健身卡却三周没去”写成 220 字有趣小故事。不要提文豪、AI、开源、奖项或 GitHub。
```

### 短评，检查是否能直接发送

```text
使用颖学 Skill 输出：回复“AI 模型更新太快，根本记不住名字”，给我 5 条真正不同思路的评论，每条不超过 35 字，只输出评论。
```

### 两条真实失败案例，复测同一题

```text
使用颖学 Skill 输出：回复评论“幽默自由这个说法戳到我了，我到现在还做不到出口成梗，看来得去读读你这份调查报告。” 要一句有新意、能直接发出去的幽默回复。
```

```text
$yingxue 输出：回复评论“曾颖是个有趣的娘们。”只要一句话，要有原话之外的新观察，别只是说“她负责有趣我负责研究”。
```

**用户之前否定过的输出已经登记为失败基线。** 新候选尚未得到人工好笑度验证，不能宣称自动通过这些案例就“恢复了幽默能力”。

把每次产生的作品与最初作品放到一起，由人匿名选择哪个好笑。测试结构的程序无法代替真实笑感评价。

## 文件说明

- `SKILL.md`：v6.0 入口，生成、拆解、陪练三模式。 
- `references/comic-persona.md`：由公开文本中的喜剧叙述者归纳的虚构人格，不等于作者真实性格。
- `examples/approved-original-demo.md`：最初获得用户认可的原创全文，非曾颖原作。
- `workflows/roleplay.md`：角色持续互动，用户主动要求后才做技巧复盘。
- `workflows/create.md`：长篇、叙事创作细节，禁止将 AI 候选自动当范文。
- `workflows/reply.md`：短评论、聊天回复专用，强调实际回应与新增幽默信息。
- `workflows/analyze.md`：幽默机制拆解。
- `workflows/coach.md`：逐轮幽默训练。
- `references/observed-humor-cases.md`：六段原始研究的机制梗概，及最初成功创作的已知情节点。
- `examples/`：历史创作候选，尚未经过真人认可；非默认输出教材。
- `evals/`：对照实验设计，包括 `evals/comment-replies.md` 的用户真实失败案例。
- `tests/`：规则与文件结构回归检查。可用 `python -m unittest discover -s tests -v` 运行。

## 独立性说明

该项目不隶属于曾颖，也不代表其合作、代言或授权。涉及第三方作品，应遵守相应版权要求。生成内容不能冒称真人原话，亦不能编造真人负面事实。

## License

MIT License，详见 [LICENSE](LICENSE)。
