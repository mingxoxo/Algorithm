# 시간 관리
# 그리디, 정렬
# 23.12.30
# https://www.acmicpc.net/problem/1263

N = int(input())
info = []
for _ in range(N):
    T, S = map(int, input().split())
    info.append((T, S, S - T))

info.sort(key=lambda x: (-x[1], -x[0]))

time = info[0][1]
for t, s, diff in info:
    time = min(diff, time - t)

print(time) if time >= 0 else print(-1)
