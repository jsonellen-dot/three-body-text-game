#!/usr/bin/env python3
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, simpledialog
import random
from datetime import datetime

class SantiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("《三体》文字穿越游戏 - 扩展版")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a2e")
        
        self.log = []
        self.name = ""
        self.choices_made = []
        self.era_results = {}
        
        # 文本显示区
        self.text_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, font=("SimHei", 11),
            bg="#16213e", fg="#e8e8e8", insertbackground="white"
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_area.config(state=tk.DISABLED)
        
        # 按钮容器
        self.btn_frame = tk.Frame(root, bg="#1a1a2e")
        self.btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # 创建7个按钮
        self.buttons = []
        for i in range(7):
            btn = tk.Button(self.btn_frame, text=f"选项{i+1}", 
                          command=lambda x=i: self.choose(x),
                          font=("SimHei", 10), bg="#0f3460", fg="white", width=12)
            btn.pack(side=tk.LEFT, padx=3)
            self.buttons.append(btn)
        
        # 控制按钮框架
        ctrl_frame = tk.Frame(root, bg="#1a1a2e")
        ctrl_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.export_btn = tk.Button(ctrl_frame, text="导出日志", command=self.export_log,
                                    font=("SimHei", 10), bg="#e94560", fg="white", width=12)
        self.export_btn.pack(side=tk.RIGHT, padx=5)
        
        self.restart_btn = tk.Button(ctrl_frame, text="重新开始", command=self.restart,
                                     font=("SimHei", 10), bg="#533483", fg="white", width=12)
        self.restart_btn.pack(side=tk.RIGHT, padx=5)
        
        self.hide_all_buttons()
        self.current_stage = 0
        self.choice = 0
        
        self.root.after(500, self.start_game)
    
    def print_text(self, text):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)
        self.text_area.config(state=tk.DISABLED)
        self.log.append(text)
    
    def hide_all_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED, text="")
            btn.pack_forget()
    
    def show_buttons(self, *texts):
        self.hide_all_buttons()
        for i, text in enumerate(texts):
            if i < 7 and text:
                self.buttons[i].config(state=tk.NORMAL, text=text)
                self.buttons[i].pack(side=tk.LEFT, padx=3)
    
    def choose(self, c):
        self.choice = c
        self.choices_made.append(c)
        self.log.append(f"[选择] 选项{c+1}")
        self.hide_all_buttons()
        self.next_stage()
    
    def start_game(self):
        self.print_text("=" * 60)
        self.print_text("        《三体》文字穿越游戏 - 扩展版")
        self.print_text("        基于刘慈欣同名小说")
        self.print_text("=" * 60)
        self.print_text("")
        
        self.name = simpledialog.askstring("输入", "请输入你的姓名：", parent=self.root)
        if not self.name:
            self.name = "穿越者"
        self.print_text(f"欢迎，{self.name}！")
        
        self.current_stage = 1
        self.next_stage()
    
    def next_stage(self):
        stages = {
            1: self.stage_gender,
            2: self.stage_background,
            3: self.stage_first_contact,
            4: self.stage_crisis_era_1,
            5: self.stage_crisis_era_2,
            6: self.stage_deterrence_era_1,
            7: self.stage_deterrence_era_2,
            8: self.stage_broadcast_era_1,
            9: self.stage_broadcast_era_2,
            10: self.stage_bunker_era,
            11: self.stage_final_choice,
            12: self.stage_ending
        }
        
        if self.current_stage in stages:
            stages[self.current_stage]()
    
    def stage_gender(self):
        self.print_text("\n请选择你的性别：")
        self.show_buttons("男", "女")
    
    def stage_background(self):
        self.XB = "男" if self.choice == 0 else "女"
        self.SF = random.choice(["少年", "青年", "中年人"]) if self.XB == "男" else random.choice(["少女", "青年女性", "中年女性"])
        
        self.print_text(f"\n作为一名{self.SF}，你穿越到了《三体》世界。")
        self.print_text("\n你发现自己身处何地？")
        self.show_buttons("红岸基地", "科研院所", "大学校园", "ETO组织", "联合国总部")
        self.current_stage = 3
    
    def stage_first_contact(self):
        locations = ["红岸基地", "科研院所", "大学校园", "ETO组织", "联合国总部"]
        self.location = locations[self.choice]
        
        self.print_text(f"\n你来到了{self.location}。")
        
        if self.location == "红岸基地":
            self.print_text("在这里，你遇到了年轻的叶文洁。")
            self.print_text("她正在操作巨大的天线阵列...")
            self.print_text("\n你选择：")
            self.show_buttons("主动接近她", "暗中观察", "向上级报告异常", "尝试理解设备", "离开此地")
        elif self.location == "科研院所":
            self.print_text("你遇到了汪淼，他正为眼前的倒计时困扰。")
            self.print_text("\n你选择：")
            self.show_buttons("询问倒计时的事", "建议他休息", "提出一起调查", "保持距离观察", "寻求其他科学家帮助")
        elif self.location == "大学校园":
            self.print_text("你遇到了罗辑，他正在给学生上社会学课程。")
            self.print_text("\n你选择：")
            self.show_buttons("课后请教问题", "邀请他喝酒聊天", "询问宇宙社会学", "成为他的助教", "只是旁听")
        elif self.location == "ETO组织":
            self.print_text("你发现自己身处一个神秘组织的聚会。")
            self.print_text("他们在讨论「主」的降临...")
            self.print_text("\n你选择：")
            self.show_buttons("假装认同加入", "暗中收集情报", "立即逃离", "质疑他们的理念", "寻找叶文洁")
        else:  # 联合国总部
            self.print_text("你见证了面壁计划的启动仪式。")
            self.print_text("\n你选择：")
            self.show_buttons("申请成为面壁者助手", "观察各国反应", "寻找破壁人线索", "研究三体信息", "保持中立")
        
        self.current_stage = 4
    
    def stage_crisis_era_1(self):
        self.print_text("\n" + "=" * 60)
        self.print_text("        危机纪元 - 第一阶段")
        self.print_text("=" * 60)
        self.print_text("\n三体舰队已经启程，人类进入危机纪元。")
        self.print_text("智子锁死了地球科技，但人类并未放弃。")
        
        # 根据之前的选择影响剧情
        if self.location == "红岸基地":
            self.print_text("\n你掌握了红岸基地的秘密。")
            self.print_text("叶文洁向你透露了三体文明的真相。")
            self.print_text("\n你决定：")
            self.show_buttons("帮助ETO", "向政府揭发", "保持中立观察", "尝试与三体沟通", "寻找对抗方法", "销毁证据")
        elif self.location == "科研院所":
            self.print_text("\n古筝行动成功，你获得了大量三体信息。")
            self.print_text("\n你选择研究方向：")
            self.show_buttons("纳米材料", "理论物理", "太空工程", "生物技术", "人工智能", "社会学")
        elif self.location == "大学校园":
            self.print_text("\n罗辑被选为面壁者，你成为了他的密友。")
            self.print_text("\n你建议他：")
            self.show_buttons("研究宇宙社会学", "建立太空舰队", "发展地下城市", "冬眠到未来", "寻找外星盟友", "制定威慑计划")
        elif self.location == "ETO组织":
            self.print_text("\n你在ETO内部获得了重要地位。")
            self.print_text("但你的真实立场是：")
            self.show_buttons("真心拥护三体", "双面间谍", "寻求和平共存", "计划背叛", "保护人类", "追求真理")
        else:
            self.print_text("\n作为面壁计划的参与者，你提出：")
            self.show_buttons("太空舰队计划", "地球防御系统", "恒星级武器", "基因改造人类", "量子通讯网", "时间延缓技术")
        
        self.current_stage = 5
    
    def stage_crisis_era_2(self):
        self.era_results['crisis_1'] = self.choice
        
        self.print_text("\n数十年过去...")
        self.print_text("人类社会发生了巨大变化。")
        
        # 随机事件
        if random.random() < 0.2:
            self.print_text("\n【隐藏事件触发】")
            self.print_text("你意外发现了一个三体叛逃者的信息！")
            self.print_text("他警告：三体舰队中有内部分歧...")
            self.print_text("\n你如何处理这个情报：")
            self.show_buttons("立即公开", "秘密研究", "与罗辑分享", "卖给最高出价者", "销毁信息", "验证真伪")
            self.hidden_event = True
        else:
            self.hidden_event = False
            self.print_text("\n面对人类的分裂和逃亡主义：")
            self.show_buttons("支持逃亡派", "坚守地球派", "寻求第三条路", "建立太空城市", "冬眠到未来", "推动国际合作")
        
        self.current_stage = 6
    
    def stage_deterrence_era_1(self):
        self.era_results['crisis_2'] = self.choice
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        威慑纪元 - 第一阶段")
        self.print_text("=" * 60)
        self.print_text("\n罗辑发现了黑暗森林法则！")
        self.print_text("他建立了对三体的威慑系统。")
        self.print_text("三体舰队停止前进，人类获得了和平。")
        
        self.print_text("\n在这个黄金时代，你选择：")
        self.show_buttons("享受和平生活", "继续研究三体", "建设太空舰队", "警惕威慑失效", "推动文化交流", "准备后路", "研究黑暗森林")
        
        self.current_stage = 7
    
    def stage_deterrence_era_2(self):
        self.era_results['deterrence_1'] = self.choice
        
        self.print_text("\n60年的和平让人类变得软弱...")
        self.print_text("罗辑年老，需要选择新的执剑人。")
        self.print_text("程心成为了候选人。")
        
        self.print_text("\n你对程心的看法：")
        self.show_buttons("支持她的仁慈", "反对她当选", "保持中立", "推荐其他人", "自己竞选", "警告危险", "相信她会成长")
        
        self.current_stage = 8
    
    def stage_broadcast_era_1(self):
        self.era_results['deterrence_2'] = self.choice
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        广播纪元 - 第一阶段")
        self.print_text("=" * 60)
        self.print_text("\n程心接任执剑人仅15分钟...")
        self.print_text("水滴摧毁了所有引力波发射器！")
        self.print_text("威慑失效，三体舰队重新启动！")
        
        self.print_text("\n在这个绝望时刻：")
        self.show_buttons("逃往太空", "坚守地球", "寻找程心", "启动备用计划", "投降三体", "发动反击", "寻找万有引力号")
        
        self.current_stage = 9
    
    def stage_broadcast_era_2(self):
        self.era_results['broadcast_1'] = self.choice
        
        self.print_text("\n万有引力号和蓝色空间号向宇宙广播了三体坐标！")
        self.print_text("黑暗森林打击即将到来...")
        self.print_text("三体舰队紧急撤离。")
        
        self.print_text("\n人类获得了短暂的喘息，你选择：")
        self.show_buttons("研究光速飞船", "建造地下城市", "寻找新家园", "等待打击", "尝试沟通", "准备反击", "记录文明")
        
        self.current_stage = 10
    
    def stage_bunker_era(self):
        self.era_results['broadcast_2'] = self.choice
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        掩体纪元")
        self.print_text("=" * 60)
        self.print_text("\n人类在木星、土星等巨行星背后建立了掩体城市。")
        self.print_text("但云天明通过童话传递了重要信息...")
        
        self.print_text("\n你破解了童话的含义：")
        self.show_buttons("曲率驱动", "维度打击", "黑域计划", "全部都是", "无法理解", "不相信童话", "寻求帮助")
        
        self.current_stage = 11
    
    def stage_final_choice(self):
        self.era_results['bunker'] = self.choice
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        最终抉择")
        self.print_text("=" * 60)
        self.print_text("\n光粒打击即将到来！")
        self.print_text("太阳系将被二维化！")
        
        self.print_text(f"\n{self.name}，在文明的最后时刻...")
        self.print_text("你的最终选择是：")
        self.show_buttons("乘光速飞船逃离", "留在太阳系", "进入四维空间", "尝试阻止打击", "记录人类文明", "寻找程心", "接受命运")
        
        self.current_stage = 12
    
    def stage_ending(self):
        self.era_results['final'] = self.choice
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        终局")
        self.print_text("=" * 60)
        
        # 根据所有选择计算结局
        total_choices = len(self.choices_made)
        survival_score = sum(1 for c in [self.era_results.get('crisis_1', 0), 
                                         self.era_results.get('deterrence_1', 0),
                                         self.era_results.get('broadcast_1', 0)] if c in [0, 2, 6])
        
        final_choice = self.era_results.get('final', 0)
        
        self.print_text("")
        
        if final_choice == 0:  # 光速飞船逃离
            self.print_text("你登上了光速飞船，逃离了太阳系。")
            self.print_text("在茫茫宇宙中，你见证了太阳系的二维化...")
            self.print_text("人类文明的火种，在你和其他幸存者手中延续。")
            ending_type = "逃亡者"
        elif final_choice == 1:  # 留在太阳系
            self.print_text("你选择留在太阳系，与地球共存亡。")
            self.print_text("在二维化的过程中，你看到了宇宙最美丽也最残酷的景象...")
            self.print_text("你的意识永远定格在了这个瞬间。")
            ending_type = "殉道者"
        elif final_choice == 2:  # 进入四维空间
            self.print_text("你找到了进入四维空间的方法。")
            self.print_text("在那个不可思议的世界里，你遇到了云天明...")
            self.print_text("你们一起见证了宇宙的终极秘密。")
            ending_type = "探索者"
        elif final_choice == 3:  # 尝试阻止
            self.print_text("你尝试阻止维度打击，但这是徒劳的。")
            self.print_text("在最后时刻，你意识到这是宇宙的必然...")
            self.print_text("但你的勇气，永远值得铭记。")
            ending_type = "反抗者"
        elif final_choice == 4:  # 记录文明
            self.print_text("你用尽最后的时间，记录下人类文明的一切。")
            self.print_text("这些信息被发送到宇宙深处...")
            self.print_text("也许有一天，会有其他文明读到人类的故事。")
            ending_type = "记录者"
        elif final_choice == 5:  # 寻找程心
            self.print_text("你找到了程心，和她一起进入了冬眠。")
            self.print_text("在遥远的未来醒来，你们见证了宇宙的重生...")
            self.print_text("新的故事，才刚刚开始。")
            ending_type = "守望者"
        else:  # 接受命运
            self.print_text("你平静地接受了命运。")
            self.print_text("在二维世界中，你成为了永恒的艺术品...")
            self.print_text("这也许是另一种形式的永生。")
            ending_type = "智者"
        
        # 特殊结局判定
        if self.hidden_event and survival_score >= 2:
            self.print_text("\n【隐藏结局达成】")
            self.print_text("由于你在危机纪元的正确决策和对三体叛逃者情报的利用...")
            self.print_text("你成功建立了人类与三体和平派的秘密联盟！")
            self.print_text("在维度打击前，你们共同逃离，建立了新的文明...")
            ending_type += " - 和平使者"
        
        self.print_text("\n" + "=" * 60)
        self.print_text("        游戏统计")
        self.print_text("=" * 60)
        self.print_text(f"\n玩家：{self.name}")
        self.print_text(f"身份：{self.SF}")
        self.print_text(f"起始地点：{self.location}")
        self.print_text(f"总选择数：{total_choices}")
        self.print_text(f"结局类型：{ending_type}")
        self.print_text("\n「给岁月以文明，而不是给文明以岁月。」")
        self.print_text("「死神永生。」")
        
        self.hide_all_buttons()
    
    def export_log(self):
        if not self.log:
            messagebox.showinfo("提示", "暂无日志可导出")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt")],
            initialfile=f"三体游戏日志_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"《三体》文字穿越游戏 - 游戏日志\n")
                f.write(f"导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                for line in self.log:
                    f.write(line + "\n")
            messagebox.showinfo("成功", f"日志已导出到:\n{filename}")
    
    def restart(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state=tk.DISABLED)
        self.log = []
        self.choices_made = []
        self.era_results = {}
        self.current_stage = 0
        self.hidden_event = False
        self.root.after(500, self.start_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = SantiGame(root)
    root.mainloop()
