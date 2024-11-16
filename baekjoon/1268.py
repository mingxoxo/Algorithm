# 임시 반장 정하기
# 24.11.16
# https://www.acmicpc.net/problem/1268


from collections import defaultdict

N = int(input())
check = defaultdict(set)
classroom_info = [list(map(int, input().split())) for _ in range(N)]

for col in zip(*classroom_info):
    for i in range(N):
        for j in range(i, N):
            if col[i] == col[j]:
                check[i].add(j)
                check[j].add(i)

answer = [0, 0]
for key, value in check.items():
    if answer[1] < len(value):
        answer = [key + 1, len(value)]
print(answer[0])
