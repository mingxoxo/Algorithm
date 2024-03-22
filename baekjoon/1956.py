# 운동 ⚠️
# 24.03.22
# 플로이드 워셜 (다익스트라 응용으로 풀려고 했는데 메모리 초과..)
# https://www.acmicpc.net/problem/1956

import sys
input=sys.stdin.readline
INF = 1e9

def floyd_warshall():
    global dist

    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return min([dist[i][i] for i in range(1, V + 1)])


V, E = map(int, input().split())
dist = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

result = floyd_warshall()
print(result) if result != INF else print(-1)
