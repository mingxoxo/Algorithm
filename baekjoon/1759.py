# 암호 만들기
# 22.08.25
# backtracking & Brute Force
# https://www.acmicpc.net/problem/1759


import sys
input = sys.stdin.readline


def backtracking(i, N, S, alphabet, password, cnt):
    if len(password) == N:
        if 1 <= cnt <= N - 2:
            print(''.join(password))
        return

    for j in range(i, S):
        password.append(alphabet[j])
        if alphabet[j] in "aeiou":
            cnt += 1

        backtracking(j + 1, N, S, alphabet, password, cnt)

        password.pop()
        if alphabet[j] in "aeiou":
            cnt -= 1


L, C = map(int, input().split())
alphabet = sorted(list(input().split()))
backtracking(0, L, C, alphabet, [], 0)
