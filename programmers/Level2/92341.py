# 주차 요금 계산
# 22.09.24
# 2022 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def solution(fees, records):
    answer = []
    parsing_info = {}
    for info in records:
        t_str, car, where = info.split()
        t_list = list(map(int, t_str.split(":")))
        time = t_list[0] * 60 + t_list[1]
        
        if where == "IN":
            if car not in parsing_info.keys():
                fee = 0
                parsing_info[car] = [0]
            
            parsing_info[car][0] = time
            parsing_info[car].append(1439 - time)
        else:
            parsing_info[car][-1] = time - parsing_info[car][0]
            
    
    for key in sorted(parsing_info):
        surcharge = sum(parsing_info[key][1:]) - fees[0]
        surcharge = surcharge if surcharge >= 0 else 0
        fee = fees[1] + math.ceil(surcharge / fees[2]) * fees[3]
        answer.append(fee)
    return answer
