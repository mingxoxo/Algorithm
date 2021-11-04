#https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
 
def solution(a, b):
    answer = 0
    if a > b :
        a, b = b, a
    numList = [i for i in range(a, b+1)]
    answer = sum(numList)
    return answer
