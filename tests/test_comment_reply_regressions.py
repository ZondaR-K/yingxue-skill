"""Regression checks for user-reported bland short replies.

These assert the *process contracts*. Human readers still judge funny.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


class CommentReplyRegressionTests(unittest.TestCase):
    def test_comment_route_is_distinct_from_long_story(self):
        entry = read("SKILL.md")
        self.assertIn("workflows/reply.md", entry)
        self.assertIn("短评论专用", entry)

    def test_reply_must_add_new_comic_information(self):
        guide = read("workflows/reply.md")
        for rule in ("复述原话", "新增信息", "换一个角度", "具体画面", "直接回复", "不要先给用户解释"):
            with self.subTest(rule=rule):
                self.assertIn(rule, guide)

    def test_real_reported_failures_are_saved(self):
        cases = read("evals/comment-replies.md")
        for piece in (
            "幽默自由这个说法戳到我了",
            "曾颖是个有趣的娘们",
            "我还在负责写教材",
            "把不好玩的部分外包给我了",
            "新增信息",
            "不是人工评分结果",
        ):
            with self.subTest(piece=piece):
                self.assertIn(piece, cases)

    def test_readme_shows_simple_reply_test(self):
        readme = read("README.md")
        self.assertIn("v5.1", readme)
        self.assertIn("短评论", readme)


if __name__ == "__main__":
    unittest.main()
