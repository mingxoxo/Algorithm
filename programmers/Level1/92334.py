#신고 결과 받기
#https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_name = defaultdict(list)
    id_report = defaultdict(int)
    
    for st in set(report):
        user1, user2 = st.split()
        report_name[user1].append(user2)
        id_report[user2] += 1
    
    stop_user = [st for st in id_report if id_report[st] >= k]
    
    for st in id_list:
        answer.append(len(set(report_name[st])&set(stop_user)))
                    
    return answer
