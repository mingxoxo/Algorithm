# 이항 계수 1
# 23.04.24
# https://www.acmicpc.net/problem/11050

def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

N, K = map(int, input().split())
print(int(factorial(N) / factorial(K) / factorial(N - K)))