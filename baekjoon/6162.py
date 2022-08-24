# Superlatives
# 22.08.24
# https://www.acmicpc.net/problem/6162

import sys
input = sys.stdin.readline


K = int(input())
for i in range(K):
    E, A = map(int, input().split())

    print('Data Set {0}:'.format(i))
    if E <= A:
        print("no drought")
    else:
        while E > A * 5:
            print("mega ", end='')
            A = A * 5
        print("drought")
    print()
