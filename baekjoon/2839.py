#설탕 배달
#https://www.acmicpc.net/problem/2839

N = int(input())

a = N//5

while(a >= 0):
    if (N - a * 5) % 3 == 0:
        print((N-a*5)//3 + a)
        break
    a -= 1

if a == -1:
    print(a)
