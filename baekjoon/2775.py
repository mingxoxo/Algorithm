#부녀회장이 될테야
#https://www.acmicpc.net/problem/2775

#Pypy3 통과
#파이썬3은 시간초과

#k층 n호
def resident(k, n):
    # 종료 조건: 0층이거나 1호일 때
    if n == 1:
        return 1
    if k == 0:
        return n
    return resident(k-1, n) + resident(k, n-1)


T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(resident(k, n))
