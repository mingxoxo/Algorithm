# 최소비용 구하기 2
# Dijkstra
# 22.11.19
# https://www.acmicpc.net/problem/11779

import copy
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def Dijkstra(graph, ori, dst, N):
    heap = [(0, ori, [ori])]
    visited = [-1] * (N + 1)
    city = [[] for _ in range(N + 1)]
    visited[ori] = 0
    city[ori].append(ori)

    while heap:
        w, n, c = heapq.heappop(heap)
        if visited[n] < w:
            continue
        if n == dst:
            break
        for x, xw in graph[n]:
            if visited[x] == -1 or w + xw < visited[x]:
                visited[x] = w + xw
                city[x] = copy.deepcopy(c)
                city[x].append(x)
                heapq.heappush(heap, (w + xw, x, city[x]))

    return visited[dst], city[dst]


N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    ori, dst, w = map(int, input().split())
    graph[ori].append((dst, w))

# (1, 2, 2), (1, 2, 5), (1, 2, 3), (1, 2, 2)
# for i in range(M):
#     graph[i].sort(key=lambda x: x[1])

ori, dst = map(int, input().split())
cost, city_list = Dijkstra(graph, ori, dst, N)
print(cost)
print(len(city_list))
print(*city_list)
