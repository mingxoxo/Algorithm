# 웜홀 ⚠️
# 벨만-포드
# 24.03.08
# 공부: https://velog.io/@nacean/%EB%B0%B1%EC%A4%801865-%EC%9B%9C%ED%99%80-C-%ED%92%80%EC%9D%B4
# INF 처리: https://www.acmicpc.net/board/view/50494

import sys
input=sys.stdin.readline

INF = 10001


def bellman_ford(N, graph):
    dist = [INF] * (N + 1)

    for _ in range(1, N + 1):
        for s, e, t in graph:
            if dist[s] + t < dist[e]:
                dist[e] = dist[s] + t
    for s, e, t in graph:
        if dist[s] + t < dist[e]:
            return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))

    if bellman_ford(N, graph) is True:
        print('YES')
    else:
        print('NO')

