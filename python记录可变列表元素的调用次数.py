# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:20:51 2017

@author: Tidus
"""

class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)
        
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)
        
    def __delitem__(self, key):
        del self.count[key]
        super().__deltiem__(key)
    
    def append(self, value):
        self.count.append(0)
        super().append(value)
    
    def pop(self,key = -1):
        del self.count[key]
        return super().pop(key)
        
    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)
    
    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()
        
    def reverse(self):
        self.count.reverse()
        super().reverse()
        