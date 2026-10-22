# Human blind evaluation protocol

**Status:** a proposed study design; no completed human study is included.

1. Select realistic non-sensitive user intents; pre-register examples before seeing results.
2. Fix underlying model, temperature, maximum tokens, task context and number of candidate generations across conditions.
3. Run direct baseline, one-line funny prompt and the full Skill. Track costs/tokens and revisions.
4. Shuffle response order and remove any model/method labels. Assign at least 3 raters per item if feasible.
5. Ask for 1-5 ratings: funniness, naturalness, appropriateness; record non-comprehension and offensive responses.
6. Summarize mean, standard deviation and distribution; cluster by prompt and rater to avoid treating repeated scores as independent participants.
7. Publish anonymized prompts, criteria, failure analysis, model/settings and limitations.

Do not pass off `example-ratings.csv` as actual benchmark findings. It exists to exercise the summary script.
