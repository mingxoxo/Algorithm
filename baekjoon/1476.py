# 날짜 계산
# 브루트포스
# https://www.acmicpc.net/problem/1476

ESM = list(map(int, input().split()))
esm_range = [15, 28, 19]
result = [1, 1, 1]
year = 1
idx = -1


while result != ESM:
    idx = (idx + 1) % 3
    if result[idx] == ESM[idx]:
        continue
    elif result[idx] < ESM[idx]:
        cnt = ESM[idx] - result[idx]
    else:
        cnt = ESM[idx] + esm_range[idx] - result[idx]
    
    year += cnt
    for i in range(3):
        result[i] = (result[i] + cnt) % esm_range[i]
        if result[i] == 0:
            result[i] = esm_range[i]
    

print(year)
