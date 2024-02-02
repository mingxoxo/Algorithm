# ABCDE
# 24.02.02
# DFS
# https://www.acmicpc.net/problem/13023

def brute_force(visited, now, cnt):
    if cnt == 4:
        return True
        
    for i in graph[now]:
        if visited[i] == False:
            visited[i] = True
            if brute_force(visited, i, cnt + 1):
                return True
            visited[i] = False
    
    return False




N, M = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(N):
    
    if brute_force([False if i != j else True for j in range(N) ], i, 0):
        print(1)
        break
else:
    print(0)
