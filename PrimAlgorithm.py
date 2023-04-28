import sys


def prim_mst(graph):
    num_vertices = len(graph)

    # Initialize distance array and visited array
    distances = [sys.maxsize] * num_vertices
    visited = [False] * num_vertices

    # Start with vertex 0 as the root
    root = 0
    distances[root] = 0

    # Loop until all vertices are visited
    while not all(visited):
        # Find the minimum distance vertex that hasn't been visited
        min_dist = sys.maxsize
        min_index = None
        for i in range(num_vertices):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_index = i

        # Mark the vertex as visited
        visited[min_index] = True

        # Update distances to adjacent vertices
        for j in range(num_vertices):
            if graph[min_index][j] != 0 and not visited[j] and graph[min_index][j] < distances[j]:
                distances[j] = graph[min_index][j]

    return sum(distances)


graph = [
    [0, 5, 6, 0],
    [5, 0, 9, 0],
    [6, 9, 0, 4],
    [0, 0, 4, 0]
]

print(prim_mst(graph))
