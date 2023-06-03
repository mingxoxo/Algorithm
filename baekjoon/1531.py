# 투명
# 23.06.03
# https://www.acmicpc.net/problem/1531

picture = [0] * 10000

N, M = map(int, input().split())
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx - 1, rx):
        for j in range(ly - 1, ry):
            picture[i * 100 + j] += 1

print(len([i for i in picture if i > M]))
