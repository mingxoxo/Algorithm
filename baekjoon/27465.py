# 소수가 아닌 수
# 23.02.11
# 수 / 애드 혹
# https://www.acmicpc.net/problem/27465

N = int(input())
if N < 4:
    print(4)
else:
    print(N) if N % 2 == 0 else print(N + 1)
