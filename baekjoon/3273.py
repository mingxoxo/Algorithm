# 두 수의 합
# 22.09.09
# 투포인터
# https://www.acmicpc.net/problem/3273

import sys
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, n - 1
cnt = 0

while start < end :
    if num[start] + num[end] <= x:
        if num[start] + num[end] == x:
            cnt += 1
        start += 1
    else:
        end -= 1

print(cnt)
