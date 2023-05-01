# 붙임성 좋은 총총이
# 23.05.01
# https://www.acmicpc.net/problem/26069

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
people = defaultdict(int)
people["ChongChong"] = 1

for _ in range(N):
    nameA, nameB = input().split()
    if people[nameA] == 1 or people[nameB] == 1:
        people[nameB] = people[nameA] = 1
 
print(list(people.values()).count(1))
