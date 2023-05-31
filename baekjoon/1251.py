# 단어 나누기
# 23.05.31
# https://www.acmicpc.net/problem/1251


def reverse_str(idx):
    piece = [word[:idx[1]], word[idx[1]:idx[2]], word[idx[2]:]]
    result = ''.join([s[::-1] for s in piece])
    return result


def Brute_Force(idx, N):
    if N == 3:
        answer.append(reverse_str(idx))
        return

    for i in range(N, len(word) - 2 + N):
        if i <= idx[N-1]:
            continue
        idx.append(i)
        Brute_Force(idx, N + 1)
        idx.pop()


answer = []
word = input()
Brute_Force([0], 1)
print(sorted(answer)[0])
