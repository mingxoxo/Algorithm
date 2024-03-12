# SMUPC 계산기
# 구현
# 24.03.12
# https://www.acmicpc.net/problem/21737

import sys
input=sys.stdin.readline

N = int(input())

num = 0
result = 0
oper = ''
cnt = 0

def update_result(oper, num, result):
    if oper == '':
        result = num
    elif oper == 'S':
        result -= num
    elif oper == 'M':
        result *= num
    elif oper == 'U' and num != 0:
        if result < 0:
            result = -(-result // num)
        else:
            result //= num
    elif oper == 'P':
        result += num
    
    return result


for ch in input().rstrip():
    if ch.isdigit():
        num = num * 10 + int(ch)
        continue
    
    result = update_result(oper, num, result)
    
    if ch == 'C':
        print(result, end=' ')
        cnt += 1
        oper = 'none'
    else:
        oper = ch
    num = 0
    
        
        
if cnt == 0:
    print("NO OUTPUT")
