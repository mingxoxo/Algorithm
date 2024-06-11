# 알고리즘 수업 - 병합 정렬 1
# 24.06.11
# 재귀
# 최적화하는 방법 다시 찾아보기
# https://www.acmicpc.net/problem/24060

store_arr = []

def merge(A, p, q, r):
    global store_arr
    
    i, j = p, q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
            
    while i <= q:
        tmp.append(A[i])
        i += 1
        
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i = p
    t = 0
    
    while i <= r:
        A[i] = tmp[t]
        store_arr.append(tmp[t])
        i += 1
        t += 1



def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)



A, K = map(int, input().split())
nums = list(map(int, input().split()))
merge_sort(nums, 0, A - 1)

if len(store_arr) < K:
    print(-1)
else:
    print(store_arr[K - 1])
