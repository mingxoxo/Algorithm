#예산
#https://programmers.co.kr/learn/courses/30/lessons/12982

import itertools

def solution(d, budget):
    d.sort()
    for i in range(len(d), 0, -1):
        if  sum(d[:i]) <= budget:
            return i
    return 0
    
'''
다른 사람의 풀이 - 1

def solution(d, budget):
   d.sort()
   while budget < sum(d):
       d.pop()
   return len(d)


다른 사람의 풀이 - 2

def solution(d, budget):
   d.sort()
   cnt = 0
   for i in d :
       budget -= i
       if budget < 0 :
              break
       cnt += 1
   answer = cnt
   return answer
'''  
