# 트리
# Tree / BFS
# 22.09.22
# https://www.acmicpc.net/problem/4803

# 코드 아래 반례 참고



import sys
from collections import deque
input = sys.stdin.readline


def BFS(node, N):
    p_node = [0] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if p_node[i] != 0:
            continue
        p_node[i] = -1
        queue = deque([i])
        while queue:
            n = queue.popleft()
            for j in node[n]:
                if p_node[j] == 0:
                    p_node[j] = n
                    queue.append(j)
                elif n == j or (p_node[n] != -1 and p_node[n] != j):
                    p_node[i] = -2

        if p_node[i] == -1:
            cnt += 1

    if cnt == 0:
        return "No trees."
    if cnt == 1:
        return "There is one tree."
    return "A forest of " + str(cnt) + " trees."


case = 0

while True:
    case += 1
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    node = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        node[n1].append(n2)
        node[n2].append(n1)

    print("Case {0}: {1}".format(str(case), BFS(node, n)))
    
'''
# https://www.acmicpc.net/board/view/19906
-------------
3 3
1 1
2 3
1 2
0 0
'''
