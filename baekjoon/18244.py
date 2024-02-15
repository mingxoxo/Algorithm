# 변형 계단 수
# 24.02.15
# DP
# https://www.acmicpc.net/problem/18244

def init_arr():
    return [[0, 0, 0] for _ in range(12)]


N = int(input())

incres = [[1, 0, 0] for _ in range(10)] + [[0, 0, 0], [0, 0, 0]]
decres = [[1, 0, 0] for _ in range(10)] + [[0, 0, 0], [0, 0, 0]]

for _ in range(N - 1):
    new_incres, new_decres = init_arr(), init_arr()
    for n in range(10):
        new_incres[n][1] = (incres[n - 1][0] + sum(decres[n - 1])) % 1000000007
        new_incres[n][2] = incres[n - 1][1]
        new_decres[n][1] = (decres[n + 1][0] + sum(incres[n + 1])) % 1000000007
        new_decres[n][2] = decres[n + 1][1]

    incres, decres = new_incres, new_decres

print(sum(sum(incres, [])) % 1000000007)
