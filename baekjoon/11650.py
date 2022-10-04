# 좌표 정렬하기
# 22.10.04
# https://www.acmicpc.net/problem/11650
# https://haesoo9410.tistory.com/193

import sys
input = sys.stdin.readline

N = int(input())
cor = []

for _ in range(N):
    x, y = map(int, input().split())
    cor.append((x, y))

cor.sort(key=lambda x: (x[0], x[1]))

for x, y in cor:
    print(x, y)
