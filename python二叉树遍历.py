# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:24:35 2017

@author: Tidus
"""

class BinaryTree(object): 
    def __init__(self, value=None, left=None, right=None): 
        self.value = value 
        self.left = left 
        self.right = right 
  
    def rebuild(self, preOrder, inOrder): 
        """ 
        根据前序列表和中序列表,重建二叉树 
        :param preOrder: 前序列表 
        :param inOrder: 中序列表 
        :return: 二叉树 
        """
        if preOrder == None or inOrder == None or len(preOrder) <=0 \ 
        or len(inOrder) <=0 or len(preOrder) != len(inOrder): 
            return None
        cur = BinaryTree(preOrder[0]) 
        index = inOrder.index(preOrder[0]) 
        cur.left = self.rebuild(preOrder[1: index+1], inOrder[:index]) 
        cur.right = self.rebuild(preOrder[index+1:], inOrder[index+1:]) 
        return cur 
  
    def preOrder(self, tree): 
        """ 
        前序遍历 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return None
        print(tree.value, end=' ') 
        self.preOrder(tree.left) 
        self.preOrder(tree.right) 
  
    def preOrderLoop(self, tree): 
        """ 
        前序遍历的循环实现 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return None
        lst = [] 
        node = tree 
        while node != None or len(lst) > 0: 
            if node != None: 
                lst.append(node) 
                print(node.value, end=' ') 
                node = node.left 
            else: 
                item = lst[len(lst)-1] 
                lst = lst[:-1] 
                node = item.right 
  
    def inOrder(self, tree): 
        """ 
        中序遍历 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return None
        self.inOrder(tree.left) 
        print(tree.value, end=' ') 
        self.inOrder(tree.right) 
  
    def inOrderLoop(self, tree): 
        """ 
        中序遍历循环实现 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return
        lst = [] 
        node = tree 
  
        while node != None or len(lst) > 0: 
            if node != None: 
                lst.append(node) 
                node = node.left 
            else: 
                item = lst[len(lst)-1] 
                lst = lst[:-1] 
                print(item.value, end=' ') 
                node = item.right 
  
    def postOrder(self, tree): 
        """ 
        后序遍历 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return None
        self.postOrder(tree.left) 
        self.postOrder(tree.right) 
        print(tree.value, end=' ') 
  
    def postOrderLoop(self, tree): 
        """ 
        后续遍历的循环实现 
        :param tree: 
        :return: 
        """
        if tree == None: 
            return None
  
        visited = set() 
        lst = [] 
        node = tree 
  
        while node != None or len(lst) > 0: 
            if node != None: 
                lst.append(node) 
                node = node.left 
            else: 
                item = lst[len(lst)-1] 
                if item.right != None and item.right not in visited: 
                    node = item.right 
                else: 
                    print(item.value, end=' ') 
                    visited.add(item) 
                    lst = lst[:-1]