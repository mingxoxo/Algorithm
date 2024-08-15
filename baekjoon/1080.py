# 행렬
# 24.08.15
# 그리디
# https://www.acmicpc.net/problem/1080


import sys
input=sys.stdin.readline


def convert_matrix(sx: int, sy: int, matrix: list[list[int]]):
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            matrix[i][j] ^= 1


N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]
matrix = [[A[i][j] ^ B[i][j] for j in range(M)] for i in range(N)]

cnt = 0


for i in range(N - 2):
    for j in range(M - 2):
        if matrix[i][j] == 1:
            convert_matrix(i, j, matrix)
            cnt += 1

print(cnt) if sum(sum(matrix, [])) == 0 else print(-1)
