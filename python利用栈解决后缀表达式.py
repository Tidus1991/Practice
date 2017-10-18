# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:16:20 2017

@author: Tidus
"""
class SStack():
    def __init__(self):
        self.elems = []
    
    def is_empty(self):
        return self.elems == []
    
    def top(self):
        if self.is_empty():
            return
        return self.elems[-1]
    
    def push(self, elem):
        self.elems.append(elem)
        
    def pop(self):
        if self.is_empty():
            return 
        return self.elems.pop()
    
    def depth(self):
        return len(self.elems)

def suf_exp_evalutor():
    operators = '+-*/'
    exp = input_part()
    st = SStack()
    
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        
        if st.depth() < 2:
            return False
        
        a = st.pop()
        b = st.pop()
        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        st.push(c)
        
    if st.depth() == 1:
        return st.pop()
    return False

def input_part():
        line = input('Suffix Experssion:')
        return line.split()
