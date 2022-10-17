# 문제 1. 합격자 찾기
# 수학 / 구현

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    avg = sum(v) / n
    cnt = 0
    for i in range(n):
        if v[i] >= avg:
            cnt += 1

    print('{0}/{1}'.format(cnt, n))