from collections import deque
from bisect import bisect_left


def bfs(graph, N, M, visited):
    mylist = [[i, j] for i in range(N) for j in range(M) if visited[i][j] == False]
    cnt = 0
    while len(mylist) != 0:
        queue = deque([mylist[0]])
        visited[mylist[0][0]][mylist[0][1]] = True
        while queue:
            v = queue.popleft()
            x = v[0]
            y = v[1]
            search = [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]
            for x, y in search:
                if 0 <= x < N and 0 <= y < M:
                    if not visited[x][y]:
                        visited[x][y] = True
                        queue.append([x, y])
        cnt+=1
        mylist = [[i, j] for i in range(N) for j in range(M) if visited[i][j] == False]
    print(cnt)


N, M = list(map(int, input().split()))
ice = []
visited = []
for i in range(N):
    ice.append(list(input()))
    visited.append([bool(int(t)) for t in ice[i]])
bfs(ice, N, M, visited)
