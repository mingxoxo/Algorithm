# 기타 레슨
# 24.08.10
# 매개 변수 탐색
# https://www.acmicpc.net/problem/2343


import sys
input=sys.stdin.readline


def is_possible_bluray_size(size) -> bool:
    global times, M
    
    cnt = 1
    sum_temp = 0
    
    for time in times:
        if size < sum_temp + time:
            cnt += 1
            sum_temp = 0
        sum_temp += time
        
    return cnt <= M


def parametric_search(N: int, M: int, times: list):
    start, end = max(times), 10000 * int(N / M + 0.5)
    
    while start <= end:
        mid = (start + end) // 2
        
        if is_possible_bluray_size(mid):
            end = mid - 1
        else:
            start = mid + 1
    
    return end + 1


N, M = map(int, input().split())
times = list(map(int, input().split()))
print(parametric_search(N, M, times))

