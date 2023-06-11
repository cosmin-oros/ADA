class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskal(graph):
    size = len(graph)
    mst = []
    edges = []

    for i in range(size):
        for j in range(i + 1, size):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    uf = UnionFind(size)

    for edge in edges:
        v1, v2, weight = edge
        root1 = uf.find(v1)
        root2 = uf.find(v2)
        if root1 != root2:  # Check if adding the edge creates a cycle
            uf.union(v1, v2)
            mst.append(edge)

    return mst


graph = [
    [0, 4, 1, 0, 0],
    [4, 0, 3, 2, 5],
    [1, 3, 0, 1, 0],
    [0, 2, 1, 0, 4],
    [0, 5, 0, 4, 0]
]

minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)
