# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:51 2017

@author: Tidus
"""

def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty(btree):
    return btree == [] 

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data
    
def set_left(btree, left):
    btree[1] = left
    
def set_right(btree, right):
    btree[2] = right

def traversal(btree): #宽度优先
    if is_empty(btree):
        return False
    print(btree[0], 1)
    for i in range(1, len(btree)):
        print(btree[i][0], i+1)
