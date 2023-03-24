# 차집합
# 23.03.24
# https://www.acmicpc.net/problem/1822

A, B = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))
sub = A_set - B_set

print(len(sub))
if sub:
    print(*sorted(list(sub)))
