#주유소
#그리디
#https://www.acmicpc.net/problem/13305


N = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

price = 0
oil = oil_price[0]
for i in range(N-1):
    if oil > oil_price[i]:
        oil = oil_price[i]
    price += oil * road_length[i]

print(price)
