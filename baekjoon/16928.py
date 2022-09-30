# 뱀과 사다리 게임
# 22.09.30
# BFS
# https://www.acmicpc.net/problem/16928


import sys
from collections import deque

input = sys.stdin.readline


def BFS(info, start, end):
    dice = [1, 2, 3, 4, 5, 6]
    queue = deque([(start, 0)])
    visited = [0] * 101
    visited[start] = 1
    
    while queue:
        x, cnt = queue.popleft()
        for dx in dice:
            if x + dx <= end and visited[x + dx] == 0:
                nx = x + dx
                visited[nx] = 1
                if nx in info.keys():
                    nx = info[nx]
                    visited[nx] = 1
                if nx == end:
                    return cnt + 1
                queue.append((nx, cnt + 1))
    

info = {}

N, M = map(int, input().split())

for _ in range(N + M):
    a, b = map(int, input().split())
    info[a] = b
    
print(BFS(info, 1, 100))
