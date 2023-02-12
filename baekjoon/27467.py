# 수학 퀴즈
# 23.02.11
# 수학
# https://www.acmicpc.net/problem/27467

N = int(input())
A = list(map(int, input().split()))

p = 0
q = 0
for n in A:
    if n % 3 == 0:
        q += 1
    elif n % 3 == 1:
        p += 1
    elif n % 3 == 2:
        p -= 1
        q -= 1
