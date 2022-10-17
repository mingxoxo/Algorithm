# 문제 3. 출석부
# 정렬 / 문자열

import sys
input = sys.stdin.readline

N, k = map(int, input().split())
info = []

for _ in range(N):
	S, t = input().split()
	info.append([S, t, int(float(t) * 100)])

info.sort(key=lambda x: (x[0], x[2]))
print('{0} {1}'.format(info[k-1][0], info[k-1][1]))


# 문제 해설
# 임의로 정렬 비교 함수를 만들어줄 수 있음
# from functools import cmp_to_key
# def cmp(a, b):
#     if a[0] == b[0]:
#         return a[1] < b[1]
#     else:
#         return a[0] < b[0]
# arr = [] # [[string1, int1], [string2, int2], ...]
# print(sorted(arr,key=cmp_to_key(cmp)))
