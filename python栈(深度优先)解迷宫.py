# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:17:02 2017

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

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2
    
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def print_path(end, pos, st):
    path = []
    path.append(st.pop())
    path.reverse()
    print('路径为：',path + [pos] + [end])
    
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def find_path(maze, start ,end):
    if start == end :
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if nextp == end:
                print_path(end, pos ,st)
                return
            if passable(maze, nextp):
                st.push(pos, i+1)
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print('No path found!')
