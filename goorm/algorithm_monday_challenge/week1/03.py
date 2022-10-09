# 문제 3. 최장 맨해튼 거리
# 탐색 / 효율적인 선택 (그리디한 선택)

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort()

print(num[-1] - num[0] + num[-2] - num[1])