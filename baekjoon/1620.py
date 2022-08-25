# 나는야 포켓몬 마스터 이다솜
# 22.08.25
# https://www.acmicpc.net/problem/1620


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}

for i in range(N):
    name = input().strip()
    pokemon[str(i + 1)] = name
    pokemon[name] = i + 1
    
for _ in range(M):
    input_str = input().strip()
    print(pokemon[input_str])
