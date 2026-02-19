"""
Expansion 纪元模块
"""

def expansion_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
扩张纪元：星际殖民
═══════════════════════════════════════

【胜利路线延续】

人类文明已经扩展到五十个星系。
地球联邦统治着一个庞大的星际帝国。

殖民舰队不断向更远的星系进发。
人类的足迹遍布银河系的一角。

但扩张带来了新的挑战：
- 殖民地要求独立
- 资源分配不均
- 文化差异加剧
- 与其他文明的冲突

你必须决定帝国的未来：

1. 【军事镇压】用武力维持统一
2. 【技术控制】通过技术优势保持统治
3. 【文化同化】用地球文化统一帝国
4. 【继续扩张】用新的征服转移矛盾
5. 【联邦改革】给予殖民地更多权力""")
    game.add_button("选择1", lambda: game.choice(5, 0, 0, 0, 0, game.expansion_era_2))
    game.add_button("选择2", lambda: game.choice(0, 5, 0, 0, 0, game.expansion_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 5, 0, 0, game.expansion_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 5, 0, game.expansion_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 5, game.expansion_era_2))

def expansion_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
扩张纪元：宇宙秩序
═══════════════════════════════════════

人类遇到了其他星际文明。

有的文明比人类弱小，被人类征服。
有的文明与人类实力相当，形成对峙。
还有的文明远比人类强大，让人类感到恐惧。

宇宙的真相逐渐显现：
这是一个充满竞争的宇宙。
弱肉强食是永恒的法则。

人类必须选择自己的道路：

1. 【建立联盟】与其他文明结盟
2. 【技术竞赛】追求更强大的技术
3. 【和平共处】尝试建立宇宙秩序
4. 【征服一切】成为宇宙的霸主
5. 【保持中立】不参与宇宙争霸""")
    game.add_button("选择1", lambda: game.choice(4, 4, 0, 0, 0, game.expansion_era_3))
    game.add_button("选择2", lambda: game.choice(0, 4, 4, 0, 0, game.expansion_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 4, 4, 0, game.expansion_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 4, 4, game.expansion_era_3))
    game.add_button("选择5", lambda: game.choice(4, 0, 0, 0, 4, game.expansion_era_3))

def expansion_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
扩张纪元：文明的抉择
═══════════════════════════════════════

人类文明站在了十字路口。

经过数百年的扩张，
人类已经成为银河系中的主要力量之一。

但代价是什么？
人类还是当初那个人类吗？

有人说：我们已经失去了人性。
有人说：这就是生存的代价。

现在，一个更强大的文明向人类发出了挑战。
这可能是人类文明的终极考验。

你的最终选择将决定人类的命运：

1. 【决战】与强敌决一死战
2. 【谈判】寻求和平解决
3. 【逃离】放弃已有的一切，逃向更远的星空
4. 【同化】加入更强大的文明
5. 【升维】寻求技术突破，进入更高维度
6. 【平衡】在各种可能中寻找最优解""")
    game.add_button("选择1", lambda: game.choice(6, 0, 0, 0, 0, game.calculate_ending))
    game.add_button("选择2", lambda: game.choice(0, 6, 0, 0, 0, game.calculate_ending))
    game.add_button("选择3", lambda: game.choice(0, 0, 6, 0, 0, game.calculate_ending))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 6, 0, game.calculate_ending))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 6, game.calculate_ending))
    game.add_button("选择6", lambda: game.choice(3, 3, 3, 3, 0, game.calculate_ending))

def choice(self, survival, tech, moral, aggr, unity, next_func):
    game.score['survival'] += survival
    game.score['technology'] += tech
    game.score['morality'] += moral
    game.score['aggression'] += aggr
    game.score['unity'] += unity
    next_func()

