# 문제 2. 동명이인
# 문자열 매칭 / 반복문

import sys
input = sys.stdin.readline

n, s = input().split()
cnt = 0

for _ in range(int(n)):
	name = input().strip()
	if s in name:
		cnt += 1

print(cnt)