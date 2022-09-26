# 요세푸스 문제 0
# 22.09.26
# queue
# https://www.acmicpc.net/problem/11866

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
answer = []

while queue:
    queue.rotate(-(K-1))
    answer.append(queue.popleft())

print("<", end='')
print(*answer, sep=", ", end='')
print(">")
