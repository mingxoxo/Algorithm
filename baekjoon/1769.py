# 3의 배수
# 22.07.05
# 구현
# https://www.acmicpc.net/problem/1769

import sys
input = sys.stdin.readline

N = list(map(int, input().strip()))
cnt = 0
while len(N) != 1:
    cnt += 1
    N = list(map(int, str(sum(N))))

print(cnt)
print("YES") if sum(N) % 3 == 0 else print("NO")

