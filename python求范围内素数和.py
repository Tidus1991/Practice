# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:45:32 2017

@author: Tidus
"""

import math

def is_prime(data):
    if data > 1:
        if data == 2:
            return True
        if data % 2 == 0:
            return False
        for current in range(3,int(math.sqrt(data)+1),2):
            if data % current == 0:
                return False
        return True
    return False

def get_prime(data):
    while True:
        if is_prime(data):
            yield data
        data += 1
        
def solve():
    total = 2
    for next_prime in get_prime(3):
        if next_prime <2000000:
            total += next_prime
        else:
            print(total)
            return
        
if __name__ == '__main__':
    solve()