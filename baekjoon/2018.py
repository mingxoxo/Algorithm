# 수들의 합 5
# 투 포인터
# 23.08.26
# https://www.acmicpc.net/problem/2018

N = int(input())

start, end = 1, 2
result = 1


while start < end and end <= N // 2 + 1:
    section_sum = (end + 1) * (end) // 2 - (start - 1) * (start) // 2
    if section_sum <= N:
        if section_sum == N:
            result += 1
        end += 1
    else:
        start += 1

print(result)
