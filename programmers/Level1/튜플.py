#https://programmers.co.kr/learn/courses/30/lessons/64065
  
def solution(s):
    s = s.replace('{', '')
    s = s.replace('}', '')

    num_list = list(map(int, s.split(','))) 
    answer = [0] * len(set(num_list))
    
    for num in set(num_list):
        answer[len(answer) - num_list.count(num)] = num

    return answer
