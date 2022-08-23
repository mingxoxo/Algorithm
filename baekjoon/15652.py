# N과 M (4) 
# 백트래킹
# 22.08.23
# https://www.acmicpc.net/problem/15652


import sys
input = sys.stdin.readline


def make_sequence(cnt, i, N, M, seq):
    if cnt == M:
        print(' '.join(map(str, seq)))
        return ;

    for j in range(i, N + 1):
        seq.append(j)
        make_sequence(cnt + 1, j, N, M, seq)

        seq.pop()


def main():
    N, M = map(int, input().split())
    make_sequence(0, 1, N, M, [])


if __name__=="__main__":
    main()
