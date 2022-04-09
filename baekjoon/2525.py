#오븐 시계
#https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())

print(((B+C)//60 + A)%24, (B+C)%60)
