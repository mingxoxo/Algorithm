#촌수계산
#https://www.acmicpc.net/problem/2644
#이전에 DFS_BFS로 풀지 못해서 한번 더 품

from collections import deque

def relatives_bfs(graph, num1, num2):
    visited = [0] * (n+1)
    queue = deque([num1])
    while queue:
        node = queue.popleft()
        for i in graph[node-1]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1 + visited[node]
                if i == num2:
                    return visited[num2]
    return -1


n = int(input()) #전체 사람의 수
num1, num2 = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호

m = int(input()) #부모 자식든 간의 관계의 개수
graph = [[] * n for i in range(n)]

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node2-1].append(node1)
    graph[node1-1].append(node2)

print(relatives_bfs(graph, num1, num2))
