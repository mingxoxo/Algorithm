#스택
#https://www.acmicpc.net/problem/10828

import sys
input=sys.stdin.readline

stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        return print(-1)
    print(stack.pop())
    return

def size():
    return print(len(stack))

def empty():
    if not stack:
        return print(1)
    return print(0)

def top():
    if not stack:
        return print(-1)
    return print(stack[-1])


N = int(input())
for i in range(N):
    input_list = input().split()
    if input_list[0] == 'push':
        push(int(input_list[1]))
    else: locals()[input_list[0]]()
      
      
# 공부 참고 사이트
#https://velog.io/@gillog/Python-Stack-Queue-%EA%B8%B0%EB%B3%B8-module-%EC%82%AC%EC%9A%A9-%EC%A0%95%EB%A6%AC
#https://gusdnd852.tistory.com/242
#https://www.delftstack.com/ko/howto/python/python-call-function-from-a-string/

#import sys
#input=sys.stdin.readline

