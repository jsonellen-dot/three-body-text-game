"""
Bunker 纪元模块
"""

# 掩体纪元
def bunker_era_1(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
掩体纪元：巨行星的阴影
═══════════════════════════════════

了掩体。

星、天王星、海王星的背后，
大的太空城市。

：当黑暗森林打击来临时，
挡住攻击。

留下了少数人。
类生活在掩体城市中。

看似安全的时代。
行星的阴影下生活，
平与繁荣。

全吗？

加固掩体】继续强化防御系统
发展科技】提升掩体城市的技术水平
保持警惕】建立预警系统
准备撤离】暗中准备逃离方案
享受和平】相信掩体的保护""")
    game.add_button("选择1", lambda: game.choice(5, 0, 0, 0, 0, game.bunker_era_2))
    game.add_button("选择2", lambda: game.choice(0, 5, 0, 0, 0, game.bunker_era_2))
    game.add_button("选择3", lambda: game.choice(0, 0, 5, 0, 0, game.bunker_era_2))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 5, 0, game.bunker_era_2))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 5, game.bunker_era_2))

def bunker_era_2(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
掩体纪元：虚假的安全
═══════════════════════════════════

去了。

繁荣发展。
类在巨行星的阴影下出生、成长。
见过地球的蓝天。

AA从冬眠中醒来。
人类社会已经完全改变。

号光速飞船的建造者被判刑。
谴责他们"危害全人类安全"。

的星空中，
的光点正在接近太阳系...

定：

提高警戒】加强对太空的监视
技术储备】秘密研究逃离技术
社会稳定】维持现有的和平
寻求外援】尝试联系其他文明
准备最坏】为可能的灾难做准备""")
    game.add_button("选择1", lambda: game.choice(4, 4, 0, 0, 0, game.bunker_era_3))
    game.add_button("选择2", lambda: game.choice(0, 4, 4, 0, 0, game.bunker_era_3))
    game.add_button("选择3", lambda: game.choice(0, 0, 4, 4, 0, game.bunker_era_3))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 4, 4, game.bunker_era_3))
    game.add_button("选择5", lambda: game.choice(4, 0, 0, 0, 4, game.bunker_era_3))

def bunker_era_3(game):
    game.clear_buttons()
    game.show_text("""═══════════════════════════════════════
掩体纪元：二向箔
═══════════════════════════════════

箔从天而降。

如此美丽，像一张透明的卡片。
质是降维打击——
间降为二维。

始坍缩。
任何作用。
它们背后的城市一起，
二维的画面。

环"号和少数光速飞船逃离。

几乎全灭。

时刻，你的选择是：

坚守到底】与文明共存亡
逃向星空】加入逃亡的飞船
记录一切】为后世留下人类的记忆
寻找希望】相信还有生还的可能
接受命运】平静地面对终结
最后的抗争】即使无用也要反抗""")
    game.add_button("选择1", lambda: game.choice(6, 0, 0, 0, 0, game.calculate_ending))
    game.add_button("选择2", lambda: game.choice(0, 6, 0, 0, 0, game.calculate_ending))
    game.add_button("选择3", lambda: game.choice(0, 0, 6, 0, 0, game.calculate_ending))
    game.add_button("选择4", lambda: game.choice(0, 0, 0, 6, 0, game.calculate_ending))
    game.add_button("选择5", lambda: game.choice(0, 0, 0, 0, 6, game.calculate_ending))
    game.add_button("选择6", lambda: game.choice(3, 3, 0, 0, 3, game.calculate_ending))

