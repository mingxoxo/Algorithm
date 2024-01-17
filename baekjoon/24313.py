# 알고리즘 수업 - 점근적 표기 1
# 24.01.17
# 수학
# https://www.acmicpc.net/problem/24313

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(int(a0 <= (c - a1) * n0)) if 0 <= c - a1 else print(0)
