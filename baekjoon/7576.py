#토마토
#BFS
#https://www.acmicpc.net/problem/7576
#https://programmers.co.kr/learn/courses/4008/lessons/12738

import sys
from collections import deque
input = sys.stdin.readline

def BFS(storage, ripe_tomatoes, N, M):
    queue = deque(ripe_tomatoes)
    cor_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    while queue:
        node = queue.popleft()
        for a, b in cor_list:
            x, y = node[0] + a, node[1] + b
            if 0 <= x < N and 0 <= y < M:
                if storage[x][y] == 0:
                    queue.append((x, y))
                    storage[x][y] = storage[node[0]][node[1]] + 1
                    cnt = storage[node[0]][node[1]]

    for i in range(N):
        for j in range(M):
            if storage[i][j] == 0:
                return (-1)
    return (cnt)
    # if sum(storage, []).count(0) != 0:
    #     return (-1)
    # return (max(sum(storage, [])) - 1)


M, N = map(int, input().split())
storage = []
ripe_tomatoes = []

for i in range(N):
    storage.append(list(map(int, input().split())))
    ripe_tomatoes.extend([(i, j) for j in range(M) if storage[-1][j] == 1])

print(BFS(storage, ripe_tomatoes, N, M))
