# Router
# queue
# 22.10.31
# https://www.acmicpc.net/problem/15828

import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
queue = deque()
cnt = 0

while True:
    cmd = int(input())
    if cmd == -1:
        break
    if cmd == 0:
        queue.popleft()
        cnt -= 1
    elif cnt < n:
        queue.append(cmd)
        cnt += 1

print(*queue, sep=' ') if queue else print("empty")
