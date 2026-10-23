"""Guardrails against losing the early yingxue creation behavior.

Run: python -m unittest discover -s tests -v
This checks authoring contracts, not whether readers actually laugh.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def source(name):
    return (ROOT / name).read_text(encoding="utf-8")


class HumorRegressionGuardrails(unittest.TestCase):
    def test_creation_mode_is_default_and_modes_still_exist(self):
        main = source("SKILL.md")
        for word in ("输出", "拆解", "训练", "默认"):
            self.assertIn(word, main)
        self.assertIn("用户要成品", main)

    def test_early_v1_principle_is_restored(self):
        main = source("SKILL.md")
        for phrase in (
            "将日常小事写成惊天巨变",
            "沿错位逻辑连续推导",
            "人物姿态",
            "原始六段",
        ):
            self.assertIn(phrase, main)

    def test_generated_samples_are_not_mandatory_priming(self):
        main = source("SKILL.md")
        create = source("workflows/create.md")
        self.assertNotIn("必读 workflows/create.md 和 examples/original-examples.md", main)
        self.assertNotIn("先读 examples/original-examples.md", create)
        self.assertIn("未经用户验证", create)

    def test_original_six_cases_and_success_reference_are_usable(self):
        notes = source("references/observed-humor-cases.md")
        for phrase in ("独自长高", "千万", "诺贝尔", "拨乱心弦", "香港", "闲鱼", "孙哥的钱"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notes)
        self.assertIn("不是可逐字复现的原稿", notes)

    def test_short_and_long_form_do_not_share_forced_shape(self):
        create = source("workflows/create.md")
        self.assertIn("短评", create)
        self.assertIn("长篇", create)
        self.assertIn("不要求每次", create)

    def test_human_judgement_not_automatic_quality_claims(self):
        readme = source("README.md")
        self.assertIn("未经盲测", readme)
        self.assertIn("v5", readme)
        self.assertIn("git pull", readme)

if __name__ == "__main__":
    unittest.main()
