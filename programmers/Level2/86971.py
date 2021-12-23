#전력망을 둘로 나누기
#https://programmers.co.kr/learn/courses/30/lessons/86971

import copy
from collections import deque

def bfs(n, wires_list, remove_edge):
    visited = [0] * n
    wires_list[remove_edge[0]].remove(remove_edge[1])
    wires_list[remove_edge[1]].remove(remove_edge[0])
    queue = deque([wires_list[1]])
    visited[0] = 1
    
    while queue:
        node = queue.popleft()
        for i in node:
            if visited[i-1] != 1:
                queue.append(wires_list[i])
            visited[i-1] = 1
            
    return abs(visited.count(0)-visited.count(1))

def solution(n, wires):
    answer = 101
    wires_list = [[] for _ in range(n+1)]
    for i in wires:
        wires_list[i[0]].append(i[1])
        wires_list[i[1]].append(i[0])
    
    for edge in wires:
        answer = min(answer, bfs(n, copy.deepcopy(wires_list), edge))
    
    return answer
