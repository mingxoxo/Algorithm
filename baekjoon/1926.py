#그림
#BFS
#https://www.acmicpc.net/problem/1926

import sys
from collections import deque
input = sys.stdin.readline

def BFS(paper, n, m, starting_point):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt, max_area = 0, 0
    while starting_point:
        start_node = starting_point.popleft()
        if paper[start_node[0]][start_node[1]] == 0:
            continue
        paper[start_node[0]][start_node[1]] = 0
        cnt += 1
        area = 1
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            x, y = node[0], node[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if paper[nx][ny] == 1:
                        area += 1
                        paper[nx][ny] = 0
                        queue.append((nx, ny))
        max_area = max(max_area, area)
    return cnt, max_area


def main():
    paper = []
    starting_point = deque()
    n, m = map(int, input().split())
    for i in range(n):
        paper.append(list(map(int, input().split())))
        starting_point.extend([(i, j) for j in range(m) if paper[-1][j] == 1])
    cnt, max_area = BFS(paper, n, m, starting_point)
    print(cnt)
    print(max_area)

if __name__ == "__main__":
    main()
