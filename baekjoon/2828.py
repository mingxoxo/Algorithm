# 사과 담기 게임
# 그리디
# 24.07.14
# https://www.acmicpc.net/problem/2828


N, M = map(int, input().split())
J = int(input())

l, r = 1, M
dist = 0
for _ in range(J):
    pos = int(input())
    if l <= pos <= r:
        continue
    
    if pos < l:
        diff = l - pos
        l = pos
        r -= diff
    else:
        diff = pos - r
        r = pos
        l += diff
    
    dist += diff

print(dist)
