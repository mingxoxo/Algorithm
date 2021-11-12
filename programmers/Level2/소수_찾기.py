#https://programmers.co.kr/learn/courses/30/lessons/42839
#(다른 답안 확인결과) 에라토스테네스체로 쉽게 구현할 수 있음 -- > 공부필요
#itertools.permutation 사용

import itertools

def solution(numbers):
    case_list = []
    num_case = []
    answer = 0
    for i in range(1, len(numbers)+1):
        case_list.extend(list(itertools.permutations(numbers, i)))
    for i in case_list:
        num_case.append(int(''.join(i)))


    for case in set(num_case):
        count = 0
        for j in range(2, case):
            if case%j == 0:
                count+=1
                break
        if count == 0 and case != 1 and case != 0:
            print(case)
            answer+=1
    return answer
