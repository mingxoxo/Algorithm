# N과 M (7)
# 백트래킹
# 22.11.01
# https://www.acmicpc.net/problem/15656

import sys
input = sys.stdin.readline


def backtracking(num, n, cnt, result):
    if cnt == n:
        print(*result, sep=' ')
        return
    for i in num:
        result.append(i)
        brute_force(num, n, cnt + 1, result)
        result.pop()


N, M = map(int, input().split())
num = sorted(list(set(map(int, input().split()))))
backtracking(num, M, 0, [])
