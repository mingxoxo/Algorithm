# N과 M (8)
# 백트래킹
# 22.11.01
# https://www.acmicpc.net/problem/15657

import sys
input = sys.stdin.readline


def backtracking(N, M, index, num, result):
    if M == 0:
        print(*result, sep=' ')
        return

    for i in range(index, N):
        result.append(num[i])
        backtracking(N, M - 1, i, num, result)
        result.pop()


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N

backtracking(N, M, 0, num, [])
