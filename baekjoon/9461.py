# 파도반 수열
# 수학, DP
# 23.10.14
# https://www.acmicpc.net/problem/9461


def get_dp():
    dp = [0, 1, 1, 1]
    for i in range(4, 101):
        dp.append(dp[i - 3] + dp[i - 2])

    return dp


dp = get_dp()
T = int(input())
for _ in range(T):
    print(dp[int(input())])
