# 우당탕탕 영화예매
# 23.09.15
# https://www.acmicpc.net/problem/29700


import sys
input=sys.stdin.readline


N, M, K = map(int, input().split())
result = 0
for _ in range(N):
    row = list(map(int, list(input().rstrip())))
    result += [sum(row[i - K : i]) for i in range(K, M + 1)].count(0)

print(result)
