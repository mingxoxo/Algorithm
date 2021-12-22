#모음사전
#https://programmers.co.kr/learn/courses/30/lessons/84512
#itertools.product(str, repeat=개수)

import itertools

def solution(word):
    result = []
    for i in range(1, 6):
        for w in list(itertools.product("AEIOU", repeat=i)):
            result.append(''.join(w))
    result.sort()
    return result.index(word)+1
