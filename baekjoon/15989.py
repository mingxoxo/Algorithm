# 1, 2, 3 더하기 4
# DP
# https://www.acmicpc.net/problem/15989

def check_cnt(max_n):
    dp = [[1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 2, 1]]
    for _ in range(4, max_n):
        dp.append([dp[-1][0], dp[-2][0] + dp[-2][1], sum(dp[-3])])
    
    return dp
        


T = int(input())
nums = [ int(input()) for _ in range(T)]
dp = check_cnt(max(nums))

for n in nums:
    print(sum(dp[n-1]))
