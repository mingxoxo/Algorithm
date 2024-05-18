# 별 찍기 - 23
# 구현
# 24.05.18
# https://www.acmicpc.net/problem/13015


N = int(input())

blank = 2 * N - 3
string = "*" + " " * (N - 2) + "*"

print("*" * N + " " * blank + "*" * N)
for i in range(1, N - 1):
    blank -= 2
    print(" " * i + string + " " * blank + string)
print(" " * (N - 1) + string + " " * (N - 2) + "*")
for i in reversed(range(1, N - 1)):
    print(" " * i + string + " " * blank + string)
    blank += 2
print("*" * N + " " * blank + "*" * N)
