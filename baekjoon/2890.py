# 카약
# 24.05.07
# https://www.acmicpc.net/problem/2890


import sys
input=sys.stdin.readline

R, C = map(int, input().split())
info = []

for i in range(R):
    line = input().rstrip()
    for i in reversed(range(C)):
        if '1' <= line[i] <= '9':
            info.append((i, int(line[i])))
            break
    
rank = 1
rank_info = [-1 for _ in range(10)]
info.sort(reverse=True)

for i in range(len(info)):
    if i != 0 and info[i - 1][0] != info[i][0]:
        rank += 1
    rank_info[info[i][1]] = rank
    
print(*rank_info[1:], sep='\n')
