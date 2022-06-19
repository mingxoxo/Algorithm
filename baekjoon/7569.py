#22.06.19
#토마토(3차원)
#BFS
#https://www.acmicpc.net/problem/7569

import sys
from collections import deque
input = sys.stdin.readline

def BFS(storage, ripe_tomatoes, M, N, H):
    queue = deque(ripe_tomatoes)
    cor = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    day = 0
    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in cor:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and storage[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                storage[nz][nx][ny] = storage[z][x][y] + 1
                day = max(day, storage[z][x][y])
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if storage[i][j][k] == 0:
                    return -1
    return day




M, N, H = map(int, input().split())

storage = [[] for i in range(H)]
ripe_tomatoes = []

for i in range(H):
    for j in range(N):
        storage[i].append(list(map(int, input().split())))
        ripe_tomatoes.extend([(i, j, k) for k in range(M) if storage[i][-1][k] == 1])

print(BFS(storage, ripe_tomatoes, M, N, H))

