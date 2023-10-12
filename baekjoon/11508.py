# 2+1 세일
# 그리디, 정렬
# 23.10.12
# https://www.acmicpc.net/problem/11508

N = int(input())
C = sorted([int(input()) for _ in range(N)], reverse=True)

answer = 0
for i in range(0, N, 3):
    group = C[i : i + 3]
    answer += group[0] + group[1] if len(group) == 3 else sum(group)

print(answer)
