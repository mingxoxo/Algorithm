# Z
# 재귀 / 분할 정복
# 23.04.05
# https://www.acmicpc.net/problem/1074

def recursive(N, x, y, n, pos):
    d = 2**(N-1)
    dx, dy = [0, 0, d, d], [0, d, 0, d]
    
    if N == 0:
        print(n)
        return
    
    for i in range(4):
        sx, sy = x + dx[i], y + dy[i]
        if sx <= pos[0] < sx + d and sy <= pos[1] < sy + d:
            recursive(N-1, sx, sy, n +  i * (d * d), pos)
        

N, r, c = map(int, input().split())
recursive(N, 0, 0, 0, (r, c))
