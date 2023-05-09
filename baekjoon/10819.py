# 차이를 최대로
# 브루트포스
# https://www.acmicpc.net/problem/10819

from itertools import permutations

def func(arr):
    global N
    result = 0
    for i in range(N - 1):
        result += abs(arr[i] - arr[i + 1])
    return result


N = int(input())
A = list(map(int, input().split()))
print(max(map(func, permutations(A, N))))
