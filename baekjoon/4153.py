#직각삼각형
#https://www.acmicpc.net/problem/4153

while(1):
    h = list(map(int, input().split()))
    if sum(h) == 0:
        break
    h.sort()
    print("right") if h[2]**2 == (h[0]**2 + h[1]**2) else print("wrong")
