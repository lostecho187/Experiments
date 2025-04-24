import pandas as pd

scenario = '1' # select from 't', '1', '2', '3'
auth = pd.DataFrame()
#20 17 16
if scenario == '1':
    start_index = 1
    length = 20
elif scenario == '2':
    start_index = 20 + 1
    length = 17
elif scenario == '3':
    start_index = 20 + 17 + 1
    length = 16
else:
    start_index = 1
    length = 20 + 17 + 16

for i in range(length):
    df = pd.read_csv("../lms/attack/attack_path_" + str(i + start_index) + ".csv")
    print(df)
    auth = pd.concat([auth, df], axis=0)
    print(auth)

auth = auth[['time', 'src_user', 'user', 'src', 'dst', 'auth_t', 'logon_t', 'auth_o', 'sf', 'is_attack']]
auth.columns = ['time', 'src_t', 'user', 'src', 'dst', 'auth_t', 'log_t', 'auth_o', 's_f', 'label']
print(auth)

df = pd.read_csv("../lms/auth_h.csv", header=None, 
                 names=['time', 'src_t', 'user', 'src', 'dst', 'auth_t', 'log_t', 'auth_o', 's_f', 'label'])
df['label'] = False
print(df)
auth = pd.concat([auth, df], axis=0)
auth = auth.sort_values(by='time')
print(auth)

auth.to_csv("./auth_ntlm.csv", index=False)