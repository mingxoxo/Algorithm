# Dance Dance Revolution
# 23.03.20
# DP
# https://www.acmicpc.net/problem/2342
# 공부 : https://chinpa.tistory.com/84 / https://dkrnfls.tistory.com/174

def power(i, j):
    if i == j:
        return 1
    elif i == 0 or j == 0:
        return 2
    elif abs(i - j) == 2:
        return 4
    return 3

INF = 1e8
num = list(map(int, input().split()))
dp = [[[INF] * 5 for i in range(5)] for _ in range(len(num))]
dp[0][0][0] = 0

for i in range(1, len(num)):
    move = num[i - 1]
    for l in range(5):
        for r in range(5):
            dp[i][move][r] = min(dp[i][move][r], dp[i-1][l][r] + power(l, move))
            dp[i][l][move] = min(dp[i][l][move], dp[i-1][l][r] + power(r, move))

answer = INF
for i in range(5):
    answer = min(answer, min(dp[-1][i]))

print(answer)
