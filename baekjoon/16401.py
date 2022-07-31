# 과자 나눠주기
# 22.07.31
# 이분탐색 & 매개변수탐색
# https://www.acmicpc.net/problem/16401

import sys

def binary_search(N, M, snack):
    start, end = 1, max(snack)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = sum([snack[i] // mid for i in range(N)])
        if cnt < M:
            end = mid - 1
        else:
            result = max(result, mid)
            start = mid + 1
            
    return result
        

M, N = map(int, input().split())
snack = list(map(int, input().split()))
print(binary_search(N, M, snack))
