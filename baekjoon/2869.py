#달팽이는 올라가고 싶다
#https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())

cnt = (V-A) / (A-B)
if not cnt == int(cnt):
    cnt = round(cnt+0.5)

print(int(cnt+1))
