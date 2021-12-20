#https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = money - (count*(count+1)/2 * price)
    answer = - answer if answer < 0 else 0
    return answer
