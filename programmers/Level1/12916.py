#문자열 내 p와 y의 개수
#https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    p_count , y_count = 0, 0
    for i in s.lower():
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1

    return p_count == y_count

#다른 사람의 풀이
#return s.lower().count('p') == s.lower().count('y')
