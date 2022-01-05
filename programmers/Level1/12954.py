#x만큼 간격이 있는 n개의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    if x == 0:
        return [0]*n
    num = x*n+1 if x*n >= 0 else x*n-1
    for i in range(x, num, x):
        answer.append(i)
    return answer

#다른 사람의 풀이
#return [i * x + x for i in range(n)]
