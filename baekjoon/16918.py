# 봄버맨
# 23.05.13
# https://www.acmicpc.net/problem/16918
# 그냥 배열로 직접 접근해서 값 바꾸는 것이 더 빠름..!

import sys
input = sys.stdin.readline

bomb = set()

R, C, N = map(int, input().split())
for i in range(R):
    row = list(input().rstrip())
    bomb.update((i, j) for j in range(C) if row[j] == 'O')
if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    for _ in range(N // 2):
        empty = set()
        for x, y in bomb:
            empty.update(((x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)))
        bomb = set((i, j) for j in range(C) for i in range(R)) - empty
    for i in range(R):
        for j in range(C):
            print('O', end='') if (i, j) in bomb else print('.', end='')
        print()
