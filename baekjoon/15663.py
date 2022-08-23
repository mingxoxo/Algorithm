# N과 M (9) 
# 백트래킹
# 22.08.23
# https://www.acmicpc.net/problem/15663


import sys
input = sys.stdin.readline


def make_sequence(N, M, seq, num, result, visited):
    if M == 0:
        result.add(tuple(seq))
        return result

    for j in range(N):
        if visited[j] is False:
            visited[j] = True
            seq.append(num[j])
            result = make_sequence(N, M - 1, seq, num, result, visited)

            seq.pop()
            visited[j] = False

    return result


def main():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    visited = [False] * (N + 1)
    result = set()
    make_sequence(N, M, [], num, result, visited)
    for re in sorted(list(result)):
        print(' '.join(map(str, re)))


if __name__=="__main__":
    main()
