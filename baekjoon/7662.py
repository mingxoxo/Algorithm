# 이중 우선순위 큐
# 우선순위 큐
# 23.07.16
# https://www.acmicpc.net/problem/7662

import heapq
from collections import defaultdict

def heap_pop(heap, cnt, flag):
    while heap:
        num = heapq.heappop(heap) * flag
        if cnt[num] > 0:
            cnt[num] -= 1
            return


def run_case():
    k = int(input())
    cnt = defaultdict(int)
    min_heap = []
    max_heap = []
    for _ in range(k):
        cmd, n = input().split()
        if cmd == 'I':
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -1 * int(n))
            cnt[int(n)] += 1
        elif cmd == 'D' and (min_heap or max_heap):
            if int(n) == -1:
                heap_pop(min_heap, cnt, 1)
            elif int(n) == 1:
               heap_pop(max_heap, cnt, -1)

    result = []
    if max_heap:
        while max_heap:
            num = heapq.heappop(max_heap) * -1
            if cnt[num] > 0:
                result.append(num)
                break
        
    if min_heap:
        while min_heap:
            num = heapq.heappop(min_heap)
            if cnt[num] > 0:
                result.append(num)
                break

    return result



T = int(input())
for _ in range(T):
    result = run_case()
    if result:
        print(result[0], result[-1])
    else:
        print("EMPTY")
