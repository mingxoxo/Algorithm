# 문자열 잘라내기
# 24.01.12
# https://www.acmicpc.net/problem/2866
# 다른 사람의 풀이는 이분탐색을 활용함

import sys
input=sys.stdin.readline

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

cols = sorted([''.join(reversed(col)) for col in zip(*arr)])
result = 0

for i in range(C - 1):
    cnt = 0
    for j in range(R):
        if cols[i][j] != cols[i + 1][j]:
           result = max(cnt, result)
           break
        cnt += 1
print(R - 1 - result)
