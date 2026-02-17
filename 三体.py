import random
import time

def slow_print(text, delay=0.03):
    """逐字打印效果"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dramatic_pause(seconds=1):
    """戏剧性停顿"""
    time.sleep(seconds)

# ==================== 游戏开始 ====================
print("=" * 50)
print("        《三体》文字穿越游戏")
print("        基于刘慈欣同名小说")
print("=" * 50)
print()

name = input("欢迎进入小说穿梭机，请输入你的姓名：")
print(f"你好，{name}！")

choice = input("请输入您的性别（1=男 / 2=女）：")
XB = "男" if choice == "1" else "女" if choice == "2" else "男"

if XB == "男":
    SF = random.choice(["正太", "少年", "青年男子", "大叔"])
else:
    SF = random.choice(["萝莉", "少女", "女青年", "成熟女性"])

print()
slow_print(f"第一年，作为一名{SF}，你穿越到了刘慈欣所著的《三体》世界里。")

# 穿越地点
DF = random.choice(["科研基地", "乡村", "小城市", "农场", "大学"])
slow_print(f"穿越后你发现自己出现在了一个{DF}里。")
slow_print(f"你来到了一个与前生完全不同的陌生世界，在{DF}里，好在是魂穿，没过多久就无缝融入了当地社会中。")

# 时代背景描述
if DF == "科研基地":
    slow_print(f"在{DF}和科研人员的交谈中，你得知自己来到了一个与世纪初祖国很相似的国内环境，实验室布满了有些年代的老旧仪器和实验机器，视觉中在科技感之余还多了一层沧桑。")
elif DF == "乡村":
    slow_print(f"在{DF}的田野里，你被看热闹的村民围住，交流中你得知自己来到了近似世纪初祖国的世界，村民们敦厚淳朴和你热情地拉扯起家长里短。")
elif DF == "小城市":
    slow_print(f"在{DF}的街道中，你行走在车来车往熙熙攘攘的马路上，在马路上的巨幅广告牌旁，你获知自己来到了2007年初的中国。")
elif DF == "农场":
    slow_print(f"在{DF}，你被农场的工友发现在劳动中晕倒在了庄稼上。你揉了揉眼醒来，在和工友的闲聊中得知自己来到了一个和世纪初的祖国差不多的世界。")
elif DF == "大学":
    slow_print(f"在{DF}的课堂里，你走神被嬉笑的同学唤醒。下课后，你看了一下课本的内容并从课本资料中了解自己来到了2007年初的中国。")

# 工作和遇到的人物
if DF == "科研基地":
    GZ = random.choice(["打杂清洁", "辅助实验", "整理档案", "后厨烧饭"])
    RS = random.choice(["汪淼", "叶文洁", "丁仪", "罗辑"])
elif DF == "乡村":
    GZ = random.choice(["种地", "征粮", "养殖鱼类", "饲养家畜"])
    RS = random.choice(["汪淼", "叶文洁", "丁仪", "罗辑"])
elif DF == "小城市":
    GZ = random.choice(["工厂", "供销社", "修鞋等修补", "宣传员"])
    RS = random.choice(["汪淼", "叶文洁", "丁仪", "罗辑"])
elif DF == "农场":
    GZ = random.choice(["繁重劳动", "挑水砍柴", "插秧犁地", "给农场人员做思想教育"])
    RS = random.choice(["汪淼", "叶文洁", "丁仪", "罗辑"])
elif DF == "大学":
    GZ = random.choice(["给导师担任助理", "辅助实验", "下乡义务劳动", "为班级布置文艺活动"])
    RS = random.choice(["汪淼", "叶文洁", "丁仪", "罗辑"])

slow_print(f"你在{DF}附近，以{GZ}为生，渐渐融入了所在环境中。")
slow_print(f"并且在{DF}的{GZ}工作中，结识到了{RS}。")

# 人物介绍
print()
if RS == "汪淼":
    slow_print("你从周围人的交谈中得知，汪淼是国家科学院院士，科研任务紧迫，正在进行纳米材料的研究。")
    slow_print("他为人谦和，但最近似乎心事重重，时常望着天空发呆...")
elif RS == "叶文洁":
    slow_print("叶文洁年岁已高，头发花白，身材瘦削，目前正于清华大学任教，外表看上去像一个慈祥的老太太。")
    slow_print("但你偶尔能从她深邃的眼神中，看到一种难以言喻的沧桑与秘密...")
elif RS == "丁仪":
    slow_print("丁仪是一名物理学家，为人不修边幅，爱喝酒；但又非常有才能。")
    slow_print("曾在对球状闪电的研究中发现宏原子而闻名于世。他总是说一些让人摸不着头脑的话...")
elif RS == "罗辑":
    slow_print("罗辑是一名大学社会学教授，为人玩世不恭，喜欢泡妞和享乐。")
    slow_print("但你隐约觉得，在他那副吊儿郎当的外表下，藏着某种深不可测的东西...")

dramatic_pause(2)

# ==================== 第一章：命运的齿轮 ====================
print()
print("=" * 50)
print("        第一章：命运的齿轮")
print("=" * 50)
print()

# 初始化玩家属性
player_stats = {
    "trust": 0,  # 信任度
    "knowledge": 0,  # 知识水平
    "influence": 0,  # 影响力
    "survival": 0  # 生存能力
}

# 根据主角展开不同剧情
if RS == "汪淼":
    # 汪淼线：倒计时与纳米材料
    slow_print("几个月后的一天，汪淼突然找到你，神色慌张。")
    slow_print(f"「{name}，你...你能看到吗？」他指着自己的眼睛。")
    slow_print("「看到什么？」你疑惑地问。")
    slow_print("「倒计时...我眼前一直有倒计时...」汪淼的声音在颤抖。")
    print()
    
    print("【第一个选择】")
    choice1 = input("你选择：\n1. 安慰他可能是幻觉，建议休息\n2. 认真询问详情，记录现象\n3. 建议他去看医生做检查\n4. 询问是否有其他科学家遇到类似情况\n5. 提议一起调查这个现象的原因\n请选择(1-5)：")
    
    if choice1 == "2":
        slow_print("你认真地听汪淼讲述了他的遭遇——")
        slow_print("科学边界组织、三体游戏、宇宙闪烁...")
        player_stats["trust"] += 2
        player_stats["knowledge"] += 2
    elif choice1 == "4":
        slow_print("汪淼告诉你，丁仪和其他几位物理学家也遇到了类似的怪事。")
        slow_print("粒子加速器的实验结果完全混乱...")
        player_stats["knowledge"] += 1
        player_stats["trust"] += 1
    elif choice1 == "5":
        slow_print("汪淼感激地看着你：「我就知道你会相信我。」")
        slow_print("他决定带你一起深入调查。")
        player_stats["trust"] += 3
    else:
        slow_print("汪淼失望地离开了。但几天后，他又来找你。")
        slow_print("这一次，他带来了更多证据...")
        player_stats["trust"] += 1
    
    dramatic_pause(1)
    print()
    print("【第二个选择】")
    slow_print("汪淼邀请你参加一个神秘的聚会——科学边界组织的集会。")
    choice2 = input("你选择：\n1. 欣然前往，想了解更多\n2. 婉拒，觉得太危险\n3. 答应去，但暗中通知警方\n4. 提议先调查这个组织的背景\n5. 要求汪淼先告诉你更多信息\n6. 建议带上其他可信任的人一起去\n请选择(1-6)：")
    
    if choice2 == "1":
        slow_print("在聚会上，你见到了各种各样的人——")
        slow_print("科学家、企业家、甚至还有军方人员...")
        slow_print("他们都在讨论一个话题：三体文明。")
        player_stats["knowledge"] += 3
        player_stats["influence"] += 1
        know_eto = True
    elif choice2 == "3":
        slow_print("警方突袭了聚会现场！")
        slow_print("但你发现，这个组织的势力远比想象的要大...")
        slow_print("汪淼对你的背叛感到愤怒。")
        player_stats["trust"] -= 2
        player_stats["survival"] += 2
        know_eto = True
    elif choice2 == "4":
        slow_print("你花了几天时间调查，发现这个组织与多起科学家自杀案有关...")
        slow_print("这让你更加警惕。")
        player_stats["knowledge"] += 2
        player_stats["survival"] += 1
        know_eto = True
    else:
        slow_print("你最终还是去了，但保持着警惕。")
        player_stats["knowledge"] += 1
        player_stats["survival"] += 1
        know_eto = True
    
    dramatic_pause(1)
    print()
    print("【第三个选择】")
    slow_print("你得知了「古筝行动」——军方计划用纳米丝切割审判日号。")
    slow_print("汪淼的纳米材料将成为关键。")
    choice3 = input("你选择：\n1. 全力协助汪淼完成纳米材料\n2. 担心行动会造成人员伤亡，提出反对\n3. 建议先尝试和平谈判\n4. 要求参与行动现场\n5. 提议记录整个过程作为历史资料\n6. 暗中联系ETO组织，试图阻止行动\n7. 保持中立，观察事态发展\n请选择(1-7)：")
    
    if choice3 == "1":
        slow_print("在你的协助下，纳米材料提前完成。")
        slow_print("古筝行动取得了完美成功！")
        player_stats["trust"] += 3
        player_stats["influence"] += 2
        action_success = True
    elif choice3 == "2":
        slow_print("你的反对被驳回了。")
        slow_print("「这是战争，」常伟思将军说，「必须有牺牲。」")
        player_stats["trust"] -= 1
        action_success = True
    elif choice3 == "4":
        slow_print("你登上了观察船，亲眼见证了这惊心动魄的一幕——")
        slow_print("纳米丝如同死神的琴弦，将审判日号切成了薄片...")
        player_stats["knowledge"] += 2
        player_stats["survival"] += 1
        action_success = True
    elif choice3 == "6":
        slow_print("你的背叛被发现了！")
        slow_print("但古筝行动还是成功了。你被军方逮捕...")
        player_stats["trust"] -= 5
        player_stats["survival"] -= 3
        action_success = True
        arrested = True
    else:
        slow_print("行动如期进行。")
        slow_print("三体文明的存在，终于被证实了。")
        player_stats["knowledge"] += 1
        action_success = True
    
    trust_level = player_stats["trust"]

elif RS == "叶文洁":
    # 叶文洁线：红岸往事
    slow_print("一个深夜，你无意中发现叶文洁独自坐在天台上，望着星空。")
    slow_print("「叶教授，您还没休息？」你走上前去。")
    slow_print("她转过头，眼中闪烁着复杂的光芒。")
    slow_print("「你相信...宇宙中有其他文明吗？」她轻声问道。")
    print()
    
    choice = input("你选择：1. 相信，宇宙这么大  2. 不太相信  3. 反问她为什么这么问\n请选择(1/2/3)：")
    
    if choice == "1" or choice == "3":
        slow_print("叶文洁沉默了很久，然后开始讲述一个尘封多年的故事——")
        slow_print("红岸基地、那个改变人类命运的信号、以及她年轻时做出的选择...")
        slow_print("「我向太阳发射了信号，利用太阳作为放大器...」")
        slow_print("「八年后，我收到了回复...」")
        slow_print("你震惊得说不出话来。")
        know_truth = True
    else:
        slow_print("叶文洁只是笑了笑，没有再说什么。")
        slow_print("但你注意到，她的眼角似乎有泪光闪过...")
        know_truth = False
    
    dramatic_pause(1)
    slow_print("无论你是否知道真相，历史的车轮已经开始转动。")
    slow_print("三体舰队，正在向地球进发...")

elif RS == "丁仪":
    # 丁仪线：水滴与物理学的尽头
    slow_print("丁仪总是喜欢拉着你喝酒，讨论一些奇怪的物理问题。")
    slow_print("「你知道吗，」他醉醺醺地说，「物理学可能已经死了。」")
    slow_print("「什么意思？」你不解。")
    slow_print("「粒子加速器的结果...完全是随机的。好像有人在捣乱...」")
    print()
    
    choice = input("你选择：1. 这不可能，物理定律是恒定的  2. 也许真的有什么在干扰  3. 你喝多了，丁教授\n请选择(1/2/3)：")
    
    slow_print("丁仪大笑起来：「智子！是智子在锁死我们的科技！」")
    slow_print("「三体人派来的智子，一种质子级的超级计算机...」")
    slow_print("「它们无处不在，监视着我们的一切...」")
    
    dramatic_pause(1)
    slow_print("多年后，当三体探测器「水滴」到达太阳系时...")
    slow_print("丁仪作为科学家代表，登上了前往迎接的飞船。")
    slow_print("你在地球上，通过直播看到了那个美丽而致命的水滴...")
    slow_print("以及随后发生的，人类舰队的毁灭。")
    slow_print("丁仪，再也没有回来。")

elif RS == "罗辑":
    # 罗辑线：面壁者的诞生
    slow_print("罗辑的生活一如既往地悠闲——上课、泡妞、喝酒。")
    slow_print("直到有一天，一切都变了。")
    slow_print("「联合国要见我？」罗辑一脸懵逼，「我又没犯法。」")
    print()
    slow_print("你陪他去了联合国。")
    slow_print("在那里，罗辑被宣布为「面壁者」——")
    slow_print("四个被赋予无限权力、制定对抗三体计划的人之一。")
    print()
    
    choice = input("你选择：1. 恭喜他获得如此殊荣  2. 担心他的安全  3. 觉得这是个阴谋\n请选择(1/2/3)：")
    
    slow_print("罗辑自己也不明白为什么被选中。")
    slow_print("但三体人似乎非常害怕他——")
    slow_print("ETO组织开始疯狂地追杀他。")
    slow_print("「为什么是我？」罗辑问叶文洁。")
    slow_print("叶文洁只说了两个字：「宇宙社会学。」")
    
    dramatic_pause(1)
    slow_print("在接下来的岁月里，你见证了罗辑从一个玩世不恭的教授...")
    slow_print("逐渐蜕变为人类文明的守护者。")
    slow_print("他发现了黑暗森林法则，建立了对三体的威慑...")
    slow_print("成为了真正的「执剑人」。")

# ==================== 第二章：危机纪元 ====================
print()
print("=" * 50)
print("        第二章：危机纪元")
print("=" * 50)
print()

slow_print("时间流逝，人类进入了「危机纪元」。")
slow_print("三体舰队预计将在400年后到达地球。")
slow_print("整个人类社会都在为这场终极对决做准备。")
print()

# 随机事件：平行世界分支
parallel_event = random.random()

if parallel_event < 0.1:
    # 10%概率：三体人提前发展出光速引擎
    print()
    print("【平行世界事件】")
    slow_print("然而，命运在这个世界线上发生了可怕的偏转——")
    slow_print("三体人比预期更快地发展出了光速引擎！")
    slow_print("原本需要400年的航程，被缩短到了50年！")
    print()
    slow_print("人类措手不及。")
    slow_print("面壁计划还未完成，太空舰队还在建设中...")
    slow_print("当三体舰队出现在太阳系边缘时，地球陷入了绝望。")
    print()
    
    choice = input("面对这个绝境，你选择：1. 加入地下抵抗组织  2. 尝试与三体人谈判  3. 寻找逃离太阳系的方法\n请选择(1/2/3)：")
    
    if choice == "1":
        slow_print("你加入了人类最后的抵抗力量。")
        slow_print("虽然科技差距巨大，但人类的意志从未屈服。")
        slow_print("在地下城市中，你们用游击战术与三体人周旋...")
        ending = "resistance"
    elif choice == "2":
        slow_print("你冒险尝试与三体人建立联系。")
        slow_print("出乎意料的是，三体世界中也有和平派...")
        slow_print("经过艰难的谈判，人类获得了在太阳系边缘生存的权利。")
        ending = "negotiation"
    else:
        slow_print("你参与了「方舟计划」——建造逃离太阳系的飞船。")
        slow_print("虽然只有少数人能够离开，但人类的火种得以延续...")
        slow_print("在茫茫宇宙中，寻找新的家园。")
        ending = "escape"

elif parallel_event < 0.2:
    # 10%概率：人类提前击败三体
    print()
    print("【平行世界事件】")
    slow_print("在这个世界线上，人类的运气出奇地好——")
    slow_print("一位天才科学家发现了智子的漏洞！")
    slow_print("人类成功破解了智子的封锁，科技开始爆发式发展！")
    print()
    slow_print("仅仅100年后，人类就掌握了曲率驱动技术。")
    slow_print("当三体舰队还在半路上时，人类舰队已经迎了上去。")
    slow_print("一场单方面的屠杀开始了——这次，人类是猎人。")
    print()
    
    choice = input("面对胜利，你选择：1. 主张彻底消灭三体文明  2. 呼吁和平共处  3. 担忧黑暗森林的后果\n请选择(1/2/3)：")
    
    if choice == "1":
        slow_print("人类舰队追击到了三体星系。")
        slow_print("三颗恒星的混乱舞蹈中，三体文明被彻底摧毁。")
        slow_print("人类成为了太阳系附近最强大的文明...")
        slow_print("但这份力量，也让人类变得傲慢而危险。")
        ending = "conqueror"
    elif choice == "2":
        slow_print("在你的呼吁下，人类选择了宽恕。")
        slow_print("三体人被允许在太阳系边缘建立殖民地。")
        slow_print("两个文明开始了艰难但真诚的交流...")
        slow_print("也许，这才是宇宙中最珍贵的东西。")
        ending = "peace"
    else:
        slow_print("你的担忧是对的。")
        slow_print("人类与三体的战争，暴露了太阳系的位置。")
        slow_print("更强大的文明注意到了这里...")
        slow_print("黑暗森林中的猎人，正在瞄准。")
        ending = "dark_forest"

else:
    # 80%概率：正常剧情
    slow_print("在漫长的等待中，人类社会经历了巨大的变化。")
    slow_print("有人绝望，有人奋斗，有人背叛，有人坚守。")
    print()
    
    # 根据之前的主角，展开后续剧情
    if RS == "汪淼":
        slow_print("汪淼的纳米材料技术，成为了太空电梯的关键。")
        slow_print("你协助他完成了这项伟大的工程。")
        slow_print("当第一批人类乘坐电梯进入太空时，你站在地面上，热泪盈眶。")
    elif RS == "叶文洁":
        slow_print("叶文洁在晚年写下了回忆录，记录了红岸的一切。")
        slow_print("你是她最信任的助手，帮助她整理这些珍贵的历史。")
        slow_print("「历史会审判我的，」她说，「但我不后悔。」")
    elif RS == "丁仪":
        slow_print("丁仪虽然牺牲了，但他的研究被你继承了下来。")
        slow_print("你继续探索着物理学的边界，寻找突破智子封锁的方法。")
        slow_print("「物理学没有死，」你对自己说，「它只是在等待。」")
    elif RS == "罗辑":
        slow_print("作为罗辑最亲近的朋友，你见证了他的一切。")
        slow_print("从面壁者到执剑人，从被追杀到成为人类的守护神。")
        slow_print("「我只是做了我该做的，」罗辑说，「仅此而已。」")
    
    ending = "normal"

# ==================== 第三章：结局 ====================
print()
print("=" * 50)
print("        第三章：宇宙的回响")
print("=" * 50)
print()

if ending == "resistance":
    slow_print("抵抗持续了很多年。")
    slow_print("虽然人类最终没能夺回地球，但精神从未被征服。")
    slow_print(f"而你，{name}，成为了抵抗军的传奇人物。")
    slow_print("在地下城市的壁画上，你的名字与人类最伟大的英雄并列。")
    
elif ending == "negotiation":
    slow_print("和平来之不易，但它确实实现了。")
    slow_print("人类和三体人开始了漫长的共存之路。")
    slow_print(f"而你，{name}，作为第一批「星际外交官」，")
    slow_print("为两个文明的理解架起了桥梁。")
    
elif ending == "escape":
    slow_print("方舟飞船在宇宙中航行了数百年。")
    slow_print("当它终于找到一颗宜居行星时，船上的人类已经繁衍了好几代。")
    slow_print(f"而你，{name}，虽然早已化为尘土，")
    slow_print("但你的名字被刻在了新世界的第一块纪念碑上。")
    
elif ending == "conqueror":
    slow_print("人类成为了宇宙中的霸主。")
    slow_print("但权力带来了腐败，傲慢带来了毁灭。")
    slow_print(f"在你生命的最后时刻，{name}，你看着人类重蹈三体的覆辙，")
    slow_print("不禁想起了那句古老的话：「凝视深渊时，深渊也在凝视你。」")
    
elif ending == "peace":
    slow_print("两个文明的融合，创造了前所未有的奇迹。")
    slow_print("人类学会了三体的技术，三体人学会了人类的情感。")
    slow_print(f"而你，{name}，成为了「星际和平奖」的第一位获得者。")
    slow_print("在颁奖典礼上，你说：「宇宙很大，但爱更大。」")
    
elif ending == "dark_forest":
    slow_print("黑暗森林的打击来得很快。")
    slow_print("一颗光粒，将太阳变成了死星。")
    slow_print("人类和三体，这对曾经的宿敌，在末日面前终于和解。")
    slow_print(f"在最后的时刻，{name}，你握着一个三体人的手，")
    slow_print("一起看着太阳最后的光芒。")
    slow_print("「至少，」你说，「我们不是孤独地死去。」")
    
else:  # normal ending
    slow_print("岁月流逝，你在这个世界度过了漫长而充实的一生。")
    slow_print(f"作为{RS}的朋友和同伴，你见证了人类历史上最波澜壮阔的时代。")
    print()
    
    final_event = random.choice([
        "你看到了人类舰队与水滴的第一次接触。",
        "你参与了黑暗森林威慑的建立。",
        "你见证了地球文明向宇宙广播自己的坐标。",
        "你在冬眠中醒来，看到了数百年后的新世界。",
        "你的后代登上了飞向新星系的飞船。"
    ])
    slow_print(final_event)
    print()
    slow_print("在生命的尽头，你望着星空，想起了穿越那天的自己。")
    slow_print(f"「{name}，」你对自己说，「这一趟，值了。」")

# ==================== 游戏结束 ====================
print()
print("=" * 50)
print("        【游戏结束】")
print("=" * 50)
print()
print(f"玩家：{name}")
print(f"身份：{SF}")
print(f"穿越地点：{DF}")
print(f"结识人物：{RS}")
print(f"结局类型：{ending}")
print()
print("感谢游玩《三体》文字穿越游戏！")
print("「给岁月以文明，而不是给文明以岁月。」")
print()

# 是否重玩
replay = input("是否重新开始？(y/n)：")
if replay.lower() == 'y':
    exec(open(__file__).read())
