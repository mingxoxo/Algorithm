# solved.ac 2022
# 23.06.22
# https://www.acmicpc.net/problem/25318


import sys
input = sys.stdin.readline


def get_time(time):
    info = {2019: (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
            2020: (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
            2021: (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
            2022: (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)}
    ans = 0
    for i in range(2019, time[0]):
        ans += sum(info[i])
    ans += sum(info[time[0]][:time[1] - 1]) + time[2]
    ans += (time[3] + time[4] / 60 + time[5] / 3600) / 24
    return ans


def time_diff(time1, time2):
    return get_time(time1) - get_time(time2)


N = int(input())
if N == 0:
    print(0)
else:
    time = []
    level = []

    for i in range(N):
        *ti, li = input().rstrip().split()
        ti[0] = list(map(int, ti[0].split('/')))
        ti[1] = list(map(int, ti[1].split(':')))

        time.append(ti[0] + ti[1])
        level.append(int(li))

    p = []
    for i in range(N):
        p.append(max(0.5 ** (time_diff(time[N - 1], time[i]) / 365), 0.9 ** (N - i - 1)))

    print(round(sum([i * j for i, j in zip(p, level)]) / sum(p)))
