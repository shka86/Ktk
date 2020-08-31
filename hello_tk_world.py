#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk


class Frame():

    def __init__(self, root, label):
        self.r = 0
        self.root = root
        self.frm = tk.LabelFrame(root, text=label)
        self.frm.pack(padx=5, pady=5)

    def dropdown(self, label, values):
        name = tk.Label(self.frm, text=label)
        name.grid(row=self.r, column=0)
        db = ttk.Combobox(self.frm, state='readonly')
        db["values"] = values
        db.current(0)
        db.grid(row=self.r, column=1, padx=3, pady=3)
        self.r += 1

    def slider(self, label, min_, max_):
        name = tk.Label(self.frm, text=label)
        name.grid(row=self.r, column=0)
        sl = tk.Scale(self.frm, from_=min_, to=max_, orient=tk.HORIZONTAL)
        sl.grid(row=self.r, column=1, padx=3, pady=3)
        self.r += 1

    def checkbox(self, label, ture_false):
        name = tk.Label(self.frm, text=label)
        name.grid(row=self.r, column=0)

        if ture_false:
            val = tk.BooleanVar().set(True)
        else:
            val = tk.BooleanVar().set(False)

        cb = tk.Checkbutton(self.frm, variable=val)
        cb.grid(row=self.r, column=1, padx=3, pady=3)
        self.r += 1

class Window():

    def __init__(self, title_):
        self.root = tk.Tk()
        self.root.title(title_)

        self.nb = ttk.Notebook()

    def add_tab(self, tabname):
        self.tab = tk.Frame(self.nb)
        self.nb.add(self.tab, text=tabname, padding=3)
        self.nb.pack(expand=1, fill='both')

####################################################
if __name__ == '__main__':
    # waku ##########################
    window1 = Window("sample waku")


    # tab1 = window1.add_tab("classtab1")

    # tab1 ##########
    nb = ttk.Notebook()
    tab1 = tk.Frame(nb)
    nb.add(tab1, text="tab1", padding=3)
    nb.pack(expand=1, fill='both')

    # frame 1-1
    frm_1_1 = Frame(tab1, 'frame 1-1')
    frm_1_1.slider("param1", 0, 100)
    frm_1_1.dropdown("param2", ["1", "2", "3"])
    frm_1_1.dropdown("param3", ["a", "b", "c"])


    # frame 1-2
    frm_1_2 = Frame(tab1, 'frame 1-2')
    frm_1_2.slider("param1", 0, 100)
    frm_1_2.dropdown("param2", ["1", "2", "3"])
    frm_1_2.dropdown("param3", ["a", "b", "c"])
    frm_1_2.checkbox("param4", True)

    # # tab2 = window1.add_tab("classtab2")

    # tab2 ##########
    tab2 = tk.Frame(nb)
    nb.add(tab2, text="tab2", padding=3)
    nb.pack(expand=1, fill='both')

    # frame 2-1
    frm_2_1 = Frame(tab2, 'frame 2-1')
    frm_2_1.dropdown("param1", ["a", "b", "c"])
    frm_2_1.checkbox("param2", True)

    # gen gui
    window1.root.mainloop()
