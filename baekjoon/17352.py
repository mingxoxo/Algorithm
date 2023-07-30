# 여러분의 다리가 되어 드리겠습니다!
# union-find
# 23.07.30
# https://www.acmicpc.net/problem/17352


def find_root(parent, n):
    if parent[n] != n:
        parent[n] = find_root(parent, parent[n])
    return parent[n]


def union(parent, a, b):
    root_a, root_b = find_root(parent, a), find_root(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


N = int(input())
island = [i for i in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    union(island, a, b)

for i in range(2, N + 1):
    if island[1] != find_root(island, island[i]):
        print(1, i)
        break
