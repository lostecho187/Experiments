import pickle
import numpy as np
import pandas as pd


auth = pd.read_csv("./auth_ntlm.csv")
df = auth[['time', 'src', 'dst', 'label']]
del auth

times = []
srcs = []
dsts = []
labels = []
for index, row in df.iterrows():
    times.append(row['time'])
    if row['src'][1:].isdigit():
        srcs.append(row['src'][1:])
    else:
        srcs.append(0)

    if row['dst'][1:].isdigit():
        dsts.append(row['dst'][1:])
    else:
        dsts.append(0)

    if row['label']:
        labels.append(0)
    else:
        labels.append(1)

    if index % 1000000 == 0:
        print(index)

df = pd.DataFrame({
    'u': srcs, 
    'i': dsts, 
    'ts': times, 
    'label' :labels
})
del times, srcs, dsts, labels
print('df', df)

feat = pd.read_csv('./new_feat_authlog.csv', header=None)
# feat = feat[['ID_usr', 'ID_src', 'ID_usr_src', 'OD_usr', 'OD_dst', 'OD_usr_dst', 'ODAF_usr', 'ODAF_dst', 'ODAF_usr_dst']]
feat = feat.iloc[:, -9:]
print('feat', feat)
if df.shape[0] == feat.shape[0]:
    df = pd.concat([df, feat], axis = 1)
    print(df)

    df.to_csv('auth.csv', index = False, header = False)
else:
    print('df:', df.shape[0], ', feat:', feat.shape[0])
