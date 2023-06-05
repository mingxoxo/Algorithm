# 영단어 암기는 괴로워
# 23.06.05
# 정렬
# https://www.acmicpc.net/problem/20920

import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
vocabulary = []

for _ in range(N):
    word = input().rstrip()
    if M <= len(word):
        vocabulary.append(word)
        
cnt = Counter(vocabulary)
print(*sorted(cnt.keys(), key=lambda x: (-cnt[x], -len(x), x)), sep='\n')
