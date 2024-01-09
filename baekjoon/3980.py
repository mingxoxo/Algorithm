# 선발 명단
# 브루트포스, 백트래킹
# 24.01.09
# https://www.acmicpc.net/problem/3980

import sys
input=sys.stdin.readline

def brute_force(used, power, idx = 0, power_sum = 0, result = 0):
    if idx == 11:
        return max(result, power_sum)
    
    for i in range(11):
        if power[i][idx] == 0 or used[i] == True:
           continue
        used[i] = True
        result = brute_force(used, power, idx + 1, power_sum + power[i][idx], result)
        used[i] = False
    
    return result



C = int(input())
for _ in range(C):
    power = [list(map(int, input().split())) for _ in range(11)]
    print(brute_force([False] * 11, power))
