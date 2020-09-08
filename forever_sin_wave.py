#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys
import math
import time
import matplotlib.pyplot as plt
import datetime
dt = datetime.datetime.now()
import datetime

class SinWaveGenerator():
    def __init__(self):
        self.make_graph_canvas()
        self.initialize_wave(omega=0, init_phase=0)
        self.define_wave1()
        self.flg_loop = False

    def make_graph_canvas(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111)

    def define_wave1(self):
        self.lines, = self.ax1.plot(self.list_x, self.list_y, 
                        marker='d',             # マーカーの形状
                        markersize=4,           # マーカー全体のサイズ
                        markerfacecolor='#66DDDD',  # マーカーの色は白
                        markeredgewidth=1,      # マーカーエッジのサイズ
                        markeredgecolor='#44BBBB',  # マーカーエッジを赤にする
                        linestyle='None')

    def initialize_wave(self, omega, init_phase=0):
        self.list_x = []
        self.list_y = []
        self.t = 0
        self.omega = omega
        self.init_phase = init_phase

    def run(self):
        self.flg_loop = True

    def stop(self):
        self.flg_loop = False

    def genloop(self):

        while self.flg_loop:
            x = self.t
            y = math.sin(x + self.init_phase)

            # print(x, y)

            self.list_x.append(x)
            self.list_y.append(y)

            # next step
            if self.t < 10:
                self.t += 0.1
            else:
                # plt
                self.lines.set_data(self.list_x, self.list_y)
                self.ax1.set_xlim(min(self.list_x), max(self.list_x))
                self.ax1.set_ylim(-1, 1)
                plt.pause(0.5)

                # reset
                dt = datetime.datetime.now()
                dt = dt.strftime('%M%S')
                dt = (int(dt) % 100) / 10
                self.init_phase = random.gauss(mu=0, sigma=0.3)
                print(self.init_phase)

                # self.initialize_wave(omega = 0, init_phase=0)
                self.t = 0
                self.list_x.clear
                self.list_y.clear
                time.sleep(0.5)

if __name__ == '__main__':
    
    a = SinWaveGenerator()

    a.run()
    a.genloop()
