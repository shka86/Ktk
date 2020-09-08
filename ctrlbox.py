#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from tkbase import *

import forever_sin_wave as f_sin

####################################################

def test_action_print():
    print("hell_world")

def run():
    pass

def stop():
    pass


def ctrl_box():
    # make window ##########################
    window1 = Window("sample waku1")

    # make tab1
    tab1 = Tab(window1, "Tab1")
    box1_1 = Box(tab1, "box1_1")
    box1_2 = Box(tab1, "box1_2")

    btn_run = Button(box1_1, "run", wavegen.run)
    btn_stop = Button(box1_1, "stop", wavegen.stop)

    btn2 = Button(box1_2, "btn2", wavegen.initialize_wave)
    slider = Slider(box1_1, "param1", 0, 100)
    dropdown1 = DropDown(box1_1, "param2", ["1", "2", "3"])

    # make tab2
    tab2 = Tab(window1, "Tab2")
    box2_1 = Box(tab2, "box2_1")
    box2_2 = Box(tab2, "box2_2")
    dropdown2 = DropDown(box2_1, "param3", ["a", "b", "c"])
    checkbox = CheckBox(box2_1, "param4", True)

    # gen gui
    window1.root.mainloop()


####################################################
if __name__ == '__main__':

    # gen wave generator
    # wavegen = f_sin.SinWaveGenerator()
    # memo：これ↑するとguiが出てこない。
    # やりたいこと(ctrl_boxからsin波形をいじる)するには
    # "tkinterで別クラスへ値をinsertする方法"で検索すると幸せになれそう

    # gen tk ctrl box
    ctrl_box()

