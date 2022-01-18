#숫자의 표현
#https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        s = 0
        for j in range(i, n//2+2):
            s += j
            if s == n:
                answer += 1
            if s >= n:
                break
    return answer
