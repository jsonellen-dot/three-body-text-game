"""
Broadcast 纪元模块
"""

# 广播纪元
def broadcast_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
广播纪元：黑暗森林打击
═══════════════════════════════════

力"号向宇宙广播了三体世界的坐标。

打击来临。
文明向三体星系发射了光粒。
颗太阳被摧毁。
覆灭。

失去了母星，陷入混乱。
自由。

沉重的——
了自己的存在。
打击可能随时降临地球。

进入广播纪元。
知道：我们的坐标已经暴露。

定人类的未来：

逃亡计划】建造星际飞船，逃离太阳系
掩体工程】在太阳系边缘建立防御体系
和平共处】与三体舰队残部谈判
主动出击】趁机消灭三体舰队
科技爆发】利用三体技术快速发展""")
    game.add_button("选择1", lambda: game.choice(4, 0, 0, 0, 0, game.broadcast_era_2))
    game.add_button("选择2", lambda: game.choice(0, 4, 0, 0, 0, game.broadcast_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 4, 0, 0, game.broadcast_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 4, 0, game.broadcast_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 4, game.broadcast_era_2))

def broadcast_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
广播纪元：云天明的礼物
═══════════════════════════════════

一个被送往三体世界的人类大脑，
童话故事向人类传递了重要信息。

破译出了关键技术：
——能够进行光速航行的技术。

术有一个可怕的副作用：
行路径上留下"航迹"，
会降低光速，形成"黑域"。

作为安全声明：
被降低的星系，对其他文明没有威胁。

选择：

建造光速飞船】不管后果，掌握光速航行
研究黑域】主动降低太阳系光速，换取安全
破译更多】继续研究云天明的信息
技术封锁】禁止任何相关研究
秘密进行】只让少数人掌握这项技术""")
    game.add_button("选择1", lambda: game.choice(3, 3, 0, 0, 0, game.broadcast_era_3))
    game.add_button("选择2", lambda: game.choice(0, 3, 3, 0, 0, game.broadcast_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 3, 3, 0, game.broadcast_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 3, 3, game.broadcast_era_3))
    game.add_button("选择5", lambda: game.choice(3, 0, 0, 0, 3, game.broadcast_era_3))

def broadcast_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
广播纪元：最后的选择
═══════════════════════════════════

面临选择。

颗星球——DX3906，
明送给她的礼物。

了两派：
飞船派：建造光速飞船逃离
派：在木星等巨行星背后建立掩体城市

票：禁止光速飞船研究。
光速飞船的航迹会暴露地球坐标。

秘密建造了光速飞船"星环"号。
决定是否阻止他们。

，掩体工程开始。
星、土星背后建立了巨大的城市。

将决定人类的命运：

支持光速飞船】人类需要逃离的能力
支持掩体计划】在太阳系内寻求安全
两手准备】暗中支持光速飞船，明面支持掩体
强制统一】用强权统一人类意志
自由选择】让每个人自己决定
寻找第三条路】也许还有其他可能""")
    game.add_button("选择1", lambda: game.choice(5, 0, 0, 0, 0, game.bunker_era_1))
    game.add_button("选择2", lambda: game.choice(0, 5, 0, 0, 0, game.bunker_era_1))
    game.add_button("选择3", lambda: game.choice(0, 0, 5, 0, 0, game.bunker_era_1))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 5, 0, game.bunker_era_1))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 5, game.bunker_era_1))
    game.add_button("选择6", lambda: game.choice(2, 2, 0, 2, 0, game.bunker_era_1))

