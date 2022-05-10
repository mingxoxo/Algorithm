#스택 수열
#https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

N = int(input())
sequence = []
for i in range(N):
    sequence.append(int(input()))

stack = []
calculation = []

tmp = 1

for i in sequence:
    while tmp <= i:
        stack.append(tmp)
        calculation.append('+')
        tmp += 1
    if stack and stack[-1] == i:
        stack.pop()
        calculation.append('-')

if stack:
    print("NO")
else:
    for c in calculation:
        print(c)

