#스트릿 코딩 파이터
#https://www.acmicpc.net/problem/23348

import sys
input = sys.stdin.readline

score = list(map(int, input().split()))
N = int(input())
result = 0

for i in range(N):
    use = []
    for j in range(3):
        use.extend(list(map(int, input().split())))
    result = max(result, sum([use[i]*score[i%3] for i in range(9)]))

print(result)
