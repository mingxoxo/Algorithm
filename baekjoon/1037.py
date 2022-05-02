#약수
#https://www.acmicpc.net/problem/1037

N = int(input())
divisor = list(map(int, input().split()))
print(min(divisor)*max(divisor))
