# 벽 부수고 이동하기 ⚠️
# 24.02.20
# BFS
# https://www.acmicpc.net/problem/2206
# 코드 참고: https://hongcoding.tistory.com/18

from collections import deque
import sys
input=sys.stdin.readline


def bfs(N, M, graph):
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y, is_break = queue.popleft()
        if (x + 1, y + 1) == (N, M):
            return visited[x][y][is_break]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and is_break == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, True))
                elif graph[nx][ny] == 0 and visited[nx][ny][is_break] == 0:
                    visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                    queue.append((nx, ny, is_break))
    
    return -1



N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(N, M, graph))
