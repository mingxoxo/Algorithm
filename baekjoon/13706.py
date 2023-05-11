# 제곱근
# 23.05.11
# https://www.acmicpc.net/problem/13706

def square_root(n: int) -> int:
    start, end = 1, n // 2

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            start = mid + 1
        else:
            end = mid - 1
    return 1


N = int(input())
print(square_root(N))
