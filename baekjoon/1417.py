# 국회의원 선거
# 우선순위 큐
# 23.12.18
# https://www.acmicpc.net/problem/1417

import heapq

N = int(input())
dasom = int(input())
vote = [-1 * int(input()) for _ in range(N - 1)]
heapq.heapify(vote)
result = 0

if N == 1:
    print(0)
else:
    while dasom <= -1 * vote[0]:
        heapq.heapreplace(vote, vote[0] + 1)
        dasom += 1
        result += 1

    print(result)
