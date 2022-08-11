# 부분합
# https://www.acmicpc.net/problem/1806
# 22.08.11
# 투 포인터 / 누적합

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 1

arr_sum = [0]
result = 0

# 누적합 구하기
for i in range(N):
    arr_sum.append(arr_sum[-1] + arr[i])

while start <= end and end <= N:
    if arr_sum[end] - arr_sum[start] >= S:
        result = end - start if end - start < result or result == 0 else result
        start += 1
    else:
        end += 1

print(result)
