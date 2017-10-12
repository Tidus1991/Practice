# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:22:59 2017

@author: Tidus
"""

class Nstr(int):
    def __init__(self,arg = ''):
        if isinstance(arg,str):
            self.total = 0
            for each_word in arg:
                self.total += ord(each_word)
        else:
            print('输入错误')
    
    def __add__(self,other):
        return self.total + other.total
    
    def __sub__(self,other):
        return self.total - other.total
    
    def __mul__(self,other):
        return self.total * other.total
    
    def __truediv__(self,other):
        return self.total / other.total
    
    def __floordiv__(self,other):
        return self.total // other.total
    
