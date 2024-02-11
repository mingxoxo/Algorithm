# A와 B
# 구현, 그리디, 문자열
# 24.02.11
# https://www.acmicpc.net/problem/12904
# 다른 사람의 풀이: https://www.acmicpc.net/source/54257433

S = input()
T = input()

S_len, T_len = len(S), len(T)
start, end = 0, T_len - 1
flag = 1

while S_len != T_len:
    if T[end] == 'A':
        end -= flag
    elif T[end] == 'B':
        end -= flag
        start, end = end, start
        flag *= -1
    else:
        break

    T_len -= 1

if S_len != T_len:
    print(0)
else:
    if flag == 1:
        T_result = T[start:end + 1]
    if flag == -1:
        start, end = end, start
        T_result = list(reversed(T[start:end + 1]))
    print(int(S == ''.join(T_result)))
