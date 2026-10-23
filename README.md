# 颖学 Skill v6.2

**生成 · 拆解 · 陪练**。目标：让一个拥有情绪、欲望和荒诞思维的虚构喜剧人物自然说话，创作原创中文幽默。

## 这次的关键变化

**六篇原文直接公开放入仓库，并且成为生成模式的必读资料。** 之前需要手动解压的私人补充包不再是使用新版 Skill 的前提。

生成模式加载顺序：

1. [references/zy-six-originals.md](references/zy-six-originals.md)：用户提供的六篇原文，保留场景、语气和分段。
2. [references/observed-humor-cases.md](references/observed-humor-cases.md)：六篇的幽默心理、语言节奏和叙事分析。
3. [references/comic-persona.md](references/comic-persona.md)：从作品归纳的**虚构**喜剧叙述者画像。
4. [examples/approved-original-demo.md](examples/approved-original-demo.md)：用户最初认可的原创全文《我被蒸馏成 Skill》。
5. 根据任务读取 [workflows/reply.md](workflows/reply.md) 或 [workflows/create.md](workflows/create.md)。

这几个文件**都需要在创作前实际读取**，仅安装或仅看到文件名还不等于完整加载。

## 三个入口

| 模式 | 调用示例 |
| --- | --- |
| 生成（默认） | `用颖学生成：回复“曾颖是个有趣的娘们”` |
| 拆解 | `用颖学拆解：为什么这句话好笑？` |
| 陪练 | `用颖学陪练：和我来回聊天练接梗` |

系统课程式训练继续通过 `用颖学训练` 调用。

## 本地更新

在当前已安装的仓库中，先确认没有需要保存的本地修改，然后执行：

```bash
git pull --ff-only
```

第一次安装可使用 `git clone https://github.com/ZondaR-K/yingxue-skill.git`，放入客户端对应的 Skill 目录。Claude Code 常用 `~/.claude/skills/yingxue`，Codex 常用 `~/.agents/skills/yingxue`。安装后在新会话中确认真正读取了以上资料。

## 关于素材与质量

六篇作品由用户在聊天中提供并要求加入公开仓库，**版权仍属于原作者**，不意味着已有公开转载授权；如有权利争议应按原作者要求处理。其中有现实人物的未经核实的指控，纯作文本修辞研究，切勿当成新闻事实。

早期讨论的分析已整理进研究资料，但不是逐字聊天记录。最初成功的《我被蒸馏成 Skill》是 AI 的原创示范，也不代表曾颖本人言论。

**尚未完成真人盲评，绝不声称这次更新必然更好笑。** 对照实验见 [evals/ablation-v6.1.md](evals/ablation-v6.1.md)。文件存在和模型是否能创造好笑内容，是两道不同的关卡。
