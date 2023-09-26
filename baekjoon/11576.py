# Base Conversion
# 수학, 구현
# 23.09.26
# https://www.acmicpc.net/problem/11576

A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

base10 = sum([nums[i] * (A ** (m - i - 1))for i in range(m)])
base_b = []

while base10:
    base_b.append(base10 % B)
    base10 //= B

print(*reversed(base_b))
