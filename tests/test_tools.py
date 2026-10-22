import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class ToolTests(unittest.TestCase):
    def test_dataset(self):
        self.assertEqual(load('validate_dataset').validate_file(ROOT/'evals/dataset.jsonl'),4)
    def test_candidates(self):
        self.assertEqual(load('validate_dataset').validate_file(ROOT/'examples/candidates.json'),3)
    def test_reject_duplicate(self):
        validator=load('validate_dataset')
        bad={'task_id':'t','context':'c','candidates':[{'id':'a','mechanism':'mock_epic','text':'x'},{'id':'a','mechanism':'mock_epic','text':'y'}]}
        with self.assertRaises(ValueError): validator.validate_candidates(bad)
    def test_diagnostic(self):
        metrics=load('score_candidates').diagnostic('我已经决定早睡。结果睡在客厅。')
        self.assertIn('结果',metrics['transition_cues'])
        self.assertFalse(metrics['may_overexplain'])
    def test_ratings(self):
        report=load('summarize_ratings').summarize(ROOT/'evals/example-ratings.csv')
        self.assertEqual(report['skill']['humor']['count'],2)
        self.assertEqual(report['skill']['humor']['mean'],4)
    def test_skill_frontmatter(self):
        text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\nname: yingxue\n'))
        self.assertIn('\ndescription:',text)

if __name__=='__main__': unittest.main()
