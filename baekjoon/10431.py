# 줄세우기
# 24.04.17
# https://www.acmicpc.net/problem/10431


P = int(input())
for _ in range(P):
    T, *arr = map(int, input().split())
    cnt = 0
    for i in range(19):
        for j in range(i + 1, 20):
            if arr[j] < arr[i]:
                cnt += 1
    print(T, cnt)
    
