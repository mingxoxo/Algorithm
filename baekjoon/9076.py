#점수 집계
#https://www.acmicpc.net/problem/9076

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    score = sorted(list(map(int, input().split())))
    if score[3] - score[1] >= 4:
        print("KIN")
    else:
        print(sum(score[1:4]))
