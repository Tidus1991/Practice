# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:59:36 2017

@author: Tidus
"""

class PrioQueueError(ValueError):
    pass

class PrioQueue:
    def __init__(self, elist=[]):
        self.elems = list(elist)
        if elist:
            self.buildheap
        
    def is_empty(self):
        return not self.elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems[-1]
    
    def enqueue(self, e):
        self.elems.append(None)
        self.siftup(e, len(self.elems)-1)
        
    def siftup(self, e, last):
        elems, i, j = self.elems, last, (last-1)/2
        while i > 0 and e < elems[j]:
            i, j = j, (j-1)//2
        elems[i] = e
        
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self.elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
    
    def siftdown(self, e, begin, end):
        elems, i, j = self.elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e
        
    def buildheap(self):
        end = len(self.elems)
        for i in range(end//2, 1, -1):
            self.siftdown(self.elems[i], i, end)