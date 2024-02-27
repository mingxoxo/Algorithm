# K번째 수 ⚠️
# 이분 탐색, 매개변수 탐색
# 24.02.27
# https://www.acmicpc.net/problem/1300
# 풀이 공부: https://st-lab.tistory.com/281

def count_min_value(n):
    global N
    
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(n // i, N)
    
    return cnt


N = int(input())
k = int(input())

start, end = 1, k

while start < end:
    mid = (start + end) // 2
    cnt = count_min_value(mid)

    if cnt < k:
        start = mid + 1
    else:
        end = mid

print((start + end) // 2)
