#아기상어2
#https://www.acmicpc.net/problem/17086
#python3로 통과 ( 33016KB / 112ms )

from collections import deque

def positive_space(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def safe_space(space, baby_shark):
    visited = [[0] * M for _ in range(N)]
    queue = deque(baby_shark)
    for x, y in baby_shark:
        space[x][y] = 0
        visited[x][y] = 1

    while queue:
        node = queue.popleft()
        for a, b in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
            if positive_space(node[0] + a, node[1] + b):
                space[node[0]][node[1]] = min(space[node[0]][node[1]], space[node[0]+a][node[1]+b] + 1)
                if visited[node[0] + a][node[1] + b] == 0:
                    visited[node[0] + a][node[1] + b] = 1
                    queue.append((node[0] + a, node[1] + b))
    return space


N, M = map(int, input().split())
baby_shark = []
space = [[] for _ in range(N)]
for i in range(N):
    space[i] = list(map(int, input().split()))
    for j in list(filter(lambda x: space[i][x] == 1, range(M))): #filter와 lambda
        baby_shark.append((i, j))

safe = [[51] * M for _ in range(N)]
safe = safe_space(safe, baby_shark)

print(max(map(max, safe)))


