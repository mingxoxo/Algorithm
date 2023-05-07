# 나선
# 23.05.07
# https://www.acmicpc.net/problem/1491

N, M = map(int, input().split())
pos_x, pos_y = -1, 0
move = 1

while N and M:
    M -= 1
    pos_x += move * N
    pos_y += move * M
    move *= -1
    N -= 1

print(pos_x, pos_y)
