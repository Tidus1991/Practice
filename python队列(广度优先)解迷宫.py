# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:48:24 2017

@author: Tidus
"""

from collections import deque

def mark(maze, pos):
    maze[pos[0]][pos[0]] = 2
    
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def maze_solver_queue(maze, start, end):
    if start == end:
        print('Path finds')
        return
    qu = deque()
    mark(maze, start)
    qu.append(start)
    while not len(qu):
        pos = qu.popleft()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print('Path finds')
                    return
                mark(maze, nextp)
                qu.append(nextp)