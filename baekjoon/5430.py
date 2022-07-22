# AC
# 22.07.20
# deque
# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    queue = deque(list(input().strip().strip('[]').split(',')))
    if n == 0:
        queue.clear()
    reverse_flag = 1
    for c in p:
        if c == 'R':
            reverse_flag *= -1
        elif c == 'D':
            if not queue:
                queue.append('X')
                break
            queue.popleft() if reverse_flag == 1 else queue.pop()
    if 'X' in queue:
        print('error')
    else:
        if reverse_flag == 1:
            result = list(map(int, queue))
        else:
            result = list(map(int, reversed(queue)))
        print('[', end='')
        print(*result, sep=',', end='')
        print(']')
