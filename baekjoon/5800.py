# 성적 통계
# 24.02.01
# 구현, 정렬
# https://www.acmicpc.net/problem/5800

K = int(input())
for i in range(K):
    N, *score = map(int, input().split())
    score.sort()
    gap = max([score[i + 1] - score[i] for i in range(N - 1)])
    print("Class", i + 1)
    print('Max {}, Min {}, Largest gap {}'.format(score[-1], score[0], gap))
