# 개미
# 24.02.18
# https://www.acmicpc.net/problem/4307

import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    length, n = map(int, input().split())
    pos = [int(input()) for _ in range(n)]
    
    min_ans = 0
    max_ans = 0
    for i in pos:
        min_ans = max(min_ans, min(i, length - i))
        max_ans = max(max_ans, max(i, length - i))
    print(min_ans, max_ans)
    
