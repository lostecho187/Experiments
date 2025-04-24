import pandas as pd
import os
import random
from attack_lib import synthesize_attack, AttackPathConfig
from data_types import ScenarioConstants
from attack_capabilities import AttackerCapabilities
from attack_stealth import MovementConstraints

folder_path = './attack'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 加载登录数据
logins = pd.read_csv('./auth.txt', header = None, names=['time', 'src_user', 'user', 'src', 'dst', 'auth_t', 'logon_t', 'auth_o', 'sf'])
print(logins)

logins['day'] = logins['time'] // (24 * 3600)
logins['is_src_client'] = True
logins['is_dst_client'] = True

dsts = logins['dst'].drop_duplicates()
targets = random.sample(list(dsts), 1)

while len(os.listdir(folder_path)) < 20:
    attack_config = AttackPathConfig(
        attack_goal=ScenarioConstants.GOAL_EXPLORATION,
        attacker_knowledge = AttackerCapabilities.KNOWLEDGE_LOCAL,
        stealth=ScenarioConstants.STEALTH_NONE,
        protocol='all',  # 或 'windows' 或其他协议
        start_state=None,  # 可以指定起始状态，或者让系统随机选择
        src_preference=MovementConstraints.SRC_PREF_NONE,
        compromise_cred_hrs=24,  # 凭证暴露时间窗口
        active_cred_hrs=1,  # 活跃凭证时间窗口
        src_history_hrs=6,  # 源历史时间窗口
        target_machines=set(targets)  # 目标机器
    )

    # 调用 synthesize_attack 方法生成攻击路径
    attack_path = synthesize_attack(logins, attack_config)
    if attack_path.empty:
        continue
    # 检查合成的攻击路径
    file_number = len(os.listdir(folder_path)) + 1
    attack_path.to_csv(folder_path + '/attack_path_' + str(file_number) + '.csv', index=False)

while len(os.listdir(folder_path)) < 37:
    # 创建攻击配置
    attack_config = AttackPathConfig(
        attack_goal=ScenarioConstants.GOAL_SPREAD,
        attacker_knowledge = AttackerCapabilities.KNOWLEDGE_GLOBAL,
        stealth=ScenarioConstants.STEALTH_NONE,
        protocol='all',  # 或 'windows' 或其他协议
        start_state=None,  # 可以指定起始状态，或者让系统随机选择
        src_preference=MovementConstraints.SRC_PREF_NONE,
        compromise_cred_hrs=24,  # 凭证暴露时间窗口
        active_cred_hrs=1,  # 活跃凭证时间窗口
        src_history_hrs=6,  # 源历史时间窗口
        target_machines=set(targets)  # 目标机器
    )

    # 调用 synthesize_attack 方法生成攻击路径
    attack_path = synthesize_attack(logins, attack_config)
    if attack_path.empty:
        continue
    # 检查合成的攻击路径
    file_number = len(os.listdir(folder_path)) + 1
    attack_path.to_csv(folder_path + '/attack_path_' + str(file_number) + '.csv', index=False)

while len(os.listdir(folder_path)) < 53:
    # 创建攻击配置
    attack_config = AttackPathConfig(
        attack_goal=ScenarioConstants.GOAL_TARGETED,
        attacker_knowledge = AttackerCapabilities.KNOWLEDGE_GLOBAL,
        stealth=ScenarioConstants.STEALTH_NONE,
        protocol='all',  # 或 'windows' 或其他协议
        start_state=None,  # 可以指定起始状态，或者让系统随机选择
        src_preference=MovementConstraints.SRC_PREF_NONE,
        compromise_cred_hrs=24,  # 凭证暴露时间窗口
        active_cred_hrs=1,  # 活跃凭证时间窗口
        src_history_hrs=6,  # 源历史时间窗口
        target_machines=set(targets)  # 目标机器
    )

    # 调用 synthesize_attack 方法生成攻击路径
    attack_path = synthesize_attack(logins, attack_config)
    if attack_path.empty:
        continue
    # 检查合成的攻击路径
    file_number = len(os.listdir(folder_path)) + 1
    attack_path.to_csv(folder_path + '/attack_path_' + str(file_number) + '.csv', index=False)
