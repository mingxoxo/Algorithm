# 가로수
# 유클리드 호제법
# 23.11.02
# https://www.acmicpc.net/problem/2845

import sys
input=sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
colonnade = [int(input()) for _ in range(N)]
distance = colonnade[1] - colonnade[0]
for i in range(2, N):
    distance = gcd(distance, colonnade[i] - colonnade[i - 1])

total = (max(colonnade) - min(colonnade)) // distance + 1
print(total - N)
