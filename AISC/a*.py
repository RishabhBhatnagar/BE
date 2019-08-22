class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.children = []
    def __repr__(self):
        return self.name

class Path:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return " -> ".join(map(lambda x: x.name, self.path))


def algo(nodes, start=0):
    path = []
    cost = 0
    current = nodes[start]
    while True:
        path.append(current)
        if current.children:
            all_costs = [(node, node.h + wt) for node, wt in current.children if node not in path]
            if all_costs:
                child = min(all_costs, key=lambda x: x[1])[0]
                current = child
            else: 
                break
        else:
            break
    return Path(path)


def matrix_to_nodes(graph, h_list, n):
    # convert 3d graph to list of children nodes.
    # n: number of rows and cols of adj matrix.
    assert len(graph) == len(h_list), "len of rows of h_list should be same as number of rows in the graph."
    nodes = [Node(chr(i + ord('A')), h) for i, h in enumerate(h_list)]
    for i in range(n):
        for j, cell in enumerate(graph[i]):
            if (i ^ j) and (graph[i][j] != 0):
                nodes[i].children.append((nodes[j], graph[i][j]))
                nodes[j].children.append((nodes[i], graph[i][j]))
    return nodes


matrix = [
    [0, 2, 3], # A
    [0, 0, 1, 2, 3], # B
    [0, 0, 0, 0, 0, 0, 7], # C
    [0, 0, 0, 0, 0, 3], # D
    [], # E
    [], # F
    [0, 0, 0, 1]  # G
]
n = len(matrix)
h = [0, 3, 1, 3, 1, 2, 4]

nodes = matrix_to_nodes(matrix, h, n)
print(algo(nodes))

