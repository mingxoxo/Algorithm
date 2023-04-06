# Project Teams
# 정렬
# 23.04.06
# https://www.acmicpc.net/problem/20044

n = int(input())
ability = sorted(list(map(int, input().split())))
answer = 1e12

for i in range(len(ability) // 2):
    answer = min(answer, ability[i] + ability[-1 - i])
print(answer)
