"""
Victory 纪元模块
"""

# 胜利纪元（特殊路线）
def victory_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
胜利纪元：人类的反击
═══════════════════════════════════

线：人类击败三体】

导下，人类展现了前所未有的团结。
了智子的封锁。
事力量击退了三体舰队。

在母星被摧毁后，
向人类投降。

了太阳系的真正主宰。
从未在原著中出现的可能性。

来了新的问题：
处理三体俘虏？
面对更广阔的宇宙？
会成为下一个侵略者吗？

定胜利后的道路：

仁慈对待】给予三体人平等的地位
技术掠夺】榨取三体的所有技术
建立秩序】以人类为中心建立新秩序
继续扩张】向更远的星系进军
保持警惕】防范可能的威胁""")
    game.add_button("选择1", lambda: game.choice(5, 0, 0, 0, 0, game.victory_era_2))
    game.add_button("选择2", lambda: game.choice(0, 5, 0, 0, 0, game.victory_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 5, 0, 0, game.victory_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 5, 0, game.victory_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 5, game.victory_era_2))

def victory_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
胜利纪元：新的征程
═══════════════════════════════════

进入了前所未有的繁荣期。

被完全吸收。
用力材料、智子技术、曲率驱动...
技水平突飞猛进。

改造成了一个巨大的工业基地。
向周边星系派遣探索舰队。

黑暗森林法则依然存在。
决定：成为猎人，还是继续隐藏？

积极扩张】占领更多星系
科技优先】继续提升技术水平
寻找盟友】在宇宙中寻找可以合作的文明
建立威慑】让其他文明畏惧人类
谨慎前进】小心翼翼地探索宇宙""")
    game.add_button("选择1", lambda: game.choice(4, 4, 0, 0, 0, game.victory_era_3))
    game.add_button("选择2", lambda: game.choice(0, 4, 4, 0, 0, game.victory_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 4, 4, 0, game.victory_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 4, 4, game.victory_era_3))
    game.add_button("选择5", lambda: game.choice(4, 0, 0, 0, 4, game.victory_era_3))

def victory_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
胜利纪元：星际帝国
═══════════════════════════════════

已经扩展到了十几个星系。
了星际帝国的首都。

部开始出现分裂：
派：坚持地球的统治地位
地派：要求更多自治权
派：主张用技术改造人类自身
派：坚持传统人类价值观

宙中的其他文明也注意到了人类。
了友好信号，有的则充满敌意。

文明的关键时刻：

中央集权】强化地球的统治
联邦制度】给予殖民地更多自由
技术升级】用技术改造人类
军事扩张】继续征服更多星系
文化输出】用人类文化影响宇宙
平衡发展】在各个方面保持平衡""")
    game.add_button("选择1", lambda: game.choice(6, 0, 0, 0, 0, game.expansion_era_1))
    game.add_button("选择2", lambda: game.choice(0, 6, 0, 0, 0, game.expansion_era_1))
    game.add_button("选择3", lambda: game.choice(0, 0, 6, 0, 0, game.expansion_era_1))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 6, 0, game.expansion_era_1))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 6, game.expansion_era_1))
    game.add_button("选择6", lambda: game.choice(3, 3, 3, 0, 0, game.expansion_era_1))

