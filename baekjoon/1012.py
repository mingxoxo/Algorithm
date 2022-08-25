# 유기농 배추
# 22.08.25
# BFS
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
input = sys.stdin.readline

def BFS(field, N, M, start):
    queue = deque([start])
    cor_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dy, dx in cor_list:
            ny, nx = y + dy, x + dx            
            if 0 <= ny < N and 0 <= nx < M:
                if field[ny][nx] == 1:
                    queue.append((nx, ny))
                    field[ny][nx] = 0
                    
    return 1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]* M for _ in range(N)]
    cabbage = []
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
        cabbage.append((x, y))

    for x, y in cabbage:
        if field[y][x] == 1:
            field[y][x] = 0
            cnt += BFS(field, N, M, (x, y))
    
    print(cnt)
