# 킹
# 22.07.4
# 구현
# https://www.acmicpc.net/problem/1063

import sys
input = sys.stdin.readline

direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
             'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

king, stone, N = map(list, input().split())
king = list(map(ord, king))
stone = list(map(ord, stone))


for _ in range(int(''.join(N))):
    move = input().strip()
    dx, dy = direction[move][0], direction[move][1]
    if ord('A') <= king[0] + dx <= ord('H') and ord('1') <= king[1] + dy <= ord('8'):
        if [king[0] + dx, king[1] + dy] == stone:
            if ord('A') <= stone[0] + dx <= ord('H') and ord('1') <= stone[1] + dy <= ord('8'):
                stone = [stone[0] + dx, stone[1] + dy]
            else:
                continue
        king = [king[0] + dx, king[1] + dy]


king = list(map(chr, king))
stone = list(map(chr, stone))
print(''.join(king))
print(''.join(stone))
