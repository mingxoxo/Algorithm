# 음식물 피하기
# 22.08.15
# BFS
# https://www.acmicpc.net/problem/1743

import sys
from collections import deque
input = sys.stdin.readline

def BFS(space, visited, N, M, start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([start])
    result = 0
    
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        result += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if space[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    
    return result


def main():
    N, M, K = map(int, input().split())
    space = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    trash = []
    result = 0
    
    for _ in range(K):
        r, c = map(int, input().split())
        space[r-1][c-1] = 1
        trash.append((r-1, c-1))
    
    for r, c in trash:
        if visited[r][c] == 0:
            visited[r][c] = 1
            result = max(result, BFS(space, visited, N, M, (r, c)))
    
    print(result)
    

if __name__=="__main__":
    main()
