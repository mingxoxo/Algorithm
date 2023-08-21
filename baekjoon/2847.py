# 게임을 만든 동준이
# 그리디
# 23.08.21
# https://www.acmicpc.net/problem/2847


N = int(input())
score = [int(input()) for _ in range(N)]
prev = sum(score)
for i in reversed(range(N - 1)):
    score[i] = min(score[i + 1] - 1, score[i])

print(prev - sum(score))
