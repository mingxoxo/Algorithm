# 팰린드롬 만들기
# 그리디
# 22.02.18
# https://www.acmicpc.net/problem/1213

from collections import defaultdict

charset = defaultdict(int)
S = input()

for c in S:
    charset[c] += 1

result = []
flag = 0
last = ''

for c in sorted(charset.keys()):
    result.append(charset[c] // 2 * c)
    if charset[c] % 2 == 1: 
        if flag == 0:
            last = c
            flag = 1
        elif flag == 1:
            flag = 2
            break
    
if flag == 2:
    print("I\'m Sorry Hansoo")
else:
    print(''.join(result) + last + ''.join(reversed(result)))
