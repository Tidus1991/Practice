# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:51 2017

@author: Tidus
"""

class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self, elist=[]):
        self.elems = list(elist)
        self.elems.sort(reverse = True)
        
    def enqueue(self, e):
        i = len(self.elems) - 1
        while i >= 0:
            if self.elems[i] > e:
                i -= 1
            else:
                break
        self.elems.insert(i + 1 ,e)
    
    def is_empty(self):
        return not self.elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems[-1]
    
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in pop')
        return self.elems.pop()