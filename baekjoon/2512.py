# 예산
# 23.07.08
# 이분탐색, 매개변수 탐색
# https://www.acmicpc.net/problem/2512

N = int(input())
money = list(map(int, input().split()))
total = int(input())

start, end = 0, max(money)
result, max_sum = 0, 0

while start <= end:
    mid = (start + end) // 2
    mid_sum = sum([i if i < mid else mid for i in money])
    
    if total < mid_sum:
        end = mid - 1
    else:
        if max_sum < mid_sum:
            result = mid
            max_sum = mid_sum
        start = mid + 1
    
print(result)
