# 3진법 뒤집기
#https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    mul = 1
    three_list = []
    while n >= 3 :
        three_list.append(n%3)
        n = n // 3
    three_list.append(n)
    
    for i in reversed(three_list):
        answer  += i*mul
        mul *= 3
        
    return answer
  
  
#다른 사람의 풀이
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer
