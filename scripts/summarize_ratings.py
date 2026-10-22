#!/usr/bin/env python3
"""Summarize rating CSV; illustrative dataset is NOT a benchmark result."""
import csv
import statistics
import sys
from collections import defaultdict

def summarize(path):
    groups = defaultdict(lambda: defaultdict(list))
    with open(path,encoding='utf-8',newline='') as handle:
        for row in csv.DictReader(handle):
            for field in ('humor','naturalness','appropriateness'):
                score = float(row[field])
                if not 1 <= score <= 5: raise ValueError(f'out-of-range score: {score}')
                groups[row['condition']][field].append(score)
    return {name:{field:{'count':len(vals),'mean':round(statistics.mean(vals),3),'std':round(statistics.stdev(vals),3) if len(vals)>1 else None} for field,vals in dimensions.items()} for name,dimensions in groups.items()}

if __name__ == '__main__':
    if len(sys.argv)!=2: sys.exit('Usage: python scripts/summarize_ratings.py ratings.csv')
    import json
    print(json.dumps(summarize(sys.argv[1]),ensure_ascii=False,indent=2))
    print('NOTE: Aggregation only; no significance or causal claims.')
