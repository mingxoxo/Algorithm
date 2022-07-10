# 영역 구하기
# 22.07.11
# BFS
# https://www.acmicpc.net/problem/2583

import sys
from collections import deque
input = sys.stdin.readline

def BFS(M, N, paper):
    cnt = 0
    area_list = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(M):
        for j in range(N):
            if paper[i][j] == 1:
                continue
            queue = deque([(i, j)])
            paper[i][j] = 1
            area = 0
            while queue:
                node = queue.popleft()
                x, y = node[0], node[1]
                area += 1
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and paper[nx][ny] == 0:
                        paper[nx][ny] = 1
                        queue.append((nx, ny))
            cnt += 1
            area_list.append(area)
    return cnt, sorted(area_list)

M, N, K = map(int, input().split())

paper = [[0] * N for _ in range(M)]
rect = set()
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    rect.update([(i, j) for j in range(x1, x2) for i in range(y1, y2)])

paper = [[1 if (i, j) in rect else 0 for j in range(N)] for i in range(M) ]
cnt, area_list = BFS(M, N, paper)
print(cnt)
print(*area_list)


