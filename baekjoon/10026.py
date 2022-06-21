#적록색약
#22.06.22
#BFS
#https://www.acmicpc.net/problem/10026

import sys
from collections import deque
input = sys.stdin.readline


def BFS(N, picture):
    cor_queue = deque([(i, j) for i in range(N) for j in range(N)])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cnt = 0
    while cor_queue:
        cor = cor_queue.popleft()
        a, b = cor[0], cor[1]
        if picture[a][b] == 'X':
            continue
        queue = deque([(a, b)])
        group = picture[a][b]
        picture[a][b] = 'X'
        cnt += 1
        while queue:
            node = queue.popleft()
            x, y = node[0], node[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if picture[nx][ny] == group:
                        queue.append((nx, ny))
                        picture[nx][ny] = 'X'
    return cnt


N = int(input())
RGBpicture = []
RBpicture = []
for i in range(N):
    RGBpicture.append(list(input().strip()))
    RBpicture.append([c if c != 'G' else 'R' for c in RGBpicture[-1]])

print(BFS(N, RGBpicture), BFS(N, RBpicture))

