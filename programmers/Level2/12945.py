#피보나치 수
#https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[-2] + F[-1])
        
    return F[-1]%1234567

#다른 사람의 풀이
#a,b = b,a+b
