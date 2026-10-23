"""Regression checks for the *structure* of the v6.1 Yingxue skill.

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

    def test_private_full_text_never_required_for_public_install(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/private/zy-six-originals.md", entry)
        self.assertIn("不存在则继续", entry)
        ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("references/private/", ignored)

    def test_reply_keeps_real_publishers_identity(self):
        reply = (ROOT / "workflows/reply.md").read_text(encoding="utf-8")
        self.assertIn("用户本人", reply)

    def test_eval_has_real_ablation_groups(self):
        eval_doc = (ROOT / "evals/ablation-v6.1.md").read_text(encoding="utf-8")
        for group in ("A｜", "B｜", "C｜", "D｜"):
            self.assertIn(group, eval_doc)


if __name__ == "__main__":
    unittest.main()
