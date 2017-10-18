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

priority = {'(':1, '+':3, '-':3, '*':5, '/':5}
infix_operators = '+-*/()'
def trans_infix_suffix():
    line = input_part()
    st = SStack()
    exp = []
    for x in line:
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.top() != '(':#括号之间的元素全部出栈
                exp.append(st.pop())
            if st.is_empty():
                return False
            st.pop()
        else:
            while not st.is_empty() and priority[st.top()] > priority[x]:
                exp.append(st.pop())
            st.push(x)   
            
    while not st.is_empty():
        if st.top() == '(':
            return False
        exp.append(st.pop())
    return exp

def input_part():
        line = input('trans_infix_suffix: ')
        return line.split()

if __name__ == '__main__':
    print(trans_infix_suffix())