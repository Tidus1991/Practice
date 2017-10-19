 # -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:16:20 2017

@author: Tidus
"""

def mark(maze, pos):
    maze[pos[0]][pos[0]] = 2
    
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def find_path(maze, pos ,end):
    mark(maze, pos)
    if pos == end:
        print(pos, end = ' ')
        return True
    for i in range (4):
        nextp = pos[0] +dir[i][0], pos[1] +dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end = ' ')
                return True
    return False