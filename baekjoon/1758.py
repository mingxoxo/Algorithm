# 알바생 강호
# 그리디, 정렬
# 23.09.10
# https://www.acmicpc.net/problem/1758

import sys
input = sys.stdin.readline

N = int(input())
moneys = sorted([int(input()) for _ in range(N)], reverse=True)
result = 0
for i in range(N):
    result += max(0, moneys[i] - i)

print(result)
