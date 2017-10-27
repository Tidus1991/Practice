# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:51 2017

@author: Tidus
"""
from collections import deque

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

class BinTNode:
    def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    
def count_BinTnodes(t):
    return 1 + count_BinTnodes(t.left) + count_BinTnodes(t.right)

def sum_BinTnodes(t):
    if t is None:
        return 0
    return t.data + sum_BinTnodes(t.left) + sum_BinTnodes(t.right)

def print_BinTnodes(t): #先根遍历
    if t is None:
        print('^', end='')
        return
    print('('+str(t.data), end='')
    print_BinTnodes(t.left)
    print_BinTnodes(t.right)
    print(')', end='')
    
def print_BinTnodes1(t): #中根遍历 
    if t is None:
        print('^', end='')
        return
    print_BinTnodes1(t.left)
    print('('+str(t.data), end='')
    print_BinTnodes1(t.right)
    print(')', end='')

def print_BinTnodes2(t): #后根遍历
    if t is None:
        print('^', end='')
        return
    print_BinTnodes2(t.left)
    print_BinTnodes2(t.right)
    print('('+str(t.data), end='')
    print(')', end='')
    
def levelorder(t, proc): #宽度优先遍历
    qu = deque()
    qu.append(t)
    while len(qu):
        t = qu.popleft()
        if t is None:
            continue
        qu.append(t.left)
        qu.append(t.right)
        proc(t.data)
    
def preorder_nonrec(t, proc): #深度优先遍历
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.right
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None
