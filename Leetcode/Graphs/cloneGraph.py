class Node(object):
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        def dfs(node, oldToNew):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei, oldToNew))
            return copy

        oldToNew = {}
        return dfs(node, oldToNew)


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

nodes = [Node(i) for i in range(1, len(adjList) + 1)]

for i, neighbors in enumerate(adjList):
    nodes[i].neighbors = [nodes[n - 1] for n in neighbors]

solution = Solution()

cloned_node = solution.cloneGraph(nodes[0])


def print_graph(node, visited):
    if node in visited:
        return
    visited.add(node)
    print(f"Node {node.val} neighbors: {[neighbor.val for neighbor in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)


print_graph(nodes[0], set())
