# 단지번호붙이기
# 22.08.31
# BFS
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline


def BFS(N, house_map, start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([start])
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1:
                queue.append((nx, ny))
                house_map[nx][ny] = 0

    return cnt

N = int(input())
house_map = [list(map(int, input().strip())) for _ in range(N)]

cnt = []
for i in range(N):
    for j in range(N):
        if house_map[i][j] == 1:
            house_map[i][j] = 0
            cnt.append(BFS(N, house_map, (i, j)))

print(len(cnt))
print(*(sorted(cnt)), sep='\n')
