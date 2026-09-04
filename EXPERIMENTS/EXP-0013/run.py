import json
from experiment import aggregate

out = {m: aggregate(m) for m in ('B','C','D')}
with open('RESULTS/EXP-0013/raw_results.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2)
print('EXP-0013 executed; results written to RESULTS/EXP-0013/raw_results.json')
for m in ('B','C','D'):
    x=out[m]
    print(m, 'adapt', round(x['adaptation_mean'],3), 'reward', round(x['reward_mean'],3), 'false', round(x['false_switch_mean'],3), 'transfer', round(x['transfer_mean'],3))
