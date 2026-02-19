"""
Crisis 纪元模块
"""

# 前危机纪元
def crisis_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
三体 - 文明抉择
前危机纪元：觉醒
═══════════════════════════════════

07年，叶文洁按下了发送键。
的信号穿越星际，飞向半人马座α星。

回复到达地球。
锁死了人类的基础科学。
着地球的一切。

面临前所未有的危机。
，三体舰队将抵达太阳系。

者计划的一员，你必须做出第一个选择：

生存至上】不惜一切代价保存人类火种
科技突破】寻找智子封锁的漏洞
道德坚守】即使面对毁灭也要保持人性
主动出击】以攻为守，寻找三体的弱点
团结一致】凝聚全人类的力量共同应对""")
    game.add_button("选择1", lambda: game.choice(2, 0, 0, 0, 0, game.crisis_era_2))
    game.add_button("选择2", lambda: game.choice(0, 3, 0, 0, 0, game.crisis_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 3, 0, 0, game.crisis_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 2, 0, game.crisis_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 3, game.crisis_era_2))

def crisis_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
前危机纪元：抉择
═══════════════════════════════════

开始实施。
地球三体组织）的余党仍在暗中活动。
开始分裂：逃亡派、抵抗派、投降派...

星防御理事会召开紧急会议。
定人类文明的发展方向：

建造方舟】秘密建造星际飞船，保存人类文明
太空电梯】大力发展太空工业，建立轨道防御
思想钢印】用技术手段统一人类意志
恒星级武器】研发能够威慑三体的终极武器
地下城市】在地球深处建立避难所""")
    game.add_button("选择1", lambda: game.choice(3, 0, 0, 0, 0, game.crisis_era_3))
    game.add_button("选择2", lambda: game.choice(0, 3, 0, 0, 0, game.crisis_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 2, 0, 0, game.crisis_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 3, 0, game.crisis_era_3))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 2, game.crisis_era_3))

def crisis_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
前危机纪元：转折
═══════════════════════════════════

去了。
在智子的封锁下艰难前行。
、心理学、战略学都有了长足发展。

辑发现了黑暗森林法则：
一座黑暗森林，每个文明都是带枪的猎人。

改变了一切。
须决定如何利用这个秘密：

建立威慑】用黑暗森林法则威慑三体
隐藏真相】将这个秘密作为最后的底牌
寻求和平】用真相换取三体的和平共处
先发制人】立即向宇宙广播三体坐标
全民皆知】公开真相，让全人类共同决定
平衡发展】在各个方向都保持投入""")
    game.add_button("选择1", lambda: game.choice(2, 2, 0, 0, 0, game.deterrence_era_1))
    game.add_button("选择2", lambda: game.choice(0, 2, 2, 0, 0, game.deterrence_era_1))
    game.add_button("选择3", lambda: game.choice(0, 0, 2, 2, 0, game.deterrence_era_1))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 2, 2, game.deterrence_era_1))
    game.add_button("选择5", lambda: game.choice(2, 0, 0, 0, 2, game.deterrence_era_1))
    game.add_button("选择6", lambda: game.choice(1, 1, 1, 1, 1, game.deterrence_era_1))

