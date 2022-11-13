# 문제 2. 모래섬
# 2차원 배열 / 시뮬레이션 / 그래프 탐색

import sys
import copy
from collections import deque

input = sys.stdin.readline


def check_bridge_bfs(visited, start, N, M):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    queue.append((nx, ny))

    return 1


def bfs(sand, water, N, M):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    result = 0

    while water:

        queue = deque(copy.deepcopy(water))
        water = deque()
        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if sand[nx][ny] == 1:
                        sand[nx][ny] = 0
                        water.append((nx, ny))
        result += 1

        visited = copy.deepcopy(sand)
        cnt = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 1:
                    visited[i][j] = 0
                    cnt += check_bridge_bfs(visited, (i, j), N, M)

        if 1 < cnt:
            return result

    return -1


N, M = map(int, input().split())
sand = []
water = []
for i in range(N):
    sand.append(list(map(int, input().split())))
    water.extend([(i, j) for j in range(M) if sand[i][j] == 0])

print(bfs(sand, water, N, M))