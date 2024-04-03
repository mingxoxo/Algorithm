# 스택 2
# 24.04.03
# https://www.acmicpc.net/problem/28278


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        print(int(not stack))
    elif cmd[0] == 5:
        print(stack[-1]) if stack else print(-1)
