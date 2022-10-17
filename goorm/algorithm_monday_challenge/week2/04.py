# 문제 4. 폭탄 구현하기
# 2차원 배열

import sys
input = sys.stdin.readline


def count_bomb(bomb, n):
	cnt = 0
	dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
	for x, y in bomb:
		if 0 < x <= n and 0 < y <= n:
			cnt += 1
			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 < nx <= n and 0 < ny <= n:
					cnt += 1

	return cnt


n, k = map(int, input().split())
bomb = []

for _ in range(k):
	a, b = map(int, input().split())
	bomb.append((a, b))

print(count_bomb(bomb, n))
