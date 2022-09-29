# 분해합
# 22.09.29
# BruteForce
# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline

def brute_force(N):
    for i in range(N):
        if N == i + sum(map(int, str(i))):
            return i
    return 0


N = int(input())
print(brute_force(N))
