# 계란으로 계란치기
# 백트래킹
# 24.01.13
# https://www.acmicpc.net/problem/16987

POWER = 1
WEIGHT = 2

def brute_force(i, result, cnt):
    if i == N:
        return max(result, cnt)
    
    if eggs[i][POWER] <= 0:
        return brute_force(i + 1, result, cnt)
    
    for j in range(N):
        if i == j:
            continue
        if eggs[j][POWER] <= 0:
            continue
        
        eggs[i][POWER] -= eggs[j][WEIGHT]
        eggs[j][POWER] -= eggs[i][WEIGHT]
        
        result = brute_force(i + 1, result, cnt + (eggs[i][POWER] <= 0) + (eggs[j][POWER] <= 0))
        
        eggs[i][POWER] += eggs[j][WEIGHT]
        eggs[j][POWER] += eggs[i][WEIGHT]
        
    return max(result, cnt)
    


N = int(input())
eggs = [[i] + list(map(int, input().split())) for i in range(N)]
print(brute_force(0, 0, 0))
