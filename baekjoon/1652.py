# 누울 자리를 찾아라
# 23.12.20
# https://www.acmicpc.net/problem/1652

import sys
input=sys.stdin.readline

N = int(input())
room = list(input().rstrip() for _ in range(N))
rows = [row.split('X') for row in room]
cols = [''.join(col).split('X') for col in zip(*room)]

row_cnt = 0
col_cnt = 0
for i in range(N):
    row_cnt += len([row for row in rows[i] if 2 <= len(row)])
    col_cnt += len([col for col in cols[i] if 2 <= len(col)])
print(row_cnt, col_cnt)
