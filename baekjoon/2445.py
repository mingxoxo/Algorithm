# 별 찍기 - 8
# 23.02.12
# 구현
# https://www.acmicpc.net/problem/2445

import sys
input = sys.stdin.readline

N = int(input())
i = 1
flag = 1
while i != 0:
    print('*' * i + ' ' * (N - i) * 2 + '*' * i)
    if i == N:
        flag = -1
    i += flag
