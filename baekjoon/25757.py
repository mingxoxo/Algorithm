# 임스와 함께하는 미니게임
# 24.04.21
# https://www.acmicpc.net/problem/25757


import sys
input=sys.stdin.readline

game_headcount = {"Y": 2, "F": 3, "O": 4}

N, type = input().split()
name_set = set()

for _ in range(int(N)):
    name_set.add(input().rstrip())

max_headcount = game_headcount[type]
print(len(name_set) // (max_headcount - 1))
