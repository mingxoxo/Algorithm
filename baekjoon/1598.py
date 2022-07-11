# 꼬리를 무는 숫자 나열
# 22.07.12
# https://www.acmicpc.net/problem/1598

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(abs((a - 1) // 4 - (b - 1) // 4) + abs((a - 1) % 4 - (b - 1) % 4))
