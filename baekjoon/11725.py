# 트리의 부모 찾기
# 22.09.16
# https://www.acmicpc.net/problem/11725

import sys
from collections import deque
input = sys.stdin.readline

def BFS(node):
    p_node = [0] * (N + 1)
    queue = deque([1])
    p_node[1] = -1

    while queue:
        n = queue.popleft()
        for i in node[n]:
            if p_node[i] == 0:
                p_node[i] = n
                queue.append(i)

    return p_node[2:]

N = int(input())
node = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    node[n1].append(n2)
    node[n2].append(n1)


print(*(BFS(node)), sep='\n')
