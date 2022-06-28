# 데스 나이트
# 22.06.29
# BFS
# https://www.acmicpc.net/problem/16948

import sys
from collections import deque
input = sys.stdin.readline


def BFS(N, r1, c1, r2, c2):
    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]
    board = [[0] * N for _ in range(N)]
    queue = deque([(r1, c1)])
    while queue:
        node = queue.popleft()
        r, c = node[0], node[1]
        if (r, c) == (r2, c2):
            return board[r][c]
        for i in range(6):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                queue.append((nr, nc))
    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(BFS(N, r1, c1, r2, c2))
