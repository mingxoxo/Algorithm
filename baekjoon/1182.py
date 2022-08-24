# 부분수열의 합
# 22.08.25
# Brute force
# https://www.acmicpc.net/problem/1182


import sys
input = sys.stdin.readline


def backtracking(i, N, S, num, seq, result):
    if seq and S == sum(seq):
        result += 1

    for j in range(i, N):
        seq.append(num[j])
        result = backtracking(j + 1, N, S, num, seq, result)
        seq.pop()

    return result


N, S = map(int, input().split())
num = sorted(list(map(int, input().split())))
result = 0

print(backtracking(0, N, S, num, [], result))
