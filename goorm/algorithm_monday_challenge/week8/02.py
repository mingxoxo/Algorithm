# 문제 2. 뒤통수가 따가워
# 스택

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

queue = deque()
cnt = 0

for i in range(N):
	print(cnt, end=' ')
	while queue:
		if queue[-1] > height[i]:
			break
		cnt -= 1
		queue.pop()
	queue.append(height[i])
	cnt += 1
