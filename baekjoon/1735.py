# 분수 합
# 24.07.08
# 유클리드 호제법
# https://www.acmicpc.net/problem/1735

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b:
        a, b = b, a % b
    return a

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

A3 = A1 * B2 + A2 * B1
B3 = B1 * B2

gcd = get_gcd(A3, B3)
print(A3 // gcd, B3 // gcd)
