# Script to read in raw snapshot data
# and remove 0 balances

import json
import numpy as np
import os

tokens = ['wZNN', 'Cake-LP']

for t in tokens:
    output = []
    with open(os.path.join(t, 'balances', f'{t}.json')) as f:
        d = json.load(f)
        for line in d:
            if line['balance'] != '0.000000000000000000':
                output.append({
                    'address': line['wallet'],
                    'balance': np.format_float_positional(float(line['balance']), trim='-')
                })

    final = json.dumps(output, indent=2)

    with open(f'{t}_data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)