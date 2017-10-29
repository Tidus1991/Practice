# -*- coding: utf-8 -*-
"""
Created on 2017/10/29 21:11

@author: Tidus
"""

def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i <mid and j < high:
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1

def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i +2 * slen < llen:
        merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2*slen
    if i+slen < llen:
        merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]

def merge_sort(nums):
    slen, llen = 1, len(nums)
    templst = [None]*llen
    while slen < llen:
        merge_pass(nums, templst, llen, slen)
        slen *= 2
        merge_pass(templst, nums, llen, slen)
        slen *= 2
    return nums
if __name__ == '__main__':
    nums = [5, 2, 4, 9, 8, 0, 6, 1, 7, 3]
    print('merge_sort:',merge_sort(nums))