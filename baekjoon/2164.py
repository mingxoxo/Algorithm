# 카드2
# 큐
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([i for i in range(1, N + 1)])

while True:
    card = queue.popleft()
    if not queue:
        break
    queue.rotate(-1)

print(card)
