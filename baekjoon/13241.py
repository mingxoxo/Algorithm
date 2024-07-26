# 최소공배수
# 24.07.26
# 수학, 유클리드 호제법
# https://www.acmicpc.net/problem/13241

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


A, B = map(int, input().split())
print(A * B // gcd(A, B))
