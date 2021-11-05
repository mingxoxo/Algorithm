#https://www.acmicpc.net/problem/10815
#이진탐색

import sys

N = int(input())
numList = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
searchList = list(map(int, sys.stdin.readline().split()))

for target in searchList:
    pr = 0
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if numList[mid] == target:
            pr = 1
            break
        elif numList[mid] < target:
            start = mid+1
        else:
            end = mid-1
    print(pr, end = ' ')
