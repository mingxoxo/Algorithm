# 스타트링크
# 22.08.31
# BFS
# https://www.acmicpc.net/problem/5014

import sys
from collections import deque
input = sys.stdin.readline


def BFS(F, S, G, U, D):
    dx = [U, -1 * D]
    building = [-1] * (F + 1)

    queue = deque([S])
    building[S] = 0
    if S == G:
        return 0
    while queue:
        x = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 0 < nx <= F and building[nx] == -1:
                building[nx] = building[x] + 1
                if nx == G:
                    return building[nx]
                queue.append(nx)
    
    return "use the stairs"
    

F, S, G, U, D = map(int, input().split())

print(BFS(F, S, G, U, D))
