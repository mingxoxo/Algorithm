# 2239 스도쿠
# Solved on 2023. 02. 19.
# 백트래킹
# https://www.acmicpc.net/problem/2239

board = []
group1 = [[0] * 10 for _ in range(9)] #row
group2 = [[0] * 10 for _ in range(9)] #col
group3 = [[0] * 10 for _ in range(9)] #rect

def rect_num(i, j):
    return i // 3 * 3 + j // 3

def group_init(i, j, n, value):
    group1[i][n] = value
    group2[j][n] = value
    group3[rect_num(i, j)][n] = value

def possible_num(x, y):
    num = set([i for i in range(1, 10) if group1[x][i] == 0])
    num = num & set([i for i in range(1, 10) if group2[y][i] == 0])
    num = num & set([i for i in range(1, 10) if group3[rect_num(x, y)][i] == 0])
    return num

def backtracking(i, j):
    while i < 9:
        while j < 9:
            if board[i][j] == 0:
                num = possible_num(i, j)
                for n in sorted(num):
                    board[i][j] = n
                    group_init(i, j, n, 1)
                    if backtracking(i, j + 1) == 1:
                        return 1
                    board[i][j] = 0
                    group_init(i, j, n, 0)
                return 0
            j += 1
        i += 1
        j = 0
    return 1

for i in range(9):
    board.append(list(map(int, input())))
    for j in range(9):
        if board[i][j] == 0:
            continue
        n = board[i][j]
        group_init(i, j, n, 1)

backtracking(0, 0)
for i in range(9):
    print(*board[i], sep='')
