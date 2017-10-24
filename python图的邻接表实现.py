# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:29:38 2017

@author: Tidus
"""

class GraphError(ValueError):
    pass

class GraphAl:
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argumet for Graph!')
        self._mat = [self._out_edges(mat[i], unconn) for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum
        
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum -1
    
    def add_edge(self, vi, vj, val =1):
        if self._vnum == 0:
            raise GraphError('Cannot add edge to empty graph')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        row = self.mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat.insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        for i, val in self._invalid[vi]:
            if i == vj:
                return val
            return self._unconn
    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + 'is not a valid vertex')
        return self._mat[vi]
    
    def _invalid(self, v):
        return 0 > v or v >= self._vnum
        
@staticmethod
def _out_edges(row, unconn):
    edges = []
    for i in range (len(row)):
        if row[i] != unconn:
            edges.append((i, row[i]))
    return edges