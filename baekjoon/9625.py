# BABBA
# DP
# 23.06.28
# https://www.acmicpc.net/problem/9625

A, B = 1, 0

for _ in range(int(input())):
    A, B = B, A + B

print(A, B)
