# 보물
# 23.01.31
# 그리디
# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
result = 0
for a, b in zip(A, B):
    result += a * b
print(result)
