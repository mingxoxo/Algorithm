# 아우으 우아으이야!!
# 스위핑
# 24.01.11
# https://www.acmicpc.net/problem/15922

import sys
input=sys.stdin.readline

N = int(input())
result = 0
last_y = -1000000000

for _ in range(N):
    x, y = map(int, input().split())
    if last_y < x:
        last_y = y
        result += y - x
        continue
    
    if last_y < y:
        result += y - last_y
        last_y = y


print(result)
