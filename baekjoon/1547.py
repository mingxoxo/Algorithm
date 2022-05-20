#공
#https://www.acmicpc.net/problem/1547

import sys
input = sys.stdin.readline

N = int(input())
cup = [0, 1, 0, 0]

for i in range(N):
    X, Y = map(int, input().split())
    cup[X], cup[Y] = cup[Y], cup[X]

print(cup.index(1))
