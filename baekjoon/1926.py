#그림
#BFS
#시간초과
#https://www.acmicpc.net/problem/1926

import sys
from collections import deque
input = sys.stdin.readline

def starting_point(paper, n, m):
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1:
                paper[i][j] = 0
                return [(i, j)]
    return []

def BFS(paper, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    max_area = 0
    while (1):
        queue = deque(starting_point(paper, n, m))
        if not queue:
            break
        cnt += 1
        area = 1
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
    n, m = map(int, input().split())
    for i in range(n):
        paper.append(list(map(int, input().split())))
    cnt, max_area = BFS(paper, n, m)
    print(cnt)
    print(max_area)

if __name__ == "__main__":
    main()
