# 네트워크 연결
# 22.12.13
# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1922

import sys
import heapq
input = sys.stdin.readline


def find(parent, v):
    if parent[v] == v:
        return v
    parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, v1, v2):
    root1 = find(parent, v1)
    root2 = find(parent, v2)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


def KruskalMST(graph, N):
    parent = [i for i in range(N + 1)]
    result = 0
    size = N
    while 1 < size :
        w, h1, h2 = heapq.heappop(graph)
        if find(parent, h1) == find(parent, h2):
            continue
        union(parent, h1, h2)
        result += w
        size -= 1

    return result



graph = []
N = int(input())
M = int(input())
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(graph, (C, A, B))

print(KruskalMST(graph, N))
