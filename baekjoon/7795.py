# 먹을 것인가 먹힐 것인가
# 22.08.07
# 투포인터
# https://www.acmicpc.net/problem/7795

import sys

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    j = M
    
    cnt = 0
    for i in reversed(range(N)):
        while j and A[i] <= B[j-1]:
            j -= 1
        cnt += j
    print(cnt)
