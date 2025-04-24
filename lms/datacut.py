import pandas as pd
from attack_lib import synthesize_attack, AttackPathConfig
from data_types import ScenarioConstants
from attack_capabilities import AttackerCapabilities
from attack_stealth import MovementConstraints

# 加载登录数据
logins = pd.read_csv('./auth.csv', header = None, names=['time', 'src_user', 'user', 'src', 'dst', 'suth_t', 'logon_t', 'auth_o', 'sf'])
print(logins)

logins = logins.head(len(logins) // 2)
print(logins)

logins.to_csv('auth_h.csv', index=False, header=False)
