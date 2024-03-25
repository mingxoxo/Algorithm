# 대칭 차집합
# 24.03.25
# https://www.acmicpc.net/problem/1269

import sys
input=sys.stdin.readline

A, B = map(int, input().split())
a_arr = set(map(int, input().split()))
b_arr = set(map(int, input().split()))
print(len(a_arr ^ b_arr))
