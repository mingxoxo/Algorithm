# 회사에 있는 사람
# 23.03.21
# https://www.acmicpc.net/problem/7785

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
log = defaultdict(int)

for _ in range(n):
    name, go = input().split()
    if go == "enter":
        log[name] = 1
    elif go == "leave":
        log[name] = 0

print(*sorted([n for n in log.keys() if log[n] == 1], reverse=True), sep='\n')
