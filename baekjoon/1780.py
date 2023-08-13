# 종이의 개수
# 분할정복, 재귀
# 23.08.13
# https://www.acmicpc.net/problem/1780


def is_same_paper(paper, x, y, cnt):
    for i in range(x, x + cnt):
        for j in range(y, y + cnt):
            if paper[x][y] != paper[i][j]:
                return False
    return True


def recursive_paper(paper, x, y, cnt):
    if is_same_paper(paper, x, y, cnt) is True:
        return [paper[x][y]]

    cnt //= 3
    result = []
    for i in range(3):
        for j in range(3):
            result.extend(recursive_paper(paper, x + cnt * i, y + cnt * j, cnt))

    return result


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

result = recursive_paper(paper, 0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
