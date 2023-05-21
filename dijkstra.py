import sys
from heapq import heappop, heappush


def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    previous = [None] * n
    visited = [False] * n
    heap = [(0, start)]

    while heap:
        cost, current = heappop(heap)
        visited[current] = True

        for neighbor, weight in graph[current]:
            if visited[neighbor]:
                continue

            new_cost = cost + weight
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                previous[neighbor] = current
                heappush(heap, (new_cost, neighbor))

    return distance, previous


def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


def main():
    # Read graph from input file
    with open('g_dir_weigh_positive_5_15.txt', 'r') as file:
        N = int(file.readline())
        M = int(file.readline())
        graph = [[] for _ in range(N)]

        for _ in range(M):
            city1, city2, price = map(int, file.readline().split())
            graph[city1].append((city2, price))

    # Read source and destination cities from standard input
    source = int(input("Enter the source city: "))
    destination = int(input("Enter the destination city: "))

    # Run Dijkstra's algorithm
    distance, previous = dijkstra(graph, source)

    # Check if a path exists
    if distance[destination] == float('inf'):
        print("No path found from source to destination.")
    else:
        # Reconstruct the path and calculate the total cost
        path = reconstruct_path(previous, source, destination)
        total_cost = distance[destination]
        print("Cheapest travel route:", ' -> '.join(map(str, path)))
        print("Total price:", total_cost)


if __name__ == "__main__":
    main()
