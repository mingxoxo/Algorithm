#손익분기점
#https://www.acmicpc.net/problem/1712

# A --> 고정 비용
# B --> 가변 비용

A, B, C = map(int, input().split())

if B >= C:
    print("-1")
else:
    print(int(A/(C-B)) + 1)
