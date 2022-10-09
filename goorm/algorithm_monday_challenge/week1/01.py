# 문제 1. 경로의 개수
# 수학 / 구현 / 큰 수 개념(BigInteger)

import sys
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))
result = 1

for cnt in bridge:
    result *= cnt

print(result)