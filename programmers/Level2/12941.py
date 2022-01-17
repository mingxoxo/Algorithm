#최솟값 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    for a, b in zip(sorted(A), sorted(B, reverse = True)):
        answer += a*b

    return answer

#다른 사람의 풀이
#sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
