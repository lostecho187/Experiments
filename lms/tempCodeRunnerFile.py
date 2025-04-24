
targets = ['C743']

# 创建攻击配置
attack_config = AttackPathConfig(
    attack_goal=ScenarioConstants.GOAL_EXPLORATION,
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

# 检查合成的攻击路径
print(targets)
print(attack_path)
# attack_path = attack_path['time', 'src_user', 'user', 'src', 'dst', 'suth_t', 'logon_t', 'auth_o', 'sf']
attack_path.to_csv('attack_path.csv', index=False)