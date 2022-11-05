# A → B
# 그리디
# 22.11.06
# https://www.acmicpc.net/problem/16953

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
result = -1

while A <= B:
    if A == B:
        result = cnt + 1
        break
    if B % 2 == 0:
        B = B // 2
    elif B % 10 == 1:
        B = B // 10
    else:
        break
    cnt += 1

print(result)
