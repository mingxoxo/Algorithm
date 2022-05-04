#괄호
#스택
#https://www.acmicpc.net/problem/9012

T = int(input())

for _ in range(T):
    s = input()
    cnt = 0
    for c in s:
        cnt = cnt + 1 if c == '(' else cnt - 1
        if cnt < 0:
            break
    print("NO") if cnt != 0 else print("YES")
