#연구소
#22.06.24
#구현, 그래프 이론, 브루트포스 알고리즘, BFS
#https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def BFS(lab, N, M, virus, area):
    queue = deque(virus)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if lab[nx][ny] == 0 and (nx, ny) not in area:
                    queue.append((nx, ny))
                    lab[nx][ny] = 2
                    cnt += 1
    return cnt

N, M = map(int, input().split())
lab = []
virus = []
safe_area = []
max_s = 0

for i in range(N):
    lab.append(list(map(int, input().split())))
    virus.extend([(i, j) for j in range(M) if lab[-1][j] == 2])
    safe_area.extend([(i, j) for j in range(M) if lab[-1][j] == 0])

len_s = len(safe_area) - 3
area = combinations(safe_area, 3)
for area_element in area:
    max_s = max(max_s, len_s - BFS(copy.deepcopy(lab), N, M, virus, area_element))

print(max_s)





