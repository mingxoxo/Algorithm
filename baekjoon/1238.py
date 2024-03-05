# 파티
# 24.03.05
# 다익스트라
# https://www.acmicpc.net/problem/1238
# 다익스트라 heapq 구현 공부: https://velog.io/@jaegil123/%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python-%ED%9E%99-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90

from collections import defaultdict
import heapq
import sys
input=sys.stdin.readline

INF = 10 ** 7

def dijkstra(start):
    global graph, N
    
    queue = []
    dist = [INF] * (N + 1)
    
    dist[start] = 0
    heapq.heappush(queue, (0, start))
    
    while queue:
        node_dist, node = heapq.heappop(queue)
        if dist[node] < node_dist:
            continue
        
        for idx, time in graph[node]:
            cost = dist[node] + time
            if cost < dist[idx]:
                dist[idx] = cost
                heapq.heappush(queue, (cost, idx))
    
    return dist


N, M, X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    

result = [0] * (N + 1)
for i in range(1, N + 1):
    dist = dijkstra(i)
    if i != X:
        result[i] += dist[X]
    else:
        for j in range(1, N + 1):
            result[j] += dist[j]

print(max(result))
    
    
