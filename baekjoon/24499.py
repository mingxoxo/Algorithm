# blobyum
# 슬라이딩 윈도우
# 24.05.26
# https://www.acmicpc.net/problem/24499


N, K = map(int, input().split())
level = list(map(int, input().split()))
level.extend(level)


result = level_sum = sum(level[:K])

for i in range(K, N + K):
    level_sum -= level[i - K]
    level_sum += level[i]
    
    if result < level_sum:
        result = level_sum
    
print(result)
