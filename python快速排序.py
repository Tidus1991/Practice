# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:54:01 2017

@author: Tidus
"""
#import re
arr = input()
#lists = re.findall(r'.{1}',lists)
arr = arr.split(' ')
arr = list(map(int, arr))

def QuickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]      #将第一个值做为基准
        for i in arr:
            if i < pivot:
                less.append(i)
                print('less:',less)
            elif i > pivot:
                more.append(i)
                print('more:',more)
            else:
                pivotList.append(i)
                print('pivotList:',pivotList)

        less = QuickSort(less)      #得到第一轮分组之后，继续将分组进行下去。Key Step!
        more = QuickSort(more)
        print('a:',less)
        print('b:',pivotList)
        print('c:',more)
        return less + pivotList + more
    

def qsort(lists):
    if not lists:
        return []
    else:
        pivot = lists[0]
        less = [x for x in lists     if x <  pivot]
        more = [x for x in lists[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)
print(qsort(lists))