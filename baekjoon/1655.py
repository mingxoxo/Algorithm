# 가운데를 말해요
# heapq - 우선순위 큐
# 22.10.24
# https://www.acmicpc.net/problem/1655
# 아이디어 - https://www.acmicpc.net/board/view/2983


import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
heap_front = []
heap_back = []
cnt_f = 0
cnt_b = 0

for i in range(N):
    num = int(input())
    if i == 0:
        heappush(heap_front, -1 * num)
        cnt_f = 1
        print(heap_front[0] * -1)
        continue
    if -1 * heap_front[0] <= num:
        heappush(heap_back, num)
        cnt_b += 1
    else:
        heappush(heap_front, -1 * num)
        cnt_f += 1

    if cnt_f < cnt_b:
        heappush(heap_front, -1 * heappop(heap_back))
        cnt_f += 1
        cnt_b -= 1
    elif cnt_f > cnt_b + 1:
        heappush(heap_back, -1 * heappop(heap_front))
        cnt_f -= 1
        cnt_b += 1
    print(heap_front[0] * -1)
