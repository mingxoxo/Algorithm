# 아기 상어
# 24.03.04
# BFS
# https://www.acmicpc.net/problem/16236
# 예제 4번 해결 참고: https://www.acmicpc.net/board/view/66829

import heapq
from collections import deque
import sys
input=sys.stdin.readline


def bfs(N, size, sx, sy):
    global graph

    visited = [[-1] * N for _ in range(N)]
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

    queue = deque([(sx, sy)])
    visited[sx][sy] = 0

    result = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] != -1 or size < graph[nx][ny]:
                    continue

                visited[nx][ny] = visited[x][y] + 1

                if 0 < graph[nx][ny] < size:
                    heapq.heappush(result, (visited[nx][ny], nx, ny))
                queue.append((nx, ny))

    if result:
        return heapq.heappop(result)
    return 0, 0, 0



N = int(input())
graph = []
sx, sy = -1, -1
fish_cnt = 0
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    for j in range(N):
        if 1 <= graph[i][j] <= 6:
            fish_cnt += 1
        elif graph[i][j] == 9:
            sx, sy = i, j


time, size, size_cnt = 0, 2, 0
while fish_cnt:
    graph[sx][sy] = 0
    add_time, sx, sy = bfs(N, size, sx, sy)
    if add_time == 0:
        break
    time += add_time

    fish_cnt -= 1
    size_cnt += 1
    if size == size_cnt:
        size += 1
        size_cnt = 0

print(time)
