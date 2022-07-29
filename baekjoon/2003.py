# 수들의 합 2
# 투포인터
# 22.07.27
# https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
num_sum = A[0]

while start < N and end < N:
    if num_sum < M:
        end += 1
        num_sum += A[end] if end < N else 0
        continue
    if num_sum == M:
        cnt += 1
    num_sum -= A[start]
    start += 1

print(cnt)
