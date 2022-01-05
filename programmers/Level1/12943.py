#콜라츠 추측
#https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    for i in range(500):
        if num == 1:
            return i
        num = num/2 if num % 2 == 0 else num*3 + 1
    return -1
