# 달이 차오른다, 가자.
# 24.03.29
# BFS, 비트마스킹
# https://www.acmicpc.net/problem/1194


from collections import deque, defaultdict
import sys
input=sys.stdin.readline


def set_bit(n, bit):
    return n | (1 << bit)


def get_bit(n, bit):
    return n & (1 << bit)


def bfs(sx, sy):
    global N, M, maze

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[defaultdict(lambda: 10**7) for _ in range(M)] for _ in range(N)]
    visited[sx][sy][0] = 0

    queue = deque([(sx, sy, 0)])
    while queue:
        x, y, key = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            new_key = key
            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue
            ch = maze[nx][ny]
            if ch == '1':
                return visited[x][y][key] + 1
            if ch == '#':
                continue
            if ch.isalpha():
                if ch.isupper() and get_bit(new_key, ord(ch) - ord('A')) == 0:
                    continue
                elif ch.islower():
                    new_key = set_bit(new_key, ord(ch) - ord('a'))

            if visited[nx][ny][new_key] <= visited[x][y][key] + 1:
                continue
            visited[nx][ny][new_key] = visited[x][y][key] + 1
            queue.append((nx, ny, new_key))

    return -1


N, M = map(int, input().split())
sx, sy = -1, -1
maze = []

for i in range(N):
    maze.append(list(input().rstrip()))
    if sx == -1 and sy == -1:
        for j in range(M):
            if maze[i][j] == '0':
                sx, sy = i, j
                maze[i][j] = '.'

print(bfs(sx, sy))
