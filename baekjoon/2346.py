# 풍선 터뜨리기
# 덱
# 24.04.02
# https://www.acmicpc.net/problem/2346


from collections import deque

N = int(input())

arr = list(map(int, input().split()))
queue = deque([(i + 1, arr[i]) for i in range(N)])


while queue:
    idx, paper = queue.popleft()
    print(idx, end=' ')
    if 0 < paper:
        paper -= 1
    queue.rotate(-(paper))
