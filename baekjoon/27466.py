# 그래서 대회 이름 뭐로 하죠
# 23.02.11
# 구현 / 문자열 / 그리디
# https://www.acmicpc.net/problem/27466

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()

a = [i for i in range(N) if S[i] == 'A']
result = ""

flag = 0
for i in range(1, len(a)):
    if a[i] + 1 < N:
        if a[i] + 1 - (a[i] - a[i - 1]) + 2 >= M:
            result = S[a[i - 1] - (M - 3): a[i - 1]] + 'AA'
            for j in range(a[i] + 1, N):
                if S[j] not in ['A', 'E', 'I', 'O', 'U']:
                    result += S[j]
                    flag = 1
                    print("YES")
                    break
            if flag == 1:
                print(result)
                break

if flag == 0:
    print("NO")
