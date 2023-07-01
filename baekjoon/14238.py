# 출근 기록 ⚠️
# DP + DFS(재귀)
# 23.07.01
# https://www.acmicpc.net/problem/14238

# 공부: https://imnotabear.tistory.com/34
# 코드 참고 : https://hjp845.tistory.com/166

from collections import Counter

S = input()
cnt = Counter(S)

# dp[51][51][51][3][3]
dp = [[[[[False] * 3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
n = len(S)
ans = [0] * 50


def recursive_dp(a, b, c, p1, p2):
    if a == 0 and b == 0 and c == 0:
       return True

    if dp[a][b][c][p1][p2] is True:
        return False
    dp[a][b][c][p1][p2] = True

    if 0 < a:
        ans[n-a-b-c] = 'A'
        if recursive_dp(a-1, b, c, 0, p1):
            return True
    if 0 < b and p1 != 1:
        ans[n - a - b - c] = 'B'
        if recursive_dp(a, b - 1, c, 1, p1):
            return True
    if 0 < c and 2 not in [p1, p2]:
        ans[n - a - b - c] = 'C'
        if recursive_dp(a, b, c - 1, 2, p1):
            return True
    return False


result = recursive_dp(cnt['A'], cnt['B'], cnt['C'], 0, 0)
print(''.join(ans[:n])) if result else print(-1)

