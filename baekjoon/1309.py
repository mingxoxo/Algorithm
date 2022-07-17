# 동물원
# 22.07.18
# DP
# https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

N = int(input())

cnt = [1, 0]
for i in range(2, N + 1):
    cnt = [cnt[0] + cnt[1], 2 * cnt[0] + cnt[1]]

print((cnt[0]*3 + cnt[1]*2)%9901)
