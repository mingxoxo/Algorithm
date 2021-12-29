# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
# Brute Force(브루트 포스) == 완전탐색

import itertools

height = []
for i in range(9):
    height.append(int(input()))

for key in list(itertools.permutations(height, 7)):
    if sum(key) == 100:
        answer = key
        break

for i in sorted(answer):
    print(i)

#다른 사람의 풀이
#아홉 난쟁이 키 합에서 두명의 난쟁이 키를 뺀 합이 100인것을 판별하도록 한다.
#그리고 리스트를 찾으면 2명의 난쟁이 키 값을 리스트에서 삭제