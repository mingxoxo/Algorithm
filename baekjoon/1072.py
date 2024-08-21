# 게임
# 수학 (이분탐색도 가능함)
# 23.08.21
# https://www.acmicpc.net/problem/1072


import math

X, Y = map(int, input().split())
now = int(Y * 100 / X)

if 99 <= now:
    print(-1)
else:
    num = ((now + 1) * X - 100 * Y) / (99 - now)
    print(math.ceil(num))
