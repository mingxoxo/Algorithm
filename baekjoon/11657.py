# 타임머신
# 22.12.10
# 벨만-포드
# https://www.acmicpc.net/problem/11657

import sys
input = sys.stdin.readline

def Bellman_Ford(edges, N):
    distance = [-1] * (N + 1)
    visited = [False] * (N + 1)

    visited[1] = True
    distance[1] = 0
    for i in range(N):
        for v1, v2, w in edges:
            if visited[v1] is False:
                continue
            if visited[v2] is False or distance[v1] + w < distance[v2]:
                if i == N - 1:      # cycle check
                    return [-1]
                distance[v2] = distance[v1] + w
                visited[v2] = True

    return distance[2:]



N, M = map(int, input().split())
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

print(*Bellman_Ford(edges, N), sep='\n')
