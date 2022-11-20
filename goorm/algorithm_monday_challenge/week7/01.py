# 문제 1. UXUI 디자이너
# 구현

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
event = [0] * (N + 1)
for _ in range(M):
    user = list(map(int, input().split()))
    for i in range(1, user[0] + 1):
        event[user[i]] += 1

max_cnt = max(event)
result = [i for i in range(N, 0, -1) if event[i] == max_cnt]
print(*result)