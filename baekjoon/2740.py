# 행렬 곱셈
# 23.04.09
# 수학, 구현
# https://www.acmicpc.net/problem/2740

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

for i in range(N):
    ans = [0] * K
    for j in range(K):
        for k in range(M):
            ans[j] += A[i][k] * B[k][j]
    print(*ans)
