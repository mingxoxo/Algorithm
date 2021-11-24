#카카오
#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    message = []
    nickname = {}
    print_message = {'Enter':"님이 들어왔습니다.", 'Leave':"님이 나갔습니다."}
    for mes in record:
        message.append(mes.split())
        if "Leave" not in mes:
            nickname[mes.split()[1]] = mes.split()[2]

    for mes in message:
        if mes[0] == "Change":
            continue
        answer.append(nickname[mes[1]]+print_message[mes[0]])
    return answer
