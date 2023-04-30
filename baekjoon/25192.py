# 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
user_dict = defaultdict(int)
result = 0

for _ in range(N):
    S = input().rstrip()
    if S == 'ENTER':
        user_dict = defaultdict(int)
        continue
    user_dict[S] += 1
    if user_dict[S] == 1:
        result += 1

print(result)
