# 플로이드
# 23.06.25
# 플로이드-워셜
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 10**9
cost = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for i in range(n):
    cost[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(n):
    for j in range(n):
        print(cost[i][j], end=' ') if cost[i][j] != INF else print(0, end=' ')
    print()
