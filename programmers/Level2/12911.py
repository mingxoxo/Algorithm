#다음 큰 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    cnt = bin(n).count("1")
    while True:
        n += 1
        if cnt == bin(n).count("1"):
            break
    return n
