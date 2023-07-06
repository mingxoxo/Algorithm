# 여행가자
# 23.07.06
# https://www.acmicpc.net/problem/1976

# BFS로 풀었는데 Union-find로 풀면 더 빠르게 해결 가능할 듯..!

from collections import deque


def BFS(N, graph, start):
    visited = [False] * N
    
    queue = deque([(start)])
    
    while queue:
        city = queue.popleft()
        visited[city] = True
        
        for next_city in range(N):
            if graph[city][next_city] == 1 and visited[next_city] == False:
                visited[next_city] = True
                queue.append(next_city)
    
    
    return set([i + 1 for i in range(N) if visited[i] == True])
    
    

N = int(input())
M = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

path = list(map(int, input().split()))
print("YES") if BFS(N, graph, path[0] - 1) & set(path) == set(path) else print("NO")
