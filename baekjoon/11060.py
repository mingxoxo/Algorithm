# 점프 점프
# BFS
# https://www.acmicpc.net/problem/11060

import sys
from collections import deque
input = sys.stdin.readline

def BFS(maze, N):
    visited = [0] * N
    queue = deque([0])
    while queue:
        x = queue.popleft()
        if x == N - 1:
            return visited[x]
        for dx in range(1, maze[x] + 1):
            nx = x + dx
            if 0 <= nx < N and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return -1


N = int(input())
maze = list(map(int, input().split()))
print(BFS(maze, N))
