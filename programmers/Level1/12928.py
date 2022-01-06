#약수의 합
#https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])

#다른 사람의 풀이
#print(n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0]))
