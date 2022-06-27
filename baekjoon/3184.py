# 양
# 22.06.28
# BFS
# https://www.acmicpc.net/problem/3184

import sys
from collections import deque
input = sys.stdin.readline


def BFS(yard, sheep, wolf, R, C):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    wolf_queue = deque(wolf)
    result = [len(sheep), len(wolf)]
    while wolf_queue:
        pos = wolf_queue.popleft()
        if yard[pos[0]][pos[1]] == 'X':
            continue
        w_cnt = 1
        s_cnt = 0
        yard[pos[0]][pos[1]] = 'X'
        queue = deque([pos])
        while queue:
            node = queue.popleft()
            x, y = node[0], node[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and yard[nx][ny] not in ['X', '#']:
                    if yard[nx][ny] == 'o':
                        s_cnt += 1
                    elif yard[nx][ny] == 'v':
                        w_cnt += 1
                    yard[nx][ny] = 'X'
                    queue.append((nx, ny))
        if w_cnt >= s_cnt:
            result[0] -= s_cnt
        else:
            result[1] -= w_cnt
    return result


yard = []
sheep = []
wolf = []
R, C = map(int, input().split())
for i in range(R):
    yard.append(list(input().strip()))
    sheep.extend((i, j) for j in range(C) if yard[i][j] == 'o')
    wolf.extend((i, j) for j in range(C) if yard[i][j] == 'v')

print(*BFS(yard, sheep, wolf, R, C))
