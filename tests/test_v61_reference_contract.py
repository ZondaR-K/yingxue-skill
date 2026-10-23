"""Regression checks for the *structure* of the v6.2 Yingxue skill.

These tests do not test whether a joke is funny. Use evals/ablation-v6.1.md
for blinded human comparisons.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReferenceContractTests(unittest.TestCase):
    def test_main_entry_stays_short(self):
        self.assertLessEqual(len((ROOT / "SKILL.md").read_text(encoding="utf-8")), 1300)

    def test_three_modes_remain_available(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for mode in ("生成", "拆解", "陪练"):
            self.assertIn(mode, entry)

    def test_all_public_sources_exist_and_are_named_in_entry(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        sources = (
            "references/zy-six-originals.md",
            "references/observed-humor-cases.md",
            "references/comic-persona.md",
            "examples/approved-original-demo.md",
        )
        for path in sources:
            with self.subTest(source=path):
                self.assertIn(path, entry)
                self.assertTrue((ROOT / path).is_file())

    def test_original_approved_example_is_complete(self):
        text = (ROOT / "examples/approved-original-demo.md").read_text(encoding="utf-8")
        self.assertIn("诺贝尔先生去世得太早", text)
        self.assertIn("蒸馏孙哥的钱", text)

    def test_six_full_text_samples_are_public_and_loaded(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        path = "references/zy-six-originals.md"
        self.assertIn(path, entry)
        text = (ROOT / path).read_text(encoding="utf-8")
        for phrase in ("独自长高", "千万要开心", "拨乱了他的心弦", "为了这个账号"):
            self.assertIn(phrase, text)
        self.assertNotIn("不需要另装私人研究包", text)

    def test_reply_keeps_real_publishers_identity(self):
        reply = (ROOT / "workflows/reply.md").read_text(encoding="utf-8")
        self.assertIn("用户本人", reply)

    def test_eval_has_real_ablation_groups(self):
        eval_doc = (ROOT / "evals/ablation-v6.1.md").read_text(encoding="utf-8")
        for group in ("A｜", "B｜", "C｜", "D｜"):
            self.assertIn(group, eval_doc)


if __name__ == "__main__":
    unittest.main()
