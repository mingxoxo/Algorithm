# 문제 2. 철자 분리 집합
# 문자열 처리(슬라이싱) / 조건문

# 문제에서 flag가 불필요하기 때문에 없어도 상관 없음

import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

i = 0
cnt = 1
#flag = 0

for i in range(1, len(S)):
	if S[i - 1] != S[i]:
		cnt += 1
	# if S[i - 1] != S[i]:
	# 	flag = 1
	# if flag == 1:
	# 	cnt += 1
	# 	flag = 0

print(cnt)
