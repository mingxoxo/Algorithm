# 녹색 옷 입은 애가 젤다지?
# 24.04.01
# BFS
# https://www.acmicpc.net/problem/4485


from collections import deque
import sys
input=sys.stdin.readline

INF = 10 ** 7
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(N, graph):
    global dx, dy

    visited = [[INF] * N for _ in range(N)]
    queue = deque([(0, 0, graph[0][0])])
    visited[0][0] = graph[0][0]

    while queue:
        x, y, rupee = queue.popleft()
        if visited[x][y] < rupee:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_rupee = rupee + graph[nx][ny]
                if visited[nx][ny] <= new_rupee:
                    continue
                visited[nx][ny] = new_rupee
                queue.append((nx, ny, new_rupee))

    return visited[N-1][N-1]



i = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(N)]
    print(f'Problem {i}: {bfs(N, graph)}')
    i += 1
