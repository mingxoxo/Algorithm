# 트리의 지름
# 트리 / DFS
# 22.10.26
# https://www.acmicpc.net/problem/1967

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def postorder(tree, i):
    global result
    sum_list = []

    if not tree[i]:
        return 0

    for c, w in tree[i]:
        prev = postorder(tree, c)
        sum_list.append(prev + w)

    sum_list.sort()
    result = max(result, sum(sum_list[-2:]))
    return sum_list[-1]



tree = defaultdict(list)

n = int(input())
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))

result = 0
postorder(tree, 1)
print(result)
