# 회전하는 큐
# 22.07.22
# deque
# https://www.acmicpc.net/problem/1021

import sys
from collections import deque

input = sys.stdin.readline

cnt = 0
N, M = map(int, input().split())
positions = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)])

for p in positions:
    while True:
        if queue[0] == p:
            queue.popleft()
            N -= 1
            break
        idx = queue.index(p)
        queue.rotate(1) if idx > N - idx - 1 else queue.rotate(-1)
        cnt += 1

print(cnt)
