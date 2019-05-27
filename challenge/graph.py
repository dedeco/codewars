import sys

from vertex import Vertex


class Graph:

    def __init__(self, directed=False):
        self.vertex = {}
        self.directed = directed

    def insert_vertex(self, id):
        v = Vertex(id)
        self.vertex[id] = v
        return v

    def insert_edge(self, _from, _to, distance=0):
        if _from not in self.vertex:
            self.insert_vertex(_from)
        if _to not in self.vertex:
            self.insert_vertex(_to)
        self.vertex[_from].insert_vertex_adjacent(self.vertex[_to], distance)
        if not self.directed:
            self.vertex[_to].insert_vertex_adjacent(
                self.vertex[_from], distance)

    def get_vertex(self, id):
        if id in self.vertex:
            return self.vertex[id]
        else:
            return None

    def get_vertexs(self):
        return [v for k,v in self.vertex.items()]

    def get_cycles(self, frm, to):
        queue = [(frm, [], 0)]
        while queue:
            (state, path, distance) = queue.pop()
            if path and state == to:
                yield (path, distance)
                continue
            vertex_adjs = map(lambda x: x.get_id(), self.get_vertex(state).get_vertex_adjacents())
            for next in vertex_adjs:
                sum_ = (self.get_vertex(state).get_cost(self.get_vertex(next)) or 0) + distance
                nx = self.get_vertex(next)
                if next in path:
                    continue
                queue.append((nx.get_id(), path + [nx.get_id()], sum_))

    def bfs_paths_cost(self, frm, to, max_=0):
        queue = [(frm, [], 0)]
        while queue:
            #print('q',queue)
            (vertex, path, distance) = queue.pop(0)
            vertex_adjs = list(map(lambda x: x.get_id(), self.get_vertex(vertex).get_vertex_adjacents()))
            #print('vertex_adjs',vertex_adjs,'set(path)',set(path),'-',set(vertex_adjs) - set(path))
            for next in set(vertex_adjs)- set(path):
                sum_ = (self.get_vertex(vertex).get_cost(self.get_vertex(next)) or 0) + distance
                if next == to:
                    cycles = self.get_cycles(to, to)
                    if cycles:
                        yield ([frm] + path + [next], sum_)
                        for cycle, cycl_dist in cycles:
                            if not max_:
                                yield ([frm] + path + [next] + cycle, sum_ + cycl_dist)
                            else:
                                total = 0
                                i = 1
                                while (total < max_):
                                    total = sum_ + (cycl_dist * i)
                                    yield ([frm] + path + [next] + cycle * i, total)
                                    i += 1
                    else:
                        yield ([frm] + path + [next], sum_)
                else:
                    queue.append((next, path + [next], sum_))

    def bfs_paths(self, frm, to):
        queue = [(frm, [], 0)]
        while queue:
            #print('q',queue)
            (vertex, path, distance) = queue.pop(0)
            vertex_adjs = list(map(lambda x: x.get_id(), self.get_vertex(vertex).get_vertex_adjacents()))
            print('vertex_adjs',vertex_adjs,'set(path)',set(path),'-',set(vertex_adjs) - set(path))
            for next in set(vertex_adjs)- set(path):
                sum_ = (self.get_vertex(vertex).get_cost(self.get_vertex(next)) or 0) + distance
                if next == to:
                    yield ([frm] + path + [next], sum_)
                else:
                    queue.append((next, path + [next], sum_))

    def get_list_vertexs_adjs(self):
        for v in self.vertex:
            yield (self.vertex[v].get_vertex_adjs_with_cost())
            #print( v, [(adj.get_id(), self.vertex[v].get_cost(adj)) for adj in self.vertex[v].get_vertex_adjacents()])
