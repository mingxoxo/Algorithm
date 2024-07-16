# 아시아 정보올림피아드
# 정렬
# 24.07.16
# https://www.acmicpc.net/problem/2535


import sys
input=sys.stdin.readline


results = []
COUNTRY_CODE = 0

N = int(input())
results = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[2])

third_index = 2
if results[0][COUNTRY_CODE] == results[1][COUNTRY_CODE]:
    while results[0][COUNTRY_CODE] == results[third_index][COUNTRY_CODE]:
        third_index += 1

for i in (0, 1, third_index):
    print(*results[i][:2])
