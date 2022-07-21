# 특별한 날
# https://www.acmicpc.net/problem/10768

M = int(input())
D = int(input())

day = M * 100 + D
print("Before") if day < 218 else print("Special") if day == 218 else print("After")
