# 옥상 정원 꾸미기
# 스택
# 24.04.09
# https://www.acmicpc.net/problem/6198

import sys
input=sys.stdin.readline

N = int(input())
stack = []

result = 0

for i in range(N):
    h = int(input())
    
    while stack and stack[-1][0] <= h:
        _, idx = stack.pop()
        result += i - idx - 1

    stack.append((h, i))
    
if stack:
    _, last_idx = stack.pop()
    while stack:
        _, idx = stack.pop()
        result += last_idx - idx

print(result)
