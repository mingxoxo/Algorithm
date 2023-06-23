# 케빈 베이컨의 6단계 법칙
# 23.06.23
# 플로이드 워셜
# https://www.acmicpc.net/problem/1389

# 공부: https://it-garden.tistory.com/247

import sys

inf = sys.maxsize

N, M = map(int, input().split())
dist = [[inf] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, N + 1):   # 거치는 점
    for i in range(1, N + 1):   # 시작 점
        for j in range(1, N + 1):   # 끝 점
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
kevin_bacon = [sum(arr[1:]) for arr in dist[1:]]
print(kevin_bacon.index(min(kevin_bacon)) + 1)
