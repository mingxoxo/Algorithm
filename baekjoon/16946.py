# 벽 부수고 이동하기 4 ⚠️
# BFS
# 24.02.21
# https://www.acmicpc.net/problem/16946

from collections import deque
import sys
input=sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
group_idx = -1
group_cnt = {}

def is_movable(nx, ny):
    return (0 <= nx < N and 0 <= ny < M)

def bfs(graph, start):
    global N, M
    global dx, dy, group_idx
    
    queue = deque([start])
    graph[start[0]][start[1]] = group_idx
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not is_movable(nx, ny):
                continue
            if graph[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = group_idx
            cnt += 1
    
    group_cnt[group_idx] = cnt % 10
    group_idx -= 1


def get_move_cnt(graph, x, y):
    global dx, dy
    global group_cnt

    cnt = 1
    dup_check = set()
    for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_movable(nx, ny) and graph[nx][ny] != 1:
                if graph[nx][ny] == 0:
                    bfs(graph, (nx, ny))
                dup_check.add(graph[nx][ny])
                
    for idx in dup_check:
        cnt += group_cnt[idx]
    return cnt % 10


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]


for i in range(N):
    for j in range(M):
        print(get_move_cnt(graph, i, j), end='') if graph[i][j] == 1 else print(0, end='')
    print()
    
