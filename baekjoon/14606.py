# 피자 (Small)
# 24.03.07
# https://www.acmicpc.net/problem/14606


from collections import deque

N = int(input())

ans = 0
queue = deque([N])
while queue:
    h = queue.popleft()
    if h == 1:
        continue
    
    half = h // 2
    ans += half * (h - half)
    queue.append(half)
    queue.append(h - half)

print(ans)
