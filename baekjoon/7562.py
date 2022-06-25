# 나이트의 이동
# 22.06.25
# BFS
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

def BFS(I, start, dest):
    if start == dest:
        return 0
    visited = [[0] * I for i in range(I)]
    queue = deque([start])
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if dest == (nx, ny):
                        return visited[nx][ny]
    return 0


T = int(input())
for _ in range(T):
    I = int(input())
    starting_point = tuple(map(int, input().split()))
    destination = tuple(map(int, input().split()))
    print(BFS(I, starting_point, destination))
