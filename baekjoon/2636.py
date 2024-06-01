# 치즈
# 24.06.01
# BFS
# https://www.acmicpc.net/problem/2636

from collections import deque
from collections import defaultdict


def bfs(h, w, board):
    visited = [[False for _ in range(w)] for _ in range(h)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    time_queue = deque([(0, 0, 0)])
    time_cnt = defaultdict(int)

    while time_queue:
        queue = deque([time_queue.popleft()])

        while queue:
            x, y, time = queue.popleft()
            visited[x][y] = True
            if time != 0 and board[x][y] == 1:
                time_cnt[time] += 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] is False:
                    if board[nx][ny] == 0:
                        queue.append((nx, ny, time))
                        visited[nx][ny] = True
                        continue

                    if board[nx][ny] == 1:
                        time_queue.append((nx, ny, time + 1))
                        visited[nx][ny] = True

    return time, time_cnt[time]


h, w = map(int, input().split())
board = [list(map(int, input().split())) for j in range(h)]
time, cnt = bfs(h, w, board)
print(time)
print(cnt)
