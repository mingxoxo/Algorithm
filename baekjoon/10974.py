# 모든 순열
# 23.04.07
# 백트래킹
# https://www.acmicpc.net/problem/10974

def backtracking(N, arr, answer):
    if len(answer) == N:
        print(*answer)
        return
    for i in range(1, N + 1):
        if arr[i] == 0:
            answer.append(i)
            arr[i] = 1
            backtracking(N, arr, answer)
            arr[i] = 0
            answer.pop()

N = int(input())
arr = [0] * (N + 1)
answer = []
backtracking(N, arr, answer)
