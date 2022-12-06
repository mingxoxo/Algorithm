# 쇠막대기
# 22.12.06
# 스택
# https://www.acmicpc.net/problem/10799

S = input()
bar_cnt = 0
total = 0
i = 0
while i < len(S):
    if S[i] == '(':
        if S[i+1] == ')':
            total += bar_cnt
            i += 1
        else:
            bar_cnt += 1
            total += 1
    elif S[i] == ')':
        bar_cnt -= 1
    i += 1

print(total)
