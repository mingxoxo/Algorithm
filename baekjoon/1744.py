# 수 묶기기
# 그리디
# 22.07.24
# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

def cal(arr, len):
    result = []
    for i in range(0, len, 2):
        result.append(arr[i] * arr[i + 1]) if len != i + 1 else result.append(arr[i])
    return (sum(result))


N = int(input())
arr = [int(input()) for _ in range(N)]

pos = sorted([i for i in arr if i > 1], reverse=True)
neg = sorted([i for i in arr if i < 1])
pos_len, neg_len = len(pos), len(neg)
print(cal(pos, len(pos)) + cal(neg, len(neg)) + arr.count(1))


# 다른 사람의 풀이
# def hap(arr):
#     res = 0
#     for i in range(1, len(arr), 2):
#         res += arr[i - 1] * arr[i]
#     if len(arr) % 2 == 1:
#         res += arr[-1]
#     return res