# 키 순서
# 24.02.22
# 플로이드 워셜 (Pypy로 통과 / python3는 시간 초과)
# python3로 통과한 코드에서는 대부분 dfs로 해결
# https://www.acmicpc.net/problem/2458

import sys
input=sys.stdin.readline

INF = 10**4
N, M = map(int, input().split())
dist = [[INF] * (N + 1) for _ in range(N + 1)]
arr = [[0, 0] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    arr[a][1] += 1
    arr[b][0] += 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                if dist[i][j] == INF:
                    arr[i][1] += 1
                    arr[j][0] += 1
                dist[i][j] = dist[i][k] + dist[k][j]

cnt = 0    
for in_cnt, out_cnt in arr:
    if in_cnt + out_cnt == N - 1:
        cnt += 1
        
print(cnt)
