# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:22:59 2017

@author: Tidus
"""

import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['天','小时','分钟','秒']
        self.prompt = '未开始计时...'
        self.lasted = []
        self.starttime = 0
        self.stoptime = 0
    
    def __add__(self,other):
        prompt = '总共运行了'
        result = []
        for index in range (2,6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt +=(str(result[index]) + self.unit[index])
        return prompt
    
    def __str__(self):
        return self.prompt
    
    def __repr__(self):
        return self.prompt
    
    #开始计时
    def start(self):
        self.starttime = t.localtime()
        self.prompt = '请先停止计时'
        print('计时开始!')
    
    #停止计时
    def stop(self):
        if not self.starttime:
            print('请先开始计时')
        else:
            self.stoptime = t.localtime()
            self._clac()
            print('计时停止!')
            
    #计算时间
    def _clac(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range (2,6):
            self.lasted.append(self.stoptime[index] - self.starttime[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
                
    #为下一轮计时初始化变量
        self.starttime = 0
        self.stoptime = 0
