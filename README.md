# 颖学 Skill

**An Agent Skill for Chinese Humor Generation, Analysis & Practice**

> 正经研究幽默，严肃对待胡说八道。

这是一套适用于 Claude Code、Codex 等兼容 Agent Skills 工作流的中文幽默创作方案。侧重**语境理解 → 机制规划 → 多候选生成 → 批评修订 → 人类反馈**；同时提供标准化数据格式、离线校验和评测汇总工具。

**功能边界：**这是可阅读的指令 Skill 与轻量 Python 工具链；没有训练模型参数，没有集成外部推理 API，没有经过证明的幽默胜率，也没有官方授权或代言关系。

## Quick start

1. 将仓库目录放到所用 Agent 产品支持的 Skill 路径（不同产品路径和发现机制可能不同）。
2. 让智能体读取 `SKILL.md`，输入如：`把“我今天又加班了”改写成两条一本正经的荒诞幽默，避免讽刺具体同事。`
3. 若在本机校验项目：

```bash
python scripts/validate_dataset.py evals/dataset.jsonl
python scripts/validate_dataset.py examples/candidates.json
python scripts/score_candidates.py examples/candidates.json
python scripts/summarize_ratings.py evals/example-ratings.csv
python -m unittest discover -s tests -v
```

不要求安装第三方 Python 包。

## Architecture

```text
User context
  → audience + boundaries
  → humor mechanism selection
  → 3–5 divergent drafts
  → semantic / rhythm / safety critique
  → compact rewrite
  → user feedback
```

`SKILL.md` 是按需加载的入口；`references/` 用来解释机制，`workflows/` 定义行为流程；`schemas/` 约束记录结构；`scripts/` 仅执行数据校验、启发式文本分析及人工评分汇总。

## Evaluation principles

- **3-way comparison:** 直接生成 / 简短“幽默化”指令 / 本 Skill，使用相同任务、相同模型与采样设置。
- **Blind rating:** 将不同来源候选随机排序、隐藏组别，邀请多位受试者分别评价好笑程度、自然度和边界恰当性。
- **Report uncertainty:** 报告样本量、均值、方差、个体差异和失败案例。无真实实验结果时不做胜率宣称。
- **Offline checks:** 字数、意外转折标志、末句长度等只用于诊断，不能充当真人觉得好笑的证据。

## Structure

- `references/`: comedy mechanisms, style, recurring characters, research notes
- `workflows/`: generation, rewriting, analysis, coaching, critique
- `schemas/`: JSON Schema contracts
- `evals/`: evaluation rubric, prompts, example rating data
- `examples/`: original fictional jokes and structured candidate examples
- `scripts/`: validators and evaluation utilities
- `tests/`: regression tests
- `.github/workflows/`: standard-library test CI

## Ethical use

灵感来自公开文本中可普遍分析的幽默手法；不复制第三方作品，不冒用作者身份，不捏造真人经历。使用作品或角色名称时请尊重署名和适用法律。**样例数据为合成演示，绝不代表基准结果。**

## License

MIT for repository code and original prose. Third-party quotes, names, and trademarks are not included in the license grant.
