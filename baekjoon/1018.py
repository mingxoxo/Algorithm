# 체스판 다시 칠하기
# 23.04.25
# 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

def count_painting(board, x, y):
    cnt = [0, 0]

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            ch = 'W' if (i + j) % 2 == 0 else 'B'
            if board[i][j] == ch:
                cnt[1] += 1
            else:
                cnt[0] += 1

    return min(cnt)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().rstrip())

result = 64
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, count_painting(board, i, j))

print(result)
