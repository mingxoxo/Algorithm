# 스티커
# DP
# 22.11.06
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    cnt = [0, 0, 0]
    for i in range(n):
        no = max(cnt[1], cnt[2])
        up = max(cnt[0], cnt[2]) + sticker[0][i]
        down = max(cnt[0], cnt[1]) + sticker[1][i]
        cnt = [no, up, down]
    print(max(cnt))
