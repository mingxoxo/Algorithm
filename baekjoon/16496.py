# 큰 수 만들기
# 23.03.19
# 그리디
# https://www.acmicpc.net/problem/16496

import sys
import heapq
input = sys.stdin.readline

N = int(input())
num = list(input().split())

heap = []
for i in num:
    heapq.heappush(heap, (-int((10 * i)[:10]), -len(i), i))

answer = []
while heap:
    answer.append(heapq.heappop(heap)[2])

print(int(''.join(answer)))
