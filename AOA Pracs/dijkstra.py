# dijkstra algorithm
def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    visited = [False] * n
    distances[start] = 0

    for _ in range(n):
        min_distance = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i
        
        visited[min_index] = True

        for i in range(n):
            if not visited[i] and graph[min_index][i] != 0:
                distances[i] = min(distances[i], distances[min_index] + graph[min_index][i])
    return distances

if __name__ == '__main__':
    graph = [
        [0, 3, 2, 0],
        [3, 0, 1, 5],
        [2, 1, 0, 3],
        [0, 5, 3, 0]
    ]
    start_node = 0
    shortest_dist = dijkstra(graph, start_node)
    print(f"Shortest path from {start_node}: {shortest_dist}")