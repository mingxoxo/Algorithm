# 불꽃놀이
# 24.08.06
# 그리디
# https://www.acmicpc.net/problem/21557


N = int(input())
heights = list(map(int, input().split()))

N -= 3
first = heights[0] - 1
last = heights[-1] - 1

while 0 < N:
    dist = min(N, abs(last - first) + 1)
    if first < last:
        last -= dist
    else:
        first -= dist
    N -= dist

print(max(first, last))
