# 나이순 정렬
# 22.10.06
# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

N = int(input())
arr = [input().split() for _ in range(N)]
arr.sort(key=lambda k: int(k[0]))
for age, name in arr:
    print(age, name)
