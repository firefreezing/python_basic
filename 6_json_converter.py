#%%
import json
import pandas as pd
import os

#%%
print(os.getcwd())
#%%
dat = pd.DataFrame(
    {"Dialogue": [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
    "Q": ["aaa", "bbb", "ccc", "ddd", "aaa", "bbb", "ccc", "aaa", "bbb", "ccc"],
    "A": ["x", "y", "z", "w", "x", "y", "z", "x", "y", "z"]}
)
#%%
# convert into JSON:
y = dat.to_json(orient = "records")
print(y)
#%%

multi_diag = dict()

for id in dat.Dialogue.unique():
    multi_diag[id] = dat.loc[dat.Dialogue == id]

#%%
print(multi_diag['id'])
#%%
with open('data/json_output1.json', 'w') as f:
    json.dump(multi_diag, f, indent=2)

#%%
