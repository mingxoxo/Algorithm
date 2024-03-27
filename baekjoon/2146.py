# 다리 만들기
# 24.03.27
# BFS
# https://www.acmicpc.net/problem/2146

from collections import deque
import sys
input=sys.stdin.readline


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(graph, sx, sy, N):
    global dx, dy

    visited = [[0] * N for _ in range(N)]
    bridge_queue = deque([])
    island_queue = deque([(sx, sy)])
    visited[sx][sy] = -1

    while island_queue:
        x, y = island_queue.popleft()
        graph[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] != -1:
                    visited[nx][ny] = -1
                    island_queue.append((nx, ny))
                elif graph[nx][ny] == 0 and visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    bridge_queue.append((nx, ny))

    while bridge_queue:
        x, y = bridge_queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 or visited[nx][ny] != 0:
                    continue
                if graph[nx][ny] != 0:
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                bridge_queue.append((nx, ny))

    return -1


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 1000
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans = min(ans, bfs(graph, i, j, N))

print(ans)
