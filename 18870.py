#좌표 압축
#https://www.acmicpc.net/problem/18870

#중복 부분을 set으로 처리했어도 될 것 같음

import sys
input = sys.stdin.readline

N = int(input())
X_list = list(map(int, input().split()))

X_compression = {}
i = 0
for x in sorted(X_list):
    if x not in X_compression.keys():
        X_compression[x] = i
        i+=1

for x in X_list:
    print(X_compression[x], end=' ')



