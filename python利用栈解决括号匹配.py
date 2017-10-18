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


def check_parens(text):
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')':'(', ']':'[', '}':'{'}
    
    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i <text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
            
    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at',i,'for',pr)
            return False
    print('All parentheses are correctly matched')
    return True