from ctypes import Array

import numpy
import numpy as np
import pandas as pd
import random as rand
import math
from random import choice
import time
import sys
from decimal import *  # 大数据下保持精度的方法

Process_time = [5, 8, 10, 15, 13, 7, 20, 6, 9, 17]


class env2():

    def __init__(self):
        # super(Maze, self).__init__()  对继承父类属性进行初始化
        self.actions = 10
        self.Lines = 10
        self.maxclothes = 100
        self.Humans = 17
        self.count = 0
        self.done = False
        self.Min_time = 20000
        self.Max_time = 0
        self.Min_episode = 0
        self.Min_episode_count = 0
        self.action_space = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.Error = False
        self.Have_Candidate = False
        self.Proficiency = np.zeros((self.Humans, self.Lines))
        self.Proficiency = [[0.82, 0.20, 0.13, 0.89, 0.33, 0.14, 0.83, 0.82, 0.28, 0.65],
                            [0.98, 0.24, 0.22, 0.79, 0.66, 0.75, 0.03, 0.88, 0.62, 0.02],
                            [0.50, 0.50, 0.73, 0.23, 0.14, 0.36, 0.19, 0.81, 0.52, 0.87],
                            [0.57, 0.89, 0.99, 0.17, 0.65, 0.44, 0.04, 0.03, 0.10, 0.24],
                            [0.23, 0.92, 0.33, 0.59, 0.79, 0.11, 0.50, 0.58, 0.62, 0.70],
                            [0.89, 0.74, 0.58, 0.69, 0.07, 0.95, 0.80, 0.35, 0.36, 0.66],
                            [0.79, 0.24, 0.97, 0.92, 0.90, 0.68, 0.92, 0.36, 0.44, 0.98],
                            [0.59, 0.50, 0.60, 0.49, 0.71, 0.57, 0.67, 0.30, 0.83, 0.63],
                            [0.55, 0.22, 0.09, 0.14, 0.62, 0.14, 0.93, 0.04, 0.43, 0.66],
                            [0.52, 0.14, 0.78, 0.82, 0.23, 0.95, 0.19, 0.67, 0.22, 0.38],
                            [0.23, 0.84, 0.58, 0.92, 0.09, 0.05, 0.07, 0.49, 0.37, 0.17],
                            [0.89, 0.82, 0.87, 0.69, 0.70, 0.61, 0.03, 0.94, 0.37, 0.78],
                            [0.40, 0.78, 0.46, 0.27, 0.56, 0.49, 0.67, 0.17, 0.36, 0.33],
                            [0.95, 0.51, 0.12, 0.32, 0.93, 0.89, 0.75, 0.78, 0.67, 0.03],
                            [0.13, 0.14, 0.35, 0.64, 0.46, 0.66, 0.07, 0.71, 0.29, 0.66],
                            [0.52, 0.25, 0.73, 0.63, 0.64, 0.81, 0.23, 0.87, 0.90, 0.36],
                            [0.11, 0.67, 0.87, 0.45, 0.64, 0.91, 0.16, 0.63, 0.44, 0.56]]
        self.Proficiency = np.array(self.Proficiency)
        # self.Workers = [[0, 0, 1],
        #                 [0, 1, 0],
        #                 [1, 0, 0],
        #                 [0, 0, 1],
        #                 [0, 1, 0],
        #                 [0, 1, 0]]
        self.Workers = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
        self.now_state = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
        self.begin = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
        self.Workers = np.array(self.Workers)
        self.Min_state = []
        self.Candidate = []
        self.false_action = []
        self.action_ = self.Humans * self.Lines + 1
        self.stay_count = 0

    def step(self, action, episode):
        E = episode
        self.Action_choice(action)
        self.count += 1
        self.done = False

        reward = self.Check_reward(action)
        if E > 2000 and (self.Max_time + self.Min_time) / 2 > self.Time():
            self.Error = True
        self.Min_time = min(self.Time(), self.Min_time)
        # E = self.Jump_out(E)  # 跳出局部最优
        self.done = True
        self.now_state = np.array(self.now_state)
        instead_state = self.now_state
        instead_time = self.Time()
        x = self.State_transform(instead_state)  # 输出类型切换
        print(self.Rule(self.now_state))

        print('\033[1;32m')  # 颜色绿色标注
        print(self.Time())
        print(instead_state)
        print('\033[0m')

        return x, reward, self.done, instead_time, E, self.Error

    def Action_choice(self, a):
        act = np.array(a)
        if isinstance(act, list):  # 判断是否为数组
            act = a[0]
        actions_1 = act % self.Lines
        actions_0 = act / self.Lines
        x = math.floor(actions_0)
        y = actions_1
        for i in range(self.Lines):
            self.now_state[x][i] = 0
        if isinstance(y, numpy.ndarray):
            y = y[0]
        print(type(y))
        print(x, y)
        self.now_state[x][y] = 1
        if not self.Rule(self.now_state):
            self.now_state = self.begin

    def Check_reward(self, a):
        reward = 0
        Proficiency_sum = np.sum(self.Proficiency, axis=1)
        Worker_place = np.argmax(self.Workers, axis=1)
        if a == self.action_:  # 长期待在同一位置的惩罚
            self.stay_count += 1
            reward -= (1.001 ** self.stay_count)
            print("*******", reward)
        self.action_ = a
        if not self.Rule(self.now_state):
            print(self.Rule(self.now_state))
            reward -= 10
            self.now_state = self.Workers
        Proficiency_now = []
        Utilization_rate = []
        for i in range(self.Humans):
            Proficiency_now.append(self.Proficiency[i][Worker_place[i]])
        for i in range(self.Humans):
            Utilization_rate.append(Proficiency_now[i] / Proficiency_sum[i])
        Utilization_rate = sum(Utilization_rate)
        # print(Utilization_rate)
        # print(self.Variance())
        V = self.Variance()
        if str(1 / self.Variance()) == "nan":
            V = 99999999999999999
        b = Utilization_rate
        c = 1 / V
        d = self.Min_time - self.Time()

        b = round(b, 5)
        c = round(c, 5)
        d = round(d, 5)
        print(reward)
        print(b)
        print(c)
        print(d)
        print(0.01 * round(self.Time(), 5))
        reward += b + c + 0.01 * d
        reward -= 0.01 * round(self.Time(), 5)
        print(reward)
        return reward

    def State_transform(self, state):
        new_s = []
        x = state.reshape(1, self.Lines * self.Humans)
        for i in x:
            s = list(map(int, i))
            new_s.append(s)
        return new_s

    def State_transform_back(self, state):
        s = np.array(state)
        x = s.reshape(self.Humans, self.Lines)
        return x

    def Prepare_Sum_proficiency(self):
        if self.Rule(self.now_state):
            Sum_proficiency = [a * b for a, b in zip(self.Proficiency, self.now_state)]
        else:
            Sum_proficiency = [a * b for a, b in zip(self.Proficiency, self.begin)]
        Sum_proficiency = np.sum(Sum_proficiency, axis=0)
        return Sum_proficiency

    def Time(self):
        t = 0
        t_ = self.Prepare_Sum_proficiency()
        C = [a / b for a, b in zip(Process_time, t_)]
        for i in range(self.actions - 1):
            t += max(C[0:i + 1]) + max(C[i:self.actions])
        return t

    def Variance(self):
        x = self.Prepare_Sum_proficiency()
        combat = [a / b for a, b in zip(Process_time, x)]
        t = np.var(combat)
        return t

    def Cover(self, episode):
        self.Min_time = self.Time()
        self.Min_state = self.now_state
        self.Min_episode = episode
        self.Min_episode_count = 0

    def Jump_out(self, episode):
        E = episode
        if self.Time() == self.Min_time and self.Min_episode_count >= 1000:
            E += 0.5

        return E

    def reset(self):
        self.now_state = self.begin
        s = np.array(self.now_state)
        s_ = s.reshape(1, self.Humans * self.Lines)
        self.Error = False
        return s_

    def Rule(self, state):
        Count_1_Workers = np.sum(state, axis=0)
        Rule_judgment = True
        for i in range(self.Lines):
            if Count_1_Workers[i] == 0:
                Rule_judgment = False
        return Rule_judgment

    # def Exchange(self):
    #     while Have_Candidate:
    #         rand.choice(self.Candidate)
    #         a = 1  # 想要替换的数字
    #         b = 0  # 替换后的数字
    #         index = (self.Workers == a)
    #         self.Workers[index] = b
    #         Have_Candidate = False
