# 집 주소 
# 22.07.08
# https://www.acmicpc.net/problem/1284

import sys
input = sys.stdin.readline

num_list = [4, 2] + [3] * 8

while True:
    num = list(map(int, input().strip()))
    if num == [0]:
        break
    print(sum([num_list[i] for i in num]) + len(num) + 1)
