# 문제 1. 구름 숫자
# 문자열 매칭 / 구현

import sys
input = sys.stdin.readline


groom_num = {"qw": 1, "as": 2, "zx": 3, "we": 4, "sd": 5,
						"xc": 6, "er": 7, "df": 8, "cv": 9, "ze": 0}

N = int(input())
S = input().rstrip()
result = []

if 2 <= N:
	for i in range(N - 1):
		num = S[i: i+2]
		if num in groom_num.keys():
			result.append(groom_num[num])
	print(*result, sep='')