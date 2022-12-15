# 후위 표기식
# 22.12.15
# 스택
# https://www.acmicpc.net/problem/1918

import sys
input = sys.stdin.readline

rank = {'+': 3, '-': 3, '*': 2, '/': 2, '(': 1, ')': 1}

stack = []
S = input().rstrip()
flag = 0

for c in S:
    if c.isupper():
        print(c, end='')
        continue
    if c == '(':
        stack.append(c)
        continue
    if c == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
        continue
    while stack and rank[stack[-1]] <= rank[c]:
        if stack[-1] == '(':
            break
        print(stack.pop(), end='')
    stack.append(c)

while stack:
    print(stack.pop(), end='')
