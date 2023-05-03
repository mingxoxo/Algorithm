# 십자카드 문제
# 23.05.03
# 브루트포스, 정렬
# https://www.acmicpc.net/problem/2659

# 다른 사람의 풀이 : https://www.acmicpc.net/source/52616072

from collections import deque

def get_clock_num(card):
    case = set()
    queue = deque(card)
    for i in range(4):
        case.add(int(''.join(queue)))
        queue.rotate()

    return min(case)

input_card = get_clock_num(list(input().split()))
cnt = 1

for i in range(1111, input_card):
    if get_clock_num(list(str(i))) == i:
        cnt += 1

print(cnt)