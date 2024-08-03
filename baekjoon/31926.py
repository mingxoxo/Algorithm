# 밤양갱
# 24.08.03
# 그리디
# https://www.acmicpc.net/problem/31926


# d a l d i dal g o -> 8
# daldida n -> 2 (daldida 도 앞에서 붙여서 사용가능)

N = int(input())
time = 9
cnt = 1

while 0 < N:
    N -= cnt
    time += 1
    cnt *= 2
 
print(time)  
