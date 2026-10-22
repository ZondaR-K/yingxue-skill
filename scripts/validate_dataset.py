#!/usr/bin/env python3
"""Validate the repository's lightweight JSON/JSONL task and candidate formats."""
import json
import sys
from pathlib import Path

MECHANISMS = {'incongruity', 'benign_violation', 'semantic_reframe', 'mock_epic', 'running_gag', 'self_deprecation'}

def validate_candidates(data):
    if not isinstance(data, dict) or not isinstance(data.get('task_id'), str) or not data['task_id'].strip():
        raise ValueError('task_id must be a non-empty string')
    if not isinstance(data.get('context'), str):
        raise ValueError('context must be a string')
    candidates = data.get('candidates')
    if not isinstance(candidates, list) or not candidates:
        raise ValueError('candidates must be a non-empty list')
    seen = set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise ValueError('candidate must be an object')
        cid = candidate.get('id')
        if not isinstance(cid, str) or not cid or cid in seen:
            raise ValueError('candidate ids must be unique nonempty strings')
        seen.add(cid)
        if candidate.get('mechanism') not in MECHANISMS:
            raise ValueError('invalid mechanism')
        if not isinstance(candidate.get('text'), str) or not candidate['text'].strip():
            raise ValueError('candidate text must be nonempty')
    return len(candidates)

def validate_dataset_row(data):
    if not isinstance(data, dict):
        raise ValueError('dataset entry must be object')
    for key in ('id','prompt','audience','mechanism'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} missing')
    if data['mechanism'] not in MECHANISMS:
        raise ValueError('invalid mechanism')
    if not isinstance(data.get('constraints'), list) or not all(isinstance(x,str) for x in data['constraints']):
        raise ValueError('constraints must be list of strings')
    return 1

def validate_file(path):
    path = Path(path)
    if path.suffix == '.jsonl':
        rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        ids = [row.get('id') for row in rows]
        if len(ids) != len(set(ids)):
            raise ValueError('duplicate dataset ids')
        return sum(validate_dataset_row(row) for row in rows)
    return validate_candidates(json.loads(path.read_text(encoding='utf-8')))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: python scripts/validate_dataset.py PATH [PATH ...]')
    try:
        for filename in sys.argv[1:]:
            print(f'PASS {filename}: {validate_file(filename)} records')
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        sys.exit(f'FAIL: {exc}')
