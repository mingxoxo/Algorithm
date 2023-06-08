# 별 찍기 - 11
# 23.06.08
# https://www.acmicpc.net/problem/2448

def recursive(N):
    if N == 3:
        return ["*", "* *", "*****"]
    size = N // 2
    pattern = recursive(size)
    new = []
    for i in range(size):
        blank = (size - i) * 2 - 1
        new.append(''.join([pattern[i] + ' ' * blank + pattern[i]]))
    return pattern + new


N = int(input())
for i, line in enumerate(recursive(N)):
    print(' ' * (N - i - 1), end='')
    print(line, end='')
    print(' ' * (N - i - 1))
