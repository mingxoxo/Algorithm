# 사이클 단어
# 25.01.12
# https://www.acmicpc.net/problem/1544

import sys
input=sys.stdin.readline

word_list = set()
word_cnt = 0

N = int(input())
for _ in range(N):
    word = input().rstrip()
    if word not in word_list:
        word_cnt += 1
        for i in range(len(word)):
            word_list.add(word[i:len(word)] + word[:i])

print(word_cnt)
