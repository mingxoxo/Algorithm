# 귀걸이
# 23.06.02
# https://www.acmicpc.net/problem/1380

scenario = 1
while True:
    n = int(input())
    if n == 0:
        break
    name = [input() for _ in range(n)]
    check = {'A': set(), 'B': set()}
    for _ in range(2 * n - 1):
        num, memo = input().split()
        check[memo].add(int(num))
    print(scenario, name[list((check['A'] | check['B']) - (check['A'] & check['B']))[0] - 1])
    scenario += 1
