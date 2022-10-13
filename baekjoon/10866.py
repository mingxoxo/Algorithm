# 덱(deque)
# 22.10.13
# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

N = int(input())
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == "push_front":
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(queue.popleft()) if queue else print(-1)
    elif cmd[0] == "pop_back":
        print(queue.pop()) if queue else print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(0) if queue else print(1)
    elif cmd[0] == "front":
        print(queue[0]) if queue else print(-1)
    elif cmd[0] == "back":
        print(queue[-1]) if queue else print(-1)
