#구간 합 구하기 4
#https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [0, 0] + list(map(int, input().split()))

for i in range(3, 2+N):
    num[i] = num[i-1] + num[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(num[j+1]-num[i])


