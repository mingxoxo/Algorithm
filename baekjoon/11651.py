# 좌표 정렬하기 2
# 22.10.03
# https://www.acmicpc.net/problem/11651
# 2차원 리스트 정렬 - https://haesoo9410.tistory.com/193

import sys
input = sys.stdin.readline

N = int(input())
cor = []

for _ in range(N):
    x, y = map(int, input().split())
    cor.append((x, y))

cor.sort(key=lambda x: (x[-1], x[0]))

for x, y in cor:
    print(x, y)
