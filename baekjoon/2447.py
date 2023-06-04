# 별 찍기 - 10
# 23.06.04
# 재귀, 분할정복
# https://www.acmicpc.net/problem/2447

def recursive(N):
    if N == 3:
        return ["***", "* *", "***"]
    size = N // 3
    pattern = recursive(size)
    new = []
    for i in range(N):
        if i // size == 1:
            new.append(pattern[i % size] + ' ' * size + pattern[i % size])
        else:
            new.append(pattern[i % size] * 3)
    return new


N = int(input())
print(*recursive(N), sep='\n')


