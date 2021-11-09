import copy
from collections import deque


def dfs(graph, v):
    if graph[v][v] != -1:
        print(v + 1, end=' ')
        for i in range(len(graph)):
            graph[i][v] = -1  # 방문했다
    while True:
        node = graph[v].index(1) if 1 in graph[v] else None# 방문하지 않은 연결된 노드 가져오기
        if node is None:
            return
        graph[v][node] = -1  # 방문했다
        dfs(graph, node)
    return


def bfs(graph, firstV):
    queue = deque([firstV])
    graph[firstV][firstV] = -1
    for i in range(len(graph)):
        graph[i][firstV] = -1  # 방문했다
    while queue:
        v = queue.popleft()
        print(v + 1, end=' ')
        while True:
            try:
                node = graph[v].index(1)  # 방문하지 않은 연결된 노드 가져오기
            except:
                break
            if graph[node][node] != -1:
                queue.append(node)
                for i in range(len(graph)):
                    graph[i][node] = -1  # 방문했다


N, M, V = list(map(int, input().split()))

# 인접행렬로 그래프 표현 ( 연결X --> 0 / 연결O --> 1)
graph = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    edge1, edge2 = list(map(int, input().split()))
    graph[edge1 - 1][edge2 - 1] = 1
    graph[edge2 - 1][edge1 - 1] = 1

dfs(copy.deepcopy(graph), V - 1)
print()
bfs(copy.deepcopy(graph), V - 1)

