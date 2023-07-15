# 거짓말
# union-find
# 23.07.15
# https://www.acmicpc.net/problem/1043

from itertools import combinations

def find_parent(idx):
    if parent[idx] != idx:
        parent[idx] = find_parent(parent[idx])
    return parent[idx]


def union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b



N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
_, *truth_nums = map(int, input().split())

party = []
for _ in range(M):
    _, *party_nums = map(int, input().split())
    party.append(party_nums)

if not truth_nums:
    print(M)
else:
    for a, b in combinations(party_nums, 2):
        union(a, b)

    for nums in party:
        for a, b in combinations(nums, 2):
            union(a, b)

    truth_nums = [find_parent(i) for i in truth_nums]
    truth_nums = [i for i in range(1, N + 1) if find_parent(i) in truth_nums]

    cnt = 0
    for nums in party:
        if len(set(nums) & set(truth_nums)) == 0:
            cnt += 1

    print(cnt)
