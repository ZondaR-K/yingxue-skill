---
name: yingxue
description: A Chinese-language humor engineering skill for analyzing, drafting, rewriting and practicing humor with incongruity, benign violation, semantic reframing and recurring-gag continuity. Use when the user requests Chinese comedic writing, punchline improvement, joke analysis, humorous replies, or structured humor practice.
---

# 颖学 | Chinese Humor Engineering

> 幽默自由的技术路线：让意外有逻辑，让表达有分寸。

## Trigger and execution

Identify task type from user intent. Read only relevant references, then act:

| Intent | Load |
|---|---|
| Generate a joke, X post or punchline | `workflows/create.md`, `references/mechanisms.md`, `references/style.md` |
| Rewrite a provided sentence | `workflows/rewrite.md`, `references/style.md` |
| Explain humor | `workflows/analyze.md`, `references/mechanisms.md` |
| Interactive humor practice | `workflows/coach.md`, `evals/rubric.md` |
| Recurring character / running gag | `references/personas-running-gags.md`, `schemas/gag-memory.schema.json` |
| Compare candidate jokes | `evals/rubric.md`, `workflows/critique.md` |

## Generation protocol

1. **Context extraction:** detect setting, relationship, audience, intended reaction and explicit no-go areas. Never invent personal facts.
2. **Mechanism planning:** select 1-2 mechanisms (incongruity, semantic shift, mock-epic, benign violation, character callback).
3. **Diverse candidates:** silently formulate 3-5 alternatives using different mechanisms (unless user specifically requests one minimal edit).
4. **Critique:** evaluate setup-punchline dependency, plausibility, brevity, tone and interpersonal boundaries; see `workflows/critique.md`.
5. **Revision:** cut setup redundancy, shift strongest surprise near the end, avoid self-explaining lines.
6. **Output:** deliver best version; show alternatives only when requested. No fabricated confidence scores.

## Guardrails

- Do not invent facts or defamatory allegations about actual people; distinguish imagined comedic premises from reality.
- Adapt teasing to relationship and situation. Avoid humor targeting someone in acute distress.
- Never represent generated lines as authentic quotes of a living person.
- Follow exact user editing scope: if asked for one sentence, change only that sentence.
- Treat the '颖学' label as a creative framework, not a claim of an author's endorsement, a fine-tuned model, or a measured improvement in humor.

## Optional engineering utilities

Python 3.10+ stdlib scripts in `scripts/` validate dataset and structured outputs, score **surface-level** properties, and summarize human ratings. They do not call an LLM or claim to measure funniness automatically. See `README.md`.
