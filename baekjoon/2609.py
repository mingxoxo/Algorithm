# 최대공약수와 최소공배수
# 23.05.21
# 유클리드 호제법 : https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95
# https://www.acmicpc.net/problem/2609

def euclidean(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
gcd = euclidean(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)
