# 4연산
# BFS
# 24.01.05
# https://www.acmicpc.net/problem/14395

from collections import deque

def calculate(s, op):
    result = {'+': s + s, '*': s * s, '/': 1}
    return result[op]
    

def bfs(s, t):
    if s == t:
        return 0
    if t == 0:
        return '-'
    if t == 1:
        return '/'
    if t % 2 != 0 and t % s != 0:
        return -1
    
    visited = set([s])
    queue = deque([(s, '')])
    while queue:
        s, cmd = queue.popleft()
        for op in "*+/":
            next_s, next_cmd = calculate(s, op), cmd + op
            if next_s == t:
                return next_cmd
            if next_s not in visited and next_s < t:
                queue.append((next_s, next_cmd))
                visited.add(next_s)
    return -1


s, t = map(int, input().split())
print(bfs(s, t))
