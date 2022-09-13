# Football Scoring
# 22.09.11
# https://www.acmicpc.net/problem/24736

import sys
input = sys.stdin.readline

visiting_score = list(map(int, input().split()))
home_score = list(map(int, input().split()))
score = [6, 3, 2, 1, 2]

print(sum([visiting_score[i] * score[i] for i in range(5)]), end = ' ')
print(sum([home_score[i] * score[i] for i in range(5)]))
