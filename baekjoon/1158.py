# 요세푸스 문제
# 22.12.01
# 큐
# https://www.acmicpc.net/problem/1158

from collections import deque


N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    queue.rotate(-K + 1)
    result.append(queue.popleft())

print("<", end='')
print(*result, sep=', ', end='')
print(">", end='')
