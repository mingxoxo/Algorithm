# RGB거리 2
# 22.12.30
# DP
# https://www.acmicpc.net/problem/17404
# 설명 참고 : https://vitriol95.github.io/posts/boj17404/
# ! 다시 풀어보기 !

import sys
input = sys.stdin.readline

INF = 1e9
result = 1e9

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

# R: 0, G: 1, B: 2
for color in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]

    #첫번째 집 색을 미리 지정
    dp[0][color] = cost[0][color]

    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    #첫번째 집과 색이 다른 마지막 집의 cost만 비교
    for i in range(3):
        if i == color:
            continue
        result = min(result, dp[-1][i])

print(result)
