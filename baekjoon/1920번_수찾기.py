#링크 : https://www.acmicpc.net/problem/1920
#입력을 빠르게 : https://paris-in-the-rain.tistory.com/72
#이진탐색으로 풀어야만 시간초과가 되지 않음 !!!
import sys

N = int(input())
numList = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
searchList = list(map(int, sys.stdin.readline().split()))

for i in searchList:
    pr = 0
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if numList[mid] == i:
            pr = 1
            break
        elif numList[mid] > i:
            end = mid-1
        else:
            start = mid+1
    print(pr)

