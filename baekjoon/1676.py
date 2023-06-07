# 팩토리얼 0의 개수
# 23.06.07
# https://www.acmicpc.net/problem/1676

import math

N = int(input())
num = math.factorial(N)
cnt = 0
while num % 10 == 0:
    cnt += 1
    num //= 10

print(cnt)
