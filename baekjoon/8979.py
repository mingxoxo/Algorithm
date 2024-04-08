# 올림픽
# 24.04.08
# https://www.acmicpc.net/problem/8979


N, K = map(int, input().split())
k_stat = []
stats = []

for _ in range(N):
    stat = list(map(int, input().split()))
    if stat[0] == K:
        k_stat = stat
    else:
        stats.append(stat)

rank = 1
for _, gold, silver, bronze in stats:
    if k_stat[1] < gold:
        rank += 1
    elif k_stat[1] == gold and k_stat[2] < silver:
        rank += 1
    elif k_stat[1] == gold and k_stat[2] == silver and k_stat[3] < bronze:
        rank += 1

print(rank)
