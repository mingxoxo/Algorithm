# 문제 1. 개미와 진딧물
# 구현 / 완전 탐색 / 좌표 추출
# 맨해튼 거리로 계산하면 빠르게 할 수 있음


import sys
from collections import deque

input = sys.stdin.readline


def bfs(house, ant, N, M):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    result = 0

    while (ant):
        visited = [[0] * N for _ in range(N)]
        queue = deque([ant.popleft()])

        while queue:
            x, y = queue.popleft()

            if M <= visited[x][y]:
                continue

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                    if house[nx][ny] == 2:
                        result += 1
                        queue.clear()
                        break

    print(result)


N, M = map(int, input().split())
house = []
ant = deque()
for i in range(N):
    house.append(list(map(int, input().split())))
    ant.extend([(i, j) for j in range(N) if house[i][j] == 1])

bfs(house, ant, N, M)