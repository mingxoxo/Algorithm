# 다리 놓기
# 23.05.30
# https://www.acmicpc.net/problem/1010

import sys
input = sys.stdin.readline

def dp(N, M):
    num = [1] * M
    for i in range(N - 1):
        prefix = [0]
        for n in num[:-1]:
            prefix.append(prefix[-1] + n)
        num = prefix
    return sum(num)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N, M))
