# 주몽
# 22.08.07
# 투포인터
# https://www.acmicpc.net/problem/1940

N = int(input())
M = int(input())
items = sorted(list(map(int, input().split())))


left = 0
right = N - 1
cnt = 0

while left < right:
    if items[left] + items[right] < M:
        left += 1
    else:
        if items[left] + items[right] == M: 
            cnt += 1
        right -= 1

print(cnt)
