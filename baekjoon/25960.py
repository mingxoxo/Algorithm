# 폰의 각성
# Dijkstra / graph
# 22.11.20
# https://www.acmicpc.net/problem/25960

import sys
import heapq

input = sys.stdin.readline


def Dijkstra(graph, ori, dst):
    heap = [(0, ori)]
    visited = {pos : -1 for pos in graph.keys()}
    visited[ori] = 0

    while heap:
        w, n = heapq.heappop(heap)
        if visited[n] < w:
            continue
        for x, xw in graph[n]:
            if visited[x] == -1 or w + xw < visited[x]:
                visited[x] = w + xw
                heapq.heappush(heap, (w + xw, x))
    return visited[dst]


def check_cor_loop_eight(role, x, y, graph, board, N, node_number):
    if role == 'N':
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [1, -1, -2, 2, 2, -2, -1, 1]
        cnt = 2
    else:
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        cnt = 1

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] not in ['0', 'P']:
            graph[node_number[x][y]].append((node_number[nx][ny], cnt))


def check_cor_loop_inf(role, x, y, graph, board, N, node_number):
    if role == 'R':
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
    elif role == 'B':
        dx = [-1, -1, 1, 1]
        dy = [-1, 1, -1, 1]

    for i in range(4):
        nx, ny = x, y
        cnt = 0
        while True:
            cnt += 1
            nx, ny = nx + dx[i], ny + dy[i]
            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                break
            if board[nx][ny] not in ['0', 'P']:
                graph[node_number[x][y]].append((node_number[nx][ny], cnt))
                break


def check_include_edge(board, N, node_number):
    graph = {}

    for x in range(N):
        for y in range(N):
            role = board[x][y]
            if role == '0':
                continue
            graph[node_number[x][y]] = []

            if role in ['N', 'P']:
                check_cor_loop_eight(role, x, y, graph, board, N, node_number)
            if role in ['B', 'Q']:
                check_cor_loop_inf('B', x, y, graph, board, N, node_number)
            if role in ['R', 'Q']:
                check_cor_loop_inf('R', x, y, graph, board, N, node_number)
    return graph

  
N = int(input())
board = []
node_number = [[0] * N for _ in range(N)]

for i in range(N):
    board.append(input().strip().split())

number = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == '0':
            continue
        node_number[i][j] = number
        number += 1
        if board[i][j] == 'P':
            P = node_number[i][j]
        if board[i][j] == 'K':
            K = node_number[i][j]


graph = check_include_edge(board, N, node_number)
print(Dijkstra(graph, P, K))
