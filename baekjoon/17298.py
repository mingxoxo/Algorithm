# 오큰수
# 22.12.25
# 스택
# https://www.acmicpc.net/problem/17298

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
result = [-1]
n = seq.pop()
stack = [n]

while seq:
    n = seq.pop()
    while stack and n >= stack[-1]:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)
    stack.append(n)


result.reverse()
print(*result)
