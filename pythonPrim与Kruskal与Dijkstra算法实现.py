# -*- coding: utf-8 -*-
"""
Created on 2017/10/25 18:26

@author: Tidus
"""
from collections import deque

def prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = deque([0, 0, 0])
    count = 0
    while count < vnum and len(cands):
        w, u, v = cands.popleft()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.append((u, v, vi))
    return mst

class GraphError(ValueError):
    pass

def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w,vi,vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj), w)
            if len(mst) == vnum-1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep

def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None]*vnum
    count = 0
    cands = deque([(0, v0, v0)])
    while count < vnum and len(cands):
        plen, u, vmin = cands.popleft()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.append((plen + w, vmin, v))
        count += 1
    return paths

class Graph:
    def __init__(self, mat, unconn=0):
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