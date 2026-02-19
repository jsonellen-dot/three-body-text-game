"""
Deterrence 纪元模块
"""

# 威慑纪元
def deterrence_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
威慑纪元：黑暗森林威慑
═══════════════════════════════════

08年，威慑纪元开始。

执剑人，手握向宇宙广播地球和三体坐标的开关。
停止前进，开始减速。
进入了恐怖的平衡。

开始向地球传输技术和文化。
进入了黄金时代。

基础是脆弱的——
一个人的意志，一个随时可能按下按钮的人。

代的决策者，你需要选择：

强化威慑】确保威慑系统万无一失
技术交流】加速吸收三体科技
文化融合】促进两个文明的相互理解
军事准备】暗中准备最终决战
制度建设】建立长期稳定的威慑机制""")
    game.add_button("选择1", lambda: game.choice(4, 0, 0, 0, 0, game.deterrence_era_2))
    game.add_button("选择2", lambda: game.choice(0, 4, 0, 0, 0, game.deterrence_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 4, 0, 0, game.deterrence_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 4, 0, game.deterrence_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 4, game.deterrence_era_2))

def deterrence_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
威慑纪元：和平幻象
═══════════════════════════════════

和平让人类变得柔软。
类在富足中成长，他们不理解威慑的残酷。

为时代的主题。
质疑：真的需要威慑吗？
的会毁灭我们吗？

辑已经老了。
新的执剑人。

个充满爱心的女性，成为候选人。
新时代的价值观。

定：

支持程心】相信爱与和平的力量
选择强硬派】执剑人必须有按下按钮的决心
建立委员会】让多人共同掌握威慑权
AI执剑】让人工智能成为执剑人
维持现状】说服罗辑继续担任执剑人""")
    game.add_button("选择1", lambda: game.choice(3, 2, 0, 0, 0, game.deterrence_era_3))
    game.add_button("选择2", lambda: game.choice(0, 3, 2, 0, 0, game.deterrence_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 3, 2, 0, game.deterrence_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 3, 2, game.deterrence_era_3))
    game.add_button("选择5", lambda: game.choice(2, 0, 0, 0, 3, game.deterrence_era_3))

def deterrence_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
威慑纪元：关键时刻
═══════════════════════════════════

70年，程心成为执剑人。

分钟后，三体世界发动了攻击。
了所有引力波发射台。
了地球的控制系统。

按下按钮。
担毁灭两个世界的责任。

了。

宣布：人类将被迁移到澳大利亚，
为人类保留地。

中，仍有一线希望——
力"号和"蓝色空间"号战舰逃离了太阳系。

必须做出最关键的选择：

接受现实】配合三体的安排，保存人类
寻找机会】暗中准备反抗
支持逃亡】帮助更多人逃离地球
绝地反击】即使没有希望也要战斗
等待奇迹】相信逃亡的战舰会带来转机
多线准备】在各个方向都留下希望""")
    game.add_button("选择1", lambda: game.choice(5, 0, 0, 0, 0, check_victory_path))
    game.add_button("选择2", lambda: game.choice(0, 5, 0, 0, 0, check_victory_path))
    game.add_button("选择3", lambda: game.choice(0, 0, 5, 0, 0, check_victory_path))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 5, 0, check_victory_path))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 5, check_victory_path))
    game.add_button("选择6", lambda: game.choice(2, 2, 2, 0, 0, check_victory_path))
    game.add_button("选择7【威慑失败】", lambda: game.choice(0, 0, 3, 0, 0, enter_dark_era))

# 检查是否进入胜利纪元（小概率）
def check_victory_path(game):
    # 条件：科技>20 且 侵略性>15 且 团结度>15
    if game.score['technology'] > 20 and game.score['aggression'] > 15 and game.score['unity'] > 15:
        game.era_path.append('victory')
        from .victory import victory_era_1
        victory_era_1(game)
    else:
        game.era_path.append('broadcast')
        from .broadcast import broadcast_era_1
        broadcast_era_1(game)

def enter_dark_era(game):
    """进入黑暗纪元"""
    game.era_path.append('dark')
    from .dark import dark_era_1
    dark_era_1(game)

