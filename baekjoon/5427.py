# 불
# 24.06.20
# BFS
# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

input=sys.stdin.readline
IMPOSSIBLE = 10**7

def bfs(graph, start, fire, w, h):
    global IMPOSSIBLE

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    fire_queue = deque(fire)
    queue = deque([start])

    while queue:
        fire_queue_cnt = len(fire_queue)
        for _ in range(fire_queue_cnt):
            x, y, cnt = fire_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] in ['@', '.']:
                    graph[nx][ny] = '*'
                    fire_queue.append((nx, ny, cnt + 1))

        queue_cnt = len(queue)
        for _ in range(queue_cnt):
            x, y, cnt = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < h and 0 <= ny < w):
                    return cnt + 1
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    queue.append((nx, ny, cnt + 1))

    return IMPOSSIBLE


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    start = (0, 0)
    fire = []
    for i in range(h):
        graph.append(list(input().rstrip()))
        for j in range(w):
            if graph[i][j] == '@':
                start = (i, j, 0)
            elif graph[i][j] == '*':
                fire.append((i, j, 0))

    result = bfs(graph, start, fire, w, h)
    print(result) if result != IMPOSSIBLE else print("IMPOSSIBLE")
