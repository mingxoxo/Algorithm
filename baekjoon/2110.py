# 공유기 설치
# 22.08.03
# https://www.acmicpc.net/problem/2110
# https://www.acmicpc.net/board/view/8301

import sys
input = sys.stdin.readline


def binary_search(C, cor):
    start, end = 1, cor[-1] - cor[0]
    result = 1
    while start <= end:
        mid = (start + end) // 2
        tmp = cor[0]
        cnt = 1
        for i in range(1, len(cor)):
            if cor[i] - tmp >= mid:
                tmp = cor[i]
                cnt += 1
        if cnt < C:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

N, C = map(int, input().split())
cor = sorted([int(input()) for _ in range(N)])
print(binary_search(C, cor))
