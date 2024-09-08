# 소가 길을 건너간 이유 3
# 24.09.08
# 그리디, 정렬
# https://www.acmicpc.net/problem/14469


import sys
input=sys.stdin.readline

N = int(input())
infos = sorted([tuple(map(int, input().split())) for _ in range(N)])

time = 0
for arrival_time, inspection_time in infos:
    time = max(time, arrival_time) + inspection_time

print(time)
