# 연구소 3
# 브루트포스, BFS
# 23.07.05
# https://www.acmicpc.net/problem/17142

import sys
input = sys.stdin.readline

import copy
from itertools import combinations
from collections import deque

def bfs(N, info, active_virus, cnt):
    queue = deque(active_virus)

    if cnt == 0:
        return 0
        
    while queue:
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        x, y, time = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and info[nx][ny] != 1:
                if info[nx][ny] == 0:
                    cnt -= 1
                    if cnt == 0:
                        info[nx][ny] = 1
                        return time + 1
                info[nx][ny] = 1
                queue.append((nx, ny, time + 1))
        
    
    return 10**9
    

N, M = map(int, input().split())
virus = []

info = []
cnt = 0
for i in range(N):
    info.append(list(map(int, input().split())))
    for j in range(N):
        if info[i][j] == 0:
            cnt += 1
        elif info[i][j] == 2:
            virus.append((i, j, 0))
            

ans = 10 ** 9
for active_virus in combinations(virus, M):
    for x, y, _ in active_virus:
        info[x][y] = 1

    ans = min(ans, bfs(N, copy.deepcopy((info)), active_virus, cnt))

    for x, y, _ in active_virus:
        info[x][y] = 2


print(ans) if ans != 10 ** 9 else print(-1)
