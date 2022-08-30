# 섬의 개수
# 22.08.31
# BFS
# https://www.acmicpc.net/problem/4963


import sys
from collections import deque
input = sys.stdin.readline


def BFS(h, w, square, start):
    dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and square[nx][ny] == 1:
                queue.append((nx, ny))
                square[nx][ny] = 0

    return 1

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    square = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if square[i][j] == 1:
                square[i][j] = 0
                cnt += BFS(h, w, square, (i, j))

    print(cnt)
