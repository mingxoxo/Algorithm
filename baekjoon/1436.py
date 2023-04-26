# 영화감독 숌
# 23.04.26
# 브루트포스
# https://www.acmicpc.net/problem/1436

N = int(input())
cnt = 1
i = 1665
answer = 666

while cnt < N:
    i += 1
    while "666" not in str(i):
        i += 1
    cnt += 1
    answer = i

print(answer)
