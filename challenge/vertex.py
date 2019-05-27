class Vertex:

    def __init__(self, id):
        self._id = id
        self._vertex_adjacents = {}
        self._distance = 0
        self._visited  = False
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
        return self._id, [(k.get_id(),v) for k,v in self._vertex_adjacents.items()]

    def __str__(self):
        return str(self._id)
