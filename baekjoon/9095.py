# 1, 2, 3 더하기
# 23.03.01
# DP
# https://www.acmicpc.net/problem/9095
# 공부 : https://www.acmicpc.net/board/view/95422

import sys
input = sys.stdin.readline

answer = [0, 1, 2, 4, 7]
for i in range(5, 12):
    answer.append(sum(answer[-3:]))

T = int(input())
for _ in range(T):
    print(answer[int(input())])
