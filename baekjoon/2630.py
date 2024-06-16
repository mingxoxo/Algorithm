# 색종이 만들기
# 24.06.16
# 분할정복, 재귀
# https://www.acmicpc.net/problem/2630


def divide_and_conquer(N, sx, sy, paper):
    cnt = [0, 0]
    if N == 1:
        cnt[paper[sx][sy]] += 1
        return cnt

    N //= 2
    for x, y in [(sx, sy), (sx + N, sy), (sx, sy + N), (sx + N, sy + N)]:
        w_cnt, b_cnt = divide_and_conquer(N, x, y, paper)
        cnt[0] += w_cnt
        cnt[1] += b_cnt

    if cnt == [0, 4]:
        return [0, 1]
    elif cnt == [4, 0]:
        return [1, 0]
    else:
        return cnt



N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
print(*divide_and_conquer(N, 0, 0, paper), sep='\n')
