#문자열 내 마음대로 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x))
    return answer
  
#정렬할 때 key, lambda 사용, 다중정렬은 ()로 묶어줌
