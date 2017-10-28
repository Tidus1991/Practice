# -*- coding: utf-8 -*-
"""
Created on 2017/10/28 14:01

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

class BinTNode:
    def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

class DictBinTree: #二叉排序树(字典)类
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def serach(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if bt.left is None:
                bt.left = BinTNode(Assoc(key, value))
                return
            bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
    def delete(self, key):
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return

            if q.left is None:
                if p is None:
                    self._root = q.right
                elif q is p.left:
                    p.left = q.right
                else:
                    p.right = q.right
                return
            r = q.left
            while r.right is not None:
                r = r.right
            r.right = q.right
            if p is None:
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left

    def print(self):
        for k, v in self.entries():
            print(k, v)

    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value, t.data.value
            t = t.right

    def build_dictBinTree(entries):
        dic = DictBinTree()
        for k, v in entries():
            dic.insert(k, v)
        return dic

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)

class AVLNode(BinTNode):
    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0

class DictAVL(DictBinTree):
    def __init__(self):
        DictBinTree.__init__(self)

    def insert(self, key, value):
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None
        while p is not None:
            if key == p.data.key:
                p.data.value = value
                return
            if p.bf != 0:
                pa, a = q, p
            a = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right

        node  = AVLNode(Assoc(key, value))
        if key < q.data.key:
            q.left = node
        else:
            q.right = node
        if key < a.data.key:
            p = b = a.lefet
            d = 1
        else:
            p = b = a.right
            d = -1

        while p != node:
            if key < p.data.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return

        if d == 1:
            if b.bf == 1:
                b = DictAVL.LL(a, b)
            else:
                b = DictAVL.LR(a, b)
        else:
            if b.bf == -1:
                b = DictAVL.RR(a, b)
            else:
                b = DictAVL.LL(a, b)
        if pa is None:
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

    @staticmethod #
    #LL type:
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf =0
        return b

    #RR type:
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    #LR type:
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = -1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    #RL type:
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right= a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c
