#2022.06.13
#인간-컴퓨터 상호작용
#https://www.acmicpc.net/problem/16139

import sys
import copy

input = sys.stdin.readline

string = input().strip()
arr = [0] * 26
prefix_sum = [copy.deepcopy(arr)]

for i in range(len(string)):
    arr[ord(string[i]) - ord('a')] += 1
    prefix_sum.append(copy.deepcopy(arr))

q = int(input())
for num in range(q):
    char, index1, index2 = input().split()
    sys.stdout.write(str(prefix_sum[int(index2) + 1][ord(char) - ord('a')] - prefix_sum[int(index1)][ord(char) - ord('a')]) + "\n")

