# 덱 2
# 24.03.30
# deque
# https://www.acmicpc.net/problem/28279


from collections import deque
import sys
input=sys.stdin.readline


queue = deque([])

N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == '1':
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        queue.append(int(cmd[1]))
    elif cmd[0] == '3':
        print(queue.popleft()) if queue else print(-1)
    elif cmd[0] == '4':
        print(queue.pop()) if queue else print(-1)
    elif cmd[0] == '5':
        print(len(queue))
    elif cmd[0] == '6':
        print(int(len(queue) == 0))
    elif cmd[0] == '7':
        print(queue[0]) if queue else print(-1)
    elif cmd[0] == '8':
        print(queue[-1]) if queue else print(-1)
