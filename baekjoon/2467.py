# 용액
# 투포인터(인데 이분탐색으로도 풀 수 있음)
# 22.08.04
# https://www.acmicpc.net/problem/2467

N = int(input())
arr = list(map(int, input().split()))

result = [abs(arr[-1] + arr[0]), arr[0], arr[-1]]
start, end = 0, N-1

while start < end:
    if abs(arr[start] + arr[end]) <= result[0]:
        result[0] = abs(arr[start] + arr[end])
        result[1] = arr[start]
        result[2] = arr[end]
        
    if abs(arr[start]) <= abs(arr[end]):
        end -= 1
    else:
        start += 1

print(result[1], result[2], sep = ' ')
