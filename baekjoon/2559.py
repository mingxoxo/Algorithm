# 수열
# 슬라이딩 윈도우
# 23.08.25
# https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
nums = list(map(int, input().split()))
result = sum(nums[:K])
temp = result

for i in range(K, N):
    temp = temp - nums[i - K] + nums[i]
    result = max(result, temp)

print(result)
