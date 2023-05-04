# 단어 뒤집기 2
# 23.05.04
# https://www.acmicpc.net/problem/17413

S = input()
split_list = S.replace('>', '>,').replace('<', ',<').split(',')
for ss in split_list:
    if ss and ss[0] == '<':
        print(ss, end='')
    else:
        print(' '.join(rstr[::-1] for rstr in ss.split()), end='')
