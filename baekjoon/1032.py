# 명령 프롬프트
# 구현
# 24.04.12
# https://www.acmicpc.net/problem/1032

N = int(input())
pattern = list(input())
for i in range(N - 1):
    string = input()
    for j in range(len(string)):
        if pattern[j] != string[j]:
            pattern[j] = '?'

print(''.join(pattern))
