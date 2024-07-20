INF = 999 # consider infinity
def display(dist):
    n = len(dist)
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end='   ')
            if j == n - 1:
                print()


def FloydWarshall(graph):
    n = len(graph)

    dist = [[INF] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    
    for k in range(n): # check connection by each vertex
        for i in range(n): # source vertex
            for j in range(n): # destination vertex
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == '__main__':
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
            ]
    print("\nEntered graph")
    display(graph)
    result = FloydWarshall(graph)
    print("\nFinal graph")
    display(result)