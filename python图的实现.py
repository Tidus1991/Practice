# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:05:21 2017

@author: Tidus
"""
class GraphError(ValueError):
    pass

class Graph:
    def __init__(self, mat, unconn):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argumet for Graph!')
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum
        
    def vertex_num(self):
        return self.vertex_num
    
    def _invalid(self, v):
        return 0 > v or v >= self._vnum
    
    def add_vertex(self):
        raise GraphError('Adj-Matrix does not support "add_vertex".')
        
        
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        self._mat[vi][vj] = val
    
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        return self._mat[vi][vj]