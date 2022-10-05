# 수 정렬하기 2
# mergesort
# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline


def merge(arr, l, mid, r):
    marr = []
    i = l
    j = mid + 1

    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            marr.append(arr[i])
            i += 1
        else:
            marr.append(arr[j])
            j += 1

    while i <= mid:
        marr.append(arr[i])
        i += 1
    while j <= r:
        marr.append(arr[j])
        j += 1

    for k in range(l, r + 1):
        arr[k] = marr[k - l]


def rMergeSort(arr, l, r):
    if l >= r:
        return arr
    mid = (l + r) // 2
    rMergeSort(arr, l, mid)
    rMergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)



N = int(input())
num = [int(input()) for _ in range(N)]
rMergeSort(num, 0, N - 1)
print(*num, sep='\n')
