# 키로거
# 23.03.16
# 자료구조
# https://www.acmicpc.net/problem/5397

from collections import deque
import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    L = input().rstrip()
    cursor = 0
    password = deque()
    for i in L:
        if i == '<':
            if 0 < cursor:
                password.rotate(1)
                cursor -= 1
        elif i == '>':
            if cursor < len(password):
                password.rotate(-1)
                cursor += 1
        elif i == '-':
            if cursor:
                password.pop()
                cursor -= 1
        else:
            password.append(i)
            cursor += 1
    
    password.rotate(cursor)
    print(*password, sep='')
