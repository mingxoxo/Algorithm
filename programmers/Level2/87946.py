#https://programmers.co.kr/learn/courses/30/lessons/87946

import itertools

def solution(k, dungeons):
    answer = 0
    result = list(itertools.permutations(dungeons, len(dungeons)))
    for i in result:
        hp = k
        cnt = 0
        for hp_first, hp_minus in i:
            if hp_first <= hp:
                hp-= hp_minus
                cnt+=1
        answer = max(answer, cnt)
        
    return answer
