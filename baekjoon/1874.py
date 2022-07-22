#스택 수열
#https://www.acmicpc.net/problem/1874

# 22.07.21
import sys

input = sys.stdin.readline
stack = []
op = []
flag = 1
i = 1

n = int(input())
for _ in range(n):
    k = int(input())
    while i <= k:
        stack.append(i)
        op.append('+')
        i += 1
    element = stack.pop()
    if element != k:
        flag = 0
        continue
    op.append('-')

print(*op, sep='\n') if flag else print("NO")

