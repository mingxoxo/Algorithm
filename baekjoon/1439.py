# 뒤집기
# 23.03.25
# 그리디
# https://www.acmicpc.net/problem/1439

S = input()

cnt = 1
for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        cnt += 1

print(cnt // 2)
