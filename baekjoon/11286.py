# 절댓값 힙
# 22.10.23
# https://www.acmicpc.net/problem/11286

# heapq custom comparator
# https://lucky516.tistory.com/5

import sys
import heapq

input = sys.stdin.readline

class node:
    def __init__(self, x):
        self.A = abs(x)
        self.B = x
        
    def __lt__(self, other):
        if self.A < other.A:
            return True
        elif self.A == other.A:
            return self.B < other.B
        else:
            return False
    
    def __str__(self):
        return str(self.B)
    
        
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap)) if heap else print("0")
    else:
        heapq.heappush(heap, node(x))
