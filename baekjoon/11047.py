#동전 0 (그리디)
#https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coin = [int(input()) for i in range(N)]

answer = 0
for i in reversed(coin):
    answer += K//i
    K = K - (K//i)*i

print(answer)
