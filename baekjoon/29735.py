# 택배가 안와잉
# 구현
# 24.02.28
# https://www.acmicpc.net/problem/29735


def convert_miniute(string):
    hh, mm = map(int, string.split(':'))
    return hh * 60 + mm


start, end = map(convert_miniute, input().split())
N, T = map(int, input().split())
N = N + 1


now = start
day = 0
while N:
    if end <= now + T:
        now = start
        day += 1
        continue
    
    N -= 1
    now += T


print(day)
print(f'{now // 60:02}:{now % 60:02}')
