# Best Grass
# 24.07.29
# 구현
# https://www.acmicpc.net/problem/6186

R, C = map(int, input().split())

pasture_map = [list(input()) for _ in range(R)]
result = 0

for i in range(R):
    for j in range(C):
        if pasture_map[i][j] == '.':
            continue
        
        result += 1
        if i != R - 1 and pasture_map[i + 1][j] == '#':
            pasture_map[i + 1][j] = '.'
        elif j != C - 1 and pasture_map[i][j + 1] == '#':
            pasture_map[i][j + 1] = '.'

print(result)
