from math import isfinite

def analyze(data):
    intervals = data['intervals']
    if not isinstance(intervals,list):
        raise ValueError('Expected an array of intervals')
    merged = []
    for start,end in sorted(intervals):
        if not all(type(x) in (int,float) and isfinite(x) for x in (start,end)) or start >= end:
            raise ValueError('Invalid interval')
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start,end])
    return {'merged': merged, 'coverage': sum(b-a for a,b in merged),
            'gaps': [[a[1],b[0]] for a,b in zip(merged,merged[1:])]}

if __name__ == "__main__":
    import json
    from pathlib import Path
    import sys
    try:
        path, = sys.argv[1:]
        result = analyze(json.loads(Path(path).read_text(encoding="utf-8")))
        print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError) as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(2)
