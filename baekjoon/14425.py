# 문자열 집합
# https://www.acmicpc.net/problem/14425
# set은 해시 테이블 구조를 사용

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
str_set = set([input().strip() for _ in range(N)])
cnt = 0

for _ in range(M):
    if input().strip() in str_set:
        cnt += 1
        
print(cnt)
