# 십자카드 문제
# 23.05.03
# 브루트포스, 정렬
# https://www.acmicpc.net/problem/2659

from itertools import product
from collections import deque

def make_num_case(card):
    case = set()
    queue = deque(card)
    for i in range(4):
        case.add(int(''.join(queue)))
        queue.rotate()
    return case

input_card = list(input().split())
total_case = make_num_case(input_card)
clock_num = min(total_case)

total_card = product([i for i in range(1, 10)], repeat = 4)

cnt = 1
for card in total_card:
    card = list(map(str, card))
    card_num = int(''.join(card))
    if clock_num == card_num:
        break
    if card_num in total_case:
        continue
    total_case |= make_num_case(card)
    cnt += 1

print(cnt)