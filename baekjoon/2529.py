# 부등호
# 23.05.12
# https://www.acmicpc.net/problem/2529

def is_correct(a, b, symbol):
    if symbol == '<':
        return a < b
    return a > b


def brute_force(cnt, choose, result):
    global N, symbol, answer

    if N == cnt:
        if answer is None:
            print(''.join(map(str, result)))
        answer = ''.join(map(str, result))
        return

    for i in reversed(range(10)):
        if choose[i] is True:
            continue
        if result and is_correct(result[-1], i, symbol[cnt]) is False:
            continue
        result.append(i)
        choose[i] = True
        brute_force(cnt + 1, choose, result)
        result.pop()
        choose[i] = False



N = int(input())
symbol = input().split()
choose = [False] * 10
answer = None
brute_force(-1, choose, [])
print(answer)
