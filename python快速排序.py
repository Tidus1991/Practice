# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:54:01 2017

@author: Tidus
"""
def QuickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]      
        for i in arr:
            if i < pivot:
                print('less:',less)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = QuickSort(less)     
        more = QuickSort(more)
        return less + pivotList + more
    

def QuickSort1(lists):
    if not lists:
        return []
    else:
        pivot = lists[0]
        less = [x for x in lists     if x <  pivot]
        more = [x for x in lists[1:] if x >= pivot]
        return QuickSort1(less) + [pivot] + QuickSort1(more)
