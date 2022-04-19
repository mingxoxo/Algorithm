#직각삼각형
#https://www.acmicpc.net/problem/4153

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2) #두 중점 사이의 거리
    if d == 0: # 중점이 동일한 원
        if r1 == r2: print("-1")
        else: print("0")
    else:
        cnt = 2 if abs(r1-r2) < d < r1+r2 else 1 if d == r1+r2 or abs(r1-r2) == d else 0
        print(cnt)

