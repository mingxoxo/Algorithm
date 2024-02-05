# 사이클 게임
# 24.02.05
# union-find
# https://www.acmicpc.net/problem/20040

import sys
input=sys.stdin.readline

def find_parent(node):    
    if parent[node] == node:
        return node
    
    parent[node] = find_parent(parent[node])
    return parent[node]


def union(a, b):
    a_root = find_parent(a)
    b_root = find_parent(b)
    
    parent[a_root] = parent[b_root] = min(a_root, b_root)


n, m = map(int, input().split())
step = [tuple(map(int, input().split())) for _ in range(m)]
    
parent = [i for i in range(n)]
for i in range(m):
    a, b = step[i]
    if find_parent(a) == find_parent(b):
        print(i + 1)
        break
    union(a, b)
else:
    print(0)
