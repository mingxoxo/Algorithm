# 카드 정렬하기
# heapq - 우선순위 큐
# 22.10.24
# https://www.acmicpc.net/problem/1715

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
heap = []
result = 0

for i in range(N):
    num = int(input())
    heappush(heap, num)

while heap:
    num1 = heappop(heap)
    if not heap:
        break
    num2 = heappop(heap)
    heappush(heap, num1 + num2)
    result += num1 + num2

print(result)
