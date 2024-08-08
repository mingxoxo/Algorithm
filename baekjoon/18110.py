# solved.ac
# 24.08.08
# https://www.acmicpc.net/problem/18110


import sys
input=sys.stdin.readline

n = int(input())
levels = sorted([int(input()) for _ in range(n)])
remove_cnt = int(n * 0.15 + 0.5)

if 0 < n-remove_cnt*2:
    print(int(sum(levels[remove_cnt:n-remove_cnt])/(n-remove_cnt*2) + 0.5))
else:
    print(0)
