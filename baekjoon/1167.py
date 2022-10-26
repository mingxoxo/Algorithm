# 트리의 지름
# 트리 / DFS
# 22.10.26
# 1967.py에서 확장해서 생각
# https://www.acmicpc.net/problem/1167

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def DFS(tree, i, visited):
    global result
    sum_list = []

    if visited[i] == 1:
        return 0
    visited[i] = 1

    for c, w in tree[i]:
        if visited[c] == 1:
            continue
        prev = DFS(tree, c, visited)
        sum_list.append(prev + w)

    sum_list.sort()
    result = max(result, sum(sum_list[-2:]))
    if not sum_list:
        return 0
    return sum_list[-1]



tree = defaultdict(list)

n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split()))
    i = tmp[0]
    for j in range(1, len(tmp) - 1, 2):
        tree[i].append(tmp[j:j+2])

result = 0
visited = [0] * (n + 1)
DFS(tree, 1, visited)
print(result)
