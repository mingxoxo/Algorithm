def dfs(graph, x, y, N, M):
    if x < 0 or y < 0 or x >= N or y >= M or graph[x][y] == 0:
        return 99999
    if x == N - 1 and y == M - 1:
        return 1
    miro[x][y] = 0

    min_list = [dfs(graph, x + 1, y, N, M),
                dfs(graph, x - 1, y, N, M),
                dfs(graph, x, y - 1, N, M),
                dfs(graph, x, y + 1, N, M)]
    return min(min_list) + 1


N, M = list(map(int, input().split()))
miro = []
visited = []
for i in range(N):
    miro.append(list(map(int, input())))
print(dfs(miro, 0, 0, N, M))
