# 2048 (Easy)
# 24.02.07
# 구현, 시뮬레이션, 백트래킹
# https://www.acmicpc.net/problem/12100

import sys
input=sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def get_next_line(line, reverse_flag):
    result = []
    flag = False # 비교 가능 flag
    
    if reverse_flag:
        line = reversed(line)
    
    for i in line:
        if i == 0:
            continue
        
        if flag is True and result[-1] == i:
            result.pop()
            result.append(i * 2)
            flag = False
            continue
        
        result.append(i)
        flag = True
        
    result += [0] * (N - len(result))
    return result if reverse_flag is False else list(reversed(result))



def get_next_graph(num, graph):
    global N

    if 1 < num:
        graph = list(map(list, zip(*graph)))
    reverse_flag = False if num % 2 == 0 else True
    
    new = []
    for i in range(N):
        new.append(get_next_line(graph[i], reverse_flag))
        
    if 1 < num:
        return list(map(list, zip(*new)))
    return new


def backtracking(move, graph):
    global pos
    
    if move == 5:
        return max(sum(graph, []))
    
    result = 0
    for i in range(4):
        result = max(result, backtracking(move + 1, get_next_graph(i, graph)))
    
    return result

print(backtracking(0, graph))
