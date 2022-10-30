# N과 M (5) 
# 백트래킹
# 22.10.30
# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline


def backtracking(N, M, visited, num, result):
    if M == 0:
        print(*result, sep = ' ')
        return
    
    for i in range(N):
        if visited[i] == 1:
            continue
        
        visited[i] = 1
        result.append(num[i])
        backtracking(N, M - 1, visited, num, result)
        visited[i] = 0
        result.pop()
    


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N

backtracking(N, M, visited, num, [])
