# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:22:59 2017

@author: Tidus
"""
import math
class point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
        
class line():
    def __init__(self, p1, p2):
        self.a = p1.getx()
        self.b = p1.gety()
        self.c = p2.getx()
        self.d = p2.gety()
    
    def getLen(self):
        distance = math.sqrt((self.a-self.c) * (self.a-self.c) + (self.b-self.d) * (self.b-self.d))
        return distance
