#H-Index
#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    for idx, t in list(enumerate(sorted(citations, reverse = True))):
        if idx+1 > t:
            return idx
    return len(citations)
    
# #다른사람의 풀이
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
