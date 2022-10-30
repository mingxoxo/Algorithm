# 문제 2. 단풍나무
# 2차원 배열 / 시뮬레이션 / BFS

import sys
from collections import deque
import copy

input = sys.stdin.readline


def BFS(graph, queue, N):
    result = 0
    cnt = len(queue)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp = copy.deepcopy(graph)

    while queue:
        x, y = queue.popleft()
        cnt -= 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if tmp[nx][ny] == 0:
                    graph[x][y] -= 1
            if graph[x][y] == 0:
                break

        if graph[x][y] != 0:
            queue.append((x, y))

        if cnt == 0:
            result += 1
            cnt = len(queue)
            tmp = copy.deepcopy(graph)

    return result


N = int(input())
graph = []
queue = deque()

for i in range(N):
    graph.append(list(map(int, input().strip().split(' '))))
    queue.extend([(i, j) for j in range(N) if graph[-1][j] != 0])

print(BFS(graph, queue, N))


# 문제 해설 -> 최악의 시간 복잡도 탐구 O(TN^2)