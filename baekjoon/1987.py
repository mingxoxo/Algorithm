# 알파벳
# 23.02.10
# 백트래킹, DFS - Pypy3
# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline

result = 0
R, C = map(int, input().split())

def dfs(board, charset, x, y, cnt):
    global result, R, C

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord('A')
            if charset[idx] == 0:
                charset[idx] = 1
                dfs(board, charset, nx, ny, cnt + 1)
                charset[idx] = 0
            else:
                result = cnt if result < cnt else result

board = []
for _ in range(R):
    board.append(list(input().rstrip()))


charset = [0] * 26
idx = ord(board[0][0]) - ord('A')
charset[idx] = 1
dfs(board, charset, 0, 0, 1)

print(result)
