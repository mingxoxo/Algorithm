# 국영수
# 23.03.14
# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

N = int(input())
student = [list(input().split()) for _ in range(N)]
student.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(N):
    print(student[i][0])
