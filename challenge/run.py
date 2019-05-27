

class Vertex:

    def __init__(self, id):
        self._id = id
        self._vertex_adjacents = {}
        self._distance = 0
        self._visited = False
        self._previous = None

    def get_id(self):
        return self._id

    def set_distance(self, distance):
        self._distance = distance

    def get_distance(self):
        return self._distance

    def set_visited(self, visited=True):
        self._visited = visited

    def get_visited(self):
        return self._visited

    def set_previous(self, previous):
        self._previous = previous

    def get_previous(self):
        return self._previous

    def insert_vertex_adjacent(self, to_=None, distance=0):
        self._vertex_adjacents[to_] = distance

    def get_vertex_adjacents(self):
        return self._vertex_adjacents.keys()

    def get_cost(self, to_):
        return self._vertex_adjacents.get(to_, None)

    def get_vertex_adjs_with_cost(self):
        return self._id, [(k.get_id(), v) for k, v in self._vertex_adjacents.items()]

    def __str__(self):
        return str(self._id)

import sys

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
        return [v for k, v in self.vertex.items()]

    def get_cycles(self, frm, to):
        queue = [(frm, [], 0)]
        while queue:
            (state, path, distance) = queue.pop()
            if path and state == to:
                yield (path, distance)
                continue
            vertex_adjs = map(lambda x: x.get_id(), self.get_vertex(
                state).get_vertex_adjacents())
            for next in vertex_adjs:
                sum_ = (self.get_vertex(state).get_cost(
                    self.get_vertex(next)) or 0) + distance
                nx = self.get_vertex(next)
                if next in path:
                    continue
                queue.append((nx.get_id(), path + [nx.get_id()], sum_))

    def get_list_vertexs_adjs(self):
        for v in self.vertex:
            yield (self.vertex[v].get_vertex_adjs_with_cost())


def initialize_single_source(g, s):
    for v in g.get_vertexs():
        v.set_distance(sys.maxsize)
        v.set_visited(False)

    g.get_vertex(s).set_distance(0)


def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.get_distance() < min.get_distance():
            min = v
    Q.remove(min)
    return min


def relax(u, v):
    if v.get_distance() > u.get_distance() + u.get_cost(v):
        v.set_distance(u.get_distance() + u.get_cost(v))
        v.set_previous(u)


def dijkstra(g, s):

    initialize_single_source(g, s)

    S = []
    Q = [v for v in g.get_vertexs()]

    while len(Q):

        u = extract_min(Q)

        u.set_visited()

        S.append(u)

        for v in u.get_vertex_adjacents():

            if v.get_visited():
                continue

            relax(u, v)

def _cal_bwt_vertex(src, dest):
    s, d = str(src), str(dest)
    if len(s) == 1: 
        s = s*2
    if len(d) == 1:
        d = d*2
    return abs(int(s[0])-int(d[0])) + abs(int(s[1])-int(d[1]))

def get_shortest_route_djk(g, frm, to):
    dijkstra(g, frm)
    return (g.get_vertex(to).get_distance())

#def get_keys():


def test():
    g = Graph()

    stations = [0, 65, 93, 36]

    for i in range(len(stations)):
        for j in range(len(stations)):
            distance = _cal_bwt_vertex(stations[i], stations[j])
            if distance > 0:
                g.insert_edge(stations[i], stations[j], distance)

    dist = {}

    for i in range(len(stations)):
        for j in range(len(stations)):
            if stations[i] != stations[j]:
                key = (str(stations[i])+'-'+str(stations[j]))
                d = get_shortest_route_djk(g, stations[i], stations[j])
                if dist.get(key):
                    if d < dist.get(key):
                        dist[key] = d
                else:
                    dist[key] = d
    print(dist)

    paths = []


    
#def _shortest_path(dist, path):
#    for k in dist.keys():
#        kk = k.split('-')[1]
#        dd = {k: v for k, v in dist.items() if k.split('-')[0] == kk}
        

if __name__ == "__main__":    
    test()

