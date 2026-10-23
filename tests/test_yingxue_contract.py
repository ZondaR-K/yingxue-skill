"""Structural contract tests for 颖学 Skill.

These tests check routing, dependencies and known regressions.
They DO NOT prove that a generated joke is funny.
Run: python -m unittest discover -s tests -v
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class YingxueContractTest(unittest.TestCase):
    def test_entry_file_declares_three_modes(self):
        text = read("SKILL.md")
        for name in ("输出", "拆解", "训练"):
            with self.subTest(mode=name):
                self.assertIn(name, text)
        self.assertIn("name: yingxue", text)

    def test_creation_can_work_without_optional_references(self):
        text = read("SKILL.md")
        for token in ("抓活的事实", "找人物的执念", "连续推导", "结尾与克制"):
            with self.subTest(token=token):
                self.assertIn(token, text)
        self.assertIn("即使额外文件未加载也必须执行", text)

    def test_mode_files_are_present_and_have_distinct_output_contracts(self):
        create = read("workflows/create.md")
        analyze = read("workflows/analyze.md")
        coach = read("workflows/coach.md")
        self.assertIn("输出只交付成品", create)
        self.assertIn("预期", analyze)
        self.assertIn("一轮一题", coach)

    def test_original_research_is_separate_from_generated_samples(self):
        source = read("references/observed-humor-cases.md")
        samples = read("examples/original-examples.md")
        hero = read("examples/hero-demo.md")
        self.assertIn("六类已观察到的幽默结构", source)
        self.assertGreaterEqual(source.count("## "), 8)
        self.assertIn("尚未获得人工盲评", hero)
        self.assertIn("AI 生成的候选示例", samples)

    def test_original_premise_is_a_test_case(self):
        benchmark = read("evals/humor-reproduction.md")
        self.assertIn("复现原来的舞台", benchmark)
        self.assertIn("陌生迁移", benchmark)
        self.assertIn("控制变量", benchmark)
        self.assertIn("尚未", benchmark)

    def test_skill_calls_and_update_steps_documented(self):
        readme = read("README.md")
        for token in ("/yingxue", "$yingxue", "输出", "拆解", "训练", "git pull --ff-only"):
            with self.subTest(token=token):
                self.assertIn(token, readme)
        self.assertIn("v4.2", readme)

    def test_required_references_exist(self):
        paths = [
            "SKILL.md", "README.md", "workflows/create.md",
            "workflows/analyze.md", "workflows/coach.md",
            "references/mechanisms.md", "references/style.md",
            "references/observed-humor-cases.md",
            "examples/original-examples.md", "examples/hero-demo.md",
            "evals/humor-quality-ab.md", "evals/humor-reproduction.md",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
