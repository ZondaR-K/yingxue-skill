#!/usr/bin/env python3
"""Surface diagnostics only: not a quantitative measure of humor quality."""
import json
import re
import sys
from pathlib import Path

CUES = ('结果', '没想到', '竟然', '原来', '最后', '如今', '至少', '直到')

def diagnostic(text):
    lines = [x.strip() for x in re.split(r'[。！？!?\n]', text) if x.strip()]
    return {'characters': len(text.strip()), 'units': len(lines), 'final_unit_characters': len(lines[-1]) if lines else 0, 'transition_cues': [c for c in CUES if c in text], 'may_overexplain': any(s in text for s in ('这就是笑点', '之所以好笑是因为'))}

if __name__ == '__main__':
    if len(sys.argv) != 2: sys.exit('Usage: python scripts/score_candidates.py candidates.json')
    data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    for item in data['candidates']:
        print(json.dumps({'id':item['id'],**diagnostic(item['text'])},ensure_ascii=False))
    print('NOTE: These are text diagnostics, not human humor ratings.')
