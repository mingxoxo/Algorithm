# 벽 부수고 이동하기 2 (PyPy3)
# 24.03.01
# BFS
# https://www.acmicpc.net/problem/14442

from collections import deque
import sys
input=sys.stdin.readline


def bfs(N, M, K):
    global graph

    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, cnt = queue.popleft()
        dist = visited[x][y][cnt]

        if x + 1 == N and y + 1 == M:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and cnt < K and visited[nx][ny][cnt + 1] == 0:
                    visited[nx][ny][cnt + 1] = dist + 1
                    queue.append((nx, ny, cnt + 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = dist + 1
                    queue.append((nx, ny, cnt))

    return -1



N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(N, M, K))
