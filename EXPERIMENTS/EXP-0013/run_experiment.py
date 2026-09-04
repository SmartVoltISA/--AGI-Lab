import json
from experiment import aggregate

out = {m: aggregate(m) for m in ('B', 'C', 'D')}
with open('exp0013_results.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2)
print(json.dumps({m: {k:v for k,v in r.items() if k != 'raw'} for m,r in out.items()}, indent=2))
