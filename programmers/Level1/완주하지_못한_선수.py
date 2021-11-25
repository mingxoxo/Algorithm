#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    player = {}
    for name in completion:
        if name in player:
            player[name] += 1
        else:
            player[name] = 1
    
    for name in participant:
        if name not in player:
            return name
        player[name] -= 1
        if player[name] == 0:
            del player[name]
            
    return answer
  
# #다른 사람의 풀이
# - collections.Counter 함수 사용해서 간단하게 품
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# #- hash() 사용
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer
