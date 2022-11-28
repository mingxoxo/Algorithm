# 큐
# 22.11.28
# queue
# https://www.acmicpc.net/problem/10845


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(int(not queue))
    elif cmd[0] == "front":
        print(queue[0]) if queue else print(-1)
    elif cmd[0] == "back":
        print(queue[-1]) if queue else print(-1)

