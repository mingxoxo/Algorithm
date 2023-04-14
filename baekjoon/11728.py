# 배열 합치기
# 23.04.14
# https://www.acmicpc.net/problem/11728

from collections import deque

N, M = map(int, input().split())
A = deque(list(map(int, input().split())))
B = deque(list(map(int, input().split())))
result = []

while A and B:
    if A[0] > B[0]:
        result.append(B.popleft())
    else:
        result.append(A.popleft())

while A:
    result.append(A.popleft())

while B:
    result.append(B.popleft())

print(*result)
