# 문제 3. 비밀 편지
# 나머지 연산 / 문자열

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	S = list(input().strip())
	C, K = input().split()
	k_len = len(K)
	for i in range(len(S)):
		if S[i].isalpha():
			start = ord('A') if S[i].isupper() else ord('a')
			if C == 'E':
				S[i] = chr(((ord(S[i]) - start) + ord(K[i % k_len]) % 26) % 26 + start)
			elif C == 'D':
				S[i] = chr(((ord(S[i]) - start) - ord(K[i % k_len]) % 26) % 26 + start)

	print(''.join(S))