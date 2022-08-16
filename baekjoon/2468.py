# 안전 영역
# 22.08.16
# BFS
# https://www.acmicpc.net/problem/2468

import sys
from collections import deque
input = sys.stdin.readline

def BFS(N, area, h):
    visited = [[0 if area[i][j] > h else 1 for j in range(N)] for i in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0

    for i in range(N):
        for j in range(N):
            queue = deque()
            if visited[i][j] == 0:
                queue.append((i, j))
                cnt += 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            queue.append((nx, ny))

    return cnt


def main():
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for h in range(0, 101):
        max_cnt = max(BFS(N, area, h), max_cnt)

    print(max_cnt)


if __name__=="__main__":
    main()
