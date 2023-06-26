# 문자열 폭발
# 23.06.26
# 스택
# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = list(input().rstrip())
bomb_size = len(bomb)
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if bomb_size <= len(stack) and stack[-bomb_size:] == bomb:
        del stack[-bomb_size:]

print(''.join(stack)) if stack else print("FRULA")
