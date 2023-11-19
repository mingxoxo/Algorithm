# 올바른 배열
# 23.11.19
# 구현 / 정렬 / 투포인터
# https://www.acmicpc.net/problem/1337

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

start, end = 0, 0
result = 4

while start <= end and end < N:
    if arr[end] <= arr[start] + 4:
        result = min(5 - (end - start + 1), result)
        end += 1
        continue
    
    start += 1

print(result)
