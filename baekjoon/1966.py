# 프린터 큐
# 22.10.11
# https://www.acmicpc.net/problem/1966


import sys
from collections import deque
input = sys.stdin.readline


def search_document(search, importance):
    cnt = 0
    s_list = sorted(importance, reverse=True)
    queue = deque(enumerate(importance))

    while queue:
        if s_list[cnt] == queue.__getitem__(0)[1]:
            if search == queue.__getitem__(0)[0]:
                return cnt + 1
            cnt += 1
            queue.popleft()
        else:
            queue.rotate(-1)



T = int(input())
for _ in range(T):
    N, search = map(int, input().split())
    importance = list(map(int, input().split()))
    print(search_document(search, importance))
