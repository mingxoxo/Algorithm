#제로
#스택
#https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    i = int(input())
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))
