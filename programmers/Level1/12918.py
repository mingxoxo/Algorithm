#문자열 다루기 기본
#https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    try:
        if int(s) and (len(s) == 4 or len(s) == 6):
            return True
    except:
        pass
    return False

#다른 사람의 풀이
#return s.isdigit() and len(s) in (4, 6)
