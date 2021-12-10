#Python3로 돌리면 시간 초과
#PyPy3로 돌리면 통과 -- 메모리 197904KB / 시간 868ms

from collections import deque


def bfs(graph, N):
    visited = [0] * N
    count = 0
    while sum(visited) != N:
        queue = deque([visited.index(0)+1])
        visited[visited.index(0)] = 1
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if visited[i-1] == 0:
                    queue.append(i)
                    visited[i-1] = 1
        count+=1
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(graph, N))
