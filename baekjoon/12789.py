# 도키도키 간식드리미
# 스택
# 24.03.31
# https://www.acmicpc.net/problem/12789


import sys
input=sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))[::-1]

stack = []
for i in range(1, N + 1):
    if stack and stack[-1] == i:
        stack.pop()
        continue
    
    while arr and arr[-1] != i:
        stack.append(arr.pop())
    
    if not arr:
        print("Sad")
        break
    arr.pop()
else:
    print("Nice")
