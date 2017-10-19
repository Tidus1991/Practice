# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:05:21 2017

@author: Tidus
"""

import random
 
# 八皇后问题的前情不在此重复说明
# 验证新的皇后是否和之前的皇后所在位置有冲突：在同一列或者在对角线上
# state 为已经确定的皇后的位置元组
# nextX 为新的一个皇后的所在列的位置
def conflict(state, nextX):
    nextY = len(state) # 新的皇后所在行
    for i in range(len(state)): # 针对之前所有的皇后来判断
        # state[i]为第 i 行的皇后的所在列的位置
        # 如果 state[i] - nextX == 0，那么新的皇后和所对比的皇后在同一列，返回对比结果为True
        # 如果 abs(state[i] - nextX) == nextY - i ，那么新的皇后和所对比的皇后在对角线上，返回对比结果为True
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    # 如果新的皇后和所有历史皇后都不在同一列或者对角线上，返回对比记过为false
    return False
 
# 生成皇后元组，默认皇后元组为空
def queens(num, state=()):
    # 针对所有的皇后所在的行，判断每一列位置，0 - 7
    for pos in range(num):
        # 调用皇后位置冲突验证方法
        if not conflict(state, pos):
            # 如果已经是最后一个皇后了，就yield这个皇后的位置
            if len(state) == num-1:
                yield (pos, )
            else:
                # 如果当前位置可以放皇后，那么就继续找到下一个适合位置的皇后，直到递归找到所有皇后的位置
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result
 
# 漂亮的打印方法
def prettyprint(solution):
    def line(pos, length=len(solution)):
        # 每一行，皇后所在位置打印 X，其他位置打印 .
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    # 针对每一个皇后所在的行都进行打印
    for pos in solution:
        print(line(pos))
 
if __name__ == '__main__':
    print('一共有 {} 种可能的皇后排放位置选择'.format(len(list(queens(8)))))
    print('其中一种选择是：')
    prettyprint(random.choice(list(queens(8))))