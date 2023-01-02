# 가장 긴 증가하는 부분 수열 4
# 23.01.03
# DP
# https://www.acmicpc.net/problem/14002
# 공부: https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
import bisect
input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split()))

dp = [num[0]]
index = [0]
next_idx = [-1] * (N)
last_idx = 0

for i in range(1, N):
    if dp[-1] < num[i]:
        next_idx[i] = index[-1]
        dp.append(num[i])
        index.append(i)
    else:
        idx = bisect.bisect_left(dp, num[i])
        next_idx[i] = index[idx - 1]if idx != 0 else -1
        dp[idx] = num[i]
        index[idx] = i

result = []
idx = index[-1]
while idx != -1:
    result.append(num[idx])
    idx = next_idx[idx]

print(len(dp))
print(*reversed(result))
