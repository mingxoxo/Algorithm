# 연속합
# 23.04.28
# DP
# https://www.acmicpc.net/problem/1912

N = int(input())
num = list(map(int, input().split()))

answer = num[0]
dp = num[0]
for i in range(1, len(num)):
    dp = max(dp + num[i], num[i])
    answer = max(dp, answer)

print(answer)
