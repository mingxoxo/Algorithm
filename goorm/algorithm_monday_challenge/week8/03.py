# 문제 3. 직사각형 만들기
# 그리디

import sys
import heapq
input = sys.stdin.readline

num = []
count = [0] * (1000001)
result = 0

N = int(input())
bar = list(map(int, input().split()))

for i in bar:
	count[i] += 1
	if count[i] == 2:
		count[i] = 0
		heapq.heappush(num, -i)

while num:
	bar1 = -heapq.heappop(num)
	if not num:
		break
	bar2 = -heapq.heappop(num)
	result += bar1 * bar2

print(result)