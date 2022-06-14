# 불!
# BFS
#https://www.acmicpc.net/problem/4179

import sys
from collections import deque
input = sys.stdin.readline

def BFS(miro, first, fire, R, C):
    queue_J = deque(first)
    queue_F = deque(fire)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue_F:
        node = queue_F.popleft()
        x, y, cnt = node[0], node[1], node[2]
        miro[x][y] = cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if miro[nx][ny] in ['.', 'J']:
                    queue_F.append((nx, ny, cnt + 1))
                    miro[nx][ny] = cnt + 1
    while queue_J:
        node = queue_J.popleft()
        x, y, cnt = node[0], node[1], node[2]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if miro[nx][ny] not in ['#', 'J'] and (miro[nx][ny] == '.' or miro[nx][ny] > cnt + 1):
                    queue_J.append((nx, ny, cnt + 1))
                    miro[nx][ny] = 'J'
            else:
                return cnt + 1

    return "IMPOSSIBLE"


R, C = map(int, input().split())
miro = []
first = []
fire = []

for i in range(R):
    miro.append(list(input().strip()))
    first.extend([(i, j, 0) for j in range(C) if miro[-1][j] == 'J'])
    fire.extend([(i, j, 0) for j in range(C) if miro[-1][j] == 'F'])

print(BFS(miro, first, fire, R, C)
