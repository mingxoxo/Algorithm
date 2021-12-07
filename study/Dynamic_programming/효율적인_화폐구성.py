N, M = map(int, input().split())
coin_list = []

coin_num = [10001] * (M + 1)
coin_num[0] = 0

for i in range(N):
    coin_list.append(int(input()))

for i in range(1, M+1):
    for coin in sorted(coin_list):
        coin_num[i] = min(coin_num[i-coin]+1, coin_num[i])

answer = coin_num[M] if coin_num[M] != 10001 else -1
print(answer)
