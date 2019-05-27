import sys 

def initialize_single_source(g,s):  
    for v in g.get_vertexs():
        v.set_distance(sys.maxsize)
        v.set_visited(False)
    
    g.get_vertex(s).set_distance(0)

def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.get_distance() <min.get_distance():
            min = v
    Q.remove(min) 
    return min

def relax(u,v):
    if v.get_distance() > u.get_distance() + u.get_cost(v):
        v.set_distance(u.get_distance() + u.get_cost(v))
        v.set_previous(u)

def dijkstra(g,s):

    initialize_single_source(g,s)   

    S = []
    Q = [v for v in g.get_vertexs()]

    while len(Q):

        u = extract_min(Q)

        u.set_visited()

        S.append(u)

        for v in u.get_vertex_adjacents():

            if v.get_visited():
                continue

            relax(u,v)