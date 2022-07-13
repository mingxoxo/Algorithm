# 연산자 끼워넣기
# BruteForce
# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline

def cal(x, y, op_idx):
    result = [x + y, x - y, x * y, x // y, -1 * (abs(x) // y)]
    if op_idx == 3 and x < 0:
        return result[4]
    return result[op_idx]

def BruteForce(result, N, num, op):
    op_idx = [i for i in range(4) if op[i] > 0]
    if N == 1:
        result.append(cal(num[0], num[1], op_idx[0]))
        return result
    for idx in op_idx:
        op[idx] -= 1
        BruteForce(result, N - 1, [cal(num[0], num[1], idx)] + num[2:], op)
        op[idx] += 1
    return result


N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
result = []

result = sorted(BruteForce(result, N - 1, num, op))

print(result[-1])
print(result[0])
