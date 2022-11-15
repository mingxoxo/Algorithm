# 그릇
# 구현 / 문자열
# 22.11.15
# https://www.acmicpc.net/problem/7567

import sys
input = sys.stdin.readline

S = input().strip()
result = 10
for i in range(1, len(S)):
    if S[i - 1] == S[i]:
        result += 5
    else:
        result += 10

print(result)
