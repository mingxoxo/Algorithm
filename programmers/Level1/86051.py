#없는 숫자 더하기
#https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])

#다른 사람의 풀이
#return 45 - sum(numbers)
