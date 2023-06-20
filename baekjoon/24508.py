# 나도리팡
# 23.06.20
# 투포인터
# https://www.acmicpc.net/problem/24508


N, K, T = map(int, input().split())
baskets = sorted(list(map(int, input().split())))

l, r = 0, N - 1

while l < r:
    if baskets[l] + baskets[r] < K:
        T -= baskets[l]
        baskets[r] += baskets[l]
        baskets[l] = 0
        l += 1
    else:
        T -= K - baskets[r]
        baskets[l] -= K - baskets[r]
        baskets[r] = 0
        r -= 1

print("NO") if T < 0 or baskets[l] != 0 else print("YES") 
