# 황금 칵테일
# 23.06.22
# https://www.acmicpc.net/problem/26596

from collections import defaultdict
from itertools import combinations

info = defaultdict(int)
M = int(input())
for _ in range(M):
    s, x = input().split()
    info[s] += int(x)

for i, j in combinations(info.values(), 2):
    if i == int(j * 1.618) or j == int(i * 1.618):
        print("Delicious!")
        break
else:
    print("Not Delicious...")
