# 전쟁 - 전투
# 22.08.14
# BFS
# https://www.acmicpc.net/problem/1303

import sys
from collections import deque
input = sys.stdin.readline

def BFS(N, M, soldier, visited, start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    color = soldier[start[0]][start[1]]
    queue = deque([start])
    power = 0

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        power += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and color == soldier[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return power**2


def main():
    N, M = map(int, input().split())
    soldier = [input().strip() for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    power = {'W': 0, 'B': 0}

    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                power[soldier[i][j]] += BFS(N, M, soldier, visited, (i, j))

    print(*power.values())


if __name__=="__main__":
    main()
