#미로 탐색
#22.06.20
#BFS
#https://www.acmicpc.net/problem/2178

import sys
from collections import deque
input = sys.stdin.readline

def BFS(miro, N, M):
    queue = deque([(0, 0)])
    cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in cor:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                queue.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[N - 1][M - 1]




N, M = map(int, input().split())
miro = []

for i in range(N):
    miro.append(list(map(int, input().strip())))
print(BFS(miro, N, M))

