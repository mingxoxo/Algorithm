#올바른 괄호
#https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    
    for c in s:
        if c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
        stack.append(c)
    
    return True if not stack else False
