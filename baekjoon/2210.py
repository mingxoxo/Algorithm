# 숫자판 점프
# 23.02.09
# BFS
# https://www.acmicpc.net/problem/2210

from collections import deque

def BFS(board, start, num):
    queue = deque([start])
    cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, s = queue.popleft()
        if len(s) == 6:
            num.add(s)
            continue
        for dx, dy in cor:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                queue.append((nx, ny, s + board[nx][ny]))


board = []
num = set()
for _ in range(5):
    board.append(list(input().split()))
    
for i in range(5):
    for j in range(5):
        BFS(board, [i, j, board[i][j]], num)

print(len(num))
