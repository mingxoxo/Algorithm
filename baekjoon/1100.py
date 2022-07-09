# 하얀 칸
# 22.07.10
# https://www.acmicpc.net/problem/1100

import sys
input = sys.stdin.readline

cnt = 0
for i in range(8):
    board = list(input().strip())
    cnt += sum([1 for j in range(i % 2, 8, 2) if board[j] == 'F'])

print(cnt)


