#문자열 반복
#https://www.acmicpc.net/problem/2675

T = int(input())
for i in range(T):
    R, S = input().split()
    for ch in S:
        print(ch * int(R), end='')
    print()
