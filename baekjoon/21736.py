# 헌내기는 친구가 필요해
# BFS
# 24.12.08
# https://www.acmicpc.net/problem/21736


import sys
from collections import deque

input=sys.stdin.readline



def bfs(start):
    queue = deque([start])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 0
    graph[start[0]][start[1]] == 'X'
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 'X':
                    continue
                if graph[nx][ny] == 'P':
                    cnt += 1
                
                graph[nx][ny] = 'X'
                queue.append((nx, ny))
    
    return cnt



N, M = map(int, input().split())

graph = []
doyeon = (0, 0)

for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'I':
            doyeon = (i, j)
            
n = bfs(doyeon)
print(n) if n != 0 else print('TT')
