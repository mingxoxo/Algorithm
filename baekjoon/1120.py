# 문자열
# 브루트포스
# 24.01.18
# https://www.acmicpc.net/problem/1120

def diff(X, Y):
    cnt = 0
    for x, y in zip(X, Y):
        if x != y:
            cnt += 1
    return cnt


A, B = input().split()
len_a, len_b = len(A), len(B)

result = len_a
for i in range(len_b - len_a + 1):
    result = min(result, diff(A, B[i : i + len_a]))

print(result)
    
