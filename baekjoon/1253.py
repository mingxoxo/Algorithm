# 좋다
# 24.02.03
# 투 포인터
# https://www.acmicpc.net/problem/1253

def two_pointer(idx):
    global arr, N
    
    start, end = 0, N - 1 
    while start < end:
        if start == idx:
            start += 1
            continue
        if end == idx:
            end -= 1
            continue
        
        if arr[start] + arr[end] == arr[idx]:
            return True
        
        if arr[start] + arr[end] < arr[idx]:
            start += 1
        else:
            end -= 1
    return False
    


N = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(N):
    result += int(two_pointer(i))

print(result)
