# 1, 2, 3 더하기 3
# DP
# 23.06.30
# https://www.acmicpc.net/problem/15988

def check_cnt(max_n):
    dp = [1, 2, 4, 7]
    for _ in range(4, max_n):
        dp.append(sum(dp[-3:]) % 1000000009)

    return dp


T = int(input())
nums = [int(input()) for _ in range(T)]
dp = check_cnt(max(nums))

for n in nums:
    print(dp[n - 1])
