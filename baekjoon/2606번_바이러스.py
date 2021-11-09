import copy
from collections import deque


def bfs(graph, visited, V=1 ):
    cnt = -1
    queue = deque([V])
    visited[V] = True
    while queue:
        virus = queue.popleft()
        cnt += 1
        while len(graph[virus]):
            nextvirus = graph[virus].pop()
            if visited[nextvirus] is False:
                queue.append(nextvirus)
                visited[nextvirus] = True
#             for i in range(len(graph)):
#                 if nextvirus in graph[i]:
#                     graph[i].remove(nextvirus)
    return cnt


N = int(input())
M = int(input())

# 인접리스트로 그래프 표현 ( 0번째 인덱스 사용 X )
graph = [[] for _ in range(N + 1)]

for i in range(M):
    edge1, edge2 = list(map(int, input().split()))
    graph[edge1].append(edge2)
    graph[edge2].append(edge1)

visited = [False] * (N+1)
print(bfs(graph, visited, 1))
