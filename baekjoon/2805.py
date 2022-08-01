# 나무 자르기
# 22.08.01
# 이분탐색 & 매개변수탐색
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def binary_search(N, M, tree):
    start, end = 0, max(tree)
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        max_h = sum([tree[i] - mid if tree[i] >= mid else 0 for i in range(N) ])
        if max_h < M:
            end = mid - 1
        else:
            result = max(result, mid)
            start = mid + 1
    return result

N, M = map(int, input().split())
tree = list(map(int, input().split()))
print(binary_search(N, M, tree))
