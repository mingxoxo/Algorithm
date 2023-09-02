# 신입 사원
# 그리디 / 정렬
# 23.09.02
# https://www.acmicpc.net/problem/1946

import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = []
    for _ in range(N):
        scores.append(list(map(int, input().split())))

    cnt = 0
    scores.sort(key=lambda x: x[0])
    rank = N
    for _, s2 in scores:
        if s2 <= rank:
            cnt += 1
        rank = min(rank, s2)
        
    print(cnt)
