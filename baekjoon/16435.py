#스네이크버드
#https://www.acmicpc.net/problem/16435

import sys
input = sys.stdin.readline
N, L = map(int, input().split())

fruit = sorted(list(map(int, input().split())))

for f in fruit:
    if f > L:
        break
    L += 1

print(L)
