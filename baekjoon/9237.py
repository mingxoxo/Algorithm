# 이장님 초대
# 그리디, 정렬
# https://www.acmicpc.net/problem/9237

n = int(input())
tree = sorted(map(int, input().split()), reverse=True)
answer = 0

for i in range(n):
    answer = max(answer, tree[i] + i + 1)

print(answer + 1)
