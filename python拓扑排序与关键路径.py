# -*- coding: utf-8 -*-
"""
Created on 2017/10/26 21:39

@author: Tidus
"""
def critical_paths(graph):
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0] * vnum
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:
                    ee[j] = ee[i] + w
        return ee

    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast] * vnum
        for k in range(vnum-2, -1, -1):
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] -w <le[i]:
                    le[i] =le[j] - w
        return le

    def crt_paths(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j]-w:
                    crt_actions.append((i, j, ee[i]))
        return crt_actions

    toposeq = toposort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])
    return crt_paths(vnum, graph, ee, le)

def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0]*vnum, []
    zerov = -1
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            indegree[v] += 1
        for vi in range(vnum):
            if indegree[vi] == 0:
                indegree[vi] = zerov
                zerov = vi
        for n in range(vnum):
            if zerov == -1:
                return False
            vi = zerov
            zerov = indegree[zerov]
            toposeq.append(vi)
            for v, w in graph.out_edges(vi):
                indegree[v] -= 1
                if indegree[v] == 0:
                    indegree[v] = zerov
                    zerov = v
        return toposeq


class GraphError(ValueError):
    pass

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
        return self._vnum

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