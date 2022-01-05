# 최대공약수와 최소공배수 (유클리드호제법 공부필요)
#https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    
    if n > m:
        n, m = m, n

    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for i in range(m, n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    
    return answer
