# 통계학
# 22.10.08
# https://www.acmicpc.net/problem/2108


import sys
input = sys.stdin.readline

N = int(input())
num = sorted([int(input()) for _ in range(N)])

cnt = {i: 0 for i in set(num)}
for i in range(N):
    cnt[num[i]] += 1
cnt = list(cnt.items())
cnt.sort(key=lambda x:(-x[1], x[0]))

print(round(sum(num)/N))
print(num[N//2])
print(cnt[0][0]) if N == 1 or cnt[1][1] != cnt[0][1] else print(cnt[1][0])
print(num[-1] - num[0])
