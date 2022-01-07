#소수 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12977

import itertools

def solution(nums):

    num_list = list(sum(x) for x in itertools.combinations(nums, 3))
    
    n = max(num_list)+1
    all_list = set(x for x in range(2, n))
    
    for i in range(2, n):
        if i in all_list:
            all_list -= set(range(2*i,n,i))

    return len([i for i in num_list if i in all_list])
  
  #https://mingxoxo-record.tistory.com/139
  #중간에 소수 찾기 코드 --> 에라토스테네스의 체 ( 프로그래머스 소수찾기 문제 다른사람의 풀이에서 공부 )
