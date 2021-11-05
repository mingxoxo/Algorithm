#https://www.acmicpc.net/problem/10816
#이진탐색

import sys
from bisect import bisect_left, bisect_right

def count_card(target, numList):
    left_index = bisect_left(numList, target) #타겟의 가장 왼쪽 인덱스
    right_index = bisect_right(numList, target) #타겟의 마지막 인덱스 + 1
    return right_index-left_index

N = int(input())
numList = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
searchList = list(map(int, sys.stdin.readline().split()))

for target in searchList:
    print(count_card(target, numList), end = ' ')


