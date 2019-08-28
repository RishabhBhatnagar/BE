from functools import total_ordering


@total_ordering
class Point(complex):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, oth):
        return abs(self) < abs(oth)
    def __eq__(self, oth):
        return ((self.x ^ oth.real) + (self.y ^ oth.imag)) == 0

    
if __name__ == '__main__':
    points = tuple(map(lambda x: Point(*x), [(1, 3), (2, 1), (3, 4)]))
    print(min(points))

    
class Graph:
    def __init__(self, graph, m, n):
        self.graph = graph
        self.m = m
        self.n = n
    
    def __getitem__(self, indices):
        if type(indices) == type(Point(0, 0)):
            return self.graph[indices.real * self.n + indices.imag]
        try:
            if len(indices) == 2:
                i, j = indices
                return self.graph[i * self.n + j]
            else:
                raise NotImplementedError("Atmost 2 dimensions indexing possible.")
        except:
            i = indices
            return self.graph[i * self.n : (i + 1) * (self.n)]


G = 100
O = 0
V = 1

graph = [
    V, V, V, V, V, V,
    V, V, V, V, V, V,
    V, V, V, V, V, V,
    V, V, V, V, V, V,
    V, V, V, V, V, V,
    V, V, V, V, V, V
]
n = 6
m = len(graph) // n
if n * m != len(graph):
    raise ValueError("dimensions doesn't match, graph must be a rectangular matrix.")


def circum_navigate(graph:Graph, obs):
    # obs is representation of obstacle in the graph
    pass


def BUG1(graph, q_start, q_goal, obstacle=O, goal=G, void=V):
    path = 


g = Graph(graph, m, n)
BUG1(graph, Point(0, 0))

