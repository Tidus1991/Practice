# -*- coding: utf-8 -*-
"""
Created on 2017/10/29 14:22

@author: Tidus
"""

def bubble_sort(nums):#优化冒泡排序
    for i in range(len(nums)):
        found = False
        for j in range(1, len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                found = True
        if not found:
            return nums
    return nums

def select_sort(nums):#选择排序
    for i in range(len(nums)-1):
        k = i
        for j in range(i, len(nums)):
            if nums[j] < nums[k]:
                k = j
        if i != k:
            nums[i], nums[k] = nums[k], nums[i]
    return nums

def insert_sort(nums):#插入排序
    for i in range(1,len(nums)):
        x = nums[i]
        j = i
        while j > 0 and nums[j-1] > x:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = x
    return nums

if __name__ == '__main__':
    nums = [5, 2, 4, 9, 8, 0, 6, 1, 7, 3]
    print('bubble_sort:',bubble_sort(nums))
    print('select_sort:',select_sort(nums))
    print('insert_sort:',insert_sort(nums))