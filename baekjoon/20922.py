# 겹치는 건 싫어
# 22.12.25
# 투포인터
# https://www.acmicpc.net/problem/20922

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().split()))
cnt = [0] * 1000001

l, r = 0, 1
cnt[num[0]] += 1
result = 1


while l < r and r < N:
    cnt[num[r]] += 1
    if cnt[num[r]] <= K:
        r += 1
    else:
        result = max(result, r - l)
        while K < cnt[num[r]]:
            cnt[num[l]] -= 1
            l += 1
        r += 1

if l < r:
    result = max(result, r - l)
print(result)
