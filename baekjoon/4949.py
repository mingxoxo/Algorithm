#균형잡힌 세상
#스택
#https://www.acmicpc.net/problem/4949

pair = {')':'(', ']':'['}
while True:
    s = input()
    if s == '.': break
    stack = []
    for c in s:
        if c in ['[', '(']:
            stack.append(c)
        elif c in pair.keys():
            if not stack or stack.pop() != pair[c]:
                stack.append(c)
                break
    print("no") if stack else print("yes")
