#JadenCase 문자열 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ' '
    for i in s:
        if answer[-1] == ' ' and i.isalpha():
            answer += i.upper()
        else:
            answer += i.lower()
    return answer[1:]
