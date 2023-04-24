# 이항 계수 2
# 23.04.24
# https://www.acmicpc.net/problem/11051
# 공부: https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients

def bino_coef(n, k):
    cache = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(k + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cache[i][j] = (cache[i - 1][j] + cache[i - 1][j - 1]) % 10007

    return cache[n][k]


N, K = map(int, input().split())
print(bino_coef(N, K))

