# 문제 4. 소수 찾기
# 에라토스테네스의 체

import sys
input = sys.stdin.readline


def prime_list(n):
	check = [True] * (n + 1)
	for i in range(2, int(n**0.5) + 1):
		if check is False:
			continue
		for j in range(i+i, n+1, i):
			check[j] = False

	return [i for i in range(2, n+1) if check[i] == True ]



n = int(input())
num = list(map(int, input().split()))
result = 0
for i in prime_list(n):
	result += num[i - 1]

print(result)