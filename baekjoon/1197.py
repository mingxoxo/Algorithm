# 최소 스패닝 트리
# 22.12.12
# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

import sys
import heapq
input = sys.stdin.readline

def KruskalMST(graph, V):
    sack = [i for i in range(V + 1)]
    result = 0
    while graph:
        w, v1, v2 = heapq.heappop(graph)
        if sack[v1] == sack[v2]:
            continue
        result += w
        v1_sack, v2_sack = sack[v1], sack[v2]
        sack = [v if v != v2_sack else v1_sack for v in sack]

    return result



graph = []
V, E = map(int, input().split())
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(graph, (C, A, B))

print(KruskalMST(graph, V))
