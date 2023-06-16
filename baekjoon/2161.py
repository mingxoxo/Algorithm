# 카드1
# 23.06.16
# https://www.acmicpc.net/problem/2161

from collections import deque

N = int(input())
card = deque([i for i in range(1, N + 1)])
while card:
    print(card.popleft(), end=' ')
    card.rotate(-1)
