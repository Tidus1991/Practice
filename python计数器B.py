# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:22:59 2017

@author: Tidus
"""

import time as t

class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时...'
        self.starttime = 0
        self.stoptime = 0
        self.lasted = 0.0

    
    def __add__(self,other):
        result = self.lasted + other.lasted
        prompt = '总共运行了%0.2f秒'%result
        return prompt
        
        return prompt
    
    def __str__(self):
        return self.prompt
    
    def __repr__(self):
        return self.prompt
    
    #开始计时
    def start(self):
        self.starttime = t.perf_counter()
        self.prompt = '请先停止计时'
        print('计时开始!')
    
    #停止计时
    def stop(self):
        if not self.starttime:
            print('请先开始计时')
        else:
            self.stoptime = t.perf_counter()
            self._clac()
            print('计时停止!')
            
    #计算时间
    def _clac(self):
        self.lasted = self.stoptime - self.starttime
        self.prompt = '总共运行了%0.2f秒'%self.lasted
        
                
    #为下一轮计时初始化变量
        self.starttime = 0
        self.stoptime = 0
