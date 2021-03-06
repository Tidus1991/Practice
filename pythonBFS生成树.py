# -*- coding: utf-8 -*-
"""
Created on 2017/10/25 16:09

@author: Tidus
"""

def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None]*vnum

    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)
    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest


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
    for i in range(len(row)):
        if row[i] != unconn:
            edges.append((i, row[i]))
    return edges