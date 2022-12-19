# 늑대와 양
# 22.12.19
# 애드 혹 / 구성적
# https://www.acmicpc.net/problem/16956

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
sheep = []
result = 1
for i in range(R):
    graph.append(list(input().rstrip()))
    sheep.extend([(i, j) for j in range(C) if graph[i][j] == 'S'])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for x, y in sheep:
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] == 'W':
                result = 0
            elif graph[nx][ny] == '.':
                graph[nx][ny] = 'D'

print(result)
if result == 1:
    for g in graph:
        print(*g, sep='')
