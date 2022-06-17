#N-Queen
#https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

def check_position(queen, i, j):
    for k in range(i):
        if queen[k] == j:
            return 0
        if (queen[k] - j)**2 == (k - i)**2:
            return 0
    return 1


def recursive_queen(queen, N, i, cnt):
    if i == N:
        return cnt + 1
    for j in range(N):
        if check_position(queen, i, j):
            queen[i] = j
            cnt = recursive_queen(queen, N, i + 1, cnt)
    return cnt


N = int(input())
queen = [0] * N
print(recursive_queen(queen, N, 0, 0))

