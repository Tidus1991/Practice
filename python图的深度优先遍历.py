# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:57:03 2017

@author: Tidus
"""
def DFS_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq

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
    
    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + 'is not a valid vertex')
        return self._out_edges(self._mat[vi], self._unconn)
    
@staticmethod
def _out_edges(row, unconn):
    edges = []
    for i in range (len(row)):
        if row[i] != unconn:
            edges.append((i, row[i]))
    return edges

class SStack:
    def __init__(self):
        self.elems = []
    
    def push(self, elems):
        self.elems.append(elems)
    
    def pop(self):
        return self.elems.pop()

