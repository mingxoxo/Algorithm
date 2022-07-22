# 큐2
# https://www.acmicpc.net/problem/18258 

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
        
# # 시간 초과
# # https://nan491.tistory.com/entry/Python-3-eval-%ED%95%A8%EC%88%98%EC%99%80-exec-%ED%95%A8%EC%88%98

# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())
# queue = deque()

# cmd_dict = {"push": "queue.append(cmd[1])",
#             "pop": "print(queue.popleft()) if queue else print(-1)",
#             "size": "print(len(queue))",
#             "empty": "print(int(not queue))",
#             "front": "print(queue[0]) if queue else print(-1)",
#             "back": "print(queue[-1]) if queue else print(-1)"
#             }

# for _ in range(N):
#     cmd = list(input().split())
#     exec(cmd_dict[cmd[0]])
