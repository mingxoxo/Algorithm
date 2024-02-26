# 쉬운 최단거리
# 24.02.26
# BFS
# https://www.acmicpc.net/problem/14940

from collections import deque
import sys
input=sys.stdin.readline


def bfs(graph, start):
    global n, m
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[-1 if graph[i][j] != 0 else 0 for j in range(m)] for i in range(n)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited    
        



n, m = map(int, input().split())
graph = []
start = (-1, -1)
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)

for row in bfs(graph, start):
    print(*row)
