# 마인크래프트
# 23.05.19
# https://www.acmicpc.net/problem/18111
# Pypy3로 해결

def check_cost(h, arr, cnt, B):
    cost = 0
    inventory = B
    for i in range(cnt):
        d = arr[i] - h
        cost = cost + 2 * d if d > 0 else cost - d
        inventory += d
    if inventory < 0:
        return -1
    return cost

def brute_force(height, cnt, B):
    start, end = min(height), max(height)
    result = [check_cost(start, height, cnt, B), start]
    for i in range(start + 1, end + 1):
        cost = check_cost(i, height, cnt, B)
        if cost == -1 or result[0] < cost:
            continue
        result[0] = cost
        result[1] = i
    return result


N, M, B = map(int, input().split())
height = []
for _ in range(N):
    height.extend(list(map(int, input().split())))
print(*brute_force(height, N * M, B))
