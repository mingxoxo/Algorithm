# 서로 다른 부분 문자열의 개수
# 24.03.15
# https://www.acmicpc.net/problem/11478

S = input()
substring = set()

str_len = len(S)
for i in range(1, str_len + 1):
    for j in range(str_len - i + 1):
        substring.add(S[j:j+i])

print(len(substring))
