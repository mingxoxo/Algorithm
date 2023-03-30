# 나무조각
# 23.03.30
# 구현
# https://www.acmicpc.net/problem/2947

# 배열 선언 후 == 으로 비교해도 가능함
def is_sort(arr):
    for i in range(4):
        if arr[i + 1] < arr[i]:
            return False
    return True


arr = list(map(int, input().split()))
while is_sort(arr) is False:
    for i in range(4):
        if arr[i + 1] < arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
