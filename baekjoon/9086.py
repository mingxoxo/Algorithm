# 문자열
# https://www.acmicpc.net/problem/9086

T = int(input())

for _ in range(T):
    str = input()
    print(str[0] + str[-1])