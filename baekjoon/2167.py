# 2차원 배열의 합
# 23.01.05
# 누적합
# 11660에서 시간초과 난 풀이가 정답으로 인정 (시간 제한이 2초)
# https://www.acmicpc.net/problem/2167

import sys
input = sys.stdin.readline


def prefix_sum(line):
    result = [0]
    for n in line:
        result.append(result[-1] + n)
    return result


N, M = map(int, input().split())
arr = []

for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(prefix_sum(line))

K = int(input())
for _ in range(K):
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        total += arr[i][y2] - arr[i][y1 - 1]
    print(total)
