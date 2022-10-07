# 방 번호
# 22.10.07
# https://www.acmicpc.net/problem/1475

import math

N = input()

cnt = [0] * 9
for i in N:
    if i == '9':
        cnt[6] += 1
        continue
    cnt[int(i)] += 1

cnt[6] = math.ceil(cnt[6] / 2)

print(max(cnt))
