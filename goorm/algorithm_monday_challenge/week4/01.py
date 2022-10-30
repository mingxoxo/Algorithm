# 문제 1. 체크 카드
# 시뮬레이션 / 큐

import sys
from collections import deque

input = sys.stdin.readline

wait = deque()

N, M = map(int, input().split())
for _ in range(M):
    cmd, k = input().split()
    k = int(k)
    if cmd == "deposit":
        N += k
    elif cmd == 'pay':
        if N >= k:
            N -= k
    else:
        wait.append(k)

    while wait and N >= wait[0]:
        N -= wait.popleft()

print(N)