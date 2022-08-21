# N과 M (3)
# 22.08.22
# study _ BackTracking ver
# https://www.acmicpc.net/problem/15651

import sys
input = sys.stdin.readline

def recursion(num, N, M, result):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        result.append(i)
        recursion(num + 1, N, M, result)

        #마지막 값 실행 후 재귀가 끝나 복귀하면 이전 값을 제거하여 개수 유지
        result.pop()

N, M = map(int, input().split())
result = []
recursion(0, N, M, result)
