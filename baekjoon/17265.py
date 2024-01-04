# 나의 인생에는 수학과 함께
# BFS
# 23.01.04
# https://www.acmicpc.net/problem/17265

from collections import deque

def calculate(a, b, cmd):
    a, b = int(a), int(b)
    result = {'+': a + b, '-': a - b, '*': a * b}
    return str(result[cmd])


def bfs(N, graph):
    queue = deque([(0, 0, graph[0][0])])
    dx, dy = [0, 1], [1, 0]
    answer = []
    
    while queue:
        x, y, cmd = queue.popleft()
        
        if x == y == N - 1:
            answer.append(int(cmd))
            continue
        
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if N <= nx or N <= ny:
                continue
            next_cmd = calculate(cmd[:-1], graph[nx][ny], cmd[-1]) if cmd[-1] in "+-*" else cmd + graph[nx][ny]
            queue.append((nx, ny, next_cmd))
    
    return max(answer), min(answer)


N = int(input())
graph = [input().split() for _ in range(N)]
print(*bfs(N, graph))
    
