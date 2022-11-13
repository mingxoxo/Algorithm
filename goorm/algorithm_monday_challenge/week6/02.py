# 문제 2. 제곱암호
# 문자열 처리 / 조건문

N = int(input())
S = input()

for i in range(0, N, 2):
    print(chr((ord(S[i]) - ord('a') + (int(S[i + 1])**2)) % 26 + ord('a')), end='')


# 풀이
# import string
# alpha_small = list(string.ascii_lowercase)
