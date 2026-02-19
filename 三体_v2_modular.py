#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
三体游戏 v2 - 模块化版本
主文件：负责 UI 和游戏流程控制
"""
import tkinter as tk
from tkinter import scrolledtext

# 导入各纪元模块
from eras import crisis, deterrence, broadcast, victory, bunker, expansion, endings

class ThreeBodyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("三体 - 文明抉择")
        self.root.geometry("800x600")
        
        # 积分系统
        self.score = {
            'survival': 0,
            'technology': 0,
            'morality': 0,
            'aggression': 0,
            'unity': 0
        }
        
        # 纪元追踪
        self.era_path = []
        self.current_stage = 0
        
        # UI 组件
        self.text_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=80, height=25, 
            font=("SimHei", 12)
        )
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state=tk.DISABLED)
        
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
        btn = tk.Button(
            self.button_frame, text=text, command=command,
            width=60, height=2, font=("SimHei", 10)
        )
        btn.pack(pady=5)
        self.buttons.append(btn)
    
    def choice(self, survival=0, tech=0, moral=0, aggr=0, unity=0, next_func=None):
        """处理选择并更新积分"""
        self.score['survival'] += survival
        self.score['technology'] += tech
        self.score['morality'] += moral
        self.score['aggression'] += aggr
        self.score['unity'] += unity
        
        if next_func:
            next_func(self)
    
    def start_game(self):
        """开始游戏"""
        crisis.crisis_era_1(self)

if __name__ == "__main__":
    root = tk.Tk()
    game = ThreeBodyGame(root)
    root.mainloop()
