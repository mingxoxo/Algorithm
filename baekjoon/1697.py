#숨바꼭질
#22.06.20
#BFS
#https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

def move(x):
    return [x - 1, x + 1, 2 * x]

def BFS(map, N, K):
    queue = deque([N])
    while queue:
        x = queue.popleft()
        for nx in move(x):
            if 0 <= nx <= 100000 and map[nx] == 0:
                queue.append(nx)
                map[nx] = map[x] + 1
                if nx == K:
                    return map[K]
    return map[K]



N, K = map(int, input().split())
map = [0] * 100001
if N == K:
    print(0)
else:
    print(BFS(map, N, K))

