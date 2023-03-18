# 집합
# 23.03.18
# 구현 / 비트마스킹
# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline

M = int(input())
cmd = []
S = [0] * 21

for i in range(M):
    cmd = list(input().split())
    if cmd[0] == 'add':
        S[int(cmd[1])] = 1
    elif cmd[0] == 'remove':
        S[int(cmd[1])] = 0
    elif cmd[0] == 'check':
        print(S[int(cmd[1])])
    elif cmd[0] == 'toggle':
        S[int(cmd[1])] = (S[int(cmd[1])] + 1) % 2
    elif cmd[0] == 'all':
        S = [1] * 21
    elif cmd[0] == 'empty':
        S = [0] * 21
