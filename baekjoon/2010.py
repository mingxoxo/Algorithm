# 플러그
# https://www.acmicpc.net/problem/2010

import sys
input = sys.stdin.readline

N = int(input())
result = sum([int(input()) for _ in range(N)]) - (N - 1)
print(result)
