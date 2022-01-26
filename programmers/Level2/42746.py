#가장 큰 수
#https://programmers.co.kr/learn/courses/30/lessons/42746

import itertools

def solution(numbers):
    if set(numbers) == {0}:
        return "0"

    max_len = len(str(max(numbers)))
    str_list = [str(i) for i in numbers]
    str_list.sort(key = lambda x : x * 6, reverse = True)
    return ''.join(str_list)
                   
#다른 사람의 풀이
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
