#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import scrolledtext
import sys

class ThreeBodyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("三体 - 文明抉择")
        self.root.geometry("800x600")
        
        # 积分系统
        self.score = {
            'survival': 0,    # 生存意志
            'technology': 0,  # 科技发展
            'morality': 0,    # 道德水平
            'aggression': 0,  # 侵略性
            'unity': 0        # 团结度
        }
        
        # 纪元追踪
        self.era_path = []  # 记录经历的纪元
        self.current_stage = 0
        
        # 文本显示区域
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25, font=("SimHei", 12))
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state=tk.DISABLED)
        
        # 按钮框架
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.buttons = []
        
        # 开始游戏
        self.start_game()
    
    def clear_buttons(self):
        for btn in self.buttons:
            btn.destroy()
        self.buttons = []
    
    def show_text(self, text):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, text)
        self.text_area.config(state=tk.DISABLED)
    
    def add_button(self, text, command):
        btn = tk.Button(self.button_frame, text=text, command=command, width=60, height=2, font=("SimHei", 10))
        btn.pack(pady=5)
        self.buttons.append(btn)
    
    def start_game(self):
        self.crisis_era_1()
    
    # 前危机纪元
    def crisis_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    三体 - 文明抉择
    前危机纪元：觉醒
═══════════════════════════════════════

公元2007年，叶文洁按下了发送键。
红岸基地的信号穿越星际，飞向半人马座α星。

八年后，回复到达地球。
三体文明锁死了人类的基础科学。
智子监视着地球的一切。

人类文明面临前所未有的危机。
四百年后，三体舰队将抵达太阳系。

作为面壁者计划的一员，你必须做出第一个选择：

1. 【生存至上】不惜一切代价保存人类火种
2. 【科技突破】寻找智子封锁的漏洞
3. 【道德坚守】即使面对毁灭也要保持人性
4. 【主动出击】以攻为守，寻找三体的弱点
5. 【团结一致】凝聚全人类的力量共同应对""")
        self.add_button("选择1", lambda: self.choice(2, 0, 0, 0, 0, self.crisis_era_2))
        self.add_button("选择2", lambda: self.choice(0, 3, 0, 0, 0, self.crisis_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 3, 0, 0, self.crisis_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 2, 0, self.crisis_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 3, self.crisis_era_2))
    
    def crisis_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    前危机纪元：抉择
═══════════════════════════════════════

你的计划开始实施。
ETO（地球三体组织）的余党仍在暗中活动。
人类社会开始分裂：逃亡派、抵抗派、投降派...

联合国行星防御理事会召开紧急会议。
你需要决定人类文明的发展方向：

1. 【建造方舟】秘密建造星际飞船，保存人类文明
2. 【太空电梯】大力发展太空工业，建立轨道防御
3. 【思想钢印】用技术手段统一人类意志
4. 【恒星级武器】研发能够威慑三体的终极武器
5. 【地下城市】在地球深处建立避难所""")
        self.add_button("选择1", lambda: self.choice(3, 0, 0, 0, 0, self.crisis_era_3))
        self.add_button("选择2", lambda: self.choice(0, 3, 0, 0, 0, self.crisis_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 2, 0, 0, self.crisis_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 3, 0, self.crisis_era_3))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 2, self.crisis_era_3))
    
    def crisis_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    前危机纪元：转折
═══════════════════════════════════════

一百年过去了。
人类科技在智子的封锁下艰难前行。
但社会学、心理学、战略学都有了长足发展。

面壁者罗辑发现了黑暗森林法则：
宇宙就是一座黑暗森林，每个文明都是带枪的猎人。

这个发现改变了一切。
现在你必须决定如何利用这个秘密：

1. 【建立威慑】用黑暗森林法则威慑三体
2. 【隐藏真相】将这个秘密作为最后的底牌
3. 【寻求和平】用真相换取三体的和平共处
4. 【先发制人】立即向宇宙广播三体坐标
5. 【全民皆知】公开真相，让全人类共同决定
6. 【平衡发展】在各个方向都保持投入""")
        self.add_button("选择1", lambda: self.choice(2, 2, 0, 0, 0, self.deterrence_era_1))
        self.add_button("选择2", lambda: self.choice(0, 2, 2, 0, 0, self.deterrence_era_1))
        self.add_button("选择3", lambda: self.choice(0, 0, 2, 2, 0, self.deterrence_era_1))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 2, 2, self.deterrence_era_1))
        self.add_button("选择5", lambda: self.choice(2, 0, 0, 0, 2, self.deterrence_era_1))
        self.add_button("选择6", lambda: self.choice(1, 1, 1, 1, 1, self.deterrence_era_1))
    
    # 威慑纪元
    def deterrence_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    威慑纪元：黑暗森林威慑
═══════════════════════════════════════

公元2208年，威慑纪元开始。

罗辑成为执剑人，手握向宇宙广播地球和三体坐标的开关。
三体舰队停止前进，开始减速。
两个文明进入了恐怖的平衡。

三体世界开始向地球传输技术和文化。
人类社会进入了黄金时代。

但威慑的基础是脆弱的——
它依赖于一个人的意志，一个随时可能按下按钮的人。

作为新时代的决策者，你需要选择：

1. 【强化威慑】确保威慑系统万无一失
2. 【技术交流】加速吸收三体科技
3. 【文化融合】促进两个文明的相互理解
4. 【军事准备】暗中准备最终决战
5. 【制度建设】建立长期稳定的威慑机制""")
        self.add_button("选择1", lambda: self.choice(4, 0, 0, 0, 0, self.deterrence_era_2))
        self.add_button("选择2", lambda: self.choice(0, 4, 0, 0, 0, self.deterrence_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 4, 0, 0, self.deterrence_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 4, 0, self.deterrence_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 4, self.deterrence_era_2))
    
    def deterrence_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    威慑纪元：和平幻象
═══════════════════════════════════════

五十年的和平让人类变得柔软。
新一代人类在富足中成长，他们不理解威慑的残酷。

"爱"成为时代的主题。
人们开始质疑：真的需要威慑吗？
三体人真的会毁灭我们吗？

执剑人罗辑已经老了。
必须选择新的执剑人。

程心，一个充满爱心的女性，成为候选人。
她代表了新时代的价值观。

你必须决定：

1. 【支持程心】相信爱与和平的力量
2. 【选择强硬派】执剑人必须有按下按钮的决心
3. 【建立委员会】让多人共同掌握威慑权
4. 【AI执剑】让人工智能成为执剑人
5. 【维持现状】说服罗辑继续担任执剑人""")
        self.add_button("选择1", lambda: self.choice(3, 2, 0, 0, 0, self.deterrence_era_3))
        self.add_button("选择2", lambda: self.choice(0, 3, 2, 0, 0, self.deterrence_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 3, 2, 0, self.deterrence_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 3, 2, self.deterrence_era_3))
        self.add_button("选择5", lambda: self.choice(2, 0, 0, 0, 3, self.deterrence_era_3))
    
    def deterrence_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    威慑纪元：关键时刻
═══════════════════════════════════════

公元2270年，程心成为执剑人。

仅仅15分钟后，三体世界发动了攻击。
水滴摧毁了所有引力波发射台。
智子占领了地球的控制系统。

程心没有按下按钮。
她无法承担毁灭两个世界的责任。

威慑失败了。

三体世界宣布：人类将被迁移到澳大利亚，
那里将成为人类保留地。

但在绝望中，仍有一线希望——
"万有引力"号和"蓝色空间"号战舰逃离了太阳系。

现在，你必须做出最关键的选择：

1. 【接受现实】配合三体的安排，保存人类
2. 【寻找机会】暗中准备反抗
3. 【支持逃亡】帮助更多人逃离地球
4. 【绝地反击】即使没有希望也要战斗
5. 【等待奇迹】相信逃亡的战舰会带来转机
6. 【多线准备】在各个方向都留下希望""")
        self.add_button("选择1", lambda: self.choice(5, 0, 0, 0, 0, self.check_victory_path))
        self.add_button("选择2", lambda: self.choice(0, 5, 0, 0, 0, self.check_victory_path))
        self.add_button("选择3", lambda: self.choice(0, 0, 5, 0, 0, self.check_victory_path))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 5, 0, self.check_victory_path))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 5, self.check_victory_path))
        self.add_button("选择6", lambda: self.choice(2, 2, 2, 0, 0, self.check_victory_path))
    
    # 检查是否进入胜利纪元（小概率）
    def check_victory_path(self):
        # 条件：科技>20 且 侵略性>15 且 团结度>15
        if self.score['technology'] > 20 and self.score['aggression'] > 15 and self.score['unity'] > 15:
            self.era_path.append('victory')
            self.victory_era_1()
        else:
            self.era_path.append('broadcast')
            self.broadcast_era_1()
    
    # 广播纪元
    def broadcast_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    广播纪元：黑暗森林打击
═══════════════════════════════════════

"万有引力"号向宇宙广播了三体世界的坐标。

黑暗森林打击来临。
一个未知文明向三体星系发射了光粒。
三体的三颗太阳被摧毁。
三体文明覆灭。

三体舰队失去了母星，陷入混乱。
地球重获自由。

但代价是沉重的——
人类暴露了自己的存在。
黑暗森林打击可能随时降临地球。

人类文明进入广播纪元。
每个人都知道：我们的坐标已经暴露。

你必须决定人类的未来：

1. 【逃亡计划】建造星际飞船，逃离太阳系
2. 【掩体工程】在太阳系边缘建立防御体系
3. 【和平共处】与三体舰队残部谈判
4. 【主动出击】趁机消灭三体舰队
5. 【科技爆发】利用三体技术快速发展""")
        self.add_button("选择1", lambda: self.choice(4, 0, 0, 0, 0, self.broadcast_era_2))
        self.add_button("选择2", lambda: self.choice(0, 4, 0, 0, 0, self.broadcast_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 4, 0, 0, self.broadcast_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 4, 0, self.broadcast_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 4, self.broadcast_era_2))
    
    def broadcast_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    广播纪元：云天明的礼物
═══════════════════════════════════════

云天明，一个被送往三体世界的人类大脑，
通过三个童话故事向人类传递了重要信息。

情报部门破译出了关键技术：
曲率驱动——能够进行光速航行的技术。

但这项技术有一个可怕的副作用：
它会在航行路径上留下"航迹"，
这些航迹会降低光速，形成"黑域"。

黑域可以作为安全声明：
一个光速被降低的星系，对其他文明没有威胁。

人类面临选择：

1. 【建造光速飞船】不管后果，掌握光速航行
2. 【研究黑域】主动降低太阳系光速，换取安全
3. 【破译更多】继续研究云天明的信息
4. 【技术封锁】禁止任何相关研究
5. 【秘密进行】只让少数人掌握这项技术""")
        self.add_button("选择1", lambda: self.choice(3, 3, 0, 0, 0, self.broadcast_era_3))
        self.add_button("选择2", lambda: self.choice(0, 3, 3, 0, 0, self.broadcast_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 3, 3, 0, self.broadcast_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 3, 3, self.broadcast_era_3))
        self.add_button("选择5", lambda: self.choice(3, 0, 0, 0, 3, self.broadcast_era_3))
    
    def broadcast_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    广播纪元：最后的选择
═══════════════════════════════════════

程心再次面临选择。

她拥有一颗星球——DX3906，
那是云天明送给她的礼物。

人类分成了两派：
- 光速飞船派：建造光速飞船逃离
- 掩体派：在木星等巨行星背后建立掩体城市

联合国投票：禁止光速飞船研究。
理由是：光速飞船的航迹会暴露地球坐标。

但一些人秘密建造了光速飞船"星环"号。
程心必须决定是否阻止他们。

与此同时，掩体工程开始。
人类在木星、土星背后建立了巨大的城市。

你的选择将决定人类的命运：

1. 【支持光速飞船】人类需要逃离的能力
2. 【支持掩体计划】在太阳系内寻求安全
3. 【两手准备】暗中支持光速飞船，明面支持掩体
4. 【强制统一】用强权统一人类意志
5. 【自由选择】让每个人自己决定
6. 【寻找第三条路】也许还有其他可能""")
        self.add_button("选择1", lambda: self.choice(5, 0, 0, 0, 0, self.bunker_era_1))
        self.add_button("选择2", lambda: self.choice(0, 5, 0, 0, 0, self.bunker_era_1))
        self.add_button("选择3", lambda: self.choice(0, 0, 5, 0, 0, self.bunker_era_1))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 5, 0, self.bunker_era_1))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 5, self.bunker_era_1))
        self.add_button("选择6", lambda: self.choice(2, 2, 0, 2, 0, self.bunker_era_1))
    
    # 胜利纪元（特殊路线）
    def victory_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    胜利纪元：人类的反击
═══════════════════════════════════════

【特殊路线：人类击败三体】

在你的领导下，人类展现了前所未有的团结。
科技突破了智子的封锁。
强大的军事力量击退了三体舰队。

三体文明在母星被摧毁后，
残余舰队向人类投降。

人类成为了太阳系的真正主宰。
这是一个从未在原著中出现的可能性。

但胜利带来了新的问题：
- 如何处理三体俘虏？
- 如何面对更广阔的宇宙？
- 人类会成为下一个侵略者吗？

你必须决定胜利后的道路：

1. 【仁慈对待】给予三体人平等的地位
2. 【技术掠夺】榨取三体的所有技术
3. 【建立秩序】以人类为中心建立新秩序
4. 【继续扩张】向更远的星系进军
5. 【保持警惕】防范可能的威胁""")
        self.add_button("选择1", lambda: self.choice(5, 0, 0, 0, 0, self.victory_era_2))
        self.add_button("选择2", lambda: self.choice(0, 5, 0, 0, 0, self.victory_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 5, 0, 0, self.victory_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 5, 0, self.victory_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 5, self.victory_era_2))
    
    def victory_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    胜利纪元：新的征程
═══════════════════════════════════════

人类文明进入了前所未有的繁荣期。

三体技术被完全吸收。
强相互作用力材料、智子技术、曲率驱动...
人类的科技水平突飞猛进。

太阳系被改造成了一个巨大的工业基地。
人类开始向周边星系派遣探索舰队。

但宇宙的黑暗森林法则依然存在。
人类必须决定：成为猎人，还是继续隐藏？

1. 【积极扩张】占领更多星系
2. 【科技优先】继续提升技术水平
3. 【寻找盟友】在宇宙中寻找可以合作的文明
4. 【建立威慑】让其他文明畏惧人类
5. 【谨慎前进】小心翼翼地探索宇宙""")
        self.add_button("选择1", lambda: self.choice(4, 4, 0, 0, 0, self.victory_era_3))
        self.add_button("选择2", lambda: self.choice(0, 4, 4, 0, 0, self.victory_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 4, 4, 0, self.victory_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 4, 4, self.victory_era_3))
        self.add_button("选择5", lambda: self.choice(4, 0, 0, 0, 4, self.victory_era_3))
    
    def victory_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    胜利纪元：星际帝国
═══════════════════════════════════════

人类文明已经扩展到了十几个星系。
地球成为了星际帝国的首都。

但帝国内部开始出现分裂：
- 地球派：坚持地球的统治地位
- 殖民地派：要求更多自治权
- 改造派：主张用技术改造人类自身
- 保守派：坚持传统人类价值观

同时，宇宙中的其他文明也注意到了人类。
有的发来了友好信号，有的则充满敌意。

这是人类文明的关键时刻：

1. 【中央集权】强化地球的统治
2. 【联邦制度】给予殖民地更多自由
3. 【技术升级】用技术改造人类
4. 【军事扩张】继续征服更多星系
5. 【文化输出】用人类文化影响宇宙
6. 【平衡发展】在各个方面保持平衡""")
        self.add_button("选择1", lambda: self.choice(6, 0, 0, 0, 0, self.expansion_era_1))
        self.add_button("选择2", lambda: self.choice(0, 6, 0, 0, 0, self.expansion_era_1))
        self.add_button("选择3", lambda: self.choice(0, 0, 6, 0, 0, self.expansion_era_1))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 6, 0, self.expansion_era_1))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 6, self.expansion_era_1))
        self.add_button("选择6", lambda: self.choice(3, 3, 3, 0, 0, self.expansion_era_1))
    
    # 掩体纪元
    def bunker_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    掩体纪元：巨行星的阴影
═══════════════════════════════════════

人类选择了掩体。

木星、土星、天王星、海王星的背后，
建立了巨大的太空城市。

人类相信：当黑暗森林打击来临时，
巨行星会挡住攻击。

地球上只留下了少数人。
大部分人类生活在掩体城市中。

这是一个看似安全的时代。
人们在巨行星的阴影下生活，
享受着和平与繁荣。

但真的安全吗？

1. 【加固掩体】继续强化防御系统
2. 【发展科技】提升掩体城市的技术水平
3. 【保持警惕】建立预警系统
4. 【准备撤离】暗中准备逃离方案
5. 【享受和平】相信掩体的保护""")
        self.add_button("选择1", lambda: self.choice(5, 0, 0, 0, 0, self.bunker_era_2))
        self.add_button("选择2", lambda: self.choice(0, 5, 0, 0, 0, self.bunker_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 5, 0, 0, self.bunker_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 5, 0, self.bunker_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 5, self.bunker_era_2))
    
    def bunker_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    掩体纪元：虚假的安全
═══════════════════════════════════════

六十年过去了。

掩体城市繁荣发展。
新一代人类在巨行星的阴影下出生、成长。
他们从未见过地球的蓝天。

程心和艾AA从冬眠中醒来。
她们发现人类社会已经完全改变。

"星环"号光速飞船的建造者被判刑。
人类社会谴责他们"危害全人类安全"。

但在遥远的星空中，
一个小小的光点正在接近太阳系...

你必须决定：

1. 【提高警戒】加强对太空的监视
2. 【技术储备】秘密研究逃离技术
3. 【社会稳定】维持现有的和平
4. 【寻求外援】尝试联系其他文明
5. 【准备最坏】为可能的灾难做准备""")
        self.add_button("选择1", lambda: self.choice(4, 4, 0, 0, 0, self.bunker_era_3))
        self.add_button("选择2", lambda: self.choice(0, 4, 4, 0, 0, self.bunker_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 4, 4, 0, self.bunker_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 4, 4, self.bunker_era_3))
        self.add_button("选择5", lambda: self.choice(4, 0, 0, 0, 4, self.bunker_era_3))
    
    def bunker_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
    掩体纪元：二向箔
═══════════════════════════════════════

一片二向箔从天而降。

它看起来如此美丽，像一张透明的卡片。
但它的本质是降维打击——
将三维空间降为二维。

太阳系开始坍缩。
掩体没有任何作用。
巨行星和它们背后的城市一起，
被压缩成二维的画面。

只有"星环"号和少数光速飞船逃离。

人类文明几乎全灭。

在最后的时刻，你的选择是：

1. 【坚守到底】与文明共存亡
2. 【逃向星空】加入逃亡的飞船
3. 【记录一切】为后世留下人类的记忆
4. 【寻找希望】相信还有生还的可能
5. 【接受命运】平静地面对终结
6. 【最后的抗争】即使无用也要反抗""")
        self.add_button("选择1", lambda: self.choice(6, 0, 0, 0, 0, self.calculate_ending))
        self.add_button("选择2", lambda: self.choice(0, 6, 0, 0, 0, self.calculate_ending))
        self.add_button("选择3", lambda: self.choice(0, 0, 6, 0, 0, self.calculate_ending))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 6, 0, self.calculate_ending))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 6, self.calculate_ending))
        self.add_button("选择6", lambda: self.choice(3, 3, 0, 0, 3, self.calculate_ending))
    
    # 扩张纪元（胜利路线专属）
    def expansion_era_1(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
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
        self.add_button("选择1", lambda: self.choice(5, 0, 0, 0, 0, self.expansion_era_2))
        self.add_button("选择2", lambda: self.choice(0, 5, 0, 0, 0, self.expansion_era_2))
        self.add_button("选择3", lambda: self.choice(0, 0, 5, 0, 0, self.expansion_era_2))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 5, 0, self.expansion_era_2))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 5, self.expansion_era_2))
    
    def expansion_era_2(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
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
        self.add_button("选择1", lambda: self.choice(4, 4, 0, 0, 0, self.expansion_era_3))
        self.add_button("选择2", lambda: self.choice(0, 4, 4, 0, 0, self.expansion_era_3))
        self.add_button("选择3", lambda: self.choice(0, 0, 4, 4, 0, self.expansion_era_3))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 4, 4, self.expansion_era_3))
        self.add_button("选择5", lambda: self.choice(4, 0, 0, 0, 4, self.expansion_era_3))
    
    def expansion_era_3(self):
        self.clear_buttons()
        self.show_text("""═══════════════════════════════════════
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
        self.add_button("选择1", lambda: self.choice(6, 0, 0, 0, 0, self.calculate_ending))
        self.add_button("选择2", lambda: self.choice(0, 6, 0, 0, 0, self.calculate_ending))
        self.add_button("选择3", lambda: self.choice(0, 0, 6, 0, 0, self.calculate_ending))
        self.add_button("选择4", lambda: self.choice(0, 0, 0, 6, 0, self.calculate_ending))
        self.add_button("选择5", lambda: self.choice(0, 0, 0, 0, 6, self.calculate_ending))
        self.add_button("选择6", lambda: self.choice(3, 3, 3, 3, 0, self.calculate_ending))
    
    def choice(self, survival, tech, moral, aggr, unity, next_func):
        self.score['survival'] += survival
        self.score['technology'] += tech
        self.score['morality'] += moral
        self.score['aggression'] += aggr
        self.score['unity'] += unity
        next_func()
    
    def calculate_ending(self):
        # 判断最终纪元
        if 'victory' in self.era_path:
            final_era = 'expansion'
        else:
            final_era = 'bunker'
        
        # 找出最高属性
        sorted_scores = sorted(self.score.items(), key=lambda x: x[1], reverse=True)
        primary = sorted_scores[0][0]
        primary_val = sorted_scores[0][1]
        secondary = sorted_scores[1][0]
        
        # 根据纪元+属性决定结局
        if final_era == 'expansion':
            if primary == 'survival':
                if primary_val >= 40:
                    self.ending(19)
                else:
                    self.ending(20)
            elif primary == 'technology':
                if primary_val >= 40:
                    self.ending(21)
                else:
                    self.ending(22)
            elif primary == 'morality':
                self.ending(23)
            elif primary == 'aggression':
                if primary_val >= 40:
                    self.ending(24)
                else:
                    self.ending(25)
            else:  # unity
                self.ending(26)
        else:  # bunker
            if primary == 'survival':
                if primary_val >= 35:
                    self.ending(27)
                else:
                    self.ending(28)
            elif primary == 'technology':
                if primary_val >= 35:
                    self.ending(29)
                else:
                    self.ending(30)
            elif primary == 'morality':
                if primary_val >= 35:
                    self.ending(31)
                else:
                    self.ending(32)
            elif primary == 'aggression':
                self.ending(33)
            else:  # unity
                if primary_val >= 35:
                    self.ending(34)
                else:
                    self.ending(35)
    
    def ending(self, num):
        self.clear_buttons()
        # 根据结局编号获取文本
        ending_texts = {
            19: """═══════════════════════════════════════
    扩张结局：永恒的生存者
═══════════════════════════════════════

你选择了生存至上的道路。

人类文明成为了宇宙中最顽强的生存者。
无论面对多强大的敌人，人类总能找到生存的方法。

殖民地遍布银河系。
即使某些星系被摧毁，人类文明也能延续。

但代价是——人类失去了很多东西。
道德、文化、甚至人性本身。

这是一个生存的文明，但还是"人类"吗？

【成就解锁：终极生存者】""",
            20: """═══════════════════════════════════════
    扩张结局：流浪的种族
═══════════════════════════════════════

你选择了生存，但保留了人性。

人类成为了宇宙中的流浪者。
不断迁徙，不断适应，但始终保持着人类的本质。

这是一个艰难的道路。
但人类证明了：生存不一定要放弃一切。

【成就解锁：星际流浪者】""",
            21: """═══════════════════════════════════════
    扩张结局：技术奇点
═══════════════════════════════════════

你选择了技术至上的道路。

人类的科技达到了难以想象的高度。
掌握了维度技术、时间技术、甚至宇宙规律的修改。

人类成为了宇宙中的"神级文明"。

但在技术的巅峰，人类发现：
宇宙本身可能只是一个更高维度的实验。

【成就解锁：技术之神】""",
            22: """═══════════════════════════════════════
    扩张结局：科技文明
═══════════════════════════════════════

你选择了科技发展的道路。

人类成为了一个高度发达的科技文明。
虽然不是最强大的，但在银河系中占有一席之地。

这是一个平衡的结局。
人类既保持了发展，也保留了人性。

【成就解锁：科技文明】""",
            23: """═══════════════════════════════════════
    扩张结局：道德灯塔
═══════════════════════════════════════

你选择了道德至上的道路。

人类成为了宇宙中的道德灯塔。
即使在黑暗森林中，也坚持着文明的底线。

许多文明被人类的精神所感动。
一个以道德为基础的宇宙联盟逐渐形成。

这是一个理想主义的结局。
但也许，理想本身就是最大的力量。

【成就解锁：文明之光】""",
            24: """═══════════════════════════════════════
    扩张结局：银河霸主
═══════════════════════════════════════

你选择了征服的道路。

人类成为了银河系的霸主。
强大的军事力量让所有文明臣服。

人类建立了一个庞大的帝国。
地球成为了银河系的首都。

但在征服的顶点，你是否想过：
人类会成为下一个被黑暗森林打击的目标吗？

【成就解锁：银河帝国】""",
            25: """═══════════════════════════════════════
    扩张结局：战争机器
═══════════════════════════════════════

你选择了军事扩张的道路。

人类成为了一个战争机器。
不断征服，不断扩张。

但在无尽的战争中，
人类逐渐失去了和平的能力。

这是一个悲剧的结局。
人类赢得了战争，却失去了自己。

【成就解锁：永恒战争】""",
            26: """═══════════════════════════════════════
    扩张结局：宇宙联邦
═══════════════════════════════════════

你选择了团结的道路。

人类成为了宇宙联邦的核心。
不同的文明在人类的组织下团结起来。

这是一个理想的结局。
宇宙不再是黑暗森林，而是一个大家庭。

但这个联邦能持续多久？
当面对更强大的威胁时，团结还能维持吗？

【成就解锁：宇宙联邦】""",
            27: """═══════════════════════════════════════
    掩体结局：最后的幸存者
═══════════════════════════════════════

二向箔降临。
太阳系坍缩为二维。

但你活了下来。

作为少数逃离的人类之一，
你见证了文明的终结。

在逃亡的飞船上，
你带着人类文明的记忆，
飞向未知的星空。

这是一个悲壮的结局。
人类文明几乎全灭，但火种还在。

【成就解锁：文明火种】""",
            28: """═══════════════════════════════════════
    掩体结局：二维的永恒
═══════════════════════════════════════

你选择留在太阳系。

当二向箔降临时，
你和整个太阳系一起，
被压缩成二维的画面。

在二维世界中，
太阳系成为了一幅永恒的画。
美丽，但已经死去。

这是一个悲剧的结局。
人类文明随太阳系一起终结。

【成就解锁：二维纪念碑】""",
            29: """═══════════════════════════════════════
    掩体结局：技术的遗产
═══════════════════════════════════════

在最后时刻，
你将人类的所有技术和知识，
压缩进一个信息包，
发送向宇宙深处。

也许有一天，
某个文明会发现这个信息包，
了解曾经有一个叫"人类"的文明。

这是一个悲伤但不绝望的结局。
人类的智慧将在宇宙中永存。

【成就解锁：知识遗产】""",
            30: """═══════════════════════════════════════
    掩体结局：科技的局限
═══════════════════════════════════════

人类的科技无法对抗降维打击。

所有的掩体，所有的防御，
在二向箔面前都毫无意义。

这是一个残酷的教训：
科技不是万能的。

人类文明终结了。

【成就解锁：技术的终点】""",
            31: """═══════════════════════════════════════
    掩体结局：人性的光辉
═══════════════════════════════════════

在最后的时刻，
人类展现了最美好的一面。

没有恐慌，没有混乱。
人们互相安慰，互相拥抱。

程心和艾AA在"星环"号上，
看着太阳系坍缩成二维。

她们带着人类最美好的记忆，
飞向星空。

这是一个悲伤但温暖的结局。
人类文明虽然终结，但人性永存。

【成就解锁：人性之光】""",
            32: """═══════════════════════════════════════
    掩体结局：道德的代价
═══════════════════════════════════════

人类坚持了道德，
拒绝建造光速飞船。

因为光速飞船的航迹，
会暴露地球的坐标。

但最终，坐标还是被暴露了。
道德没能拯救人类。

这是一个讽刺的结局。
善良的选择，导致了毁灭的结果。

【成就解锁：道德困境】""",
            33: """═══════════════════════════════════════
    掩体结局：无用的反抗
═══════════════════════════════════════

你选择了战斗。

人类向二向箔发射了所有武器。
核弹、反物质弹、甚至引力波...

但一切都是徒劳的。

二向箔不可阻挡。
太阳系坍缩为二维。

这是一个悲壮的结局。
人类战斗到了最后一刻。

【成就解锁：最后的战斗】""",
            34: """═══════════════════════════════════════
    掩体结局：团结的奇迹
═══════════════════════════════════════

在最后时刻，
全人类团结起来。

所有的飞船，所有的资源，
都用来拯救尽可能多的人。

虽然大部分人类还是死去了，
但数百万人成功逃离。

他们将在宇宙中重建人类文明。

这是一个悲伤但充满希望的结局。
团结创造了奇迹。

【成就解锁：团结的力量】""",
            35: """═══════════════════════════════════════
    掩体结局：分散的希望
═══════════════════════════════════════

人类没有完全团结，
但也没有完全分裂。

一些人逃离了，一些人留下了。
一些人选择战斗，一些人选择接受。

人类文明以不同的形式延续着。

这是一个现实的结局。
不完美，但这就是人类。

【成就解锁：人类的多样性】""",
        }
        text = ending_texts.get(num, "未知结局")
        text += f"\n\n你的属性:\n"
        text += f"生存意志: {self.score['survival']}\n"
        text += f"科技发展: {self.score['technology']}\n"
        text += f"道德水平: {self.score['morality']}\n"
        text += f"侵略性: {self.score['aggression']}\n"
        text += f"团结度: {self.score['unity']}\n"
        text += f"\n经历纪元: {' → '.join(self.era_path)}"
        self.show_text(text)
        self.add_button("重新开始", self.restart_game)
        self.add_button("退出游戏", self.root.quit)
        text += f"生存意志: {self.score['survival']}\n"
        text += f"科技发展: {self.score['technology']}\n"
        text += f"道德水平: {self.score['morality']}\n"
        text += f"侵略性: {self.score['aggression']}\n"
        text += f"团结度: {self.score['unity']}\n"
        text += f"\n经历纪元: {' → '.join(self.era_path)}"
        self.show_text(text)
        self.add_button("重新开始", self.restart_game)
        self.add_button("退出游戏", self.root.quit)
    
    def restart_game(self):
        self.score = {'survival': 0, 'technology': 0, 'morality': 0, 'aggression': 0, 'unity': 0}
        self.era_path = []
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = ThreeBodyGame(root)
    root.mainloop()
