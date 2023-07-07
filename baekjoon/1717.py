# 집합의 표현
# 23.07.07
# Union-Find
# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10**6) # Recursion Error 방지
input = sys.stdin.readline

def find_parent(parent, idx):
    if parent[idx] != idx:
        parent[idx] = find_parent(parent, parent[idx])
    return parent[idx]


def union(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b



n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        print("YES") if find_parent(parent, a) == find_parent(parent, b) else print("NO")
    elif cmd == 0:
        union(parent, a, b)
