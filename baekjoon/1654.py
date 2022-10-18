# 랜선 자르기
# 이분 탐색 / 매개변수 탐색
# https://www.acmicpc.net/problem/1654
# start, end = 1, max(line) #최대 길이를 기준으로 잡아야 함!!!

import sys
input = sys.stdin.readline


def binary_search(K, N, line):
    start, end = 1, max(line) #최대 길이를 기준으로 잡아야 함

    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = sum(line[i]//mid for i in range(K))

        if cnt < N:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
print(binary_search(K, N, line))
