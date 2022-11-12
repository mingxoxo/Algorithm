# 단어순서 뒤집기
# 22.11.12
# https://www.acmicpc.net/problem/12605

N = int(input())
for i in range(N):
    cmd = input().split()
    print("Case #%d: "%(i + 1), end = '')
    print(*reversed(cmd))
