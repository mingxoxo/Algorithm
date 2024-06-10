# 후위 표기식2
# 24.06.10
# 스택
# https://www.acmicpc.net/problem/1935


def calculate(a, b, op):
    result = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
    return result[op]

N = int(input())
postfix = input()
nums = [int(input()) for _ in range(N)]

stack = []
for ch in postfix:
    if ch in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, b, ch))
    else:
        stack.append(nums[ord(ch) - ord('A')])

print(f"{stack[-1]:.2f}")
